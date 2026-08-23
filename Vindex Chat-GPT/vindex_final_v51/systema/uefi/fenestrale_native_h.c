/* Sylvia OS — Fenestrale II, Gradus H.
 * Compositorium UEFI experimentale separatum quod mailbox Gradus G vere
 * administrat et clientem PROGRAMMATA VINDEX in superficie privata exsequitur.
 * Nulla pars huius fasciculi firmware canonicum 0.51 substituit.
 */

typedef unsigned char U8;
typedef unsigned short U16;
typedef unsigned int U32;
typedef unsigned long long U64;
typedef signed int I32;
typedef unsigned long long UINTN;
typedef unsigned long long EFI_STATUS;
typedef unsigned long long EFI_PHYSICAL_ADDRESS;
typedef void *EFI_HANDLE;
typedef U16 CHAR16;

#define EFIAPI __attribute__((ms_abi))
#define EFI_SUCCESS 0
#define EFI_SCAN_UP 0x0001
#define EFI_SCAN_DOWN 0x0002
#define EFI_SCAN_RIGHT 0x0003
#define EFI_SCAN_LEFT 0x0004
#define EFI_SCAN_ESC 0x0017
#define EFI_ALLOCATE_ADDRESS 2
#define EfiLoaderData 2
#define COMMUNIS_INITIUM 0x03000000ULL
#define COMMUNIS_PAGINAE 16ULL
#define CLIENT_INITIUM 0x00400000ULL

#include "../fenestrale_ii_compositor_abi.h"

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
    EFI_STATUS (EFIAPI *FreePages)(EFI_PHYSICAL_ADDRESS, UINTN);
    void *GetMemoryMap;
    EFI_STATUS (EFIAPI *AllocatePool)(U32, UINTN, void **);
    EFI_STATUS (EFIAPI *FreePool)(void *);
    void *CreateEvent; void *SetTimer; void *WaitForEvent; void *SignalEvent; void *CloseEvent; void *CheckEvent;
    void *InstallProtocolInterface; void *ReinstallProtocolInterface; void *UninstallProtocolInterface;
    void *HandleProtocol; void *Reserved; void *RegisterProtocolNotify; void *LocateHandle; void *LocateDevicePath;
    void *InstallConfigurationTable; void *LoadImage; void *StartImage; void *Exit; void *UnloadImage; void *ExitBootServices;
    void *GetNextMonotonicCount;
    EFI_STATUS (EFIAPI *Stall)(UINTN);
    EFI_STATUS (EFIAPI *SetWatchdogTimer)(UINTN, U64, UINTN, const CHAR16 *);
    void *ConnectController; void *DisconnectController; void *OpenProtocol; void *CloseProtocol;
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

typedef struct {
    U32 *pix;
    U32 w;
    U32 h;
    U32 x;
    U32 y;
    U32 formatum;
    U64 id;
    U64 client;
    U8 visibilis;
} SUPERFICIES_H;

extern U8 _binary_programmata_g_elf_start[];
extern U8 _binary_programmata_g_elf_end[];

static EFI_GUID guid_graphica = {0x9042a9de,0x23dc,0x4a38,{0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}};
static EFI_GRAPHICS_OUTPUT_PROTOCOL *gop;
static EFI_BOOT_SERVICES *opera;
static U32 *framebuffer;
static U32 latitudo;
static U32 altitudo;
static U32 linea;
static U32 formatum;
static SUPERFICIES_H client_surface;

static void memoria_vacua(void *p, UINTN n) { U8 *q=(U8 *)p; while(n--) *q++=0; }
static void memoria_copia(void *d,const void *s,UINTN n){U8 *dd=(U8 *)d;const U8 *ss=(const U8 *)s;while(n--)*dd++=*ss++;}
static U32 argb(U8 a,U8 r,U8 g,U8 b){return((U32)a<<24)|((U32)r<<16)|((U32)g<<8)|b;}
static U8 A(U32 c){return(U8)(c>>24);} static U8 R(U32 c){return(U8)(c>>16);}
static U8 G(U32 c){return(U8)(c>>8);} static U8 B(U32 c){return(U8)c;}

static U32 misce(U32 infra,U32 supra){
    U32 a=A(supra),ia=255-a;
    if(a==0)return infra;
    if(a==255)return supra|0xff000000U;
    return argb(255,(U8)((R(supra)*a+R(infra)*ia)/255),(U8)((G(supra)*a+G(infra)*ia)/255),(U8)((B(supra)*a+B(infra)*ia)/255));
}

