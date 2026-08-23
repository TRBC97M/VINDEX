/* Sylvia OS — Fenestrale II, Gradus A.
 * Probatio UEFI resolutionis nativae sine superficie hereditaria 320x200.
 * Haec applicatio non substituit systema principale: viam graphicam futuram probat.
 */

typedef unsigned char U8;
typedef unsigned short U16;
typedef unsigned int U32;
typedef unsigned long long U64;
typedef unsigned long long UINTN;
typedef unsigned long long EFI_STATUS;
typedef void *EFI_HANDLE;
typedef U16 CHAR16;

#define EFIAPI __attribute__((ms_abi))
#define EFI_SUCCESS 0
#define EFI_SCAN_ESC 0x0017

typedef struct { U64 Signature; U32 Revision; U32 HeaderSize; U32 CRC32; U32 Reserved; } EFI_TABLE_HEADER;
typedef struct { U32 Data1; U16 Data2; U16 Data3; U8 Data4[8]; } EFI_GUID;

typedef struct { U16 ScanCode; CHAR16 UnicodeChar; } EFI_INPUT_KEY;
typedef struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL EFI_SIMPLE_TEXT_INPUT_PROTOCOL;
struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_SIMPLE_TEXT_INPUT_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *ReadKeyStroke)(EFI_SIMPLE_TEXT_INPUT_PROTOCOL *, EFI_INPUT_KEY *);
    void *WaitForKey;
};

typedef struct { U32 RedMask; U32 GreenMask; U32 BlueMask; U32 ReservedMask; } EFI_PIXEL_BITMASK;

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
    U64 FrameBufferBase;
    UINTN FrameBufferSize;
} EFI_GRAPHICS_OUTPUT_PROTOCOL_MODE;

typedef struct { U8 Blue; U8 Green; U8 Red; U8 Reserved; } EFI_GRAPHICS_OUTPUT_BLT_PIXEL;

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
    void *RaiseTPL; void *RestoreTPL; void *AllocatePages; void *FreePages; void *GetMemoryMap;
    void *AllocatePool; EFI_STATUS (EFIAPI *FreePool)(void *);
    void *CreateEvent; void *SetTimer; void *WaitForEvent; void *SignalEvent; void *CloseEvent; void *CheckEvent;
    void *InstallProtocolInterface; void *ReinstallProtocolInterface; void *UninstallProtocolInterface;
    void *HandleProtocol; void *Reserved; void *RegisterProtocolNotify; void *LocateHandle; void *LocateDevicePath;
    void *InstallConfigurationTable; void *LoadImage; void *StartImage; void *Exit; void *UnloadImage; void *ExitBootServices;
    void *GetNextMonotonicCount;
    EFI_STATUS (EFIAPI *Stall)(UINTN);
    void *SetWatchdogTimer; void *ConnectController; void *DisconnectController; void *OpenProtocol; void *CloseProtocol;
    void *OpenProtocolInformation; void *ProtocolsPerHandle; void *LocateHandleBuffer;
    EFI_STATUS (EFIAPI *LocateProtocol)(EFI_GUID *, void *, void **);
};

typedef struct {
    EFI_TABLE_HEADER Hdr;
    CHAR16 *FirmwareVendor; U32 FirmwareRevision; U32 _pad;
    EFI_HANDLE ConsoleInHandle; EFI_SIMPLE_TEXT_INPUT_PROTOCOL *ConIn;
    EFI_HANDLE ConsoleOutHandle; void *ConOut;
    EFI_HANDLE StandardErrorHandle; void *StdErr;
    void *RuntimeServices; EFI_BOOT_SERVICES *BootServices;
    UINTN NumberOfTableEntries; void *ConfigurationTable;
} EFI_SYSTEM_TABLE;

static EFI_GUID guid_graphica = {0x9042a9de,0x23dc,0x4a38,{0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}};
static EFI_GRAPHICS_OUTPUT_PROTOCOL *gop;
static U32 latitudo;
static U32 altitudo;
static U32 linea;
static U32 formatum;
static U8 *framebuffer;
static EFI_BOOT_SERVICES *opera;

static U32 color(U8 r, U8 g, U8 b) {
    if (formatum == 0) return ((U32)r) | ((U32)g << 8) | ((U32)b << 16);
    return ((U32)b) | ((U32)g << 8) | ((U32)r << 16);
}

static void rect(U32 x, U32 y, U32 w, U32 h, U32 c) {
    U32 yy;
    if (x >= latitudo || y >= altitudo) return;
    if (x + w > latitudo) w = latitudo - x;
    if (y + h > altitudo) h = altitudo - y;
    for (yy = 0; yy < h; yy++) {
        U32 *p = ((U32 *)framebuffer) + (UINTN)(y + yy) * linea + x;
        U32 xx;
        for (xx = 0; xx < w; xx++) p[xx] = c;
    }
}

