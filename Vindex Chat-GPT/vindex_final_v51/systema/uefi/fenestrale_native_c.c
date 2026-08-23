/* Sylvia OS — Fenestrale II, Gradus C.
 * Window manager minimum: muris input, hit-testing, focus, tractio,
 * minimizatio, clausura et cursor compositus super Gradum B.
 */

typedef unsigned char U8;
typedef unsigned short U16;
typedef unsigned int U32;
typedef unsigned long long U64;
typedef signed int I32;
typedef signed long long I64;
typedef unsigned long long UINTN;
typedef unsigned long long EFI_STATUS;
typedef void *EFI_HANDLE;
typedef U16 CHAR16;

#define EFIAPI __attribute__((ms_abi))
#define EFI_SUCCESS 0
#define EFI_SCAN_UP 0x0001
#define EFI_SCAN_DOWN 0x0002
#define EFI_SCAN_RIGHT 0x0003
#define EFI_SCAN_LEFT 0x0004
#define EFI_SCAN_ESC 0x0017
#define EfiLoaderData 2
#define STATUS_VISIBILIS 0
#define STATUS_MINIMUS 1
#define STATUS_CLAUSUS 2

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
    U64 FrameBufferBase; UINTN FrameBufferSize;
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
    void *RaiseTPL; void *RestoreTPL; void *AllocatePages; void *FreePages; void *GetMemoryMap;
    EFI_STATUS (EFIAPI *AllocatePool)(U32, UINTN, void **);
    EFI_STATUS (EFIAPI *FreePool)(void *);
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

typedef struct { U32 *pix; U32 w,h,x,y; } SUPERFICIES;
typedef struct { U32 x,y,w,h; } REGIO;

static EFI_GUID guid_graphica={0x9042a9de,0x23dc,0x4a38,{0x96,0xfb,0x7a,0xde,0xd0,0x80,0x51,0x6a}};
static EFI_GUID guid_muris={0x31878c87,0x0b75,0x11d5,{0x9a,0x4f,0x00,0x90,0x27,0x3f,0xc1,0x4d}};
static EFI_GUID guid_muris_absoluti={0x8d59d32b,0xc655,0x4ae9,{0x9b,0x15,0xf2,0x59,0x04,0x99,0x2a,0x43}};

static EFI_GRAPHICS_OUTPUT_PROTOCOL *gop;
static EFI_SIMPLE_POINTER_PROTOCOL *murus_relativus;
static EFI_ABSOLUTE_POINTER_PROTOCOL *murus_absolutus;
static EFI_BOOT_SERVICES *opera;
static U32 latitudo,altitudo,linea,formatum;
static U32 *framebuffer;
static SUPERFICIES programmata,tabula,taskbar,cursor;
static U8 activum=1;
static U8 status_programmata=STATUS_VISIBILIS;
static U8 status_tabula=STATUS_VISIBILIS;
static I64 murus_x=0,murus_y=0;
static U8 bulla_cruda=0,bulla_stabilis=0,bulla_aetas=0,bulla_vetus=0;
static U8 tractio=0;
static I32 tractio_dx=0,tractio_dy=0;

static U32 argb(U8 a,U8 r,U8 g,U8 b){return ((U32)a<<24)|((U32)r<<16)|((U32)g<<8)|b;}
static U8 A(U32 c){return(U8)(c>>24);} static U8 R(U32 c){return(U8)(c>>16);}
static U8 G(U32 c){return(U8)(c>>8);} static U8 B(U32 c){return(U8)c;}

static U32 misce(U32 infra,U32 supra){U32 a=A(supra),ia=255-a;if(a==0)return infra;if(a==255)return supra|0xff000000U;return argb(255,(U8)((R(supra)*a+R(infra)*ia)/255),(U8)((G(supra)*a+G(infra)*ia)/255),(U8)((B(supra)*a+B(infra)*ia)/255));}
static void framebuffer_scribe(U32 x,U32 y,U32 c){U32 r=R(c),g=G(c),b=B(c),out;if(formatum==0)out=r|(g<<8)|(b<<16);else out=b|(g<<8)|(r<<16);framebuffer[(UINTN)y*linea+x]=out;}
static U32 fundum_linea(U32 y){U32 t=(U64)y*255/(altitudo?altitudo:1);return argb(255,(U8)((11*(255-t)+6*t)/255),(U8)((79*(255-t)+27*t)/255),(U8)((130*(255-t)+49*t)/255));}