static void framebuffer_scribe(U32 x,U32 y,U32 c){
    U32 r=R(c),g=G(c),b=B(c),out;
    if(formatum==0)out=r|(g<<8)|(b<<16);else out=b|(g<<8)|(r<<16);
    framebuffer[(UINTN)y*linea+x]=out;
}

static U32 fundum(U32 x,U32 y){
    U32 t=(U64)y*255/(altitudo?altitudo:1);
    U8 r=(U8)((8*(255-t)+5*t)/255);
    U8 g=(U8)((52*(255-t)+24*t)/255);
    U8 b=(U8)((90*(255-t)+48*t)/255);
    U32 c=argb(255,r,g,b);
    U32 arcus_y=altitudo*54/100;
    if(y>=arcus_y&&y<arcus_y+2&&x>latitudo*12/100&&x<latitudo*91/100)c=argb(255,54,132,171);
    if(y>=arcus_y+42&&y<arcus_y+43&&x>latitudo*21/100&&x<latitudo*84/100)c=argb(255,34,103,151);
    return c;
}

static U32 surface_pixel(U32 sx,U32 sy){
    U32 raw=client_surface.pix[(UINTN)sy*client_surface.w+sx];
    U8 a=(U8)(raw>>24),r,g,b;
    if(client_surface.formatum==0){r=(U8)raw;g=(U8)(raw>>8);b=(U8)(raw>>16);}
    else{b=(U8)raw;g=(U8)(raw>>8);r=(U8)(raw>>16);}
    return argb(a,r,g,b);
}

static U32 intra(U32 v,U32 a,U32 b){return v>=a&&v<b;}

static void compone(void){
    U32 barra=28;
    U32 sy0=client_surface.y;
    U32 sx0=client_surface.x;
    U32 sx1=sx0+client_surface.w;
    U32 sy1=sy0+client_surface.h;
    for(U32 y=0;y<altitudo;y++){
        for(U32 x=0;x<latitudo;x++){
            U32 c=fundum(x,y);
            if(client_surface.visibilis){
                if(intra(x,sx0+8,sx1+8)&&intra(y,sy0+8,sy1+8)&&!(intra(x,sx0,sx1)&&intra(y,sy0,sy1)))
                    c=misce(c,argb(64,0,0,0));
                if(intra(x,sx0,sx1)&&intra(y,sy0,sy1))
                    c=misce(c,surface_pixel(x-sx0,y-sy0));
            }
            if(y>=altitudo-barra){
                U32 yy=y-(altitudo-barra);
                c=argb(255,8,35,61);
                if(yy==0)c=argb(255,98,215,242);
                if(yy>=4&&yy<24&&x>=4&&x<88)c=argb(255,14,66,111);
                if(yy>=4&&yy<24&&x>=98&&x<286)c=argb(255,26,93,146);
                if(yy>=9&&yy<15&&x>=18&&x<70)c=argb(255,234,248,255);
                if(yy>=9&&yy<15&&x>=112&&x<220)c=argb(255,234,248,255);
            }
            framebuffer_scribe(x,y,c);
        }
    }
}

static void responsum(FENESTRALE2_COMPOSITOR_MAILBOX *m,U64 codex){
    m->responsum=codex;
    m->seriale_responsi=m->seriale_petitionis;
    m->status=codex==0?FII_CMP_STATUS_PERFECTUM:FII_CMP_STATUS_ERRATUM;
}

static void superficiem_libera(void){
    if(client_surface.pix){opera->FreePool(client_surface.pix);client_surface.pix=0;}
    client_surface.w=client_surface.h=0;client_surface.visibilis=0;client_surface.id=0;
}

