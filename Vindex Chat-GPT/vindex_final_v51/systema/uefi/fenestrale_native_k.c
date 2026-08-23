/* Sylvia OS — Fenestrale II, Gradus K.
 * Compositorium UEFI experimentale multiplex: compositio laesa,
 * maximizatio, resize interactiva et eventa ad clientes VINDEX.
 * Via canonica Sylvia OS 0.51 non mutatur.
 */

typedef unsigned char U8;
typedef unsigned short U16;
typedef unsigned int U32;
typedef unsigned long long U64;
typedef signed int I32;
typedef signed long long I64;
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
#define STATUS_VISIBILIS 0U
#define STATUS_MINIMUS 1U
#define STATUS_CLAUSUS 2U
#define TRACTIO_NULLA 0U
#define TRACTIO_MOTUS 1U
#define TRACTIO_MENSURA 2U

#include "../fenestrale_ii_compositor_k_abi.h"

typedef struct { U64 Signature; U32 Revision; U32 HeaderSize; U32 CRC32; U32 Reserved; } EFI_TABLE_HEADER;
typedef struct { U32 Data1; U16 Data2; U16 Data3; U8 Data4[8]; } EFI_GUID;
typedef struct { U16 ScanCode; CHAR16 UnicodeChar; } EFI_INPUT_KEY;

typedef struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL EFI_SIMPLE_TEXT_INPUT_PROTOCOL;
struct _EFI_SIMPLE_TEXT_INPUT_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_SIMPLE_TEXT_INPUT_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *ReadKeyStroke)(EFI_SIMPLE_TEXT_INPUT_PROTOCOL *, EFI_INPUT_KEY *);
    void *WaitForKey;
};

typedef struct { I32 RelativeMovementX; I32 RelativeMovementY; I32 RelativeMovementZ; U8 LeftButton; U8 RightButton; } EFI_SIMPLE_POINTER_STATE;
typedef struct { U64 ResolutionX; U64 ResolutionY; U64 ResolutionZ; U8 LeftButton; U8 RightButton; } EFI_SIMPLE_POINTER_MODE;
typedef struct _EFI_SIMPLE_POINTER_PROTOCOL EFI_SIMPLE_POINTER_PROTOCOL;
struct _EFI_SIMPLE_POINTER_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_SIMPLE_POINTER_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *GetState)(EFI_SIMPLE_POINTER_PROTOCOL *, EFI_SIMPLE_POINTER_STATE *);
    void *WaitForInput;
    EFI_SIMPLE_POINTER_MODE *Mode;
};

typedef struct { U64 CurrentX; U64 CurrentY; U64 CurrentZ; U32 ActiveButtons; } EFI_ABSOLUTE_POINTER_STATE;
typedef struct { U64 AbsoluteMinX; U64 AbsoluteMinY; U64 AbsoluteMinZ; U64 AbsoluteMaxX; U64 AbsoluteMaxY; U64 AbsoluteMaxZ; U32 Attributes; } EFI_ABSOLUTE_POINTER_MODE;
typedef struct _EFI_ABSOLUTE_POINTER_PROTOCOL EFI_ABSOLUTE_POINTER_PROTOCOL;
struct _EFI_ABSOLUTE_POINTER_PROTOCOL {
    EFI_STATUS (EFIAPI *Reset)(EFI_ABSOLUTE_POINTER_PROTOCOL *, U8);
    EFI_STATUS (EFIAPI *GetState)(EFI_ABSOLUTE_POINTER_PROTOCOL *, EFI_ABSOLUTE_POINTER_STATE *);
    void *WaitForInput;
    EFI_ABSOLUTE_POINTER_MODE *Mode;
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
    U8 status;
    U8 maximus;
    U32 restitue_x,restitue_y,restitue_w,restitue_h;
} SUPERFICIES_K;

extern U8 _binary_programmata_k_elf_start[];
extern U8 _binary_programmata_k_elf_end[];
extern U8 _binary_tabula_k_elf_start[];
extern U8 _binary_tabula_k_elf_end[];

static EFI_GUID guid_graphica={0x9042a9de,0x23dc,0x4a38,{0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}};
static EFI_GUID guid_muris={0x31878c87,0x0b75,0x11d5,{0x9a,0x4f,0x00,0x90,0x27,0x3f,0xc1,0x4d}};
static EFI_GUID guid_muris_absoluti={0x8d59d32b,0xc655,0x4ae9,{0x9b,0x15,0xf2,0x59,0x04,0x99,0x2a,0x43}};