static U8 glyph(char c,U8 row){
    static const U8 A_[7]={14,17,17,31,17,17,17},B_[7]={30,17,17,30,17,17,30},C_[7]={14,17,16,16,16,17,14};
    static const U8 D_[7]={30,17,17,17,17,17,30},E_[7]={31,16,16,30,16,16,31},G_[7]={14,17,16,23,17,17,15};
    static const U8 I_[7]={31,4,4,4,4,4,31},L_[7]={16,16,16,16,16,16,31},M_[7]={17,27,21,21,17,17,17};
    static const U8 N_[7]={17,25,21,19,17,17,17},O_[7]={14,17,17,17,17,17,14},P_[7]={30,17,17,30,16,16,16};
    static const U8 R_[7]={30,17,17,30,20,18,17},S_[7]={15,16,16,14,1,1,30},T_[7]={31,4,4,4,4,4,4};
    static const U8 U_[7]={17,17,17,17,17,17,14},V_[7]={17,17,17,17,17,10,4},Y_[7]={17,17,10,4,4,4,4};
    const U8 *p=0;switch(c){case'A':p=A_;break;case'B':p=B_;break;case'C':p=C_;break;case'D':p=D_;break;case'E':p=E_;break;case'G':p=G_;break;case'I':p=I_;break;case'L':p=L_;break;case'M':p=M_;break;case'N':p=N_;break;case'O':p=O_;break;case'P':p=P_;break;case'R':p=R_;break;case'S':p=S_;break;case'T':p=T_;break;case'U':p=U_;break;case'V':p=V_;break;case'Y':p=Y_;break;default:return 0;}return p[row];
}

static void srect(SUPERFICIES*s,U32 x,U32 y,U32 w,U32 h,U32 c){if(x>=s->w||y>=s->h)return;if(x+w>s->w)w=s->w-x;if(y+h>s->h)h=s->h-y;for(U32 yy=0;yy<h;yy++){U32*p=s->pix+(UINTN)(y+yy)*s->w+x;for(U32 xx=0;xx<w;xx++)p[xx]=c;}}
static void smargo(SUPERFICIES*s,U32 x,U32 y,U32 w,U32 h,U32 c){if(w<2||h<2)return;srect(s,x,y,w,1,c);srect(s,x,y+h-1,w,1,c);srect(s,x,y,1,h,c);srect(s,x+w-1,y,1,h,c);}
static void stext(SUPERFICIES*s,U32 x,U32 y,const char*t,U32 c,U32 scala){while(*t){char ch=*t++;if(ch==' '){x+=4*scala;continue;}for(U8 r=0;r<7;r++){U8 bits=glyph(ch,r);for(U8 b=0;b<5;b++)if(bits&(16>>b))srect(s,x+b*scala,y+r*scala,scala,scala,c);}x+=6*scala;}}
static void svacua(SUPERFICIES*s){for(UINTN i=0;i<(UINTN)s->w*s->h;i++)s->pix[i]=0;}

static void fenestra_pingere(SUPERFICIES*s,const char*titulus,U8 activa,U8 genus){
    U32 w=s->w-8,h=s->h-8;svacua(s);srect(s,6,7,w,h,argb(85,0,0,0));srect(s,0,0,w,h,argb(255,247,248,246));smargo(s,0,0,w,h,activa?argb(255,185,138,82):argb(255,135,149,158));
    for(U32 i=0;i<28;i++){U8 r=(U8)(activa?51-i:74-i/2),g=(U8)(activa?126-i*2:110-i),b=(U8)(activa?174-i:130-i/2);srect(s,1,1+i,w-2,1,argb(245,r,g,b));}
    srect(s,1,1,w-2,1,argb(210,234,248,255));stext(s,10,9,titulus,argb(255,234,248,255),1);srect(s,w-64,4,18,20,argb(255,185,196,207));srect(s,w-43,4,18,20,argb(255,185,196,207));srect(s,w-22,4,18,20,argb(255,168,58,58));
    srect(s,1,29,w-2,22,argb(255,241,238,228));srect(s,1,51,w-2,34,argb(255,226,232,234));srect(s,1,85,w-2,h-105,argb(255,248,249,247));srect(s,1,h-20,w-2,19,argb(255,226,230,230));
    if(genus==1){U32 side=w>500?145:115;srect(s,1,85,side,h-105,argb(255,222,232,235));srect(s,12,103,side-24,24,argb(255,26,93,146));stext(s,24,112,"OMNIA",argb(255,234,248,255),1);U32 cx=side+22,cw=w>cx+40?w-cx-30:80;srect(s,cx,113,cw,112,argb(255,237,244,247));smargo(s,cx,113,cw,112,argb(255,26,93,146));stext(s,cx+18,142,"TABULA",argb(255,8,35,61),2);}else{U32 left=18,top=105,gw=w-36;stext(s,left,94,"TABULA",argb(255,8,35,61),1);for(U32 j=0;j<6;j++)srect(s,left,top+j*25,gw,1,argb(255,210,219,222));for(U32 j=0;j<4;j++)srect(s,left+j*(gw/3),top,1,125,argb(255,215,223,225));}
}