static void mailbox_age(void){
    FENESTRALE2_COMPOSITOR_MAILBOX *m=(FENESTRALE2_COMPOSITOR_MAILBOX *)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;
    if(m->status!=FII_CMP_STATUS_PETITUM)return;
    if(m->operatio==FII_CMP_OP_CREA){
        U64 w=m->petita_latitudo,h=m->petita_altitudo;
        if(client_surface.pix||w<320||h<240||w>latitudo-24||h>altitudo-52||w*h>8388608ULL){responsum(m,2);return;}
        void *p=0;
        if(opera->AllocatePool(EfiLoaderData,(UINTN)(w*h*4),&p)!=EFI_SUCCESS||!p){responsum(m,3);return;}
        memoria_vacua(p,(UINTN)(w*h*4));
        client_surface.pix=(U32 *)p;client_surface.w=(U32)w;client_surface.h=(U32)h;
        client_surface.x=(latitudo-client_surface.w)/2;client_surface.y=(altitudo-28-client_surface.h)/2;
        client_surface.formatum=0;client_surface.id=1;client_surface.client=m->client;client_surface.visibilis=0;
        m->superficies_id=client_surface.id;m->basis_pixelorum=(U64)(UINTN)p;
        m->pixel_per_lineam=w;m->formatum_pixelorum=0;m->x=client_surface.x;m->y=client_surface.y;
        responsum(m,0);return;
    }
    if(m->superficies_id!=client_surface.id||m->client!=client_surface.client){responsum(m,4);return;}
    if(m->operatio==FII_CMP_OP_PRAESENTA){client_surface.visibilis=1;compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_MOVE){
        U32 maxx=latitudo>client_surface.w?latitudo-client_surface.w:0;
        U32 maxy=altitudo>28+client_surface.h?altitudo-28-client_surface.h:0;
        client_surface.x=(U32)(m->x>maxx?maxx:m->x);client_surface.y=(U32)(m->y>maxy?maxy:m->y);
        compone();responsum(m,0);return;
    }
    if(m->operatio==FII_CMP_OP_OSTENDE){client_surface.visibilis=1;compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_CELA){client_surface.visibilis=0;compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_FOCUS){responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_DELE){superficiem_libera();compone();responsum(m,0);return;}
    responsum(m,5);
}

static U64 clientem_voca(U64 ingressus){
    U64 (*functio)(void)=(U64 (*)(void))(UINTN)ingressus;
    return functio();
}

static U8 clientem_gradus_init(U64 ingressus){
    FENESTRALE2_COMPOSITOR_MAILBOX *m=(FENESTRALE2_COMPOSITOR_MAILBOX *)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;
    U64 r=clientem_voca(ingressus);
    if(r!=10||m->status!=FII_CMP_STATUS_PETITUM||m->operatio!=FII_CMP_OP_CREA)return 0;
    mailbox_age();
    r=clientem_voca(ingressus);
    if(r!=11||m->status!=FII_CMP_STATUS_PETITUM||m->operatio!=FII_CMP_OP_PRAESENTA)return 0;
    mailbox_age();
    r=clientem_voca(ingressus);
    if(r!=0||m->status!=FII_CMP_STATUS_VACUUM)return 0;
    return 1;
}

