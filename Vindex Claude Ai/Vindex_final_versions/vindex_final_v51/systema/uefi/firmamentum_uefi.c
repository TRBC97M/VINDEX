/* VINDEX Systema 0.51 — ponticulus UEFI x86-64 sine libc. */

typedef unsigned char      U8;
typedef unsigned short     U16;
typedef unsigned int       U32;
typedef unsigned long long U64;
typedef signed int         I32;
typedef signed long long   I64;
typedef U64                UINTN;
typedef U64                EFI_STATUS;
typedef void              *EFI_HANDLE;
typedef U64                EFI_PHYSICAL_ADDRESS;
typedef U16                CHAR16;

#define EFIAPI __attribute__((ms_abi))
#define EFI_SUCCESS 0
#define COMMUNIS 0x03000000ULL
#define META      (COMMUNIS + 0x800ULL)
#define UMBRA     (COMMUNIS + 0x1000ULL)
#define TABULA_FS (COMMUNIS + 0x11000ULL)
#define MENSURA_FS 32768ULL
#define EFI_FILE_MODE_READ   0x0000000000000001ULL
#define EFI_FILE_MODE_WRITE  0x0000000000000002ULL
#define EFI_FILE_MODE_CREATE 0x8000000000000000ULL

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
    U8  Data4[8];
} EFI_GUID;

typedef struct _EFI_FILE_PROTOCOL EFI_FILE_PROTOCOL;
struct _EFI_FILE_PROTOCOL {
    U64 Revision;
    EFI_STATUS (EFIAPI *Open)(EFI_FILE_PROTOCOL *, EFI_FILE_PROTOCOL **,
                              CHAR16 *, U64, U64);
    EFI_STATUS (EFIAPI *Close)(EFI_FILE_PROTOCOL *);
    void *Delete;
    EFI_STATUS (EFIAPI *Read)(EFI_FILE_PROTOCOL *, UINTN *, void *);
    EFI_STATUS (EFIAPI *Write)(EFI_FILE_PROTOCOL *, UINTN *, void *);
    void *GetPosition;
    EFI_STATUS (EFIAPI *SetPosition)(EFI_FILE_PROTOCOL *, U64);
    void *GetInfo;
    void *SetInfo;
    EFI_STATUS (EFIAPI *Flush)(EFI_FILE_PROTOCOL *);
    void *OpenEx;
    void *ReadEx;
    void *WriteEx;
    void *FlushEx;
};

typedef struct _EFI_SIMPLE_FILE_SYSTEM_PROTOCOL EFI_SIMPLE_FILE_SYSTEM_PROTOCOL;
struct _EFI_SIMPLE_FILE_SYSTEM_PROTOCOL {
    U64 Revision;
    EFI_STATUS (EFIAPI *OpenVolume)(EFI_SIMPLE_FILE_SYSTEM_PROTOCOL *,
                                    EFI_FILE_PROTOCOL **);
};

typedef struct {
    U32 Revision;
    U32 _pad0;
    EFI_HANDLE ParentHandle;
    void *SystemTable;
    EFI_HANDLE DeviceHandle;
    void *FilePath;
    void *Reserved;
    U32 LoadOptionsSize;
    U32 _pad1;
    void *LoadOptions;
    void *ImageBase;
    U64 ImageSize;
    U32 ImageCodeType;
    U32 ImageDataType;
    void *Unload;
} EFI_LOADED_IMAGE_PROTOCOL;

typedef struct {
    U32 MediaId;
    U8 RemovableMedia;
    U8 MediaPresent;
    U8 LogicalPartition;
    U8 ReadOnly;
    U8 WriteCaching;
    U32 BlockSize;
    U32 IoAlign;
    U64 LastBlock;
    U64 LowestAlignedLba;
    U32 LogicalBlocksPerPhysicalBlock;
    U32 OptimalTransferLengthGranularity;
} EFI_BLOCK_IO_MEDIA;

typedef struct _EFI_BLOCK_IO_PROTOCOL EFI_BLOCK_IO_PROTOCOL;
struct _EFI_BLOCK_IO_PROTOCOL {
    U64 Revision;
    EFI_BLOCK_IO_MEDIA *Media;
    EFI_STATUS (EFIAPI *Reset)(EFI_BLOCK_IO_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *ReadBlocks)(EFI_BLOCK_IO_PROTOCOL *, U32, U64,
                                    UINTN, void *);
    EFI_STATUS (EFIAPI *WriteBlocks)(EFI_BLOCK_IO_PROTOCOL *, U32, U64,
                                     UINTN, void *);
    EFI_STATUS (EFIAPI *FlushBlocks)(EFI_BLOCK_IO_PROTOCOL *);
};