static void cursor_pingere(void){svacua(&cursor);for(U32 y=0;y<14;y++){for(U32 x=0;x<=y/2+1;x++){U32 c=(x==0||x==y/2+1||y==13)?argb(255,12,20,27):argb(255,241,238,228);srect(&cursor,x,y,1,1,c);}}srect(&cursor,4,11,2,7,argb(255,12,20,27));srect(&cursor,6,15,5,2,argb(255,12,20,27));srect(&cursor,5,12,1,4,argb(255,241,238,228));}

static void taskbar_pingere(void){svacua(&taskbar);srect(&taskbar,0,0,taskbar.w,28,argb(255,8,35,61));srect(&taskbar,0,0,taskbar.w,1,argb(255,98,215,242));srect(&taskbar,4,4,82,20,argb(255,14,66,111));stext(&taskbar,16,10,"INITIUM",argb(255,234,248,255),1);if(status_programmata!=STATUS_CLAUSUS){srect(&taskbar,96,4,164,20,(activum==1&&status_programmata==STATUS_VISIBILIS)?argb(255,26,93,146):argb(255,16,55,83));stext(&taskbar,106,10,"PROGRAMMATA",argb(255,234,248,255),1);}if(status_tabula!=STATUS_CLAUSUS){srect(&taskbar,264,4,120,20,(activum==2&&status_tabula==STATUS_VISIBILIS)?argb(255,26,93,146):argb(255,16,55,83));stext(&taskbar,276,10,"TABULA",argb(255,234,248,255),1);}}

static U8 visibilis(U8 id){return id==1?status_programmata==STATUS_VISIBILIS:status_tabula==STATUS_VISIBILIS;}
static U32 sample(const SUPERFICIES*s,U32 x,U32 y){if(x<s->x||y<s->y||x>=s->x+s->w||y>=s->y+s->h)return 0;return s->pix[(UINTN)(y-s->y)*s->w+(x-s->x)];}
static void compone(REGIO r){if(r.x>=latitudo||r.y>=altitudo)return;if(r.x+r.w>latitudo)r.w=latitudo-r.x;if(r.y+r.h>altitudo)r.h=altitudo-r.y;for(U32 y=r.y;y<r.y+r.h;y++){U32 basis=fundum_linea(y);for(U32 x=r.x;x<r.x+r.w;x++){U32 c=basis;if(y==altitudo*52/100&&x>latitudo*18/100&&x<latitudo*90/100)c=argb(255,56,126,164);if(y==altitudo*52/100+38&&x>latitudo*22/100&&x<latitudo*84/100)c=argb(255,42,104,146);if(activum==1){if(visibilis(2))c=misce(c,sample(&tabula,x,y));if(visibilis(1))c=misce(c,sample(&programmata,x,y));}else{if(visibilis(1))c=misce(c,sample(&programmata,x,y));if(visibilis(2))c=misce(c,sample(&tabula,x,y));}c=misce(c,sample(&taskbar,x,y));c=misce(c,sample(&cursor,x,y));framebuffer_scribe(x,y,c);}}}
static REGIO coniunge(REGIO a,REGIO b){U32 x=a.x<b.x?a.x:b.x,y=a.y<b.y?a.y:b.y,ar=a.x+a.w,br=b.x+b.w,ab=a.y+a.h,bb=b.y+b.h,r=ar>br?ar:br,d=ab>bb?ab:bb;REGIO o={x,y,r-x,d-y};return o;}
static REGIO regio_super(const SUPERFICIES*s){REGIO r={s->x,s->y,s->w,s->h};return r;}
static REGIO regio_cursor(void){return regio_super(&cursor);}

