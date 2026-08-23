# FENESTRALE II — GRADUS K
## Resize, maximizatio et eventa clientium VINDEX

**Status:** experimentalis, applicatio UEFI separata
**Series:** Fenestrale II
**Gradus:** K
**Praerequisitum:** Gradus J

---

## I. Propositum

Gradus J fenestras per murem moveri, minui et restitui fecit. Gradus K eas
primum ad magnitudinem mutabilem ducit et clientes VINDEX mutationem ipsam
repingere iubet.

Novae facultates sunt:

- compositio regionum laesarum;
- resize ab angulo dextro inferiore;
- praevisio clara ante confirmationem resize;
- maximizatio et restitutio per buttonem medium;
- maximizatio et restitutio per duplicem clicum tituli;
- eventa `FOCUS` et `DIMENSIO` ad clientes VINDEX;
- re-pictura vera in superficie nova;
- correctio ingressus ELF clientium.

---

## II. Compositio regionum laesarum

Gradus J totum framebuffer ad quemque motum cursoris vel fenestrae repingebat.
Hoc in resolutione `1366×768` iam plus quam decies centena milia pixelorum pro
singulo eventu significabat.

Gradus K `compone_region` et unionem duarum regionum adhibet:

- cursor: regio vetus cum regione nova;
- tractio: fenestra vetus cum fenestra nova, umbra inclusa;
- resize praevisum: terminus vetus cum termino novo;
- resize confirmatum: geometria vetus cum geometria nova.

Compositio plena manet solum ubi totus z-order aut status plurium fenestrarum
mutatur.

---

## III. Resize interactiva

Fenestra activa parvum signum bronzeum in angulo dextro inferiore ostendit.
Clic et tractio in regione `14×14 px` modum resize incipit.

Dum bulla tenetur, compositor terminum aqua praevisum pingit. Superficies et
client nondum ad quemque pixel muris reallocantur. Cum bulla solvitur:

1. nova superficies XXXII-bit attribuitur;
2. geometria nova in mailbox clientis ponitur;
3. eventum `DIMENSIO` clientem VINDEX repingere iubet;
4. solum post responsum rectum superficies vetus liberatur;
5. si client errat, geometria et memoria vetus integrae manent.

Mensura minima demonstrationis est `480×320`. Fenestra taskbar `28 px` non
tegit et limites monitorii non excedit.

---

## IV. Maximizatio et restitutio

Button medius tituli iam non est pictura iners. Clic eum fenestram ad totam
aream operabilem monitorii extendit. Locus et mensura pristina in descriptorio
interno servantur.

Alter clic buttonis, vel duplex clicus tituli, geometriam pristinam restituit.
Maximizatio eandem viam `DIMENSIO` ac resize utitur; client igitur layout suum
ad latitudinem et altitudinem novas denuo pingit.

Fenestra maxima nec trahitur nec angulo resize utitur, donec restituatur.

---

## V. Eventa clientium

ABI K mailbox Gradus G non auget nec relocat. Tres campos `reservata` nunc
sensum additivum accipiunt:

```text
reservata[0]  typus eventus
reservata[1]  argumentum primum
reservata[2]  argumentum secundum
```

Operatio nova est `FII_CMP_OP_EVENTUM`.

Eventa primi gradus:

- `FII_CMP_EVENTUM_FOCUS`: activus vel inactivus;
- `FII_CMP_EVENTUM_DIMENSIO`: latitudo et altitudo novae.

PROGRAMMATA K et TABULA K eventum focus agnoscunt. Ad eventum dimensionis
superficiem privatam totam repingunt et `20` reddunt. Compositor responsum et
statum mailbox verificat antequam memoriam veterem liberet.

---

## VI. Re-oneratio clientium

Clientes huius experimenti nondum processus permanentes sunt. Uterque ELF in
applicatione UEFI inclusus manet. Cum eventum mittendum est, compositor:

1. imaginem clientis idonei ad `0x00400000` re-onerat;
2. mailbox cum superficie persistente implet;
3. `PRINCIPALIS` vocat;
4. responsum legit;
5. alium clientem eodem spatio postea onerare potest.

Ita superficies et contentum persistunt, quamquam spatium codicis temporarium
inter clientes communicatur. Relocator ELF nondum requiritur.

---

## VII. Correctio ingressus ELF

ELF a compilatore VINDEX productus `e_entry` ad involucrum processus dirigit.
Involucrum argumenta disponit, `PRINCIPALIS` vocat et postea syscall exitus
facit. Gradus H–J `e_entry` directe tamquam functionem UEFI vocaverunt; hoc in
executione firmware rectum non erat.

Gradus K instructionem `call rel32` intra involucrum verificat, target
`PRINCIPALIS` intra imaginem resolvit et target illum directe vocat. Transitus
C/VINDEX etiam registrum `RBX` servat, quia conventio interna VINDEX eo utitur
quamquam ABI C eum callee-saved putat.

Haec via nunc probatione exsecutabili comprobatur, non sola inspectione
textuali.

---

## VIII. Probatio runtime

`tests/proba_fenestrale_ii_k_runtime.c` memorias easdem ac firmware in processu
Linux ad loca fixa describit. Deinde utrumque ELF K revera exsequitur:

1. petitio `CREA`;
2. pictura initialis;
3. petitio `PRAESENTA`;
4. finis initializationis;
5. eventum `DIMENSIO` cum re-pictura;
6. eventum `FOCUS` sine corruptione pixelorum.

Probatio cum optimizatione `-O2` currit, ut conventio registrorum quoque
vere probetur.

---

## IX. Separatio stricta

Gradus K non mutat:

- `systema/nucleus.vindex`;
- `systema/uefi/firmamentum_uefi.c`;
- `BOOTX64.EFI` canonicum;
- imaginem UEFI 0.51;
- volumen VINDEX;
- logicam `.VXNAT` Systematis principalis.

Exitus separati:

```text
FENESTRALEK.EFI
fenestrale_k_uefi.img
```

---

## X. Constructio

```bash
python3 tests/proba_fenestrale_ii_k.py
bash systema/uefi/construe_fenestrale_native_k.sh
./compilator_vindex src/programmata_fenestrale_ii_k_runtime.vindex /tmp/programmata_k.elf
./compilator_vindex src/tabula_fenestrale_ii_k_runtime.vindex /tmp/tabula_k.elf
gcc -std=c11 -O2 -Wall -Wextra -Werror -I systema \
    tests/proba_fenestrale_ii_k_runtime.c -o /tmp/proba-k
/tmp/proba-k /tmp/programmata_k.elf /tmp/tabula_k.elf
```

Scriptum constructionis clientes, compositorium PE32+ EFI et imaginem
GPT/FAT32 bootabilem producit. Workflow CI regressiones D–J et probationes
generales XXI ante K retinet. Modi exsequendi initiatorum et scriptorum
constructionis canonicorum quoque restituuntur, ne checkout recens probationes
ante compilationem vetet.

---

## XI. Proximus gradus

Gradus L potest eventa muris et claviaturae intra coordinatas clientis tradere,
ut TABULA cellulas et PROGRAMMATA elementa sua interactive tractent. Postea
launcher dynamicus clientes ex SylviaFS, non solum ex imaginibus inclusis,
onerare poterit.

> Geometria mutatur. Client repingit. Compositor memoriam tuetur.

*VINDEX Latine cogitat. Sylvia Latine loquitur.*