typedef struct {
    U16 ScanCode;
    CHAR16 UnicodeChar;
} EFI_INPUT_KEY;

typedef struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL EFI_SIMPLE_TEXT_INPUT_PROTOCOL;
struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_SIMPLE_TEXT_INPUT_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *ReadKeyStroke)(EFI_SIMPLE_TEXT_INPUT_PROTOCOL *, EFI_INPUT_KEY *);
    void *WaitForKey;
};

typedef struct _EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL;
struct _EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *OutputString)(EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *, const CHAR16 *);
    void *TestString;
    void *QueryMode;
    void *SetMode;
    void *SetAttribute;
    void *ClearScreen;
    void *SetCursorPosition;
    void *EnableCursor;
    void *Mode;
};

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

typedef struct {
    U8 Blue;
    U8 Green;
    U8 Red;
    U8 Reserved;
} EFI_GRAPHICS_OUTPUT_BLT_PIXEL;

typedef struct _EFI_GRAPHICS_OUTPUT_PROTOCOL EFI_GRAPHICS_OUTPUT_PROTOCOL;
struct _EFI_GRAPHICS_OUTPUT_PROTOCOL {
    EFI_STATUS (EFIAPI *QueryMode)(EFI_GRAPHICS_OUTPUT_PROTOCOL *, U32, UINTN *, EFI_GRAPHICS_OUTPUT_MODE_INFORMATION **);
    EFI_STATUS (EFIAPI *SetMode)(EFI_GRAPHICS_OUTPUT_PROTOCOL *, U32);
    EFI_STATUS (EFIAPI *Blt)(EFI_GRAPHICS_OUTPUT_PROTOCOL *, EFI_GRAPHICS_OUTPUT_BLT_PIXEL *, U32,
                             UINTN, UINTN, UINTN, UINTN, UINTN, UINTN, UINTN);
    EFI_GRAPHICS_OUTPUT_PROTOCOL_MODE *Mode;
};

typedef struct {
    I32 RelativeMovementX;
    I32 RelativeMovementY;
    I32 RelativeMovementZ;
    U8 LeftButton;
    U8 RightButton;
} EFI_SIMPLE_POINTER_STATE;

typedef struct {
    U64 ResolutionX;
    U64 ResolutionY;
    U64 ResolutionZ;
    U8 LeftButton;
    U8 RightButton;
} EFI_SIMPLE_POINTER_MODE;

typedef struct _EFI_SIMPLE_POINTER_PROTOCOL EFI_SIMPLE_POINTER_PROTOCOL;
struct _EFI_SIMPLE_POINTER_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_SIMPLE_POINTER_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *GetState)(EFI_SIMPLE_POINTER_PROTOCOL *, EFI_SIMPLE_POINTER_STATE *);
    void *WaitForInput;
    EFI_SIMPLE_POINTER_MODE *Mode;
};

typedef struct {
    U64 CurrentX;
    U64 CurrentY;
    U64 CurrentZ;
    U32 ActiveButtons;
} EFI_ABSOLUTE_POINTER_STATE;

typedef struct {
    U64 AbsoluteMinX;
    U64 AbsoluteMinY;
    U64 AbsoluteMinZ;
    U64 AbsoluteMaxX;
    U64 AbsoluteMaxY;
    U64 AbsoluteMaxZ;
    U32 Attributes;
} EFI_ABSOLUTE_POINTER_MODE;

typedef struct _EFI_ABSOLUTE_POINTER_PROTOCOL EFI_ABSOLUTE_POINTER_PROTOCOL;
struct _EFI_ABSOLUTE_POINTER_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_ABSOLUTE_POINTER_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *GetState)(EFI_ABSOLUTE_POINTER_PROTOCOL *, EFI_ABSOLUTE_POINTER_STATE *);
    void *WaitForInput;
    EFI_ABSOLUTE_POINTER_MODE *Mode;
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
    EFI_STATUS (EFIAPI *FreePool)(void *);
    void *CreateEvent;
    void *SetTimer;
    void *WaitForEvent;
    void *SignalEvent;
    void *CloseEvent;
    void *CheckEvent;
    void *InstallProtocolInterface;
    void *ReinstallProtocolInterface;
    void *UninstallProtocolInterface;
    EFI_STATUS (EFIAPI *HandleProtocol)(EFI_HANDLE, EFI_GUID *, void **);
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
    EFI_STATUS (EFIAPI *Stall)(UINTN);
    EFI_STATUS (EFIAPI *SetWatchdogTimer)(UINTN, U64, UINTN, const CHAR16 *);
    void *ConnectController;
    void *DisconnectController;
    void *OpenProtocol;
    void *CloseProtocol;
    void *OpenProtocolInformation;
    void *ProtocolsPerHandle;
    EFI_STATUS (EFIAPI *LocateHandleBuffer)(U32, EFI_GUID *, void *,
                                            UINTN *, EFI_HANDLE **);
    EFI_STATUS (EFIAPI *LocateProtocol)(EFI_GUID *, void *, void **);
};