static EFI_STATUS superficiem_crea(SUPERFICIES*s,U32 w,U32 h,U32 x,U32 y){void*p=0;UINTN n=(UINTN)w*h*4;if(opera->AllocatePool(EfiLoaderData,n,&p)!=EFI_SUCCESS||!p)return 1;s->pix=(U32*)p;s->w=w;s->h=h;s->x=x;s->y=y;svacua(s);return EFI_SUCCESS;}
static void superficiem_libera(SUPERFICIES*s){if(s->pix){opera->FreePool(s->pix);s->pix=0;}}

static EFI_STATUS elige_modum(void){U32 optimus=gop->Mode->Mode;U64 area_optima=0;for(U32 m=0;m<gop->Mode->MaxMode;m++){EFI_GRAPHICS_OUTPUT_MODE_INFORMATION*i=0;UINTN sz=0;if(gop->QueryMode(gop,m,&sz,&i)==EFI_SUCCESS&&i){U64 area=(U64)i->HorizontalResolution*i->VerticalResolution;if(i->PixelFormat<=1&&i->HorizontalResolution>=1024&&i->VerticalResolution>=600&&area>area_optima){optimus=m;area_optima=area;}opera->FreePool(i);}}if(area_optima&&optimus!=gop->Mode->Mode)return gop->SetMode(gop,optimus);return EFI_SUCCESS;}

static void omnia_redde(void){fenestra_pingere(&programmata,"PROGRAMMATA",activum==1,1);fenestra_pingere(&tabula,"TABULA",activum==2,2);taskbar_pingere();REGIO totum={0,0,latitudo,altitudo};compone(totum);}
static void focus_set(U8 id){if(id==1&&status_programmata!=STATUS_VISIBILIS)return;if(id==2&&status_tabula!=STATUS_VISIBILIS)return;activum=id;fenestra_pingere(&programmata,"PROGRAMMATA",activum==1,1);fenestra_pingere(&tabula,"TABULA",activum==2,2);taskbar_pingere();REGIO r=coniunge(regio_super(&programmata),regio_super(&tabula));r=coniunge(r,regio_super(&taskbar));r=coniunge(r,regio_cursor());compone(r);}
static void activum_reelige(void){if(activum==1&&status_programmata==STATUS_VISIBILIS)return;if(activum==2&&status_tabula==STATUS_VISIBILIS)return;if(status_programmata==STATUS_VISIBILIS)activum=1;else if(status_tabula==STATUS_VISIBILIS)activum=2;else activum=0;}

static U8 punctum_in(const SUPERFICIES*s,I64 x,I64 y){return x>=(I64)s->x&&y>=(I64)s->y&&x<(I64)(s->x+s->w-8)&&y<(I64)(s->y+s->h-8);}
static U8 hit_fenestra(I64 x,I64 y){if(activum==1){if(status_programmata==STATUS_VISIBILIS&&punctum_in(&programmata,x,y))return 1;if(status_tabula==STATUS_VISIBILIS&&punctum_in(&tabula,x,y))return 2;}else{if(status_tabula==STATUS_VISIBILIS&&punctum_in(&tabula,x,y))return 2;if(status_programmata==STATUS_VISIBILIS&&punctum_in(&programmata,x,y))return 1;}return 0;}

static void status_muta(U8 id,U8 status){SUPERFICIES*s=id==1?&programmata:&tabula;REGIO vetus=regio_super(s);if(id==1)status_programmata=status;else status_tabula=status;activum_reelige();fenestra_pingere(&programmata,"PROGRAMMATA",activum==1,1);fenestra_pingere(&tabula,"TABULA",activum==2,2);taskbar_pingere();REGIO r=coniunge(vetus,regio_super(&taskbar));r=coniunge(r,regio_cursor());compone(r);}

static void taskbar_click(I64 x){if(x>=96&&x<260&&status_programmata!=STATUS_CLAUSUS){if(status_programmata==STATUS_MINIMUS){status_programmata=STATUS_VISIBILIS;focus_set(1);}else if(activum==1)status_muta(1,STATUS_MINIMUS);else focus_set(1);return;}if(x>=264&&x<384&&status_tabula!=STATUS_CLAUSUS){if(status_tabula==STATUS_MINIMUS){status_tabula=STATUS_VISIBILIS;focus_set(2);}else if(activum==2)status_muta(2,STATUS_MINIMUS);else focus_set(2);}}

