/* Rectores PS/2 VINDEX: interruptiones claviaturae et muris in modo longo. */

.intel_syntax noprefix
.section .text
.code64
.global _start

_start:
    cli

    /* Pagina communis alta a memoria firmware antiqua seiuncta est. */
    mov qword ptr [0x3000000], 160
    mov qword ptr [0x3000008], 100
    mov qword ptr [0x3000010], 0
    mov qword ptr [0x3000018], 0
    mov qword ptr [0x3000030], 0
    mov qword ptr [0x3000038], 0
    mov qword ptr [0x3000040], 0
    mov qword ptr [0x3000050], 0
    mov qword ptr [0x3000800], 0
    mov byte ptr [0x3000020], 0

    /* IDT 256 portarum ad 0x5000. */
    mov edi, 0x5000
    xor eax, eax
    mov ecx, 512
    rep stosq

    lea rax, [rip + interruptio_temporis]
    mov edi, 0x5200
    call porta_idt
    lea rax, [rip + interruptio_clavis]
    mov edi, 0x5210
    call porta_idt
    lea rax, [rip + interruptio_muris]
    mov edi, 0x52c0
    call porta_idt
    lidt [rip + descriptio_idt]

    call pic_constitue
    call pit_constitue
    call ps2_constitue
    sti
    ret

porta_idt:
    mov word ptr [rdi], ax
    mov word ptr [rdi + 2], 0x18
    mov byte ptr [rdi + 4], 0
    mov byte ptr [rdi + 5], 0x8e
    mov rdx, rax
    shr rdx, 16
    mov word ptr [rdi + 6], dx
    shr rdx, 16
    mov dword ptr [rdi + 8], edx
    mov dword ptr [rdi + 12], 0
    ret

mora_portus:
    out 0x80, al
    ret

pic_constitue:
    mov al, 0x11
    out 0x20, al
    call mora_portus
    out 0xa0, al
    call mora_portus
    mov al, 0x20
    out 0x21, al
    call mora_portus
    mov al, 0x28
    out 0xa1, al
    call mora_portus
    mov al, 0x04
    out 0x21, al
    call mora_portus
    mov al, 0x02
    out 0xa1, al
    call mora_portus
    mov al, 0x01
    out 0x21, al
    call mora_portus
    out 0xa1, al
    call mora_portus
    mov al, 0xf8
    out 0x21, al
    mov al, 0xef
    out 0xa1, al
    ret

pit_constitue:
    mov al, 0x36
    out 0x43, al
    mov ax, 11932
    out 0x40, al
    mov al, ah
    out 0x40, al
    ret

ps2_exspecta_introitum:
    mov ecx, 100000
.introitus:
    in al, 0x64
    test al, 2
    jz .introitus_paratum
    loop .introitus
.introitus_paratum:
    ret

ps2_exspecta_exitum:
    mov ecx, 100000
.exitus:
    in al, 0x64
    test al, 1
    jnz .exitus_paratum
    loop .exitus
.exitus_paratum:
    ret

ps2_exhauri:
    mov ecx, 256
.iterum:
    in al, 0x64
    test al, 1
    jz .finis
    in al, 0x60
    loop .iterum
.finis:
    ret

ps2_muri_mitte:
    push rax
    call ps2_exspecta_introitum
    mov al, 0xd4
    out 0x64, al
    call ps2_exspecta_introitum
    pop rax
    out 0x60, al
    call ps2_exspecta_exitum
    in al, 0x60
    ret

ps2_constitue:
    call ps2_exhauri
    call ps2_exspecta_introitum
    mov al, 0xae
    out 0x64, al
    call ps2_exspecta_introitum
    mov al, 0xa8
    out 0x64, al

    call ps2_exspecta_introitum
    mov al, 0x20
    out 0x64, al
    call ps2_exspecta_exitum
    in al, 0x60
    mov bl, al
    or bl, 0x03
    and bl, 0xcf
    call ps2_exspecta_introitum
    mov al, 0x60
    out 0x64, al
    call ps2_exspecta_introitum
    mov al, bl
    out 0x60, al

    mov al, 0xf6
    call ps2_muri_mitte
    mov al, 0xf4
    call ps2_muri_mitte

    call ps2_exspecta_introitum
    mov al, 0xf4
    out 0x60, al
    call ps2_exspecta_exitum
    in al, 0x60
    ret

interruptio_clavis:
    push rax
    push rbx
    push rdx
    xor eax, eax
    in al, 0x60
    mov qword ptr [0x3000030], rax
    inc qword ptr [0x3000038]
    mov rbx, qword ptr [0x3000040]
    mov rdx, rbx
    and edx, 63
    mov byte ptr [rdx + 0x3000300], al
    inc rbx
    mov qword ptr [0x3000040], rbx
    mov al, 0x20
    out 0x20, al
    pop rdx
    pop rbx
    pop rax
    iretq

interruptio_temporis:
    push rax
    inc qword ptr [0x3000050]
    mov al, 0x20
    out 0x20, al
    pop rax
    iretq

interruptio_muris:
    push rax
    push rbx
    push rdx
    xor eax, eax
    in al, 0x60
    mov bl, byte ptr [0x3000020]
    cmp bl, 0
    je .primum
    cmp bl, 1
    je .secundum

    mov byte ptr [0x3000023], al
    mov byte ptr [0x3000020], 0

    movzx eax, byte ptr [0x3000021]
    and eax, 7
    mov qword ptr [0x3000010], rax

    movsx rax, byte ptr [0x3000022]
    mov rbx, qword ptr [0x3000000]
    add rbx, rax
    test rbx, rbx
    jns .x_non_negativum
    xor ebx, ebx
.x_non_negativum:
    cmp rbx, 306
    jle .x_paratum
    mov ebx, 306
.x_paratum:
    mov qword ptr [0x3000000], rbx

    movsx rax, byte ptr [0x3000023]
    mov rbx, qword ptr [0x3000008]
    sub rbx, rax
    test rbx, rbx
    jns .y_non_negativum
    xor ebx, ebx
.y_non_negativum:
    cmp rbx, 186
    jle .y_paratum
    mov ebx, 186
.y_paratum:
    mov qword ptr [0x3000008], rbx
    inc qword ptr [0x3000018]
    jmp .agnosce

.primum:
    test al, 8
    jz .agnosce
    mov byte ptr [0x3000021], al
    mov byte ptr [0x3000020], 1
    jmp .agnosce

.secundum:
    mov byte ptr [0x3000022], al
    mov byte ptr [0x3000020], 2

.agnosce:
    mov al, 0x20
    out 0xa0, al
    out 0x20, al
    pop rdx
    pop rbx
    pop rax
    iretq

descriptio_idt:
    .word 4095
    .quad 0x5000