static EFI_GRAPHICS_OUTPUT_PROTOCOL *gop;
static EFI_SIMPLE_POINTER_PROTOCOL *murus_relativus;
static EFI_ABSOLUTE_POINTER_PROTOCOL *murus_absolutus;
static EFI_BOOT_SERVICES *opera;
static U32 *framebuffer;
static U32 latitudo,altitudo,linea,formatum;
static SUPERFICIES_K superficies[SUPERFICIES_CAPACITAS];
static U8 ordo[SUPERFICIES_CAPACITAS];
static U8 numerus_ordinis;
static U64 proximus_id=1;
static U64 client_ingressus;
static I64 murus_x,murus_y;
static U8 bulla_cruda,bulla_stabilis,bulla_aetas,bulla_vetus;
static U8 tractio;
static I32 tractio_dx,tractio_dy;
static U8 tractio_index;
static U32 praevisa_w,praevisa_h;
static U64 pulsus,ultimus_click_tituli;
static I32 ultimus_click_index=-1;

static void memoria_vacua(void *p,UINTN n){U8*q=(U8*)p;while(n--)*q++=0;}
static void memoria_copia(void*d,const void*s,UINTN n){U8*dd=(U8*)d;const U8*ss=(const U8*)s;while(n--)*dd++=*ss++;}
static U32 argb(U8 a,U8 r,U8 g,U8 b){return((U32)a<<24)|((U32)r<<16)|((U32)g<<8)|b;}
static U8 A(U32 c){return(U8)(c>>24);} static U8 R(U32 c){return(U8)(c>>16);}
static U8 G(U32 c){return(U8)(c>>8);} static U8 B(U32 c){return(U8)c;}
static U32 misce(U32 infra,U32 supra){U32 a=A(supra),ia=255-a;if(a==0)return infra;if(a==255)return supra|0xff000000U;return argb(255,(U8)((R(supra)*a+R(infra)*ia)/255),(U8)((G(supra)*a+G(infra)*ia)/255),(U8)((B(supra)*a+B(infra)*ia)/255));}
static void framebuffer_scribe(U32 x,U32 y,U32 c){U32 r=R(c),g=G(c),b=B(c),out;if(formatum==0)out=r|(g<<8)|(b<<16);else out=b|(g<<8)|(r<<16);framebuffer[(UINTN)y*linea+x]=out;}
static U32 fundum(U32 x,U32 y){U32 t=(U64)y*255/(altitudo?altitudo:1);U8 r=(U8)((8*(255-t)+5*t)/255),g=(U8)((52*(255-t)+24*t)/255),b=(U8)((90*(255-t)+48*t)/255);U32 c=argb(255,r,g,b);U32 a=altitudo*54/100;if(y>=a&&y<a+2&&x>latitudo*12/100&&x<latitudo*91/100)c=argb(255,54,132,171);if(y>=a+42&&y<a+43&&x>latitudo*21/100&&x<latitudo*84/100)c=argb(255,34,103,151);return c;}
static U32 intra(U32 v,U32 a,U32 b){return v>=a&&v<b;}

static SUPERFICIES_K *inveni(U64 id,U64 client){for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++)if(superficies[i].id==id&&superficies[i].client==client)return&superficies[i];return 0;}
static SUPERFICIES_K *inveni_clientem(U64 client){for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++)if(superficies[i].id&&superficies[i].client==client)return&superficies[i];return 0;}
static I32 indicem_liberum(void){for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++)if(superficies[i].id==0)return(I32)i;return-1;}
static U32 pixel_superficiei(const SUPERFICIES_K*s,U32 x,U32 y){U32 raw=s->pix[(UINTN)y*s->w+x];U8 a=(U8)(raw>>24),r,g,b;if(s->formatum==0){r=(U8)raw;g=(U8)(raw>>8);b=(U8)(raw>>16);}else{b=(U8)raw;g=(U8)(raw>>8);r=(U8)(raw>>16);}return argb(a,r,g,b);}
static void ordinem_remove(U8 idx){for(U8 i=0;i<numerus_ordinis;i++)if(ordo[i]==idx){for(U8 j=i;j+1<numerus_ordinis;j++)ordo[j]=ordo[j+1];numerus_ordinis--;return;}}
static void focus(U8 idx){SUPERFICIES_K*s=&superficies[idx];if(!s->id||!s->visibilis||s->status!=STATUS_VISIBILIS)return;ordinem_remove(idx);if(numerus_ordinis<SUPERFICIES_CAPACITAS)ordo[numerus_ordinis++]=idx;}
static I32 top_visibilis_index(void){for(I32 i=(I32)numerus_ordinis-1;i>=0;i--){U8 idx=ordo[i];if(superficies[idx].id&&superficies[idx].visibilis&&superficies[idx].status==STATUS_VISIBILIS)return(I32)idx;}return-1;}

static U32 cursor_pixel(U32 dx,U32 dy){
    if(dy<14&&dx<=dy/2+1){if(dx==0||dx==dy/2+1||dy==13)return argb(255,12,20,27);return argb(255,241,238,228);}
    if(dx>=4&&dx<6&&dy>=10&&dy<18)return argb(255,12,20,27);
    if(dx>=6&&dx<11&&dy>=15&&dy<17)return argb(255,12,20,27);
    if(dx==5&&dy>=11&&dy<15)return argb(255,241,238,228);
    return 0;
}