static void mouse_down(void){if(murus_y>=altitudo-28){taskbar_click(murus_x);return;}U8 id=hit_fenestra(murus_x,murus_y);if(!id)return;if(id!=activum)focus_set(id);SUPERFICIES*s=id==1?&programmata:&tabula;I64 lx=murus_x-(I64)s->x,ly=murus_y-(I64)s->y;U32 w=s->w-8;if(ly>=4&&ly<24&&lx>=(I64)(w-22)&&lx<(I64)(w-4)){status_muta(id,STATUS_CLAUSUS);return;}if(ly>=4&&ly<24&&lx>=(I64)(w-64)&&lx<(I64)(w-46)){status_muta(id,STATUS_MINIMUS);return;}if(ly>=0&&ly<28&&lx>=0&&lx<(I64)(w-68)){tractio=1;tractio_dx=(I32)(murus_x-s->x);tractio_dy=(I32)(murus_y-s->y);}}

static I64 motus_normalis(I32 valor,U64 resolutio,U32 amplitudo,U32 basis){I64 m;if(valor==0)return 0;if(resolutio==0)m=valor;else m=((I64)valor*6)/(I64)resolutio;if(m==0)m=valor<0?-1:1;m=(m*(I64)amplitudo)/(I64)basis;if(m==0)m=valor<0?-1:1;if(m>96)m=96;if(m<-96)m=-96;return m;}
static U8 bullam_confirma(U8 cruda){if(cruda!=bulla_cruda){bulla_cruda=cruda;bulla_aetas=0;}else if(bulla_aetas<2)bulla_aetas++;if(bulla_aetas>=1)bulla_stabilis=bulla_cruda;return bulla_stabilis;}

static U8 murem_lege(I64*x,I64*y,U8*bulla){U8 mutatum=0;U8 raw=bulla_cruda;if(murus_absolutus&&murus_absolutus->Mode){EFI_ABSOLUTE_POINTER_STATE st;if(murus_absolutus->GetState(murus_absolutus,&st)==EFI_SUCCESS){EFI_ABSOLUTE_POINTER_MODE*m=murus_absolutus->Mode;U64 dx=m->AbsoluteMaxX-m->AbsoluteMinX,dy=m->AbsoluteMaxY-m->AbsoluteMinY;if(dx&&dy){*x=(I64)((st.CurrentX-m->AbsoluteMinX)*(latitudo-1)/dx);*y=(I64)((st.CurrentY-m->AbsoluteMinY)*(altitudo-1)/dy);raw=(U8)(st.ActiveButtons&1);mutatum=1;}}}else if(murus_relativus&&murus_relativus->Mode){EFI_SIMPLE_POINTER_STATE st;if(murus_relativus->GetState(murus_relativus,&st)==EFI_SUCCESS){*x+=motus_normalis(st.RelativeMovementX,murus_relativus->Mode->ResolutionX,latitudo,320);*y+=motus_normalis(st.RelativeMovementY,murus_relativus->Mode->ResolutionY,altitudo,200);raw=st.LeftButton?1:0;mutatum=1;}}if(*x<0)*x=0;if(*y<0)*y=0;if(*x>(I64)latitudo-1)*x=latitudo-1;if(*y>(I64)altitudo-1)*y=altitudo-1;*bulla=bullam_confirma(raw);return mutatum;}

static void cursor_move(I64 nx,I64 ny){REGIO vetus=regio_cursor();cursor.x=(U32)(nx>(I64)latitudo-(I64)cursor.w?latitudo-cursor.w:nx);cursor.y=(U32)(ny>(I64)altitudo-(I64)cursor.h?altitudo-cursor.h:ny);REGIO novum=regio_cursor();compone(coniunge(vetus,novum));}

static void drag_move(void){if(!tractio||activum==0)return;SUPERFICIES*s=activum==1?&programmata:&tabula;REGIO vetus=regio_super(s);I32 nx=(I32)murus_x-tractio_dx,ny=(I32)murus_y-tractio_dy;I32 maxx=(I32)latitudo-(I32)s->w,maxy=(I32)altitudo-28-(I32)s->h;if(nx<0)nx=0;if(ny<0)ny=0;if(nx>maxx)nx=maxx;if(ny>maxy)ny=maxy;s->x=(U32)nx;s->y=(U32)ny;REGIO r=coniunge(vetus,regio_super(s));r=coniunge(r,regio_cursor());compone(r);}

