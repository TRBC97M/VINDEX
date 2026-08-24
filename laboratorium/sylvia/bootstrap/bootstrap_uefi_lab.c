/*
 * LABORATORIUM SYLVIAE — bootstrap UEFI experimentalis.
 *
 * Haec unica exceptio pre-VINDEX est. Post saltum nullum runtime C manet.
 * Memoria nuclei et metadata fixa servantur; pila et acervus a firmware
 * separatim reservantur, ne unus tractus XLIV MiB allocationem UEFI frangat.
 */

typedef unsigned char      U8;
typedef unsigned short     U16;
typedef unsigned int       U32;
typedef unsigned long long U64;
typedef U64                UINTN;
typedef U64                EFI_STATUS;
typedef void              *EFI_HANDLE;
typedef U64                EFI_PHYSICAL_ADDRESS;

#define EFIAPI __attribute__((ms_abi))
#define EFI_SUCCESS 0
#define COMMUNIS 0x03000000ULL
#define META      (COMMUNIS + 0x800ULL)
#define UMBRA     (COMMUNIS + 0x1000ULL)
#define NUCLEUS_BASE 0x00400000ULL
#define TEXTUS_BASE  0x00430000ULL
#define NUCLEUS_LIMEN (TEXTUS_BASE - NUCLEUS_BASE)
#define NUCLEUS_PAGINAE 49ULL
#define COMMUNIS_PAGINAE 25ULL
#define ACERVUS_PAGINAE 2048ULL
#define PILA_PAGINAE 256ULL

typedef struct {
    U64 Signature;
    U32 Revision;
    U32 HeaderSize;
    U32 CRC32;
    U32 Reserved;
} EFI_TABLE_HEADER;

typedef struct {
    U32 Data1;
    U16 Data2;
    U16 Data3;
    U8 Data4[8];
} EFI_GUID;

typedef struct {
    U32 RedMask;
    U32 GreenMask;
    U32 BlueMask;
    U32 ReservedMask;
} EFI_PIXEL_BITMASK;

typedef struct {
    U32 Version;
    U32 HorizontalResolution;
    U32 VerticalResolution;
    U32 PixelFormat;
    EFI_PIXEL_BITMASK PixelInformation;
    U32 PixelsPerScanLine;
} EFI_GRAPHICS_OUTPUT_MODE_INFORMATION;

typedef struct {
    U32 MaxMode;
    U32 Mode;
    EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *Info;
    UINTN SizeOfInfo;
    EFI_PHYSICAL_ADDRESS FrameBufferBase;
    UINTN FrameBufferSize;
} EFI_GRAPHICS_OUTPUT_PROTOCOL_MODE;

typedef struct _EFI_GRAPHICS_OUTPUT_PROTOCOL EFI_GRAPHICS_OUTPUT_PROTOCOL;
struct _EFI_GRAPHICS_OUTPUT_PROTOCOL {
    EFI_STATUS (EFIAPI *QueryMode)(EFI_GRAPHICS_OUTPUT_PROTOCOL *, U32, UINTN *, EFI_GRAPHICS_OUTPUT_MODE_INFORMATION **);
    EFI_STATUS (EFIAPI *SetMode)(EFI_GRAPHICS_OUTPUT_PROTOCOL *, U32);
    void *Blt;
    EFI_GRAPHICS_OUTPUT_PROTOCOL_MODE *Mode;
};

typedef struct _EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL;
struct _EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL {
    void *Reset;
    EFI_STATUS (EFIAPI *OutputString)(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *, const U16 *);
};

typedef struct _EFI_BOOT_SERVICES EFI_BOOT_SERVICES;
struct _EFI_BOOT_SERVICES {
    EFI_TABLE_HEADER Hdr;
    void *RaiseTPL;
    void *RestoreTPL;
    EFI_STATUS (EFIAPI *AllocatePages)(U32, U32, UINTN, EFI_PHYSICAL_ADDRESS *);
    void *FreePages;
    void *GetMemoryMap;
    void *AllocatePool;
    void *FreePool;
    void *CreateEvent;
    void *SetTimer;
    void *WaitForEvent;
    void *SignalEvent;
    void *CloseEvent;
    void *CheckEvent;
    void *InstallProtocolInterface;
    void *ReinstallProtocolInterface;
    void *UninstallProtocolInterface;
    void *HandleProtocol;
    void *Reserved;
    void *RegisterProtocolNotify;
    void *LocateHandle;
    void *LocateDevicePath;
    void *InstallConfigurationTable;
    void *LoadImage;
    void *StartImage;
    void *Exit;
    void *UnloadImage;
    void *ExitBootServices;
    void *GetNextMonotonicCount;
    void *Stall;
    EFI_STATUS (EFIAPI *SetWatchdogTimer)(UINTN, U64, UINTN, const U16 *);
    void *ConnectController;
    void *DisconnectController;
    void *OpenProtocol;
    void *CloseProtocol;
    void *OpenProtocolInformation;
    void *ProtocolsPerHandle;
    void *LocateHandleBuffer;
    EFI_STATUS (EFIAPI *LocateProtocol)(EFI_GUID *, void *, void **);
};