static void compone_region(I32 rx,I32 ry,I32 rw,I32 rh){
    const U32 barra=28;
    if(rw<=0||rh<=0||rx>=(I32)latitudo||ry>=(I32)altitudo)return;
    if(rx<0){rw+=rx;rx=0;}
    if(ry<0){rh+=ry;ry=0;}
    if(rw<=0||rh<=0)return;
    if(rx+rw>(I32)latitudo)rw=(I32)latitudo-rx;
    if(ry+rh>(I32)altitudo)rh=(I32)altitudo-ry;
    I32 top=top_visibilis_index();
    for(U32 y=(U32)ry;y<(U32)(ry+rh);y++){
        for(U32 x=(U32)rx;x<(U32)(rx+rw);x++){
            U32 c=fundum(x,y);
            for(U8 k=0;k<numerus_ordinis;k++){
                SUPERFICIES_K*s=&superficies[ordo[k]];
                if(!s->visibilis||s->status!=STATUS_VISIBILIS)continue;
                if(intra(x,s->x+8,s->x+s->w+8)&&intra(y,s->y+8,s->y+s->h+8)&&!(intra(x,s->x,s->x+s->w)&&intra(y,s->y,s->y+s->h)))c=misce(c,argb(45,0,0,0));
                if(intra(x,s->x,s->x+s->w)&&intra(y,s->y,s->y+s->h))c=misce(c,pixel_superficiei(s,x-s->x,y-s->y));
                if((I32)ordo[k]==top&&s->visibilis){if((x==s->x||x+1==s->x+s->w)&&intra(y,s->y,s->y+s->h))c=argb(255,185,138,82);if((y==s->y||y+1==s->y+s->h)&&intra(x,s->x,s->x+s->w))c=argb(255,185,138,82);}
            }
            if(y>=altitudo-barra){
                U32 yy=y-(altitudo-barra);c=argb(255,8,35,61);
                if(yy==0)c=argb(255,98,215,242);
                if(yy>=4&&yy<24&&x>=4&&x<88)c=argb(255,14,66,111);
                SUPERFICIES_K*p=inveni_clientem(1),*t=inveni_clientem(2);
                if(p&&p->status!=STATUS_CLAUSUS&&yy>=4&&yy<24&&x>=98&&x<286)c=(top>=0&&superficies[top].client==1)?argb(255,26,93,146):argb(255,16,55,83);
                if(t&&t->status!=STATUS_CLAUSUS&&yy>=4&&yy<24&&x>=292&&x<430)c=(top>=0&&superficies[top].client==2)?argb(255,26,93,146):argb(255,16,55,83);
                if(yy>=9&&yy<15&&x>=18&&x<70)c=argb(255,234,248,255);
                if(p&&p->status!=STATUS_CLAUSUS&&yy>=9&&yy<15&&x>=112&&x<220)c=argb(255,234,248,255);
                if(t&&t->status!=STATUS_CLAUSUS&&yy>=9&&yy<15&&x>=310&&x<382)c=argb(255,234,248,255);
            }
            if(top>=0){SUPERFICIES_K*s=&superficies[top];if(s->visibilis&&!s->maximus&&x>=s->x&&y>=s->y&&x<s->x+s->w&&y<s->y+s->h){U32 dx=s->x+s->w-1-x,dy=s->y+s->h-1-y;if(dx<13&&dy<13&&(dx+dy==5||dx+dy==9||dx+dy==13))c=argb(255,185,138,82);}}
            if(tractio==TRACTIO_MENSURA&&tractio_index<SUPERFICIES_CAPACITAS){SUPERFICIES_K*s=&superficies[tractio_index];U32 rr=s->x+praevisa_w-1,bb=s->y+praevisa_h-1;if((x==s->x||x==rr)&&intra(y,s->y,bb+1))c=argb(255,98,215,242);if((y==s->y||y==bb)&&intra(x,s->x,rr+1))c=argb(255,98,215,242);}
            if(x>=(U32)murus_x&&y>=(U32)murus_y){U32 cp=cursor_pixel(x-(U32)murus_x,y-(U32)murus_y);if(cp)c=misce(c,cp);}
            framebuffer_scribe(x,y,c);
        }
    }
}
static void compone(void){compone_region(0,0,(I32)latitudo,(I32)altitudo);}
static void compone_duas(U32 ax,U32 ay,U32 aw,U32 ah,U32 bx,U32 by,U32 bw,U32 bh){U32 x=ax<bx?ax:bx,y=ay<by?ay:by,ar=ax+aw,br=bx+bw,ab=ay+ah,bb=by+bh,r=ar>br?ar:br,d=ab>bb?ab:bb;compone_region((I32)x,(I32)y,(I32)(r-x),(I32)(d-y));}
static void cursor_redde(I64 ox,I64 oy){U32 ax=(U32)(ox<0?0:ox),ay=(U32)(oy<0?0:oy);compone_duas(ax,ay,12,20,(U32)murus_x,(U32)murus_y,12,20);}