static void clavis_move(I32 dx,I32 dy){if(activum==0)return;SUPERFICIES*s=activum==1?&programmata:&tabula;if(!visibilis(activum))return;REGIO vetus=regio_super(s);I32 nx=(I32)s->x+dx,ny=(I32)s->y+dy;I32 maxx=(I32)latitudo-(I32)s->w,maxy=(I32)altitudo-28-(I32)s->h;if(nx<0)nx=0;if(ny<0)ny=0;if(nx>maxx)nx=maxx;if(ny>maxy)ny=maxy;s->x=(U32)nx;s->y=(U32)ny;REGIO r=coniunge(vetus,regio_super(s));r=coniunge(r,regio_cursor());compone(r);}

EFI_STATUS EFIAPI efi_main(EFI_HANDLE imago,EFI_SYSTEM_TABLE*systema){EFI_STATUS st;EFI_INPUT_KEY k;(void)imago;opera=systema->BootServices;st=opera->LocateProtocol(&guid_graphica,0,(void**)&gop);if(st!=EFI_SUCCESS||!gop||!gop->Mode||!gop->Mode->Info)return 1;st=elige_modum();if(st!=EFI_SUCCESS)return st;latitudo=gop->Mode->Info->HorizontalResolution;altitudo=gop->Mode->Info->VerticalResolution;linea=gop->Mode->Info->PixelsPerScanLine;formatum=gop->Mode->Info->PixelFormat;framebuffer=(U32*)(UINTN)gop->Mode->FrameBufferBase;if(formatum>1||!framebuffer||latitudo<800||altitudo<600)return 1;
    U32 pw=latitudo*52/100,ph=altitudo*58/100,tw=latitudo*36/100,th=altitudo*44/100;if(pw<500)pw=500;if(ph<330)ph=330;if(tw<350)tw=350;if(th<260)th=260;if(superficiem_crea(&programmata,pw+8,ph+8,latitudo*10/100,altitudo*8/100)!=EFI_SUCCESS)return 2;if(superficiem_crea(&tabula,tw+8,th+8,latitudo*56/100,altitudo*18/100)!=EFI_SUCCESS){superficiem_libera(&programmata);return 2;}if(superficiem_crea(&taskbar,latitudo,28,0,altitudo-28)!=EFI_SUCCESS){superficiem_libera(&programmata);superficiem_libera(&tabula);return 2;}if(superficiem_crea(&cursor,18,22,latitudo/2,altitudo/2)!=EFI_SUCCESS){superficiem_libera(&taskbar);superficiem_libera(&tabula);superficiem_libera(&programmata);return 2;}
    murus_x=latitudo/2;murus_y=altitudo/2;opera->LocateProtocol(&guid_muris_absoluti,0,(void**)&murus_absolutus);opera->LocateProtocol(&guid_muris,0,(void**)&murus_relativus);if(murus_absolutus)murus_absolutus->Reset(murus_absolutus,0);if(murus_relativus)murus_relativus->Reset(murus_relativus,0);cursor_pingere();omnia_redde();
    for(;;){while(systema->ConIn&&systema->ConIn->ReadKeyStroke(systema->ConIn,&k)==EFI_SUCCESS){if(k.ScanCode==EFI_SCAN_ESC)goto finis;if(k.UnicodeChar==9){if(activum==1&&status_tabula==STATUS_VISIBILIS)focus_set(2);else if(status_programmata==STATUS_VISIBILIS)focus_set(1);}if(k.ScanCode==EFI_SCAN_LEFT)clavis_move(-12,0);if(k.ScanCode==EFI_SCAN_RIGHT)clavis_move(12,0);if(k.ScanCode==EFI_SCAN_UP)clavis_move(0,-12);if(k.ScanCode==EFI_SCAN_DOWN)clavis_move(0,12);}I64 nx=murus_x,ny=murus_y;U8 nb=bulla_stabilis;if(murem_lege(&nx,&ny,&nb)){U8 mota=(nx!=murus_x||ny!=murus_y);murus_x=nx;murus_y=ny;if(mota)cursor_move(murus_x,murus_y);if(nb&&!bulla_vetus)mouse_down();if(nb&&tractio)drag_move();if(!nb&&bulla_vetus)tractio=0;bulla_vetus=nb;}opera->Stall(12000);}finis:superficiem_libera(&cursor);superficiem_libera(&taskbar);superficiem_libera(&tabula);superficiem_libera(&programmata);return EFI_SUCCESS;}
