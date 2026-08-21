/* VINDEX Systema — sector BIOS, modus realis -> longus x86-64. */

.intel_syntax noprefix
.section .text
.code16
.global _start

_start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7c00
    mov byte ptr [boot_drive], dl

    /* Primam sarcinae partem (120 sectores, LBA 1) ad 0x10000 lege. */
    mov si, offset dap
    mov ah, 0x42
    mov dl, byte ptr [boot_drive]
    int 0x13
    jc error_discorum

    /* Reliquos 136 sectores circa limitem 0x20000 sine transitu lege. */
    mov si, offset dap_secundum
    mov ah, 0x42
    mov dl, byte ptr [boot_drive]
    int 0x13
    jc error_discorum
    mov si, offset dap_quartum
    mov ah, 0x42
    mov dl, byte ptr [boot_drive]
    int 0x13
    jc error_discorum
    mov si, offset dap_tertium
    mov ah, 0x42
    mov dl, byte ptr [boot_drive]
    int 0x13
    jc error_discorum

    /* Formam litterarum BIOS 8x8 ad 0x8000 conserva. */
    mov ax, 0x1130
    mov bh, 0x03
    int 0x10
    mov ax, es
    mov ds, ax
    mov si, bp
    xor ax, ax
    mov es, ax
    mov di, 0x8000
    mov cx, 2048
    cld
    rep movsb
    xor ax, ax
    mov ds, ax
    mov es, ax

    /* Modus VGA 13h: 320x200, 256 colores, memoria ad 0xA0000. */
    mov ax, 0x0013
    int 0x10

    /* Lineam A20 per portam rapidam aperi. */
    in al, 0x92
    or al, 2
    out 0x92, al

    lgdt [gdt_descriptor]
    mov eax, cr0
    or eax, 1
    mov cr0, eax
    ljmp 0x08, protected_mode

error_discorum:
    mov si, offset error_text
.error_loop:
    lodsb
    test al, al
    jz .error_halt
    mov ah, 0x0e
    int 0x10
    jmp .error_loop
.error_halt:
    cli
    hlt
    jmp .error_halt

.code32
protected_mode:
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov esp, 0x90000

    /* ELF VINDEX integrum ex 0x10000 ad basim 0x400000 transfer. */
    mov esi, 0x10000
    mov edi, 0x400000
    mov ecx, 32768
    rep movsd
    mov eax, dword ptr [0x10018]
    mov dword ptr [kernel_entry], eax

    /* Tabulae paginarum: primum GiB per paginas 2 MiB identice mappa. */
    mov edi, 0x1000
    xor eax, eax
    mov ecx, 3072
    rep stosd
    mov dword ptr [0x1000], 0x2003
    mov dword ptr [0x2000], 0x3003
    mov edi, 0x3000
    mov eax, 0x83
    mov ecx, 512
.pagina:
    mov dword ptr [edi], eax
    mov dword ptr [edi + 4], 0
    add eax, 0x200000
    add edi, 8
    loop .pagina

    mov eax, cr4
    or eax, 1 << 5
    mov cr4, eax
    mov ecx, 0xc0000080
    rdmsr
    or eax, 1 << 8
    wrmsr
    mov eax, 0x1000
    mov cr3, eax
    mov eax, cr0
    or eax, 1 << 31
    mov cr0, eax
    ljmp 0x18, long_mode

.code64
long_mode:
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov ss, ax
    /* VINDEX reservat pilam amplam; 16 MiB spatium tutum praebent. */
    mov rsp, 0x1000000
    mov qword ptr [rsp], 0
    xor rbp, rbp
    /* Rectores PS/2 et interruptiones ante nucleum constitue. */
    mov eax, 0x41f000
    call rax
    mov eax, dword ptr [kernel_entry]
    jmp rax

.align 8
gdt:
    .quad 0x0000000000000000
    .quad 0x00cf9a000000ffff
    .quad 0x00cf92000000ffff
    .quad 0x00af9a000000ffff
gdt_end:
gdt_descriptor:
    .word gdt_end - gdt - 1
    .long gdt

dap:
    .byte 0x10, 0
    .word 120
    .word 0x0000
    .word 0x1000
    .quad 1

dap_secundum:
    .byte 0x10, 0
    .word 8
    .word 0x0000
    .word 0x1f00
    .quad 121

dap_tertium:
    .byte 0x10, 0
    .word 8
    .word 0x0000
    .word 0x2000
    .quad 129

dap_quartum:
    .byte 0x10, 0
    .word 120
    .word 0x0000
    .word 0x2100
    .quad 137

boot_drive:
    .byte 0
kernel_entry:
    .long 0
error_text:
    .asciz "ERRATUM DISCUS"

.org 510
.word 0xaa55
