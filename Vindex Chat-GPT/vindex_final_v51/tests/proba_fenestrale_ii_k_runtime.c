#define _GNU_SOURCE
#include <errno.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include <ucontext.h>

#include "fenestrale_ii_compositor_k_abi.h"

#ifndef MAP_FIXED_NOREPLACE
#define MAP_FIXED_NOREPLACE MAP_FIXED
#endif

#define CLIENT_BASIS ((uintptr_t)0x00400000ULL)
#define CLIENT_MENSURA ((size_t)(64U * 4096U))
#define COMMUNIS_BASIS ((uintptr_t)0x03000000ULL)
#define COMMUNIS_MENSURA ((size_t)(16U * 4096U))
#define PIXEL_BASIS ((uintptr_t)0x04000000ULL)
#define PIXEL_MENSURA ((size_t)(8U * 1024U * 1024U))

static uint64_t ingressus_clientis;
static const char *stadium="initium";

static uint64_t __attribute__((naked,noinline)) clientem_voca(uint64_t ingressus __attribute__((unused))) {
    __asm__ volatile("push %rbx\n\tcall *%rdi\n\tpop %rbx\n\tret");
}

static void ruina(int signum,siginfo_t *info,void *contextus) {
    ucontext_t *u=(ucontext_t*)contextus;
    fprintf(stderr,"ERRATUM: %s: signum %d ad %p, rip=0x%llx rsp=0x%llx rbp=0x%llx.\n",stadium,signum,info->si_addr,(unsigned long long)u->uc_mcontext.gregs[REG_RIP],(unsigned long long)u->uc_mcontext.gregs[REG_RSP],(unsigned long long)u->uc_mcontext.gregs[REG_RBP]);
    _exit(128+signum);
}

static int imaginem_onera(const char *via) {
    int fd=open(via,O_RDONLY);
    if(fd<0){perror("open");return 0;}
    struct stat st;
    if(fstat(fd,&st)!=0||st.st_size<32||(size_t)st.st_size>CLIENT_MENSURA){perror("fstat");close(fd);return 0;}
    memset((void*)CLIENT_BASIS,0,CLIENT_MENSURA);
    size_t facta=0;
    while(facta<(size_t)st.st_size){ssize_t n=read(fd,(void*)(CLIENT_BASIS+facta),(size_t)st.st_size-facta);if(n<=0){perror("read");close(fd);return 0;}facta+=(size_t)n;}
    close(fd);
    uint64_t involucrum=*(uint64_t*)(CLIENT_BASIS+24);
    uintptr_t finis=CLIENT_BASIS+(uintptr_t)st.st_size;
    if(involucrum<CLIENT_BASIS||involucrum>=finis)return 0;
    size_t limen=(size_t)(finis-involucrum);if(limen>64)limen=64;
    uint8_t *q=(uint8_t*)(uintptr_t)involucrum;
    if(limen<22||q[0]!=0x58)return 0;
    for(size_t i=16;i+5<limen;i++)if(q[i]==0xe8){int32_t rel;memcpy(&rel,q+i+1,sizeof(rel));uint64_t target=involucrum+i+5+(int64_t)rel;if(target>=CLIENT_BASIS&&target<finis){ingressus_clientis=target;return 1;}}
    return 0;
}