typedef struct {
    EFI_TABLE_HEADER Hdr;
    U16 *FirmwareVendor;
    U32 FirmwareRevision;
    U32 _pad;
    EFI_HANDLE ConsoleInHandle;
    void *ConIn;
    EFI_HANDLE ConsoleOutHandle;
    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *ConOut;
    EFI_HANDLE StandardErrorHandle;
    void *StdErr;
    void *RuntimeServices;
    EFI_BOOT_SERVICES *BootServices;
    UINTN NumberOfTableEntries;
    void *ConfigurationTable;
} EFI_SYSTEM_TABLE;

extern U8 _binary_nucleus_elf_start[];
extern U8 _binary_nucleus_elf_end[];
extern U8 _binary_textus_bin_start[];
extern U8 _binary_textus_bin_end[];
extern U8 _binary_forma_bin_start[];

static EFI_GUID guid_graphica = {
    0x9042a9de, 0x23dc, 0x4a38,
    {0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}
};

static void dic(EFI_SYSTEM_TABLE *systema, const U16 *textus) {
    if (systema && systema->ConOut && systema->ConOut->OutputString) {
        systema->ConOut->OutputString(systema->ConOut, textus);
    }
}

static void memoria_vacua(void *destinatio, UINTN mensura) {
    U8 *d = (U8 *)destinatio;
    while (mensura != 0) {
        *d++ = 0;
        mensura--;
    }
}

static void memoria_copia(void *destinatio, const void *fons, UINTN mensura) {
    U8 *d = (U8 *)destinatio;
    const U8 *s = (const U8 *)fons;
    while (mensura != 0) {
        *d++ = *s++;
        mensura--;
    }
}

