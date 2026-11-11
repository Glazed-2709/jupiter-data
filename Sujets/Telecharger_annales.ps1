# Telecharge les annales listees dans manifest.csv et les range dans les dossiers.
# Les fichiers deja presents sont ignores : on peut relancer sans risque.
$ErrorActionPreference = "Continue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$items = Import-Csv -Path (Join-Path $root "manifest.csv") -Delimiter ";" -Encoding UTF8
$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
$log = Join-Path $root "telechargements_rates.txt"
if (Test-Path $log) { Remove-Item $log }
$ok = 0; $skip = 0; $ko = 0; $n = 0
foreach ($i in $items) {
    $n++
    $dir = Join-Path $root $i.dossier
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $dest = Join-Path $dir $i.fichier
    if ((Test-Path $dest) -and ((Get-Item $dest).Length -gt 5000)) { $skip++; continue }
    $tmp = $dest + ".part"
    try {
        Invoke-WebRequest -Uri $i.url -OutFile $tmp -UserAgent $ua -TimeoutSec 60 -UseBasicParsing
        $b = [System.IO.File]::ReadAllBytes($tmp)
        if ($b.Length -gt 5000 -and $b[0] -eq 0x25 -and $b[1] -eq 0x50 -and $b[2] -eq 0x44 -and $b[3] -eq 0x46) {
            Move-Item -Force $tmp $dest
            $ok++
            Write-Host ("[{0}/{1}] OK  {2}" -f $n, $items.Count, $i.fichier)
        } else {
            Remove-Item $tmp -Force
            $ko++
            Add-Content $log ("PAS UN PDF : " + $i.fichier + " <- " + $i.url)
            Write-Host ("[{0}/{1}] KO  {2}" -f $n, $items.Count, $i.fichier) -ForegroundColor Yellow
        }
    } catch {
        if (Test-Path $tmp) { Remove-Item $tmp -Force }
        $ko++
        Add-Content $log ("ERREUR : " + $i.fichier + " <- " + $i.url + " (" + $_.Exception.Message + ")")
        Write-Host ("[{0}/{1}] KO  {2}" -f $n, $items.Count, $i.fichier) -ForegroundColor Yellow
    }
    Start-Sleep -Milliseconds 700
}
Write-Host ""
Write-Host ("Termine : {0} telecharges, {1} deja presents, {2} echecs." -f $ok, $skip, $ko)
if ($ko -gt 0) { Write-Host ("Details des echecs dans : " + $log) }
