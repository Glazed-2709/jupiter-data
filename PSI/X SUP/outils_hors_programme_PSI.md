# Outils de calcul hors-programme — feuille de route PSI (objectif X)

$\varepsilon$psilon — MPSI 2025–2026 → PSI 2026–2027

Principe : chaque outil ci-dessous n'est **pas exigible** au programme officiel, mais donne un avantage réel (rapidité de calcul, compréhension profonde, ou pont entre maths/physique/SII). Quand tu abordes le chapitre associé en cours, préviens-moi et je te prépare un TD (énoncé + correction) sur l'outil correspondant, dans le même format que les autres documents de prép.

---

## I. Mathématiques

| Chapitre programme PSI | Outil(s) hors-programme à voir en parallèle | Pourquoi c'est utile |
|---|---|---|
| **Algèbre linéaire / Réduction des endomorphismes** (révisions de Sup, rentrée) | Décomposition de Dunford (D + N) ; polynômes interpolateurs de Lagrange ; rayon spectral et normes matricielles | Comprendre la structure fine d'un endomorphisme, indispensable pour les exos de réduction tordus et les suites récurrentes linéaires d'ordre élevé |
| **Espaces préhilbertiens / euclidiens** | Procédé de Gram-Schmidt → décomposition QR ; méthode des moindres carrés | Lien direct avec les applications numériques (régression, approximation), récurrent en TIPE et en problèmes de recherche |
| **Séries numériques** | Règle de Bertrand (cas limites $1/(n\ln^\alpha n)$) ; transformation d'Abel / sommation par parties ; produit de Cauchy de deux séries | Débloque les cas limites classiques que la règle de comparaison standard ne tranche pas |
| **Suites et séries de fonctions / Séries entières** | Théorème taubérien d'Abel (continuité radiale) ; fonctions génératrices et lien combinatoire (récurrences, probas) | Justifie rigoureusement les passages série ↔ fonction très utilisés en physique |
| **Intégration (intégrales généralisées et à paramètre)** | Fonctions Gamma et Bêta d'Euler ; intégrales de Fresnel ; critères d'Abel-Dirichlet pour intégrales semi-convergentes | Calculs classiques qui tombent très souvent en problème de recherche (type Wallis que tu as déjà vu) |
| **Équations différentielles linéaires** | **Transformée de Laplace** (priorité haute) ; méthode de Frobenius (résolution par séries entières) ; Wronskien | La Laplace est LE pont vers une compréhension rigoureuse de l'automatique/SII (fonctions de transfert, stabilité) |
| **Séries de Fourier** | Transformée de Fourier (cas continu) ; produit de convolution ; phénomène de Gibbs | Lien direct avec le traitement du signal, l'électronique et l'optique de Fourier |
| **Fonctions de plusieurs variables / calcul différentiel** | Multiplicateurs de Lagrange (extrema sous contrainte) ; opérateurs différentiels en coordonnées cylindriques/sphériques (formulaire grad/div/rot/laplacien) ; théorèmes de Green-Riemann, Stokes, Gauss-Ostrogradsky | Fonde rigoureusement les formules "données dans le formulaire" en électromagnétisme |
| **Probabilités (var. discrètes puis continues)** | Fonctions caractéristiques ; chaînes de Markov ; théorème central limite (énoncé + démonstration des grandes lignes) | Classiques d'oraux et de sujets TIPE de modélisation aléatoire |
| **Géométrie (courbes, surfaces — fin d'année)** | Quaternions pour les rotations 3D ; courbure/torsion approfondies | Directement exploitable pour le traitement d'attitude de ton drone (IMU/MPU6050) |

---

## II. Physique

| Chapitre programme PSI | Outil(s) hors-programme à voir en parallèle | Pourquoi c'est utile |
|---|---|---|
| **Mécanique du point / du solide** | Formalisme lagrangien (équations d'Euler-Lagrange) ; linéarisation autour d'un équilibre (petites oscillations) | Résout en quelques lignes des problèmes de mécanique qui demanderaient une page en newtonien — classique à l'oral X |
| **Électromagnétisme (statique puis ondes)** | Opérateurs vectoriels en coordonnées curvilignes (formulaire complet grad/div/rot/laplacien cylindrique et sphérique) ; notation complexe pour les ondes | Manipuler Maxwell sans hésitation, gain de temps énorme en composition |
| **Électronique / Automatique (filtres, ALI, asservissements)** | **Transformée de Laplace appliquée** : fonction de transfert généralisée, réponse à une entrée quelconque ; lieu de Nyquist / critère du revers ; représentation d'état | Comprendre stabilité et correction au-delà du seul régime sinusoïdal forcé — cœur de l'épreuve S2I à l'oral X |
| **Thermodynamique (diffusion, machines thermiques)** | Équation de la chaleur résolue par séparation de variables (lien avec séries de Fourier) ; bilans exergétiques | Approfondit la diffusion thermique, fréquent en problème de recherche |
| **Optique ondulatoire** | Transformée de Fourier optique (diffraction de Fraunhofer) ; fonction d'autocorrélation et cohérence | Comprendre la diffraction "derrière" le formalisme imposé |
| **Mécanique des fluides** | Analyse dimensionnelle approfondie et nombres sans dimension (Reynolds, Froude...) ; notion de couche limite | Modélisation rapide d'écoulements, très utile en TIPE |
| **Ondes mécaniques / acoustique** | Analogies électro-mécaniques (impédances mécaniques ↔ électriques) | Pont naturel avec l'électronique, très valorisé à l'oral |

---

## III. Outils numériques transversaux (Python)

| À voir avec... | Outil | Pourquoi |
|---|---|---|
| Équations différentielles | Méthode de Runge-Kutta (ordre 4), au-delà d'Euler explicite | Simulation précise pour TIPE/SII (tu l'utilises déjà pour VOLTCORE) |
| Séries / Transformée de Fourier | FFT (transformée de Fourier discrète) | Analyse de signaux réels, lien direct avec électronique |
| Probabilités | Méthode de Monte Carlo | Estimation numérique, classique en TIPE de modélisation |

---

## Mode d'emploi

Quand tu commences un chapitre de la liste, dis-moi par exemple : *"on attaque les équations différentielles linéaires"* → je te prépare un TD énoncé + correction sur la transformée de Laplace (et éventuellement Frobenius/Wronskien selon ton niveau de besoin), dans le format habituel (PDF énoncé + PDF corrigé, header $\varepsilon$psilon).