static void margo(U32 x, U32 y, U32 w, U32 h, U32 c) {
    if (w < 2 || h < 2) return;
    rect(x,y,w,1,c); rect(x,y+h-1,w,1,c); rect(x,y,1,h,c); rect(x+w-1,y,1,h,c);
}

/* Forma litterarum VxVII minima ad probationem; non est font canonica futura. */
static U8 glyph(char c, U8 row) {
    static const U8 A[7]={14,17,17,31,17,17,17}; static const U8 B[7]={30,17,17,30,17,17,30};
    static const U8 C[7]={14,17,16,16,16,17,14}; static const U8 D[7]={30,17,17,17,17,17,30};
    static const U8 E[7]={31,16,16,30,16,16,31}; static const U8 F[7]={31,16,16,30,16,16,16};
    static const U8 G[7]={14,17,16,23,17,17,15}; static const U8 H[7]={17,17,17,31,17,17,17};
    static const U8 I[7]={31,4,4,4,4,4,31}; static const U8 L[7]={16,16,16,16,16,16,31};
    static const U8 M[7]={17,27,21,21,17,17,17}; static const U8 N[7]={17,25,21,19,17,17,17};
    static const U8 O[7]={14,17,17,17,17,17,14}; static const U8 P[7]={30,17,17,30,16,16,16};
    static const U8 R[7]={30,17,17,30,20,18,17}; static const U8 S[7]={15,16,16,14,1,1,30};
    static const U8 T[7]={31,4,4,4,4,4,4}; static const U8 U[7]={17,17,17,17,17,17,14};
    static const U8 V[7]={17,17,17,17,17,10,4}; static const U8 Y[7]={17,17,10,4,4,4,4};
    const U8 *p=0;
    switch(c){case 'A':p=A;break;case 'B':p=B;break;case 'C':p=C;break;case 'D':p=D;break;case 'E':p=E;break;
    case 'F':p=F;break;case 'G':p=G;break;case 'H':p=H;break;case 'I':p=I;break;case 'L':p=L;break;
    case 'M':p=M;break;case 'N':p=N;break;case 'O':p=O;break;case 'P':p=P;break;case 'R':p=R;break;
    case 'S':p=S;break;case 'T':p=T;break;case 'U':p=U;break;case 'V':p=V;break;case 'Y':p=Y;break;default:return 0;}
    return p[row];
}

static void text(U32 x,U32 y,const char *s,U32 c,U32 scala) {
    while (*s) {
        char ch=*s++;
        if (ch==' ') { x += 4*scala; continue; }
        for (U8 r=0;r<7;r++) {
            U8 bits=glyph(ch,r);
            for (U8 b=0;b<5;b++) if (bits & (16>>b)) rect(x+b*scala,y+r*scala,scala,scala,c);
        }
        x += 6*scala;
    }
}

static void wallpaper(void) {
    U32 y;
    U32 c0r=6,c0g=27,c0b=49,c1r=11,c1g=79,c1b=130;
    for (y=0;y<altitudo;y++) {
        U32 t=(U64)y*255/(altitudo?altitudo:1);
        U8 r=(U8)((c1r*(255-t)+c0r*t)/255);
        U8 g=(U8)((c1g*(255-t)+c0g*t)/255);
        U8 b=(U8)((c1b*(255-t)+c0b*t)/255);
        rect(0,y,latitudo,1,color(r,g,b));
    }
    for (U32 i=0;i<3;i++) {
        U32 yy=altitudo*52/100+i*38;
        U32 x0=latitudo*18/100;
        U32 w=latitudo*72/100-i*80;
        if (yy<altitudo) rect(x0+i*42,yy,w,1,color(56,126,164));
    }
}

