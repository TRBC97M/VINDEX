/* Sylvia OS — Fenestrale II, Gradus I.
 * Compositorium UEFI experimentale multiplex: PROGRAMMATA et TABULA sunt
 * clientes VINDEX distincti cum superficiebus privatis et z-order dynamico.
 * Via canonica Sylvia OS 0.51 non mutatur.
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
#define CLIENT_PAGINAE 64ULL
#define SUPERFICIES_CAPACITAS 8U

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
    U32 Version; U32 HorizontalResolution; U32 VerticalResolution; U32 PixelFormat;
    EFI_PIXEL_BITMASK PixelInformation; U32 PixelsPerScanLine;
} EFI_GRAPHICS_OUTPUT_MODE_INFORMATION;
typedef struct {
    U32 MaxMode; U32 Mode; EFI_GRAPHICS_OUTPUT_MODE_INFORMATION *Info; UINTN SizeOfInfo;
    EFI_PHYSICAL_ADDRESS FrameBufferBase; UINTN FrameBufferSize;
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
    void *RaiseTPL; void *RestoreTPL;
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
    U32 w, h, x, y, formatum;
    U64 id, client;
    U8 visibilis;
} SUPERFICIES_I;

extern U8 _binary_programmata_h_elf_start[];
extern U8 _binary_programmata_h_elf_end[];
extern U8 _binary_tabula_i_elf_start[];
extern U8 _binary_tabula_i_elf_end[];

static EFI_GUID guid_graphica={0x9042a9de,0x23dc,0x4a38,{0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}};
static EFI_GRAPHICS_OUTPUT_PROTOCOL *gop;
static EFI_BOOT_SERVICES *opera;
static U32 *framebuffer;
static U32 latitudo,altitudo,linea,formatum;
static SUPERFICIES_I superficies[SUPERFICIES_CAPACITAS];
static U8 ordo[SUPERFICIES_CAPACITAS];
static U8 numerus_ordinis;
static U64 proximus_id=1;

static void memoria_vacua(void *p,UINTN n){U8*q=(U8*)p;while(n--)*q++=0;}
static void memoria_copia(void*d,const void*s,UINTN n){U8*dd=(U8*)d;const U8*ss=(const U8*)s;while(n--)*dd++=*ss++;}
static U32 argb(U8 a,U8 r,U8 g,U8 b){return((U32)a<<24)|((U32)r<<16)|((U32)g<<8)|b;}
static U8 A(U32 c){return(U8)(c>>24);} static U8 R(U32 c){return(U8)(c>>16);}
static U8 G(U32 c){return(U8)(c>>8);} static U8 B(U32 c){return(U8)c;}
static U32 misce(U32 infra,U32 supra){U32 a=A(supra),ia=255-a;if(a==0)return infra;if(a==255)return supra|0xff000000U;return argb(255,(U8)((R(supra)*a+R(infra)*ia)/255),(U8)((G(supra)*a+G(infra)*ia)/255),(U8)((B(supra)*a+B(infra)*ia)/255));}

static void framebuffer_scribe(U32 x,U32 y,U32 c){U32 r=R(c),g=G(c),b=B(c),out;if(formatum==0)out=r|(g<<8)|(b<<16);else out=b|(g<<8)|(r<<16);framebuffer[(UINTN)y*linea+x]=out;}
static U32 fundum(U32 x,U32 y){U32 t=(U64)y*255/(altitudo?altitudo:1);U8 r=(U8)((8*(255-t)+5*t)/255),g=(U8)((52*(255-t)+24*t)/255),b=(U8)((90*(255-t)+48*t)/255);U32 c=argb(255,r,g,b);U32 a=altitudo*54/100;if(y>=a&&y<a+2&&x>latitudo*12/100&&x<latitudo*91/100)c=argb(255,54,132,171);if(y>=a+42&&y<a+43&&x>latitudo*21/100&&x<latitudo*84/100)c=argb(255,34,103,151);return c;}
static U32 intra(U32 v,U32 a,U32 b){return v>=a&&v<b;}

static SUPERFICIES_I *inveni(U64 id,U64 client){for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++)if(superficies[i].id==id&&superficies[i].client==client)return&superficies[i];return 0;}
static I32 indicem_liberum(void){for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++)if(superficies[i].id==0)return(I32)i;return-1;}
static U32 pixel_superficiei(const SUPERFICIES_I*s,U32 x,U32 y){U32 raw=s->pix[(UINTN)y*s->w+x];U8 a=(U8)(raw>>24),r,g,b;if(s->formatum==0){r=(U8)raw;g=(U8)(raw>>8);b=(U8)(raw>>16);}else{b=(U8)raw;g=(U8)(raw>>8);r=(U8)(raw>>16);}return argb(a,r,g,b);}

static void ordinem_remove(U8 idx){for(U8 i=0;i<numerus_ordinis;i++){if(ordo[i]==idx){for(U8 j=i;j+1<numerus_ordinis;j++)ordo[j]=ordo[j+1];numerus_ordinis--;return;}}}
static void focus(U8 idx){ordinem_remove(idx);if(numerus_ordinis<SUPERFICIES_CAPACITAS)ordo[numerus_ordinis++]=idx;}
static I32 top_index(void){if(numerus_ordinis==0)return-1;return(I32)ordo[numerus_ordinis-1];}

static void compone(void){
    const U32 barra=28;
    for(U32 y=0;y<altitudo;y++){
        for(U32 x=0;x<latitudo;x++){
            U32 c=fundum(x,y);
            for(U8 k=0;k<numerus_ordinis;k++){
                SUPERFICIES_I*s=&superficies[ordo[k]];
                if(!s->visibilis)continue;
                if(intra(x,s->x+8,s->x+s->w+8)&&intra(y,s->y+8,s->y+s->h+8)&&!(intra(x,s->x,s->x+s->w)&&intra(y,s->y,s->y+s->h)))c=misce(c,argb(45,0,0,0));
                if(intra(x,s->x,s->x+s->w)&&intra(y,s->y,s->y+s->h))c=misce(c,pixel_superficiei(s,x-s->x,y-s->y));
            }
            if(y>=altitudo-barra){
                U32 yy=y-(altitudo-barra);c=argb(255,8,35,61);
                if(yy==0)c=argb(255,98,215,242);
                if(yy>=4&&yy<24&&x>=4&&x<88)c=argb(255,14,66,111);
                if(yy>=4&&yy<24&&x>=98&&x<286)c=(top_index()>=0&&superficies[top_index()].client==1)?argb(255,26,93,146):argb(255,16,55,83);
                if(yy>=4&&yy<24&&x>=292&&x<430)c=(top_index()>=0&&superficies[top_index()].client==2)?argb(255,26,93,146):argb(255,16,55,83);
                if(yy>=9&&yy<15&&x>=18&&x<70)c=argb(255,234,248,255);
                if(yy>=9&&yy<15&&x>=112&&x<220)c=argb(255,234,248,255);
                if(yy>=9&&yy<15&&x>=310&&x<382)c=argb(255,234,248,255);
            }
            framebuffer_scribe(x,y,c);
        }
    }
}

static void responsum(FENESTRALE2_COMPOSITOR_MAILBOX*m,U64 codex){m->responsum=codex;m->seriale_responsi=m->seriale_petitionis;m->status=codex==0?FII_CMP_STATUS_PERFECTUM:FII_CMP_STATUS_ERRATUM;}

static void mailbox_age(void){
    FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;
    if(m->status!=FII_CMP_STATUS_PETITUM)return;
    if(m->operatio==FII_CMP_OP_CREA){
        I32 idx=indicem_liberum();U64 w=m->petita_latitudo,h=m->petita_altitudo;
        if(idx<0||w<300||h<220||w>latitudo-24||h>altitudo-52||w*h>8388608ULL){responsum(m,2);return;}
        void*p=0;if(opera->AllocatePool(EfiLoaderData,(UINTN)(w*h*4),&p)!=EFI_SUCCESS||!p){responsum(m,3);return;}
        memoria_vacua(p,(UINTN)(w*h*4));SUPERFICIES_I*s=&superficies[idx];s->pix=(U32*)p;s->w=(U32)w;s->h=(U32)h;s->formatum=0;s->id=proximus_id++;s->client=m->client;s->visibilis=0;
        if(m->client==1){s->x=latitudo/16;s->y=(altitudo-28-s->h)/3;}else{s->x=latitudo>s->w+70?latitudo-s->w-70:20;s->y=altitudo>s->h+110?110:30;}
        focus((U8)idx);m->superficies_id=s->id;m->basis_pixelorum=(U64)(UINTN)p;m->pixel_per_lineam=w;m->formatum_pixelorum=0;m->x=s->x;m->y=s->y;responsum(m,0);return;
    }
    SUPERFICIES_I*s=inveni(m->superficies_id,m->client);if(!s){responsum(m,4);return;}U8 idx=(U8)(s-superficies);
    if(m->operatio==FII_CMP_OP_PRAESENTA){s->visibilis=1;focus(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_MOVE){U32 maxx=latitudo>s->w?latitudo-s->w:0,maxy=altitudo>28+s->h?altitudo-28-s->h:0;s->x=(U32)(m->x>maxx?maxx:m->x);s->y=(U32)(m->y>maxy?maxy:m->y);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_OSTENDE){s->visibilis=1;focus(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_CELA){s->visibilis=0;compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_FOCUS){focus(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_DELE){ordinem_remove(idx);opera->FreePool(s->pix);memoria_vacua(s,sizeof(*s));compone();responsum(m,0);return;}
    responsum(m,5);
}

static U64 clientem_voca(U64 ingressus){U64(*f)(void)=(U64(*)(void))(UINTN)ingressus;return f();}
static U8 clientem_init(void){FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;U64 ingressus=*(U64*)(UINTN)(CLIENT_INITIUM+24);U64 r=clientem_voca(ingressus);if(r!=10||m->status!=1||m->operatio!=1)return 0;mailbox_age();r=clientem_voca(ingressus);if(r!=11||m->status!=1||m->operatio!=3)return 0;mailbox_age();r=clientem_voca(ingressus);return(r==0&&m->status==0)?1:0;}

static U8 clientem_onera(const U8*initium,const U8*finis){UINTN n=(UINTN)(finis-initium);if(n<32||n>CLIENT_PAGINAE*4096)return 0;memoria_vacua((void*)(UINTN)CLIENT_INITIUM,CLIENT_PAGINAE*4096);memoria_copia((void*)(UINTN)CLIENT_INITIUM,initium,n);if(*(U32*)(UINTN)CLIENT_INITIUM!=0x464c457fU)return 0;U64 e=*(U64*)(UINTN)(CLIENT_INITIUM+24);if(e<CLIENT_INITIUM||e>=CLIENT_INITIUM+n)return 0;return clientem_init();}

static EFI_STATUS modum_elige(EFI_GRAPHICS_OUTPUT_PROTOCOL*g){U32 electus=0xffffffffU;U64 area=0;for(U32 i=0;i<g->Mode->MaxMode;i++){EFI_GRAPHICS_OUTPUT_MODE_INFORMATION*info=0;UINTN m=0;if(g->QueryMode(g,i,&m,&info)==EFI_SUCCESS&&info&&info->PixelFormat<=1&&info->HorizontalResolution>=1024&&info->VerticalResolution>=600){U64 a=(U64)info->HorizontalResolution*info->VerticalResolution;if(a>area){area=a;electus=i;}}}if(electus==0xffffffffU)return 1;if(electus==g->Mode->Mode)return 0;return g->SetMode(g,electus);}

static void move_top(I32 dx,I32 dy){I32 idx=top_index();if(idx<0)return;SUPERFICIES_I*s=&superficies[idx];I32 nx=(I32)s->x+dx,ny=(I32)s->y+dy;if(nx<0)nx=0;if(ny<0)ny=0;U32 maxx=latitudo>s->w?latitudo-s->w:0,maxy=altitudo>28+s->h?altitudo-28-s->h:0;if((U32)nx>maxx)nx=(I32)maxx;if((U32)ny>maxy)ny=(I32)maxy;s->x=(U32)nx;s->y=(U32)ny;compone();}
static void alterna_focus(void){if(numerus_ordinis<2)return;focus(ordo[numerus_ordinis-2]);compone();}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago,EFI_SYSTEM_TABLE*systema){
    (void)imago;opera=systema->BootServices;if(opera->SetWatchdogTimer)opera->SetWatchdogTimer(0,0,0,0);
    EFI_STATUS status=opera->LocateProtocol(&guid_graphica,0,(void**)&gop);if(status!=0||!gop||!gop->Mode)return status;status=modum_elige(gop);if(status!=0)return status;if(!gop->Mode->Info||gop->Mode->Info->PixelFormat>1)return 1;
    latitudo=gop->Mode->Info->HorizontalResolution;altitudo=gop->Mode->Info->VerticalResolution;linea=gop->Mode->Info->PixelsPerScanLine;formatum=gop->Mode->Info->PixelFormat;framebuffer=(U32*)(UINTN)gop->Mode->FrameBufferBase;if(!framebuffer||linea<latitudo)return 1;
    EFI_PHYSICAL_ADDRESS communis=COMMUNIS_INITIUM;status=opera->AllocatePages(EFI_ALLOCATE_ADDRESS,EfiLoaderData,COMMUNIS_PAGINAE,&communis);if(status!=0||communis!=COMMUNIS_INITIUM)return status;memoria_vacua((void*)(UINTN)COMMUNIS_INITIUM,COMMUNIS_PAGINAE*4096);
    EFI_PHYSICAL_ADDRESS client=CLIENT_INITIUM;status=opera->AllocatePages(EFI_ALLOCATE_ADDRESS,EfiLoaderData,CLIENT_PAGINAE,&client);if(status!=0||client!=CLIENT_INITIUM)return status;
    FENESTRALE2_DESCRIPTOR*d=(FENESTRALE2_DESCRIPTOR*)(UINTN)FENESTRALE2_BASIS;d->magic=FENESTRALE2_MAGIC;d->versio=1;d->mensura=128;d->capacitates=FII_CAP_FRAMEBUFFER_NATIVUS|FII_CAP_PIXEL_RGB_BGR|FII_CAP_COMPOSITORIUM;d->framebuffer=gop->Mode->FrameBufferBase;d->latitudo=latitudo;d->altitudo=altitudo;d->pixel_per_lineam=linea;d->formatum_pixelorum=formatum;d->bits_per_pixel=32;d->taskbar_altitudo=28;d->scala_per_mille=1000;
    FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;m->magic=FENESTRALE2_COMPOSITOR_MAGIC;m->versio=1;m->mensura=256;m->status=0;compone();
    if(!clientem_onera(_binary_programmata_h_elf_start,_binary_programmata_h_elf_end))return 1;
    if(!clientem_onera(_binary_tabula_i_elf_start,_binary_tabula_i_elf_end))return 1;
    compone();if(systema->ConIn)systema->ConIn->Reset(systema->ConIn,0);
    for(;;){EFI_INPUT_KEY k;if(systema->ConIn&&systema->ConIn->ReadKeyStroke(systema->ConIn,&k)==0){if(k.ScanCode==EFI_SCAN_ESC)break;if(k.UnicodeChar==9)alterna_focus();if(k.ScanCode==EFI_SCAN_LEFT)move_top(-12,0);if(k.ScanCode==EFI_SCAN_RIGHT)move_top(12,0);if(k.ScanCode==EFI_SCAN_UP)move_top(0,-12);if(k.ScanCode==EFI_SCAN_DOWN)move_top(0,12);}opera->Stall(10000);}
    for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++)if(superficies[i].pix)opera->FreePool(superficies[i].pix);return EFI_SUCCESS;
}
