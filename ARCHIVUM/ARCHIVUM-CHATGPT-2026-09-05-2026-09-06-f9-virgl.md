# Session ChatGPT — F9 : VIRGL réel, residentia 3D, SUBMIT_3D et direction F9-IV

_Reconstruction de coordination, non verbatim._
_La transcription intégrale de cette période n'est pas disponible dans les partages récupérables. Ce fichier conserve les décisions, échecs et preuves recoupés avec les PR/commits canoniques._
_Période couverte : 5–6 septembre 2026._
_Sources de contrôle : PR #191/#193/#194, télémétries QEMU/virglrenderer et notes de coordination._

---

## F9-I : contexte 3D réel, pas encore de compositing GPU

    [action] PR #191 : négociation réelle de `VIRTIO_GPU_F_VIRGL`, lecture des capsets, sélection VIRGL2, `CTX_CREATE`/`CTX_DESTROY`, restauration PCI et test négatif sur backend 2D.

Preuve :

```text
VIO9 O30000003 A00000001 N00000002 S02 M00000568 I00 Q00000005 R
```

La CI utilise virglrenderer + Mesa llvmpipe : elle certifie le protocole et la sémantique, pas une mesure de performance GPU physique.

## F9-II : residentia de ressources 3D

    [action] PR #193 : `RESOURCE_CREATE_3D`, backing DMA, attach au contexte, `TRANSFER_TO_HOST_3D`, renouvellement de génération, detach/unref transactionnels. Aucun `SUBMIT_3D` n'est revendiqué dans cet incrément.

### Collision `vp` / `x2`

F9-II a révélé un défaut historique du compilateur : l'empreinte base 31 des identifiants locaux confond `vp` et `x2`, tous deux à 3770. Le défaut existait avant F9-II ; cette session l'a seulement rendu observable.

Une tentative de remplacement global de l'empreinte aurait cassé des identités historiques. La correction canonisée conserve l'empreinte/ABI historique mais résout les variables locales par identité exacte : position, longueur et comparaison des octets du source. Une régression permanente `identificatores_collisionis.vindex` garde ce cas.

Preuve F9-II :

```text
VIO10 C00000001 U00000002 A00000001 D00000001 F00000001 I00001000 G00000003 H00000004 S00000001 R
```

## F9-III : premier raster `SUBMIT_3D` réellement vérifié par pixels

    [action] PR #194 : render target RGBA8, vrai `SUBMIT_3D`, clear VIRGL, `TRANSFER_FROM_HOST_3D`, puis comparaison des 128 pixels contre l'oracle Graphica X.

Première tentative matérielle : `VIO11 ERR06`. F9-I et F9-II restant verts, le transport n'était pas en cause.

La cause était une fonction `VG3DX_SUBMIT_CLEAR` à **11 arguments**. Elle compilait, mais l'ABI UEFI ne transmettait pas ces arguments de façon fiable.

La correction remplace ces 11 arguments par un bloc de paramètres de 56 octets et une fonction à 5 arguments, avec régression native du bloc.

Preuve finale :

```text
VIO11 B00000000 S00000001 P00000080 M00000000 F00000002 R
```

Interprétation : baseline noire correcte, un vrai submit, 128 pixels comparés, zéro mismatch, deux fences submit/readback.

## Direction F9-IV — décision importante

La prochaine primitive GPU utile identifiée est d'abord **`BX_OP_COPIA`**, donc une copie opaque régionale via VIRGL BLIT.

Graphica X stocke des couleurs RGBA **prémultipliées**. Le raccourci `alpha_blend` de VIRGL/Gallium BLIT suppose au contraire un RGB non prémultiplié et calcule `src.rgb * src.a + dst.rgb * (1-src.a)`. L'utiliser directement sur GX multiplierait l'alpha deux fois.

Donc :

- F9-IV doit prouver un BLIT opaque régional avec motif source, destination distincte, offset, readback complet, comparaison à `GX_COPIA` et vérification des pixels non touchés ;
- le fallback logiciel reste obligatoire ;
- F9-IV ne doit pas être déclaré terminé sur la seule preuve d'un paquet BLIT artisanal : l'exécuteur backend `BX_OP_COPIA` doit réellement emprunter la voie GPU ;
- le compositing alpha prémultiplié viendra ensuite avec un état de blend explicitement compatible (`ONE`, `INV_SRC_ALPHA`) ou une autre voie prouvée, pas avec le shortcut BLIT straight-alpha.

## Coordination avec STRUCTURA

La réussite de F9-III ne signifie pas automatiquement que F9-IV est la priorité globale suivante. La conception STRUCTURA avait été volontairement différée jusqu'à la canonisation de F9-II ; ce prérequis est désormais satisfait. Le choix de priorité entre la branche graphique et la Phase 1 du langage doit donc être explicite, pas déduit du simple numéro F9 suivant.