typedef struct {
    EFI_TABLE_HEADER Hdr;
    CHAR16 *FirmwareVendor;
    U32 FirmwareRevision;
    U32 _pad;
    EFI_HANDLE ConsoleInHandle;
    EFI_SIMPLE_TEXT_INPUT_PROTOCOL *ConIn;
    EFI_HANDLE ConsoleOutHandle;
    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *ConOut;
    EFI_HANDLE StandardErrorHandle;
    EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL *StdErr;
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
extern U8 _binary_forma_bin_end[];

static EFI_SYSTEM_TABLE *tabula_systematis;
static EFI_SIMPLE_POINTER_PROTOCOL *murus_relativus;
static EFI_ABSOLUTE_POINTER_PROTOCOL *murus_absolutus;
static EFI_GRAPHICS_OUTPUT_PROTOCOL *graphica_globalis;
static EFI_GRAPHICS_OUTPUT_BLT_PIXEL *tabula_pixelorum;
static EFI_FILE_PROTOCOL *fasciculus_voluminis;
static EFI_BLOCK_IO_PROTOCOL *volumen_crudum;
static U8 volumen_mutabile;
static U64 signum_umbrae;
static I64 murus_x_paratus = 160;
static I64 murus_y_paratus = 100;
static U64 bullae_crudae;
static U64 bullae_stabiles;
static U64 tempus_bullarum;
static U8 murus_paratus;

static EFI_GUID guid_graphica = {0x9042a9de, 0x23dc, 0x4a38, {0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}};
static EFI_GUID guid_muris = {0x31878c87, 0x0b75, 0x11d5, {0x9a,0x4f,0x00,0x90,0x27,0x3f,0xc1,0x4d}};
static EFI_GUID guid_muris_absoluti = {0x8d59d32b, 0xc655, 0x4ae9, {0x9b,0x15,0xf2,0x59,0x04,0x99,0x2a,0x43}};
static EFI_GUID guid_imaginis_onustae = {0x5b1b31a1, 0x9562, 0x11d2, {0x8e,0x3f,0x00,0xa0,0xc9,0x69,0x72,0x3b}};
static EFI_GUID guid_systematis_fasciculorum = {0x964e5b22, 0x6459, 0x11d2, {0x8e,0x39,0x00,0xa0,0xc9,0x69,0x72,0x3b}};
static EFI_GUID guid_blocalis = {0x964e5b21, 0x6459, 0x11d2, {0x8e,0x39,0x00,0xa0,0xc9,0x69,0x72,0x3b}};

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

static U8 memoria_aequalis(const void *a, const void *b, UINTN mensura) {
    const U8 *x = (const U8 *)a;
    const U8 *y = (const U8 *)b;
    while (mensura != 0) {
        if (*x++ != *y++) return 0;
        mensura--;
    }
    return 1;
}

static U64 memoria_signa(const void *fons, UINTN mensura) {
    const U8 *p = (const U8 *)fons;
    U64 signum = 1469598103934665603ULL;
    while (mensura != 0) {
        signum ^= *p++;
        signum *= 1099511628211ULL;
        mensura--;
    }
    return signum;
}

/* Via FAT subsidium manet pro firmware sine partitione binali exposita. */
static EFI_STATUS fasciculum_lege(void) {
    UINTN mensura = MENSURA_FS;
    EFI_STATUS status;
    if (!fasciculus_voluminis) return 1;
    memoria_vacua((void *)(UINTN)TABULA_FS, MENSURA_FS);
    status = fasciculus_voluminis->SetPosition(fasciculus_voluminis, 0);
    if (status != EFI_SUCCESS) return status;
    return fasciculus_voluminis->Read(fasciculus_voluminis, &mensura,
                                      (void *)(UINTN)TABULA_FS);
}

static EFI_STATUS fasciculum_scribe(void) {
    UINTN mensura = MENSURA_FS;
    EFI_STATUS status;
    U64 signum;
    if (!fasciculus_voluminis || !volumen_mutabile) return 1;
    signum = memoria_signa((void *)(UINTN)TABULA_FS, MENSURA_FS);
    status = fasciculus_voluminis->SetPosition(fasciculus_voluminis, 0);
    if (status != EFI_SUCCESS) return status;
    status = fasciculus_voluminis->Write(fasciculus_voluminis, &mensura,
                                         (void *)(UINTN)TABULA_FS);
    if (status != EFI_SUCCESS || mensura != MENSURA_FS)
        return status == EFI_SUCCESS ? 1 : status;
    status = fasciculus_voluminis->Flush(fasciculus_voluminis);
    if (status != EFI_SUCCESS) return status;
    status = fasciculum_lege();
    if (status != EFI_SUCCESS) return status;
    return memoria_signa((void *)(UINTN)TABULA_FS, MENSURA_FS) == signum ? 0 : 1;
}

static EFI_STATUS volumen_apere(EFI_HANDLE imago) {
    EFI_LOADED_IMAGE_PROTOCOL *onusta = 0;
    EFI_SIMPLE_FILE_SYSTEM_PROTOCOL *systema_fasciculorum = 0;
    EFI_FILE_PROTOCOL *radix = 0;
    EFI_STATUS status;
    status = tabula_systematis->BootServices->HandleProtocol(
        imago, &guid_imaginis_onustae, (void **)&onusta);
    if (status != EFI_SUCCESS || !onusta) return status;
    status = tabula_systematis->BootServices->HandleProtocol(
        onusta->DeviceHandle, &guid_systematis_fasciculorum,
        (void **)&systema_fasciculorum);
    if (status != EFI_SUCCESS || !systema_fasciculorum) return status;
    status = systema_fasciculorum->OpenVolume(systema_fasciculorum, &radix);
    if (status != EFI_SUCCESS || !radix) return status;
    status = radix->Open(radix, &fasciculus_voluminis, L"VINDEX.FS",
        EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE | EFI_FILE_MODE_CREATE, 0);
    if (status == EFI_SUCCESS) volumen_mutabile = 1;
    else {
        status = radix->Open(radix, &fasciculus_voluminis, L"VINDEX.FS",
                             EFI_FILE_MODE_READ, 0);
        volumen_mutabile = 0;
    }
    radix->Close(radix);
    if (status != EFI_SUCCESS || !fasciculus_voluminis) return status;
    return fasciculum_lege();
}

static EFI_STATUS volumen_crudum_lege(void) {
    EFI_BLOCK_IO_MEDIA *m;
    if (!volumen_crudum || !volumen_crudum->Media) return 1;
    m = volumen_crudum->Media;
    memoria_vacua((void *)(UINTN)TABULA_FS, MENSURA_FS);
    return volumen_crudum->ReadBlocks(volumen_crudum, m->MediaId, 1,
        MENSURA_FS, (void *)(UINTN)TABULA_FS);
}

static EFI_STATUS volumen_crudum_scribe(void) {
    EFI_BLOCK_IO_MEDIA *m;
    EFI_STATUS status;
    U64 signum;
    if (!volumen_crudum || !volumen_crudum->Media || !volumen_mutabile) return 1;
    m = volumen_crudum->Media;
    signum = memoria_signa((void *)(UINTN)TABULA_FS, MENSURA_FS);
    status = volumen_crudum->WriteBlocks(volumen_crudum, m->MediaId, 1,
        MENSURA_FS, (void *)(UINTN)TABULA_FS);
    if (status != EFI_SUCCESS) return status;
    status = volumen_crudum->FlushBlocks(volumen_crudum);
    if (status != EFI_SUCCESS) return status;
    status = volumen_crudum_lege();
    if (status != EFI_SUCCESS) return status;
    return memoria_signa((void *)(UINTN)TABULA_FS, MENSURA_FS) == signum ? 0 : 1;
}

/* Partitionem signo VINDEXV0 invenit; structuram VINDEX non interpretatur. */
static EFI_STATUS volumen_crudum_inveni(void) {
    static const U8 signum[8] = {'V','I','N','D','E','X','V','0'};
    EFI_HANDLE *manubria = 0;
    UINTN numerus = 0;
    UINTN i;
    EFI_STATUS status = tabula_systematis->BootServices->LocateHandleBuffer(
        2, &guid_blocalis, 0, &numerus, &manubria);
    if (status != EFI_SUCCESS || !manubria) return status;
    for (i = 0; i < numerus; i++) {
        EFI_BLOCK_IO_PROTOCOL *b = 0;
        status = tabula_systematis->BootServices->HandleProtocol(
            manubria[i], &guid_blocalis, (void **)&b);
        if (status != EFI_SUCCESS || !b || !b->Media) continue;
        if (!b->Media->MediaPresent || !b->Media->LogicalPartition ||
            b->Media->BlockSize != 512 || b->Media->LastBlock < 64) continue;
        if (b->Media->IoAlign > 1 &&
            (TABULA_FS & (b->Media->IoAlign - 1)) != 0) continue;
        memoria_vacua((void *)(UINTN)TABULA_FS, 512);
        status = b->ReadBlocks(b, b->Media->MediaId, 0, 512,
                               (void *)(UINTN)TABULA_FS);
        if (status == EFI_SUCCESS &&
            memoria_aequalis((void *)(UINTN)TABULA_FS, signum, 8) &&
            *(U32 *)(UINTN)(TABULA_FS + 8) == 1 &&
            *(U32 *)(UINTN)(TABULA_FS + 12) == MENSURA_FS) {
            volumen_crudum = b;
            volumen_mutabile = b->Media->ReadOnly ? 0 : 1;
            break;
        }
    }
    tabula_systematis->BootServices->FreePool(manubria);
    if (!volumen_crudum) {
        memoria_vacua((void *)(UINTN)TABULA_FS, MENSURA_FS);
        return 1;
    }
    status = volumen_crudum_lege();
    if (status != EFI_SUCCESS) volumen_crudum = 0;
    return status;
}

static EFI_STATUS volumen_lege(void) {
    if (volumen_crudum) return volumen_crudum_lege();
    return fasciculum_lege();
}

static EFI_STATUS volumen_scribe(void) {
    if (volumen_crudum) return volumen_crudum_scribe();
    return fasciculum_scribe();
}

static void mandatum_voluminis_exsequere(void) {
    volatile U64 *meta = (volatile U64 *)META;
    U64 mandatum = meta[13];
    EFI_STATUS status;
    if (mandatum == 0) return;
    meta[13] = 0;
    if (mandatum == 1) status = volumen_scribe();
    else if (mandatum == 2) status = volumen_lege();
    else status = 1;
    meta[14] = status == EFI_SUCCESS ? 1 : 2;
}

static const U8 paletta[16][3] = {
    {0,0,0},       {0,0,170},     {0,170,0},     {0,170,170},
    {170,0,0},     {170,0,170},   {170,85,0},    {170,170,170},
    {85,85,85},    {85,85,255},   {85,255,85},   {85,255,255},
    {255,85,85},   {255,85,255},  {255,255,85},  {255,255,255}
};

/* Mutationes tabulae logicae detegit sine auxilio nuclei VINDEX. */
static U64 umbram_signa(void) {
    const U8 *umbra = (const U8 *)(UINTN)UMBRA;
    U64 signum = 1469598103934665603ULL;
    UINTN i;
    for (i = 0; i < 320U * 200U; i++) {
        signum ^= umbra[i];
        signum *= 1099511628211ULL;
    }
    return signum;
}

/* Umbram expandit et framebuffer directe scribit, sine BLT firmware. */
static void imaginem_praesenta(void) {
    EFI_GRAPHICS_OUTPUT_PROTOCOL *g = graphica_globalis;
    const U8 *umbra = (const U8 *)(UINTN)UMBRA;
    U32 latitudo;
    U32 altitudo;
    U32 y_logicus = 0;
    U64 error_y = 0;
    U32 y;

    if (!g || !g->Mode || !g->Mode->Info || !tabula_pixelorum) return;
    latitudo = g->Mode->Info->HorizontalResolution;
    altitudo = g->Mode->Info->VerticalResolution;
    if (g->Mode->FrameBufferBase == 0 ||
        g->Mode->Info->PixelsPerScanLine < latitudo ||
        g->Mode->FrameBufferSize <
            (UINTN)g->Mode->Info->PixelsPerScanLine * altitudo * 4)
        return;

    for (y = 0; y < altitudo; y++) {
        const U8 *linea_fontis = umbra + y_logicus * 320;
        EFI_GRAPHICS_OUTPUT_BLT_PIXEL *linea_exitus = tabula_pixelorum + (UINTN)y * latitudo;
        U32 x_logicus = 0;
        U64 error_x = 0;
        U32 x;
        for (x = 0; x < latitudo; x++) {
            U8 color = linea_fontis[x_logicus] & 15;
            linea_exitus[x].Blue = paletta[color][2];
            linea_exitus[x].Green = paletta[color][1];
            linea_exitus[x].Red = paletta[color][0];
            linea_exitus[x].Reserved = 0;
            error_x += 320;
            if (error_x >= latitudo) {
                error_x -= latitudo;
                if (x_logicus < 319) x_logicus++;
            }
        }
        error_y += 200;
        if (error_y >= altitudo) {
            error_y -= altitudo;
            if (y_logicus < 199) y_logicus++;
        }
    }

    if (g->Mode->Info->PixelFormat == 1) {
        for (y = 0; y < altitudo; y++) {
            U8 *destinatio = (U8 *)(UINTN)(g->Mode->FrameBufferBase +
                (UINTN)y * g->Mode->Info->PixelsPerScanLine * 4);
            memoria_copia(destinatio,
                tabula_pixelorum + (UINTN)y * latitudo, (UINTN)latitudo * 4);
        }
    } else {
        for (y = 0; y < altitudo; y++) {
            U32 x;
            for (x = 0; x < latitudo; x++) {
                EFI_GRAPHICS_OUTPUT_BLT_PIXEL p =
                    tabula_pixelorum[(UINTN)y * latitudo + x];
                U8 *destinatio = (U8 *)(UINTN)(g->Mode->FrameBufferBase +
                    ((UINTN)y * g->Mode->Info->PixelsPerScanLine + x) * 4);
                destinatio[0] = p.Red;
                destinatio[1] = p.Green;
                destinatio[2] = p.Blue;
                destinatio[3] = 0;
            }
        }
    }
}

static void nuntia(const CHAR16 *textus) {
    if (tabula_systematis && tabula_systematis->ConOut)
        tabula_systematis->ConOut->OutputString(tabula_systematis->ConOut, textus);
}

static void clavis_inpone(U8 clavis) {
    volatile U64 *caput = (volatile U64 *)(COMMUNIS + 0x40);
    volatile U8 *circulus = (volatile U8 *)(COMMUNIS + 0x300);
    U64 index = *caput;
    circulus[index & 63] = clavis;
    *caput = index + 1;
}

static U8 clavis_litterae(CHAR16 c) {
    switch (c) {
        case 'a': return 16; case 'z': return 17; case 'e': return 18;
        case 'r': return 19; case 't': return 20; case 'y': return 21;
        case 'u': return 22; case 'i': return 23; case 'o': return 24;
        case 'p': return 25; case 'q': return 30; case 's': return 31;
        case 'd': return 32; case 'f': return 33; case 'g': return 34;
        case 'h': return 35; case 'j': return 36; case 'k': return 37;
        case 'l': return 38; case 'm': return 39; case 'w': return 44;
        case 'x': return 45; case 'c': return 46; case 'v': return 47;
        case 'b': return 48; case 'n': return 49;
        default: return 0;
    }
}

static void unicode_inpone(CHAR16 c) {
    U8 maior = 0;
    U8 clavis = 0;
    if (c >= 'A' && c <= 'Z') {
        maior = 1;
        c = (CHAR16)(c + ('a' - 'A'));
    }
    clavis = clavis_litterae(c);
    if (clavis != 0) {
        if (maior) clavis_inpone(42);
        clavis_inpone(clavis);
        if (maior) clavis_inpone(170);
        return;
    }
    if (c >= '1' && c <= '9') clavis = (U8)(2 + c - '1');
    else if (c == '0') clavis = 11;
    else if (c == ' ') clavis = 57;
    else if (c == 8) clavis = 14;
    else if (c == 13 || c == 10) clavis = 28;
    else if (c == ',') clavis = 50;
    else if (c == ';') clavis = 51;
    else if (c == ':') clavis = 52;
    else if (c == '!') clavis = 53;
    if (clavis != 0) clavis_inpone(clavis);
}

static I64 motus_normalis(I32 valor, U64 resolutio) {
    I64 motus;
    if (valor == 0) return 0;
    if (resolutio == 0) motus = valor;
    else motus = ((I64)valor * 6) / (I64)resolutio;
    if (motus == 0) motus = valor < 0 ? -1 : 1;
    if (motus > 32) motus = 32;
    if (motus < -32) motus = -32;
    return motus;
}

/* Motum statim recipit, sed bullas duas vicissitudines stabiles exspectat. */
static void muri_statum_para(I64 x, I64 y, U64 bullae) {
    volatile U64 *communis = (volatile U64 *)COMMUNIS;
    if (x < 0) x = 0;
    if (y < 0) y = 0;
    if (x > 306) x = 306;
    if (y > 186) y = 186;
    murus_x_paratus = x;
    murus_y_paratus = y;
    murus_paratus = 1;
    if (bullae != bullae_crudae) {
        bullae_crudae = bullae;
        tempus_bullarum = communis[10];
    }
}

static void muri_statum_confirma(void) {
    volatile U64 *communis = (volatile U64 *)COMMUNIS;
    if (!murus_paratus) return;
    if (bullae_crudae != bullae_stabiles && communis[10] - tempus_bullarum >= 2)
        bullae_stabiles = bullae_crudae;
    if (communis[0] != (U64)murus_x_paratus ||
        communis[1] != (U64)murus_y_paratus || communis[2] != bullae_stabiles) {
        communis[0] = (U64)murus_x_paratus;
        communis[1] = (U64)murus_y_paratus;
        communis[2] = bullae_stabiles;
        communis[3]++;
    }
}

U64 firmamentum_polle(void) {
    EFI_INPUT_KEY clavis;
    volatile U64 *communis = (volatile U64 *)COMMUNIS;
    U64 novum_signum;
    U32 i;

    mandatum_voluminis_exsequere();
    novum_signum = umbram_signa();
    if (novum_signum != signum_umbrae) {
        imaginem_praesenta();
        signum_umbrae = novum_signum;
    }

    tabula_systematis->BootServices->Stall(10000);
    communis[10]++;

    for (i = 0; i < 8; i++) {
        if (tabula_systematis->ConIn->ReadKeyStroke(tabula_systematis->ConIn, &clavis) != EFI_SUCCESS)
            break;
        if (clavis.UnicodeChar != 0) unicode_inpone(clavis.UnicodeChar);
        else {
            if (clavis.ScanCode == 1) clavis_inpone(72);
            else if (clavis.ScanCode == 2) clavis_inpone(80);
            else if (clavis.ScanCode == 3) clavis_inpone(77);
            else if (clavis.ScanCode == 4) clavis_inpone(75);
            else if (clavis.ScanCode == 9) clavis_inpone(73);
            else if (clavis.ScanCode == 10) clavis_inpone(81);
            else if (clavis.ScanCode == 0x17) clavis_inpone(1);
        }
    }

    if (murus_absolutus && murus_absolutus->Mode) {
        EFI_ABSOLUTE_POINTER_STATE status;
        if (murus_absolutus->GetState(murus_absolutus, &status) == EFI_SUCCESS) {
            EFI_ABSOLUTE_POINTER_MODE *m = murus_absolutus->Mode;
            U64 dx = m->AbsoluteMaxX - m->AbsoluteMinX;
            U64 dy = m->AbsoluteMaxY - m->AbsoluteMinY;
            if (dx && dy) {
                I64 x = (I64)((status.CurrentX - m->AbsoluteMinX) * 306 / dx);
                I64 y = (I64)((status.CurrentY - m->AbsoluteMinY) * 186 / dy);
                muri_statum_para(x, y, status.ActiveButtons & 1);
                muri_statum_confirma();
                return 0;
            }
        }
    }

    if (murus_relativus && murus_relativus->Mode) {
        EFI_SIMPLE_POINTER_STATE status;
        if (murus_relativus->GetState(murus_relativus, &status) == EFI_SUCCESS) {
            I64 x = (I64)communis[0] + motus_normalis(status.RelativeMovementX, murus_relativus->Mode->ResolutionX);
            I64 y = (I64)communis[1] + motus_normalis(status.RelativeMovementY, murus_relativus->Mode->ResolutionY);
            muri_statum_para(x, y, status.LeftButton ? 1 : 0);
        }
    }
    muri_statum_confirma();
    return 0;
}

__attribute__((noreturn)) static void nucleum_voca(U64 ingressus) {
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
    EFI_STATUS status;
    U32 latitudo;
    U32 altitudo;
    EFI_PHYSICAL_ADDRESS memoria_pixelorum = 0;
    UINTN mensura_pixelorum;
    volatile U64 *meta = (volatile U64 *)META;
    U64 ingressus;
    UINTN i;
    tabula_systematis = systema;
    systema->BootServices->SetWatchdogTimer(0, 0, 0, 0);
    nuntia(L"VINDEX SYSTEMA: UEFI INITIUM...\r\n");

    status = systema->BootServices->AllocatePages(2, 2, paginae, &initium_memoriae);
    if (status != EFI_SUCCESS || initium_memoriae != 0x00400000ULL) {
        nuntia(L"ERRATUM: MEMORIA NUCLEI NON LIBERA.\r\n");
        return status;
    }
    if (kernel_mensura > 122880 || textus_mensura > 4096) {
        nuntia(L"ERRATUM: SARCINA NUCLEI NIMIS MAGNA.\r\n");
        return 1;
    }

    status = systema->BootServices->LocateProtocol(&guid_graphica, 0, (void **)&graphica);
    if (status != EFI_SUCCESS || !graphica || !graphica->Mode || !graphica->Mode->Info) {
        nuntia(L"ERRATUM: GOP GRAPHICA DEEST.\r\n");
        return status;
    }

    if (graphica->Mode->Info->PixelFormat > 1) {
        U32 modus;
        U32 electus = 0xffffffffU;
        U64 area_optima = 0;
        for (modus = 0; modus < graphica->Mode->MaxMode; modus++) {
            EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *info = 0;
            UINTN mensura_info = 0;
            if (graphica->QueryMode(graphica, modus, &mensura_info, &info) == EFI_SUCCESS && info) {
                U64 area = (U64)info->HorizontalResolution * info->VerticalResolution;
                if (info->PixelFormat <= 1 && info->HorizontalResolution >= 320 && info->VerticalResolution >= 200 && area > area_optima) {
                    electus = modus;
                    area_optima = area;
                }
            }
        }
        if (electus == 0xffffffffU || graphica->SetMode(graphica, electus) != EFI_SUCCESS) {
            nuntia(L"ERRATUM: FORMATUM PIXELORUM INCOMPATIBILE.\r\n");
            return 1;
        }
    }

    latitudo = graphica->Mode->Info->HorizontalResolution;
    altitudo = graphica->Mode->Info->VerticalResolution;
    if (latitudo < 320 || altitudo < 200) {
        nuntia(L"ERRATUM: RESOLUTIO NIMIS PARVA.\r\n");
        return 1;
    }
    mensura_pixelorum = (UINTN)latitudo * altitudo * sizeof(EFI_GRAPHICS_OUTPUT_BLT_PIXEL);
    status = systema->BootServices->AllocatePages(0, 2,
        (mensura_pixelorum + 4095) / 4096, &memoria_pixelorum);
    if (status != EFI_SUCCESS || memoria_pixelorum == 0) {
        nuntia(L"ERRATUM: DUPLEX TABULA GRAPHICA NON PARATA.\r\n");
        return status;
    }
    tabula_pixelorum = (EFI_GRAPHICS_OUTPUT_BLT_PIXEL *)(UINTN)memoria_pixelorum;
    graphica_globalis = graphica;

    memoria_vacua((void *)(UINTN)graphica->Mode->FrameBufferBase, graphica->Mode->FrameBufferSize);
    memoria_vacua((void *)(UINTN)COMMUNIS, 0x19000);
    status = volumen_crudum_inveni();
    if (status != EFI_SUCCESS) status = volumen_apere(imago);
    memoria_copia((void *)(UINTN)0x00400000ULL, _binary_nucleus_elf_start, (UINTN)kernel_mensura);
    memoria_copia((void *)(UINTN)0x0041e000ULL, _binary_textus_bin_start, (UINTN)textus_mensura);

    ((volatile U64 *)COMMUNIS)[0] = 160;
    ((volatile U64 *)COMMUNIS)[1] = 100;
    meta[0] = 1;
    meta[1] = (U64)(UINTN)&firmamentum_polle;
    meta[2] = graphica->Mode->FrameBufferBase;
    meta[3] = graphica->Mode->Info->PixelsPerScanLine;
    meta[4] = latitudo;
    meta[5] = altitudo;
    meta[6] = graphica->Mode->Info->PixelFormat;
    meta[7] = 0;
    meta[8] = 0;
    meta[9] = 0;
    meta[10] = UMBRA;
    meta[11] = (U64)(UINTN)_binary_forma_bin_start;
    meta[12] = (volumen_crudum || fasciculus_voluminis) ?
               (volumen_mutabile ? 1 : 2) : 0;
    meta[13] = 0;
    meta[14] = status == EFI_SUCCESS ? 1 : 2;
    meta[15] = volumen_crudum ? 1 : (fasciculus_voluminis ? 2 : 0);
    signum_umbrae = 0;

    systema->BootServices->LocateProtocol(&guid_muris_absoluti, 0, (void **)&murus_absolutus);
    systema->BootServices->LocateProtocol(&guid_muris, 0, (void **)&murus_relativus);
    if (murus_absolutus) murus_absolutus->Reset(murus_absolutus, 0);
    if (murus_relativus) murus_relativus->Reset(murus_relativus, 0);
    systema->ConIn->Reset(systema->ConIn, 0);

    ingressus = *(U64 *)(UINTN)(0x00400000ULL + 24);
    for (i = 0; i < 1; i++) { /* nexus explicite retentus */ }
    nucleum_voca(ingressus);
}
