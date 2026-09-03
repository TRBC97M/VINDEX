# ATMOS // TERMINAL DEPTH — POC VI / Stabilitas I

**Status: probatum automatice; probatio humana pendet.**

Hoc incrementum post feedback humanum POC V nascitur. Finis non est plura systemata addere, sed fundamentum iam demonstratum in applicationem tractabilem convertere.

## Correcta

- input clavieris ad frontes: clavis retenta unam actionem excitat, non seriem rapidam;
- ATMOS input tantum accipit dum fenestra eius foreground est;
- fenestra fixa est: resize/maximize non amplius framebuffer et HUD disiungunt;
- canvas 640×440 1:1 praesentatur, sine stretching arbitrario;
- sex actiones etiam mure cliccabiles sunt;
- actio accepta, recusata vel error save in HUD monstratur;
- ultimum contactum sonar separatim monstratur;
- game-over statum actiones claudit;
- frame cadence ad circa XXX FPS redacta est ad stabilitatem et usum CPU meliorem.

## Probatio automatica

`atmos_poc_vi.exe smoke` regressionem input exercet: eadem clavis tribus frame retenta actionem semel tantum generat; post remissionem iterum premi potest.

Deinde eandem seriem determinatam POC V exercet: sector orientalis + minera, cum ATD1/ATW1 servatis et framebuffer DCXL×CDXL praesentato.

Workflow `VINDEX — ATMOS POC VI Stabilitas I`, cursus #1 (`33804569737`) sub Windows Server 2025: **success**.

Valoribus probatis:

```text
edges      2
cycle      2
depth      120
oxygen     95
energy     86
ore        9
sector     1,0
travel     2
scanlines  440
```

Artefactum CI: `atmos-poc-vi-stabilitas`, ID `9912380004`, ZIP SHA-256 `0173c6cd6d61b2938b861bdda1ff126acff7f063d6e12fc0fe19f1b91b4fa779`.

## Puritas

Runtime POC VI et omnis codex applicationis proprius sub `PROGRAMMATA/ATMOS_TERMINAL_DEPTH` VINDEX est. Win32 DLL sunt servitia externa systematis operativi, non codex applicationis ATMOS.

Audit separatus huius proprietatis nominatur **La Passe Génocidaire** et iam automatice probatus est.

## Clausula fusionis

CI sola non sufficit ad vocabulo *stabilis*. PR #182 draft manet donec usor hanc build in machina sua exercuerit et input, fenestram, HUD, murem atque usum generalem humanitus probaverit.
