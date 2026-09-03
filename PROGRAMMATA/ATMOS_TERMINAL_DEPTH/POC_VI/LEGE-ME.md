# ATMOS // TERMINAL DEPTH — POC VI / Stabilitas I

**Status: in probatione.**

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

`atmos_poc_vi.exe smoke` etiam regressionem input exercet: eadem clavis tribus frame retenta actionem semel tantum generare debet; post remissionem iterum premi potest.

Deinde eandem seriem determinatam POC V exercet: sector orientalis + minera, cum ATD1/ATW1 servatis et framebuffer DCXL×CDXL praesentato.

## Puritas

Runtime POC VI et omnis codex applicationis proprius sub `PROGRAMMATA/ATMOS_TERMINAL_DEPTH` VINDEX est. Win32 DLL sunt servitia externa systematis operativi, non codex applicationis ATMOS.

Audit separatus huius proprietatis nominatur **La Passe Génocidaire**.
