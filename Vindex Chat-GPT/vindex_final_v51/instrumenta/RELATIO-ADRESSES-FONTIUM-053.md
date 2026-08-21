# VINDEX 0.53 — Diagnostica basium fontium

```text
RECTE: fontes dynamici adiutoribus separatis crescunt.
COMPILATIO G1=0.
--- EXECUTIO G1 ---
9101
65536
65536
140057633902592
9102
140057633640448
9103
140057633640448
131072
9101
131072
131072
140057633640448
9102
140057633312768
9103
140057633312768
262144
9104
140057633312768
214677
9201
140057633116160
140057632854016
0
214677
EXECUTIO G1=135.
--- STRACE FINIS ---
2201  mmap(NULL, 65536, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f35887af000
2201  mmap(NULL, 262144, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, 0, 0) = 0x7f358876f000
2201  write(1, "9", 1)                  = 1
2201  write(1, "2", 1)                  = 1
2201  write(1, "0", 1)                  = 1
2201  write(1, "1", 1)                  = 1
2201  write(1, "\n", 1)                 = 1
2201  write(1, "1", 1)                  = 1
2201  write(1, "3", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "8", 1)                  = 1
2201  write(1, "6", 1)                  = 1
2201  write(1, "7", 1)                  = 1
2201  write(1, "8", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "7", 1)                  = 1
2201  write(1, "5", 1)                  = 1
2201  write(1, "2", 1)                  = 1
2201  write(1, "4", 1)                  = 1
2201  write(1, "4", 1)                  = 1
2201  write(1, "8", 1)                  = 1
2201  write(1, "\n", 1)                 = 1
2201  write(1, "1", 1)                  = 1
2201  write(1, "3", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "8", 1)                  = 1
2201  write(1, "6", 1)                  = 1
2201  write(1, "7", 1)                  = 1
2201  write(1, "8", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "4", 1)                  = 1
2201  write(1, "9", 1)                  = 1
2201  write(1, "0", 1)                  = 1
2201  write(1, "3", 1)                  = 1
2201  write(1, "0", 1)                  = 1
2201  write(1, "4", 1)                  = 1
2201  write(1, "\n", 1)                 = 1
2201  write(1, "0", 1)                  = 1
2201  write(1, "\n", 1)                 = 1
2201  write(1, "2", 1)                  = 1
2201  write(1, "1", 1)                  = 1
2201  write(1, "4", 1)                  = 1
2201  write(1, "6", 1)                  = 1
2201  write(1, "7", 1)                  = 1
2201  write(1, "7", 1)                  = 1
2201  write(1, "\n", 1)                 = 1
2201  --- SIGBUS {si_signo=SIGBUS, si_code=BUS_ADRERR, si_addr=0x7f3588880000} ---
2201  +++ killed by SIGBUS (core dumped) +++
```
