# Recupere les corriges UPSTI de SI (PSI) listes dans manifest_corriges_SI.csv.
# Pour chaque sujet : recherche sur upsti.fr, ouvre les fiches, repere le PDF "Corrige" de la bonne annee.
$ErrorActionPreference = "Continue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$items = Import-Csv -Path (Join-Path $root "manifest_corriges_SI.csv") -Delimiter ";" -Encoding UTF8
$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
$log = Join-Path $root "corriges_rates.txt"
if (Test-Path $log) { Remove-Item $log }
$cache = @{}
function Get-Page($url) {
    if ($cache.ContainsKey($url)) { return $cache[$url] }
    try { $p = (Invoke-WebRequest -Uri $url -UserAgent $ua -TimeoutSec 60 -UseBasicParsing).Content } catch { $p = "" }
    $cache[$url] = $p
    Start-Sleep -Milliseconds 400
    return $p
}
$ok = 0; $skip = 0; $ko = 0; $n = 0
foreach ($i in $items) {
    $n++
    $dir = Join-Path $root $i.dossier
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $dest = Join-Path $dir $i.fichier
    if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 5000)) { $skip++; continue }
    $found = $null
    $terms = @($i.mots_cles -split "\|" | Where-Object { $_ }) + @($i.annee)
    foreach ($t in $terms) {
        if ($found) { break }
        $q = [uri]::EscapeDataString($t)
        $list = Get-Page ("https://www.upsti.fr/corriges/?q=" + $q)
        $fiches = [regex]::Matches($list, '/corriges/\d+/[a-z0-9\-]+/') | ForEach-Object { $_.Value } | Select-Object -Unique | Select-Object -First 12
        foreach ($f in $fiches) {
            $page = Get-Page ("https://www.upsti.fr" + $f)
            $links = [regex]::Matches($page, 'href="([^"]*fichiers/corrige/fichiers/[^"]+\.pdf)"') | ForEach-Object { $_.Groups[1].Value }
            foreach ($l in $links) {
                $name = [uri]::UnescapeDataString(($l -split "/")[-1])
                if ($name -match "(?i)corrige" -and $name -match ("(?i)(" + $i.concours + ")") -and $name -match ("-PSI-" + $i.annee + "-") -and $name -notmatch "(?i)info") {
                    $found = $l; break
                }
            }
            if ($found) { break }
        }
    }
    if (-not $found) { $ko++; Add-Content $log ("INTROUVABLE : " + $i.fichier); Write-Host ("[{0}/{1}] KO  {2}" -f $n, $items.Count, $i.fichier) -ForegroundColor Yellow; continue }
    if ($found.StartsWith("/")) { $found = "https://www.upsti.fr" + $found }
    $tmp = $dest + ".part"
    try {
        Invoke-WebRequest -Uri $found -OutFile $tmp -UserAgent $ua -TimeoutSec 90 -UseBasicParsing
        $b = [System.IO.File]::ReadAllBytes($tmp)
        if ($b.Length -gt 5000 -and $b[0] -eq 0x25 -and $b[1] -eq 0x50) { Move-Item -Force $tmp $dest; $ok++; Write-Host ("[{0}/{1}] OK  {2}" -f $n, $items.Count, $i.fichier) }
        else { Remove-Item $tmp -Force; $ko++; Add-Content $log ("PAS UN PDF : " + $i.fichier + " <- " + $found) }
    } catch {
        if (Test-Path $tmp) { Remove-Item $tmp -Force }
        $ko++; Add-Content $log ("ERREUR : " + $i.fichier + " <- " + $found + " (" + $_.Exception.Message + ")")
    }
}
Write-Host ""
Write-Host ("Termine : {0} telecharges, {1} deja presents, {2} introuvables/echecs." -f $ok, $skip, $ko)
if ($ko -gt 0) { Write-Host ("Details dans : " + $log) }