static EFI_STATUS modum_elige(EFI_GRAPHICS_OUTPUT_PROTOCOL *g){
    U32 electus=0xffffffffU;U64 area=0;
    for(U32 i=0;i<g->Mode->MaxMode;i++){
        EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *info=0;UINTN mensura=0;
        if(g->QueryMode(g,i,&mensura,&info)==EFI_SUCCESS&&info&&info->PixelFormat<=1&&info->HorizontalResolution>=1024&&info->VerticalResolution>=600){
            U64 a=(U64)info->HorizontalResolution*info->VerticalResolution;
            if(a>area){area=a;electus=i;}
        }
    }
    if(electus==0xffffffffU)return 1;
    if(electus==g->Mode->Mode)return EFI_SUCCESS;
    return g->SetMode(g,electus);
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago,EFI_SYSTEM_TABLE *systema){
    (void)imago;
    EFI_STATUS status;
    opera=systema->BootServices;
    if(opera->SetWatchdogTimer)opera->SetWatchdogTimer(0,0,0,0);
    status=opera->LocateProtocol(&guid_graphica,0,(void **)&gop);
    if(status!=EFI_SUCCESS||!gop||!gop->Mode)return status;
    status=modum_elige(gop);if(status!=EFI_SUCCESS)return status;
    if(!gop->Mode->Info||gop->Mode->Info->PixelFormat>1)return 1;
    latitudo=gop->Mode->Info->HorizontalResolution;altitudo=gop->Mode->Info->VerticalResolution;
    linea=gop->Mode->Info->PixelsPerScanLine;formatum=gop->Mode->Info->PixelFormat;
    framebuffer=(U32 *)(UINTN)gop->Mode->FrameBufferBase;
    if(!framebuffer||linea<latitudo||gop->Mode->FrameBufferSize<(UINTN)linea*altitudo*4)return 1;

    EFI_PHYSICAL_ADDRESS communis=COMMUNIS_INITIUM;
    status=opera->AllocatePages(EFI_ALLOCATE_ADDRESS,EfiLoaderData,COMMUNIS_PAGINAE,&communis);
    if(status!=EFI_SUCCESS||communis!=COMMUNIS_INITIUM)return status;
    memoria_vacua((void *)(UINTN)COMMUNIS_INITIUM,COMMUNIS_PAGINAE*4096);

    UINTN client_mensura=(UINTN)(_binary_programmata_g_elf_end-_binary_programmata_g_elf_start);
    EFI_PHYSICAL_ADDRESS client=CLIENT_INITIUM;
    UINTN client_paginae=(client_mensura+4095)/4096;
    status=opera->AllocatePages(EFI_ALLOCATE_ADDRESS,EfiLoaderData,client_paginae,&client);
    if(status!=EFI_SUCCESS||client!=CLIENT_INITIUM)return status;
    memoria_vacua((void *)(UINTN)CLIENT_INITIUM,client_paginae*4096);
    memoria_copia((void *)(UINTN)CLIENT_INITIUM,_binary_programmata_g_elf_start,client_mensura);
    if(*(U32 *)(UINTN)CLIENT_INITIUM!=0x464c457fU)return 1;
    U64 ingressus=*(U64 *)(UINTN)(CLIENT_INITIUM+24);
    if(ingressus<CLIENT_INITIUM||ingressus>=CLIENT_INITIUM+client_mensura)return 1;

    FENESTRALE2_DESCRIPTOR *d=(FENESTRALE2_DESCRIPTOR *)(UINTN)FENESTRALE2_BASIS;
    d->magic=FENESTRALE2_MAGIC;d->versio=FENESTRALE2_VERSIO;d->mensura=FENESTRALE2_MENSURA;
    d->capacitates=FII_CAP_FRAMEBUFFER_NATIVUS|FII_CAP_PIXEL_RGB_BGR|FII_CAP_COMPOSITORIUM;
    d->framebuffer=gop->Mode->FrameBufferBase;d->latitudo=latitudo;d->altitudo=altitudo;
    d->pixel_per_lineam=linea;d->formatum_pixelorum=formatum;d->bits_per_pixel=32;
    d->murus_x=0;d->murus_y=0;d->bullae=0;d->numerus_eventuum=0;d->taskbar_altitudo=28;d->scala_per_mille=1000;

    FENESTRALE2_COMPOSITOR_MAILBOX *m=(FENESTRALE2_COMPOSITOR_MAILBOX *)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;
    m->magic=FENESTRALE2_COMPOSITOR_MAGIC;m->versio=FENESTRALE2_COMPOSITOR_VERSIO;
    m->mensura=FENESTRALE2_COMPOSITOR_MENSURA;m->status=FII_CMP_STATUS_VACUUM;

    compone();
    if(!clientem_gradus_init(ingressus))return 1;

    if(systema->ConIn)systema->ConIn->Reset(systema->ConIn,0);
    for(;;){
        EFI_INPUT_KEY k;
        if(systema->ConIn&&systema->ConIn->ReadKeyStroke(systema->ConIn,&k)==EFI_SUCCESS){
            if(k.ScanCode==EFI_SCAN_ESC)break;
            if(client_surface.visibilis&&(k.ScanCode==EFI_SCAN_LEFT||k.ScanCode==EFI_SCAN_RIGHT||k.ScanCode==EFI_SCAN_UP||k.ScanCode==EFI_SCAN_DOWN)){
                I32 nx=(I32)client_surface.x,ny=(I32)client_surface.y;
                if(k.ScanCode==EFI_SCAN_LEFT)nx-=12;if(k.ScanCode==EFI_SCAN_RIGHT)nx+=12;
                if(k.ScanCode==EFI_SCAN_UP)ny-=12;if(k.ScanCode==EFI_SCAN_DOWN)ny+=12;
                if(nx<0)nx=0;if(ny<0)ny=0;
                U32 maxx=latitudo>client_surface.w?latitudo-client_surface.w:0;
                U32 maxy=altitudo>28+client_surface.h?altitudo-28-client_surface.h:0;
                if((U32)nx>maxx)nx=(I32)maxx;if((U32)ny>maxy)ny=(I32)maxy;
                client_surface.x=(U32)nx;client_surface.y=(U32)ny;compone();
            }
        }
        opera->Stall(10000);
    }
    superficiem_libera();
    return EFI_SUCCESS;
}