static int eventum_proba(const char *via,uint64_t client) {
    if(!imaginem_onera(via))return 0;
    FENESTRALE2_COMPOSITOR_MAILBOX *m=(FENESTRALE2_COMPOSITOR_MAILBOX*)(uintptr_t)FENESTRALE2_COMPOSITOR_BASIS;
    uint32_t *pix=mmap((void*)PIXEL_BASIS,PIXEL_MENSURA,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS|MAP_FIXED_NOREPLACE,-1,0);
    if(pix==MAP_FAILED){perror("mmap pixel");return 0;}
    memset(m,0,sizeof(*m));
    m->magic=FENESTRALE2_COMPOSITOR_MAGIC;
    m->versio=FENESTRALE2_COMPOSITOR_VERSIO;
    m->mensura=FENESTRALE2_COMPOSITOR_MENSURA;
    stadium="petitio CREA";uint64_t r=clientem_voca(ingressus_clientis);
    if(r!=10||m->status!=FII_CMP_STATUS_PETITUM||m->operatio!=FII_CMP_OP_CREA||m->client!=client){fprintf(stderr,"ERRATUM: initium clientis %llu.\n",(unsigned long long)client);munmap(pix,PIXEL_MENSURA);return 0;}
    size_t init_w=(size_t)m->petita_latitudo,init_h=(size_t)m->petita_altitudo;
    if(init_w<480||init_h<320||init_w*init_h*sizeof(uint32_t)>PIXEL_MENSURA){fprintf(stderr,"ERRATUM: mensura initialis clientis %llu.\n",(unsigned long long)client);munmap(pix,PIXEL_MENSURA);return 0;}
    m->superficies_id=client;m->basis_pixelorum=PIXEL_BASIS;m->pixel_per_lineam=init_w;m->formatum_pixelorum=0;m->responsum=0;m->status=FII_CMP_STATUS_PERFECTUM;
    stadium="pictura initialis";r=clientem_voca(ingressus_clientis);
    if(r!=11||m->status!=FII_CMP_STATUS_PETITUM||m->operatio!=FII_CMP_OP_PRAESENTA){fprintf(stderr,"ERRATUM: pictura initialis clientis %llu.\n",(unsigned long long)client);munmap(pix,PIXEL_MENSURA);return 0;}
    m->responsum=0;m->status=FII_CMP_STATUS_PERFECTUM;
    stadium="finis initialis";r=clientem_voca(ingressus_clientis);
    if(r!=0||m->status!=FII_CMP_STATUS_VACUUM){fprintf(stderr,"ERRATUM: finis initialis clientis %llu.\n",(unsigned long long)client);munmap(pix,PIXEL_MENSURA);return 0;}

    const size_t w=640,h=420,n=w*h;
    memset(pix,0,n*sizeof(uint32_t));
    memset(m,0,sizeof(*m));
    m->magic=FENESTRALE2_COMPOSITOR_MAGIC;
    m->versio=FENESTRALE2_COMPOSITOR_VERSIO;
    m->mensura=FENESTRALE2_COMPOSITOR_MENSURA;
    m->status=FII_CMP_STATUS_PERFECTUM;
    m->operatio=FII_CMP_OP_EVENTUM;
    m->client=client;
    m->superficies_id=client;
    m->basis_pixelorum=(uint64_t)(uintptr_t)pix;
    m->pixel_per_lineam=w;
    m->petita_latitudo=w;
    m->petita_altitudo=h;
    m->reservata[FII_CMP_EVENTUM_ARG_TYPUS]=FII_CMP_EVENTUM_DIMENSIO;
    stadium="eventum DIMENSIO";r=clientem_voca(ingressus_clientis);
    size_t picta=0;
    for(size_t i=0;i<n;i++)if(pix[i])picta++;
    if(r!=20||m->status!=FII_CMP_STATUS_VACUUM||picta<n/3){fprintf(stderr,"ERRATUM: eventum dimensionis clientis %llu (r=%llu, picta=%zu).\n",(unsigned long long)client,(unsigned long long)r,picta);munmap(pix,PIXEL_MENSURA);return 0;}
    uint32_t nota=pix[0];
    m->status=FII_CMP_STATUS_PERFECTUM;
    m->operatio=FII_CMP_OP_EVENTUM;
    m->reservata[FII_CMP_EVENTUM_ARG_TYPUS]=FII_CMP_EVENTUM_FOCUS;
    m->reservata[FII_CMP_EVENTUM_ARG_PRIMUM]=FII_CMP_FOCUS_ACTIVUS;
    stadium="eventum FOCUS";r=clientem_voca(ingressus_clientis);
    if(r!=20||m->status!=FII_CMP_STATUS_VACUUM||pix[0]!=nota){fprintf(stderr,"ERRATUM: eventum focus clientis %llu.\n",(unsigned long long)client);munmap(pix,PIXEL_MENSURA);return 0;}
    munmap(pix,PIXEL_MENSURA);
    return 1;
}

int main(int argc,char **argv) {
    if(argc!=3){fprintf(stderr,"USUS: %s programmata.elf tabula.elf\n",argv[0]);return 64;}
    struct sigaction act;memset(&act,0,sizeof(act));act.sa_sigaction=ruina;act.sa_flags=SA_SIGINFO;sigaction(SIGSEGV,&act,0);
    void *codex=mmap((void*)CLIENT_BASIS,CLIENT_MENSURA,PROT_READ|PROT_WRITE|PROT_EXEC,MAP_PRIVATE|MAP_ANONYMOUS|MAP_FIXED_NOREPLACE,-1,0);
    void *communis=mmap((void*)COMMUNIS_BASIS,COMMUNIS_MENSURA,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS|MAP_FIXED_NOREPLACE,-1,0);
    if(codex==MAP_FAILED||communis==MAP_FAILED){fprintf(stderr,"ERRATUM: mmap: %s\n",strerror(errno));return 77;}
    FENESTRALE2_DESCRIPTOR *d=(FENESTRALE2_DESCRIPTOR*)(uintptr_t)FENESTRALE2_BASIS;
    d->magic=FENESTRALE2_MAGIC;d->versio=FENESTRALE2_VERSIO;d->mensura=FENESTRALE2_MENSURA;d->capacitates=FII_CAP_COMPOSITORIUM;d->latitudo=1366;d->altitudo=768;d->taskbar_altitudo=28;
    if(!eventum_proba(argv[1],1)||!eventum_proba(argv[2],2))return 1;
    puts("RECTE: clientes K eventa focus et dimensionis exsequuntur.");
    return 0;
}
