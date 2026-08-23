/*
 * Sylvia OS / VINDEX — ponticulus UEFI minimus.
 *
 * Hic fasciculus solum initium firmware perficit:
 *   1. memoriam initialem reservat;
 *   2. framebuffer GOP compatibile obtinet;
 *   3. imaginem nuclei VINDEX et data initii in memoriam transfert;
 *   4. metadata firmware minima VINDEX tradit;
 *   5. semel ad ingressum VINDEX salit.
 *
 * Nullum input, volumen, compositorium, fenestram, ansam eventuum aut
 * callback runtime praebet. Post saltum VINDEX hunc codicem non revocat.
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
    void *ConOut;
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

__attribute__((noreturn)) static void ad_vindex_sali(U64 ingressus) {
    /* Solum mutatio pilae et saltus initii; nullum ministerium runtime. */
    __asm__ volatile (
        "mov $0x1000000, %%rsp\n\t"
        "and $-16, %%rsp\n\t"
        "call *%0\n\t"
        "1: hlt\n\t"
        "jmp 1b\n\t"
        : : "r"(ingressus) : "memory"
    );
    __builtin_unreachable();
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago, EFI_SYSTEM_TABLE *systema) {
    EFI_GRAPHICS_OUTPUT_PROTOCOL *graphica = 0;
    EFI_PHYSICAL_ADDRESS initium_memoriae = 0x00400000ULL;
    UINTN paginae = (0x03019000ULL - 0x00400000ULL) / 4096;
    U64 kernel_mensura = (U64)(_binary_nucleus_elf_end - _binary_nucleus_elf_start);
    U64 textus_mensura = (U64)(_binary_textus_bin_end - _binary_textus_bin_start);
    volatile U64 *meta = (volatile U64 *)META;
    EFI_STATUS status;
    U32 latitudo;
    U32 altitudo;
    U64 ingressus;

    if (!systema || !systema->BootServices) return 1;
    systema->BootServices->SetWatchdogTimer(0, 0, 0, 0);

    status = systema->BootServices->AllocatePages(2, 2, paginae, &initium_memoriae);
    if (status != EFI_SUCCESS || initium_memoriae != 0x00400000ULL) return status ? status : 1;
    if (kernel_mensura > 122880 || textus_mensura > 4096) return 1;

    status = systema->BootServices->LocateProtocol(&guid_graphica, 0, (void **)&graphica);
    if (status != EFI_SUCCESS || !graphica || !graphica->Mode || !graphica->Mode->Info) return status ? status : 1;

    if (graphica->Mode->Info->PixelFormat > 1 ||
        graphica->Mode->Info->HorizontalResolution < 320 ||
        graphica->Mode->Info->VerticalResolution < 200) {
        U32 modus;
        U32 electus = 0xffffffffU;
        U64 area_optima = 0;
        for (modus = 0; modus < graphica->Mode->MaxMode; modus++) {
            EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *info = 0;
            UINTN mensura_info = 0;
            if (graphica->QueryMode(graphica, modus, &mensura_info, &info) == EFI_SUCCESS && info) {
                U64 area = (U64)info->HorizontalResolution * info->VerticalResolution;
                if (info->PixelFormat <= 1 && info->HorizontalResolution >= 320 &&
                    info->VerticalResolution >= 200 && area > area_optima) {
                    electus = modus;
                    area_optima = area;
                }
            }
        }
        if (electus == 0xffffffffU || graphica->SetMode(graphica, electus) != EFI_SUCCESS) return 1;
    }

    latitudo = graphica->Mode->Info->HorizontalResolution;
    altitudo = graphica->Mode->Info->VerticalResolution;
    if (latitudo < 320 || altitudo < 200 || graphica->Mode->FrameBufferBase == 0) return 1;

    memoria_vacua((void *)(UINTN)COMMUNIS, 0x19000);
    memoria_copia((void *)(UINTN)0x00400000ULL, _binary_nucleus_elf_start, (UINTN)kernel_mensura);
    memoria_copia((void *)(UINTN)0x0041e000ULL, _binary_textus_bin_start, (UINTN)textus_mensura);

    ((volatile U64 *)COMMUNIS)[0] = 160;
    ((volatile U64 *)COMMUNIS)[1] = 100;

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

    ingressus = *(U64 *)(UINTN)(0x00400000ULL + 24);
    ad_vindex_sali(ingressus);
}