static void responsum(FENESTRALE2_COMPOSITOR_MAILBOX*m,U64 codex){m->responsum=codex;m->seriale_responsi=m->seriale_petitionis;m->status=codex==0?FII_CMP_STATUS_PERFECTUM:FII_CMP_STATUS_ERRATUM;}
static void mailbox_age(void){
    FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;
    if(m->status!=FII_CMP_STATUS_PETITUM)return;
    if(m->operatio==FII_CMP_OP_CREA){
        I32 idx=indicem_liberum();U64 w=m->petita_latitudo,h=m->petita_altitudo;
        if(idx<0||w<300||h<220||w>latitudo-24||h>altitudo-52||w*h>8388608ULL){responsum(m,2);return;}
        void*p=0;if(opera->AllocatePool(EfiLoaderData,(UINTN)(w*h*4),&p)!=EFI_SUCCESS||!p){responsum(m,3);return;}
        memoria_vacua(p,(UINTN)(w*h*4));SUPERFICIES_K*s=&superficies[idx];s->pix=(U32*)p;s->w=(U32)w;s->h=(U32)h;s->formatum=0;s->id=proximus_id++;s->client=m->client;s->visibilis=0;s->status=STATUS_VISIBILIS;s->maximus=0;
        if(m->client==1){s->x=latitudo/16;s->y=(altitudo-28-s->h)/3;}else{s->x=latitudo>s->w+70?latitudo-s->w-70:20;s->y=altitudo>s->h+110?110:30;}
        s->restitue_x=s->x;s->restitue_y=s->y;s->restitue_w=s->w;s->restitue_h=s->h;
        m->superficies_id=s->id;m->basis_pixelorum=(U64)(UINTN)p;m->pixel_per_lineam=w;m->formatum_pixelorum=0;m->x=s->x;m->y=s->y;responsum(m,0);return;
    }
    SUPERFICIES_K*s=inveni(m->superficies_id,m->client);if(!s){responsum(m,4);return;}U8 idx=(U8)(s-superficies);
    if(m->operatio==FII_CMP_OP_PRAESENTA){s->visibilis=1;s->status=STATUS_VISIBILIS;focus(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_MOVE){U32 maxx=latitudo>s->w?latitudo-s->w:0,maxy=altitudo>28+s->h?altitudo-28-s->h:0;s->x=(U32)(m->x>maxx?maxx:m->x);s->y=(U32)(m->y>maxy?maxy:m->y);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_OSTENDE){s->visibilis=1;s->status=STATUS_VISIBILIS;focus(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_CELA){s->visibilis=0;s->status=STATUS_MINIMUS;ordinem_remove(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_FOCUS){focus(idx);compone();responsum(m,0);return;}
    if(m->operatio==FII_CMP_OP_DELE){ordinem_remove(idx);opera->FreePool(s->pix);memoria_vacua(s,sizeof(*s));compone();responsum(m,0);return;}
    responsum(m,5);
}

static U64 __attribute__((naked,noinline)) clientem_voca(U64 ingressus __attribute__((unused))){__asm__ volatile("push %rbx\n\tcall *%rdi\n\tpop %rbx\n\tret");}
static U8 clientem_init(void){FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;U64 r=clientem_voca(client_ingressus);if(r!=10||m->status!=1||m->operatio!=1)return 0;mailbox_age();r=clientem_voca(client_ingressus);if(r!=11||m->status!=1||m->operatio!=3)return 0;mailbox_age();r=clientem_voca(client_ingressus);return(r==0&&m->status==0)?1:0;}
static U8 clientem_copia(const U8*initium,const U8*finis){UINTN n=(UINTN)(finis-initium);if(n<32||n>CLIENT_PAGINAE*4096)return 0;memoria_vacua((void*)(UINTN)CLIENT_INITIUM,CLIENT_PAGINAE*4096);memoria_copia((void*)(UINTN)CLIENT_INITIUM,initium,n);if(*(U32*)(UINTN)CLIENT_INITIUM!=0x464c457fU)return 0;U64 e=*(U64*)(UINTN)(CLIENT_INITIUM+24),finis_imaginis=CLIENT_INITIUM+n;if(e<CLIENT_INITIUM||e>=finis_imaginis)return 0;U64 restant=finis_imaginis-e,limen=restant<64?restant:64;U8*q=(U8*)(UINTN)e;if(limen<22||q[0]!=0x58)return 0;for(U32 i=16;i+5<limen;i++){if(q[i]==0xe8){I32 rel=*(I32*)(void*)(q+i+1);U64 target=e+i+5+(I64)rel;if(target>=CLIENT_INITIUM&&target<finis_imaginis){client_ingressus=target;return 1;}}}return 0;}
static U8 clientem_onera(const U8*initium,const U8*finis){if(!clientem_copia(initium,finis))return 0;return clientem_init();}
static U8 clientem_eventum(U8 idx,U64 typus,U64 primum,U64 secundum){SUPERFICIES_K*s=&superficies[idx];const U8*initium=s->client==1?_binary_programmata_k_elf_start:_binary_tabula_k_elf_start;const U8*finis=s->client==1?_binary_programmata_k_elf_end:_binary_tabula_k_elf_end;if(!clientem_copia(initium,finis))return 0;FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;memoria_vacua(m,sizeof(*m));m->magic=FENESTRALE2_COMPOSITOR_MAGIC;m->versio=FENESTRALE2_COMPOSITOR_VERSIO;m->mensura=FENESTRALE2_COMPOSITOR_MENSURA;m->status=FII_CMP_STATUS_PERFECTUM;m->operatio=FII_CMP_OP_EVENTUM;m->client=s->client;m->superficies_id=s->id;m->basis_pixelorum=(U64)(UINTN)s->pix;m->pixel_per_lineam=s->w;m->formatum_pixelorum=s->formatum;m->petita_latitudo=s->w;m->petita_altitudo=s->h;m->x=s->x;m->y=s->y;m->reservata[FII_CMP_EVENTUM_ARG_TYPUS]=typus;m->reservata[FII_CMP_EVENTUM_ARG_PRIMUM]=primum;m->reservata[FII_CMP_EVENTUM_ARG_SECUNDUM]=secundum;U64 r=clientem_voca(client_ingressus);return(U8)(r==20&&m->status==FII_CMP_STATUS_VACUUM);}
static EFI_STATUS modum_elige(EFI_GRAPHICS_OUTPUT_PROTOCOL*g){U32 electus=0xffffffffU;U64 area=0;for(U32 i=0;i<g->Mode->MaxMode;i++){EFI_GRAPHICS_OUTPUT_MODE_INFORMATION*info=0;UINTN m=0;if(g->QueryMode(g,i,&m,&info)==EFI_SUCCESS&&info){if(info->PixelFormat<=1&&info->HorizontalResolution>=1024&&info->VerticalResolution>=600){U64 a=(U64)info->HorizontalResolution*info->VerticalResolution;if(a>area){area=a;electus=i;}}opera->FreePool(info);}}if(electus==0xffffffffU)return 1;if(electus==g->Mode->Mode)return 0;return g->SetMode(g,electus);}

static I32 hit_fenestra(I64 x,I64 y){for(I32 k=(I32)numerus_ordinis-1;k>=0;k--){U8 idx=ordo[k];SUPERFICIES_K*s=&superficies[idx];if(s->visibilis&&s->status==STATUS_VISIBILIS&&x>=(I64)s->x&&y>=(I64)s->y&&x<(I64)(s->x+s->w)&&y<(I64)(s->y+s->h))return(I32)idx;}return-1;}
static void focus_eventum(U8 idx){I32 vetus=top_visibilis_index();if(vetus==(I32)idx)return;focus(idx);if(vetus>=0)clientem_eventum((U8)vetus,FII_CMP_EVENTUM_FOCUS,FII_CMP_FOCUS_INACTIVUS,0);clientem_eventum(idx,FII_CMP_EVENTUM_FOCUS,FII_CMP_FOCUS_ACTIVUS,0);compone();}
static void status_muta(U8 idx,U8 status){SUPERFICIES_K*s=&superficies[idx];if(!s->id)return;I32 vetus=top_visibilis_index();s->status=status;if(status==STATUS_VISIBILIS){s->visibilis=1;focus_eventum(idx);return;}s->visibilis=0;ordinem_remove(idx);if(vetus==(I32)idx)clientem_eventum(idx,FII_CMP_EVENTUM_FOCUS,FII_CMP_FOCUS_INACTIVUS,0);I32 novus=top_visibilis_index();if(novus>=0)clientem_eventum((U8)novus,FII_CMP_EVENTUM_FOCUS,FII_CMP_FOCUS_ACTIVUS,0);tractio=TRACTIO_NULLA;compone();}
static void taskbar_click(U64 client){SUPERFICIES_K*s=inveni_clientem(client);if(!s||s->status==STATUS_CLAUSUS)return;U8 idx=(U8)(s-superficies);I32 top=top_visibilis_index();if(s->status==STATUS_MINIMUS){status_muta(idx,STATUS_VISIBILIS);return;}if(top==(I32)idx){status_muta(idx,STATUS_MINIMUS);return;}focus_eventum(idx);}

static U8 geometria_muta(U8 idx,U32 nx,U32 ny,U32 nw,U32 nh){SUPERFICIES_K*s=&superficies[idx];if(nw<480||nh<320||nx>=latitudo||ny>=altitudo-28)return 0;if(nw>latitudo-nx)nw=latitudo-nx;if(nh>altitudo-28-ny)nh=altitudo-28-ny;if(nw&1U)nw--;if(nw<480||nh<320||(U64)nw*nh>8388608ULL)return 0;void*p=0;if(opera->AllocatePool(EfiLoaderData,(UINTN)nw*nh*4,&p)!=EFI_SUCCESS||!p)return 0;memoria_vacua(p,(UINTN)nw*nh*4);U32*vetus_pix=s->pix;U32 ox=s->x,oy=s->y,ow=s->w,oh=s->h;s->pix=(U32*)p;s->x=nx;s->y=ny;s->w=nw;s->h=nh;if(!clientem_eventum(idx,FII_CMP_EVENTUM_DIMENSIO,nw,nh)){s->pix=vetus_pix;s->x=ox;s->y=oy;s->w=ow;s->h=oh;opera->FreePool(p);return 0;}opera->FreePool(vetus_pix);compone_duas(ox,oy,ow+8,oh+8,nx,ny,nw+8,nh+8);return 1;}
static void maxima_muta(U8 idx){SUPERFICIES_K*s=&superficies[idx];U8 vetus=s->maximus;if(!s->maximus){s->restitue_x=s->x;s->restitue_y=s->y;s->restitue_w=s->w;s->restitue_h=s->h;s->maximus=1;if(!geometria_muta(idx,0,0,latitudo,altitudo-28))s->maximus=vetus;}else{s->maximus=0;if(!geometria_muta(idx,s->restitue_x,s->restitue_y,s->restitue_w,s->restitue_h))s->maximus=vetus;}compone();}

static void mouse_down(void){
    if(murus_y>=(I64)altitudo-28){if(murus_x>=98&&murus_x<286)taskbar_click(1);else if(murus_x>=292&&murus_x<430)taskbar_click(2);return;}
    I32 idx=hit_fenestra(murus_x,murus_y);if(idx<0)return;focus_eventum((U8)idx);SUPERFICIES_K*s=&superficies[idx];I64 lx=murus_x-(I64)s->x,ly=murus_y-(I64)s->y;
    if(ly>=4&&ly<24&&lx>=(I64)(s->w-26)&&lx<(I64)(s->w-6)){status_muta((U8)idx,STATUS_CLAUSUS);return;}
    if(ly>=4&&ly<24&&lx>=(I64)(s->w-70)&&lx<(I64)(s->w-52)){status_muta((U8)idx,STATUS_MINIMUS);return;}
    if(ly>=4&&ly<24&&lx>=(I64)(s->w-48)&&lx<(I64)(s->w-30)){maxima_muta((U8)idx);return;}
    if(!s->maximus&&lx>=(I64)s->w-14&&ly>=(I64)s->h-14){tractio=TRACTIO_MENSURA;tractio_index=(U8)idx;praevisa_w=s->w;praevisa_h=s->h;return;}
    if(ly>=0&&ly<28&&lx>=0&&lx<(I64)(s->w-74)){if(ultimus_click_index==idx&&pulsus-ultimus_click_tituli<=35){ultimus_click_index=-1;maxima_muta((U8)idx);return;}ultimus_click_index=idx;ultimus_click_tituli=pulsus;if(!s->maximus){tractio=TRACTIO_MOTUS;tractio_index=(U8)idx;tractio_dx=(I32)(murus_x-s->x);tractio_dy=(I32)(murus_y-s->y);}}
}
static void drag_move(void){if(tractio!=TRACTIO_MOTUS||tractio_index>=SUPERFICIES_CAPACITAS)return;SUPERFICIES_K*s=&superficies[tractio_index];if(!s->visibilis||s->maximus)return;U32 ox=s->x,oy=s->y;I32 nx=(I32)murus_x-tractio_dx,ny=(I32)murus_y-tractio_dy;I32 maxx=(I32)latitudo-(I32)s->w,maxy=(I32)altitudo-28-(I32)s->h;if(nx<0)nx=0;if(ny<0)ny=0;if(nx>maxx)nx=maxx;if(ny>maxy)ny=maxy;if((U32)nx==ox&&(U32)ny==oy)return;s->x=(U32)nx;s->y=(U32)ny;compone_duas(ox,oy,s->w+8,s->h+8,s->x,s->y,s->w+8,s->h+8);}
static void mensuram_praevidere(void){if(tractio!=TRACTIO_MENSURA||tractio_index>=SUPERFICIES_CAPACITAS)return;SUPERFICIES_K*s=&superficies[tractio_index];U32 ow=praevisa_w,oh=praevisa_h;I64 nw=murus_x-(I64)s->x+1,nh=murus_y-(I64)s->y+1;if(nw<480)nw=480;if(nh<320)nh=320;if(nw>(I64)latitudo-s->x)nw=(I64)latitudo-s->x;if(nh>(I64)altitudo-28-s->y)nh=(I64)altitudo-28-s->y;praevisa_w=(U32)nw&~1U;praevisa_h=(U32)nh;if(praevisa_w==ow&&praevisa_h==oh)return;compone_duas(s->x,s->y,ow+1,oh+1,s->x,s->y,praevisa_w+1,praevisa_h+1);}
static void mensuram_confirma(void){if(tractio!=TRACTIO_MENSURA||tractio_index>=SUPERFICIES_CAPACITAS)return;U8 idx=tractio_index;U32 w=praevisa_w,h=praevisa_h;tractio=TRACTIO_NULLA;if(!geometria_muta(idx,superficies[idx].x,superficies[idx].y,w,h))compone();}
static void move_top(I32 dx,I32 dy){I32 idx=top_visibilis_index();if(idx<0)return;SUPERFICIES_K*s=&superficies[idx];if(s->maximus)return;U32 ox=s->x,oy=s->y;I32 nx=(I32)s->x+dx,ny=(I32)s->y+dy;I32 maxx=(I32)latitudo-(I32)s->w,maxy=(I32)altitudo-28-(I32)s->h;if(nx<0)nx=0;if(ny<0)ny=0;if(nx>maxx)nx=maxx;if(ny>maxy)ny=maxy;s->x=(U32)nx;s->y=(U32)ny;compone_duas(ox,oy,s->w+8,s->h+8,s->x,s->y,s->w+8,s->h+8);}
static void alterna_focus(void){I32 top=top_visibilis_index();for(I32 k=(I32)numerus_ordinis-1;k>=0;k--){U8 idx=ordo[k];if((I32)idx!=top&&superficies[idx].visibilis&&superficies[idx].status==STATUS_VISIBILIS){focus_eventum(idx);return;}}}

static I64 motus_normalis(I32 valor,U64 resolutio,U32 amplitudo,U32 basis){I64 m;if(valor==0)return 0;if(resolutio==0)m=valor;else m=((I64)valor*6)/(I64)resolutio;if(m==0)m=valor<0?-1:1;m=(m*(I64)amplitudo)/(I64)basis;if(m==0)m=valor<0?-1:1;if(m>96)m=96;if(m<-96)m=-96;return m;}
static U8 bullam_confirma(U8 cruda){if(cruda!=bulla_cruda){bulla_cruda=cruda;bulla_aetas=0;}else if(bulla_aetas<2)bulla_aetas++;if(bulla_aetas>=1)bulla_stabilis=bulla_cruda;return bulla_stabilis;}
static U8 murem_lege(I64*x,I64*y,U8*bulla){
    U8 mutatum=0,ante=bulla_stabilis,raw=bulla_cruda;
    if(murus_absolutus&&murus_absolutus->Mode){EFI_ABSOLUTE_POINTER_STATE st;if(murus_absolutus->GetState(murus_absolutus,&st)==EFI_SUCCESS){EFI_ABSOLUTE_POINTER_MODE*m=murus_absolutus->Mode;U64 dx=m->AbsoluteMaxX-m->AbsoluteMinX,dy=m->AbsoluteMaxY-m->AbsoluteMinY;if(dx&&dy){*x=(I64)((st.CurrentX-m->AbsoluteMinX)*(latitudo-1)/dx);*y=(I64)((st.CurrentY-m->AbsoluteMinY)*(altitudo-1)/dy);raw=(U8)(st.ActiveButtons&1);mutatum=1;}}}
    if(!mutatum&&murus_relativus&&murus_relativus->Mode){EFI_SIMPLE_POINTER_STATE st;if(murus_relativus->GetState(murus_relativus,&st)==EFI_SUCCESS){*x+=motus_normalis(st.RelativeMovementX,murus_relativus->Mode->ResolutionX,latitudo,320);*y+=motus_normalis(st.RelativeMovementY,murus_relativus->Mode->ResolutionY,altitudo,200);raw=st.LeftButton?1:0;mutatum=1;}}
    if(*x<0)*x=0;
    if(*y<0)*y=0;
    if(*x>(I64)latitudo-1)*x=(I64)latitudo-1;
    if(*y>(I64)altitudo-1)*y=(I64)altitudo-1;
    *bulla=bullam_confirma(raw);
    return(U8)(mutatum||*bulla!=ante);
}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago,EFI_SYSTEM_TABLE*systema){
    (void)imago;opera=systema->BootServices;if(opera->SetWatchdogTimer)opera->SetWatchdogTimer(0,0,0,0);
    EFI_STATUS status=opera->LocateProtocol(&guid_graphica,0,(void**)&gop);if(status!=0||!gop||!gop->Mode)return status;status=modum_elige(gop);if(status!=0)return status;if(!gop->Mode->Info||gop->Mode->Info->PixelFormat>1)return 1;
    latitudo=gop->Mode->Info->HorizontalResolution;altitudo=gop->Mode->Info->VerticalResolution;linea=gop->Mode->Info->PixelsPerScanLine;formatum=gop->Mode->Info->PixelFormat;framebuffer=(U32*)(UINTN)gop->Mode->FrameBufferBase;if(!framebuffer||linea<latitudo)return 1;
    EFI_PHYSICAL_ADDRESS communis=COMMUNIS_INITIUM;status=opera->AllocatePages(EFI_ALLOCATE_ADDRESS,EfiLoaderData,COMMUNIS_PAGINAE,&communis);if(status!=0||communis!=COMMUNIS_INITIUM)return status;memoria_vacua((void*)(UINTN)COMMUNIS_INITIUM,COMMUNIS_PAGINAE*4096);
    EFI_PHYSICAL_ADDRESS client=CLIENT_INITIUM;status=opera->AllocatePages(EFI_ALLOCATE_ADDRESS,EfiLoaderData,CLIENT_PAGINAE,&client);if(status!=0||client!=CLIENT_INITIUM)return status;
    FENESTRALE2_DESCRIPTOR*d=(FENESTRALE2_DESCRIPTOR*)(UINTN)FENESTRALE2_BASIS;d->magic=FENESTRALE2_MAGIC;d->versio=1;d->mensura=128;d->capacitates=FII_CAP_FRAMEBUFFER_NATIVUS|FII_CAP_PIXEL_RGB_BGR|FII_CAP_COMPOSITORIUM;d->framebuffer=gop->Mode->FrameBufferBase;d->latitudo=latitudo;d->altitudo=altitudo;d->pixel_per_lineam=linea;d->formatum_pixelorum=formatum;d->bits_per_pixel=32;d->taskbar_altitudo=28;d->scala_per_mille=1000;
    FENESTRALE2_COMPOSITOR_MAILBOX*m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(UINTN)FENESTRALE2_COMPOSITOR_BASIS;m->magic=FENESTRALE2_COMPOSITOR_MAGIC;m->versio=1;m->mensura=256;m->status=0;
    murus_x=(I64)latitudo/2;murus_y=(I64)altitudo/2;d->murus_x=(U64)murus_x;d->murus_y=(U64)murus_y;d->bullae=0;
    opera->LocateProtocol(&guid_muris_absoluti,0,(void**)&murus_absolutus);opera->LocateProtocol(&guid_muris,0,(void**)&murus_relativus);if(murus_absolutus)murus_absolutus->Reset(murus_absolutus,0);if(murus_relativus)murus_relativus->Reset(murus_relativus,0);
    compone();if(!clientem_onera(_binary_programmata_k_elf_start,_binary_programmata_k_elf_end))return 1;if(!clientem_onera(_binary_tabula_k_elf_start,_binary_tabula_k_elf_end))return 1;compone();if(systema->ConIn)systema->ConIn->Reset(systema->ConIn,0);
    for(;;){
        pulsus++;
        EFI_INPUT_KEY k;while(systema->ConIn&&systema->ConIn->ReadKeyStroke(systema->ConIn,&k)==EFI_SUCCESS){if(k.ScanCode==EFI_SCAN_ESC)goto finis;if(k.UnicodeChar==9)alterna_focus();if(k.ScanCode==EFI_SCAN_LEFT)move_top(-12,0);if(k.ScanCode==EFI_SCAN_RIGHT)move_top(12,0);if(k.ScanCode==EFI_SCAN_UP)move_top(0,-12);if(k.ScanCode==EFI_SCAN_DOWN)move_top(0,12);}
        I64 ox=murus_x,oy=murus_y,nx=murus_x,ny=murus_y;U8 nb=bulla_stabilis;if(murem_lege(&nx,&ny,&nb)){U8 mota=(U8)(nx!=murus_x||ny!=murus_y);murus_x=nx;murus_y=ny;d->murus_x=(U64)murus_x;d->murus_y=(U64)murus_y;d->bullae=nb;if(nb&&!bulla_vetus)mouse_down();if(nb&&tractio==TRACTIO_MOTUS)drag_move();if(nb&&tractio==TRACTIO_MENSURA)mensuram_praevidere();if(!nb&&bulla_vetus){if(tractio==TRACTIO_MENSURA)mensuram_confirma();else tractio=TRACTIO_NULLA;}if(mota)cursor_redde(ox,oy);bulla_vetus=nb;}
        opera->Stall(12000);
    }
finis:
    for(U32 i=0;i<SUPERFICIES_CAPACITAS;i++){if(superficies[i].pix)opera->FreePool(superficies[i].pix);}
    return EFI_SUCCESS;
}