static void fenestra(U32 x,U32 y,U32 w,U32 h,const char *titulus,U8 activa) {
    U32 umbra=color(3,15,25), corpus=color(241,238,228), arg=color(185,196,207), bron=color(185,138,82);
    U32 aqua=color(98,215,242), rub=color(168,58,58);
    rect(x+5,y+6,w,h,umbra);
    rect(x,y,w,h,corpus); margo(x,y,w,h,activa?bron:arg);
    for(U32 i=0;i<28 && i<h;i++) {
        U8 r=(U8)(activa ? 26 - i/3 : 61 - i/4);
        U8 g=(U8)(activa ? 93 - i : 91 - i/2);
        U8 b=(U8)(activa ? 146 - i : 103 - i/2);
        rect(x+1,y+1+i,w-2,1,color(r,g,b));
    }
    rect(x+1,y+1,w-2,1,color(234,248,255));
    text(x+10,y+9,titulus,color(234,248,255),1);
    rect(x+w-64,y+4,18,20,arg); margo(x+w-64,y+4,18,20,color(91,119,135));
    rect(x+w-43,y+4,18,20,arg); margo(x+w-43,y+4,18,20,color(91,119,135));
    rect(x+w-22,y+4,18,20,rub); margo(x+w-22,y+4,18,20,color(96,30,30));
    rect(x+1,y+29,w-2,22,color(241,238,228));
    rect(x+1,y+51,w-2,34,color(226,232,234));
    rect(x+1,y+85,w-2,h>106?h-106:1,color(248,249,247));
    rect(x+1,y+h-20,w-2,19,color(226,230,230));
    if (activa) rect(x+2,y+28,w-4,1,aqua);
}

static void scena(void) {
    U32 task=28;
    U32 w1=latitudo*52/100,h1=altitudo*60/100;
    U32 x1=latitudo*12/100,y1=altitudo*9/100;
    U32 w2=latitudo*34/100,h2=altitudo*42/100;
    U32 x2=latitudo*58/100,y2=altitudo*20/100;
    wallpaper();
    text(latitudo-180,24,"SYLVIA OS",color(234,248,255),2);
    fenestra(x1,y1,w1,h1,"PROGRAMMATA",1);
    fenestra(x2,y2,w2,h2,"TABULA",0);
    rect(x1+1,y1+85,150,h1-106,color(222,232,235));
    rect(x1+12,y1+103,126,24,color(26,93,146));
    text(x1+25,y1+112,"OMNIA",color(234,248,255),1);
    rect(x1+170,y1+113,260,112,color(237,244,247));
    margo(x1+170,y1+113,260,112,color(26,93,146));
    text(x1+190,y1+142,"TABULA",color(8,35,61),2);
    rect(0,altitudo-task,latitudo,task,color(8,35,61));
    rect(0,altitudo-task,latitudo,1,color(98,215,242));
    rect(4,altitudo-24,82,20,color(14,66,111)); margo(4,altitudo-24,82,20,color(64,119,151));
    text(16,altitudo-18,"INITIUM",color(234,248,255),1);
    rect(96,altitudo-24,168,20,color(26,93,146)); margo(96,altitudo-24,168,20,color(64,119,151));
    text(108,altitudo-18,"PROGRAMMATA",color(234,248,255),1);
}

static EFI_STATUS elige_modum(void) {
    U32 optimus=gop->Mode->Mode;
    U64 area_optima=0;
    U32 m;
    for(m=0;m<gop->Mode->MaxMode;m++) {
        EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *i=0;
        UINTN sz=0;
        if(gop->QueryMode(gop,m,&sz,&i)==EFI_SUCCESS && i) {
            U64 area=(U64)i->HorizontalResolution*i->VerticalResolution;
            if(i->PixelFormat<=1 && i->HorizontalResolution>=1024 && i->VerticalResolution>=600 && area>area_optima) {
                optimus=m; area_optima=area;
            }
            if (opera && opera->FreePool) opera->FreePool(i);
        }
    }
    if(area_optima && optimus!=gop->Mode->Mode) return gop->SetMode(gop,optimus);
    return EFI_SUCCESS;
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago, EFI_SYSTEM_TABLE *systema) {
    EFI_STATUS st;
    EFI_INPUT_KEY clavis;
    (void)imago;
    opera=systema->BootServices;
    st=systema->BootServices->LocateProtocol(&guid_graphica,0,(void **)&gop);
    if(st!=EFI_SUCCESS || !gop || !gop->Mode || !gop->Mode->Info) return 1;
    st=elige_modum();
    if(st!=EFI_SUCCESS || !gop->Mode->Info) return st;
    latitudo=gop->Mode->Info->HorizontalResolution;
    altitudo=gop->Mode->Info->VerticalResolution;
    linea=gop->Mode->Info->PixelsPerScanLine;
    formatum=gop->Mode->Info->PixelFormat;
    framebuffer=(U8 *)(UINTN)gop->Mode->FrameBufferBase;
    if(formatum>1 || !framebuffer || latitudo<640 || altitudo<480) return 1;
    scena();
    for(;;) {
        if(systema->ConIn && systema->ConIn->ReadKeyStroke(systema->ConIn,&clavis)==EFI_SUCCESS) {
            if(clavis.ScanCode==EFI_SCAN_ESC) break;
        }
        systema->BootServices->Stall(16000);
    }
    return EFI_SUCCESS;
}
