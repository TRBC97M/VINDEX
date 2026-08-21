# VINDEX 0.53 — Diagnostica fontium

```text
RECTE: fons_brut et fons memoriam dynamicam crescentem adhibent.
--- G1 metadata ---
/tmp/g1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, no section header
g1=205492 octeta
fac3b84029d4a8f5719a4c8976db0a5cf416295a338716692a853a083767d3f0  /tmp/g1
--- Executio ordinaria G1 -> G2 ---
STATUS=135.
G2 deest.
--- STRACE ---
STATUS STRACE=135.
2185  execve("/tmp/g1", ["/tmp/g1", "Vindex Chat-GPT/vindex_final_v51"..., "/tmp/g2_strace"], 0x7ffe44f4e188 /* 114 vars */) = 0
2185  open("Vindex Chat-GPT/vindex_final_v51/src/compilator_vindex.vindex", O_RDONLY) = 3
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285ff5000
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285fe5000
2185  read(3, "// Bibliotheca componendi codice"..., 65536) = 65536
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285fd5000
2185  read(3, "MPONE_ONERA(codex, CONTENTUM(pos"..., 65536) = 65536
2185  mmap(NULL, 131072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285fb5000
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285fa5000
2185  read(3, "DDENS NUMERUS.\n    ACCIPIT codex"..., 65536) = 65536
2185  mmap(NULL, 262144, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285f65000
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285f55000
2185  read(3, "DO DE NUMERUS CAPACITAS 3000.\n\n "..., 65536) = 18432
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285f45000
2185  read(3, "", 65536)                = 0
2185  close(3)                          = 0
2185  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285f35000
2185  mmap(NULL, 262144, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f5285ef5000
2185  --- SIGBUS {si_signo=SIGBUS, si_code=BUS_ADRERR, si_addr=0x7f5286006000} ---
2185  +++ killed by SIGBUS (core dumped) +++
GDB deest.
--- Pila illimitata ---
STATUS PILA ILLIMITATA=135.
```
