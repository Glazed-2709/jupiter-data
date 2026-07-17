# Jupiter — déploiement et version mobile

Ce guide explique comment **héberger Jupiter gratuitement sur GitHub Pages** et faire fonctionner la **version mobile** (lecture seule : documents + questions).

---

## 1. Vue d'ensemble

Tu as deux usages :

- **Sur ordinateur** (`index.html`, `arbre.html`, `revisions.html`) : tu connectes ton dossier local via le navigateur (Chrome/Edge). Tu as tout : arbre 3D, lecture multi-documents, mode test (flashcards). Ça marche aussi bien en local qu'en ligne.
- **Sur téléphone** (`mobile.html`) : pas d'accès au disque possible. La page lit un fichier `manifest.json` publié en ligne qui décrit l'arborescence, puis ouvre les PDF et images directement depuis le dépôt. Volontairement léger : **navigation et lecture des documents uniquement** — pas d'arbre 3D (trop lourd et inutilisable sur mobile), pas de flash tests.

Le `manifest.json` est généré une fois sur PC avec `generer-manifest.html`, puis déposé dans le dépôt.

---

## 2. Structure attendue du dépôt

```
ton-depot/
├── index.html              ← accueil (PC)
├── arbre.html              ← arbre (PC)
├── revisions.html          ← révisions + brouillon (PC)
├── mobile.html             ← version mobile (lecture seule)
├── generer-manifest.html   ← outil PC pour produire les manifests
│
├── MPSI/
│   ├── manifest.json       ← généré par l'outil
│   ├── Mathématiques/
│   │   └── 01 - Intégration/
│   │       ├── Cours/cours.pdf
│   │       ├── TD/td.pdf
│   │       └── questions.json
│   └── Physique/ …
│
├── PSI/
│   ├── manifest.json
│   └── …
│
└── Culture/
    ├── manifest.json
    └── …
```

> Les dossiers `MPSI/`, `PSI/`, `Culture/` correspondent à tes sections. Chacune a son propre `manifest.json` à sa racine.

---

## 3. Publier sur GitHub Pages (gratuit)

1. Crée un compte sur **github.com** (gratuit).
2. Crée un dépôt — par exemple `jupiter`. Tu peux le mettre **public** (tes PDF sont publics, c'est OK d'après ton choix). Un dépôt privé ne peut pas servir GitHub Pages gratuitement, donc reste sur public.
3. Envoie tes fichiers dans le dépôt :
   - Le plus simple sans ligne de commande : bouton **Add file → Upload files**, puis glisse tes dossiers. (GitHub accepte le glisser-déposer de dossiers entiers.)
   - Avec Git : `git clone`, copie tes fichiers, `git add . && git commit -m "init" && git push`.
4. Dans le dépôt : **Settings → Pages**. Sous *Build and deployment*, choisis **Deploy from a branch**, branche `main`, dossier `/ (root)`. Sauvegarde.
5. Au bout d'une minute, ton site est en ligne à :
   ```
   https://TON-PSEUDO.github.io/jupiter/
   ```
   - PC : `…/jupiter/index.html`
   - Mobile : `…/jupiter/mobile.html`

---

## 4. Générer les manifests (à refaire quand tu ajoutes des fichiers)

Le mobile ne voit que ce qui est décrit dans les `manifest.json`. À chaque fois que tu ajoutes/retires des cours, TD ou questions, régénère le manifest de la section concernée :

1. Ouvre `generer-manifest.html` **sur ordinateur** (Chrome ou Edge). Tu peux l'ouvrir en ligne ou en double-cliquant le fichier local.
2. Clique **Choisir une section** et sélectionne le dossier de **la section** (par ex. `MPSI/`), pas la racine.
3. L'outil scanne, affiche un journal, puis propose **Télécharger manifest.json**.
4. Place ce `manifest.json` **dans le dossier de la section** (`MPSI/manifest.json`) dans ton dépôt et pousse la modif.
5. Recommence pour `PSI/` et `Culture/` si besoin.

> Le manifest ne contient **pas** les PDF, seulement des chemins et le texte des questions. Il est petit (quelques Ko).

---

## 5. Adapter les chemins dans `mobile.html` (si besoin)

En haut du script de `mobile.html`, la liste `SECTIONS` indique où trouver chaque manifest :

```js
const SECTIONS=[
  {id:'MPSI', …, manifest:'MPSI/manifest.json', …},
  {id:'PSI',  …, manifest:'PSI/manifest.json',  …},
  {id:'Culture', …, manifest:'Culture/manifest.json', …},
];
```

Si tes dossiers ont d'autres noms, change uniquement la valeur `manifest`. Les chemins sont **relatifs à `mobile.html`**, donc tout doit rester dans le même dépôt.

---

## 6. Installer le mobile comme une appli (option agréable)

Sur le téléphone, ouvre `…/jupiter/mobile.html` dans le navigateur, puis :
- **iPhone (Safari)** : bouton Partager → *Sur l'écran d'accueil*.
- **Android (Chrome)** : menu ⋮ → *Ajouter à l'écran d'accueil*.

Tu obtiens une icône plein écran qui se comporte comme une appli.

---

## 7. Notes et limites

- **PDF sur mobile** : la page tente d'afficher le PDF en plein écran. Si un navigateur mobile refuse de le rendre dans la page (ça arrive sur certains Android), un bouton **Ouvrir dans un onglet** (icône en haut à droite du lecteur) ouvre le fichier directement.
- **Documents sur mobile** : le mobile ne fait que naviguer dans l'arborescence et ouvrir les fichiers. Aucune donnée n'est stockée sur le téléphone.
- **Confidentialité** : sur un dépôt public, tout le monde peut accéder aux fichiers s'il connaît l'URL. Tu as confirmé que c'est acceptable. Si un jour tu veux du privé, il faudra un hébergement avec authentification (hors gratuit/simple).
- **Mettre à jour le site** : pousse simplement les fichiers modifiés sur GitHub ; Pages se met à jour tout seul en une minute. Pense à régénérer le manifest si tu as touché aux dossiers de cours.