__attribute__((noreturn)) static void ad_vindex_sali(U64 ingressus, U64 pila_summa) {
    __asm__ volatile (
        "mov %1, %%rsp\n\t"
        "and $-16, %%rsp\n\t"
        "call *%0\n\t"
        "1: hlt\n\t"
        "jmp 1b\n\t"
        : : "r"(ingressus), "r"(pila_summa) : "memory"
    );
    __builtin_unreachable();
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago, EFI_SYSTEM_TABLE *systema) {
    EFI_GRAPHICS_OUTPUT_PROTOCOL *graphica = 0;
    EFI_PHYSICAL_ADDRESS nucleus = NUCLEUS_BASE;
    EFI_PHYSICAL_ADDRESS communis = COMMUNIS;
    EFI_PHYSICAL_ADDRESS acervus = 0;
    EFI_PHYSICAL_ADDRESS pila = 0;
    U64 kernel_mensura = (U64)(_binary_nucleus_elf_end - _binary_nucleus_elf_start);
    U64 textus_mensura = (U64)(_binary_textus_bin_end - _binary_textus_bin_start);
    volatile U64 *meta = (volatile U64 *)META;
    EFI_STATUS status;
    U32 latitudo;
    U32 altitudo;
    U64 ingressus;

    if (!systema || !systema->BootServices) return 1;
    systema->BootServices->SetWatchdogTimer(0, 0, 0, 0);
    dic(systema, L"SYLVIA LABORATORIUM: INITIUM\r\n");

    if (kernel_mensura > NUCLEUS_LIMEN || textus_mensura > 4096) {
        dic(systema, L"LAB: MAGNITUDO NUCLEI INVALIDA\r\n");
        return 1;
    }

    status = systema->BootServices->AllocatePages(2, 2, NUCLEUS_PAGINAE, &nucleus);
    if (status != EFI_SUCCESS || nucleus != NUCLEUS_BASE) {
        dic(systema, L"LAB: MEMORIA NUCLEI DEFECIT\r\n");
        return status ? status : 1;
    }

    status = systema->BootServices->AllocatePages(2, 2, COMMUNIS_PAGINAE, &communis);
    if (status != EFI_SUCCESS || communis != COMMUNIS) {
        dic(systema, L"LAB: MEMORIA COMMUNIS DEFECIT\r\n");
        return status ? status : 1;
    }

    status = systema->BootServices->AllocatePages(0, 2, ACERVUS_PAGINAE, &acervus);
    if (status != EFI_SUCCESS || acervus == 0) {
        dic(systema, L"LAB: ACERVUS DEFECIT\r\n");
        return status ? status : 1;
    }

    status = systema->BootServices->AllocatePages(0, 2, PILA_PAGINAE, &pila);
    if (status != EFI_SUCCESS || pila == 0) {
        dic(systema, L"LAB: PILA DEFECIT\r\n");
        return status ? status : 1;
    }

    status = systema->BootServices->LocateProtocol(&guid_graphica, 0, (void **)&graphica);
    if (status != EFI_SUCCESS || !graphica || !graphica->Mode || !graphica->Mode->Info) {
        dic(systema, L"LAB: GOP NON INVENTUM\r\n");
        return status ? status : 1;
    }

    if (graphica->Mode->Info->PixelFormat > 1 ||
        graphica->Mode->Info->HorizontalResolution < 640 ||
        graphica->Mode->Info->VerticalResolution < 480) {
        U32 modus;
        U32 electus = 0xffffffffU;
        U64 area_optima = 0;
        for (modus = 0; modus < graphica->Mode->MaxMode; modus++) {
            EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *info = 0;
            UINTN mensura_info = 0;
            if (graphica->QueryMode(graphica, modus, &mensura_info, &info) == EFI_SUCCESS && info) {
                U64 area = (U64)info->HorizontalResolution * info->VerticalResolution;
                if (info->PixelFormat <= 1 && info->HorizontalResolution >= 640 &&
                    info->VerticalResolution >= 480 && area > area_optima) {
                    electus = modus;
                    area_optima = area;
                }
            }
        }
        if (electus == 0xffffffffU || graphica->SetMode(graphica, electus) != EFI_SUCCESS) {
            dic(systema, L"LAB: MODUS GOP DEFECIT\r\n");
            return 1;
        }
    }

    latitudo = graphica->Mode->Info->HorizontalResolution;
    altitudo = graphica->Mode->Info->VerticalResolution;
    if (latitudo < 640 || altitudo < 480 || graphica->Mode->FrameBufferBase == 0) {
        dic(systema, L"LAB: FRAMEBUFFER INVALIDUM\r\n");
        return 1;
    }

    memoria_vacua((void *)(UINTN)COMMUNIS, 0x19000);
    memoria_copia((void *)(UINTN)NUCLEUS_BASE, _binary_nucleus_elf_start, (UINTN)kernel_mensura);
    memoria_copia((void *)(UINTN)TEXTUS_BASE, _binary_textus_bin_start, (UINTN)textus_mensura);

    ((volatile U64 *)COMMUNIS)[0] = latitudo / 2;
    ((volatile U64 *)COMMUNIS)[1] = altitudo / 2;

    meta[0] = 1;
    meta[1] = (U64)(UINTN)systema;
    meta[2] = graphica->Mode->FrameBufferBase;
    meta[3] = graphica->Mode->Info->PixelsPerScanLine;
    meta[4] = latitudo;
    meta[5] = altitudo;
    meta[6] = graphica->Mode->Info->PixelFormat;
    meta[7] = (U64)(UINTN)imago;
    meta[8] = 0;
    meta[9] = 0;
    meta[10] = UMBRA;
    meta[11] = (U64)(UINTN)_binary_forma_bin_start;
    meta[12] = 0;
    meta[13] = 0;
    meta[14] = 0;
    meta[15] = 0;
    meta[16] = (U64)acervus;
    meta[17] = ACERVUS_PAGINAE * 4096ULL;
    meta[18] = 0;
    meta[19] = 0;
    meta[20] = (U64)pila;
    meta[21] = PILA_PAGINAE * 4096ULL;

    ingressus = *(U64 *)(UINTN)(NUCLEUS_BASE + 24);
    dic(systema, L"LAB: SALTUS AD VINDEX\r\n");
    ad_vindex_sali(ingressus, (U64)pila + PILA_PAGINAE * 4096ULL - 16ULL);
}
