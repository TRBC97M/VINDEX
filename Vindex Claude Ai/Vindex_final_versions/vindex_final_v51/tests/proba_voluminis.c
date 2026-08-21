#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <sys/mman.h>

#include "../systema/uefi/firmamentum_uefi.c"

U8 _binary_nucleus_elf_start[1];
U8 _binary_nucleus_elf_end[1];
U8 _binary_textus_bin_start[1];
U8 _binary_textus_bin_end[1];
U8 _binary_forma_bin_start[1];
U8 _binary_forma_bin_end[1];

static U8 discus[2015 * 512];
static U8 exspectatum[MENSURA_FS];
static U64 scripturae;
static U64 expurgationes;
static U8 corrumpe;
static EFI_HANDLE manubrium_fictum = (EFI_HANDLE)(UINTN)0x44;

static EFI_BLOCK_IO_MEDIA medium = {
    .MediaId = 44,
    .MediaPresent = 1,
    .LogicalPartition = 1,
    .ReadOnly = 0,
    .BlockSize = 512,
    .IoAlign = 1,
    .LastBlock = 2014,
};

static EFI_STATUS EFIAPI blocos_lege(EFI_BLOCK_IO_PROTOCOL *hoc, U32 id,
                                      U64 lba, UINTN mensura, void *receptaculum) {
    (void)hoc;
    if (id != medium.MediaId || lba * 512 + mensura > sizeof(discus)) return 1;
    memcpy(receptaculum, discus + lba * 512, mensura);
    return EFI_SUCCESS;
}

static EFI_STATUS EFIAPI blocos_scribe(EFI_BLOCK_IO_PROTOCOL *hoc, U32 id,
                                        U64 lba, UINTN mensura, void *receptaculum) {
    (void)hoc;
    if (id != medium.MediaId || lba * 512 + mensura > sizeof(discus)) return 1;
    memcpy(discus + lba * 512, receptaculum, mensura);
    if (corrumpe && mensura != 0) discus[lba * 512 + mensura - 1] ^= 0x5a;
    scripturae++;
    return EFI_SUCCESS;
}

static EFI_STATUS EFIAPI blocos_expurga(EFI_BLOCK_IO_PROTOCOL *hoc) {
    (void)hoc;
    expurgationes++;
    return EFI_SUCCESS;
}

static EFI_BLOCK_IO_PROTOCOL blocos = {
    .Revision = 0x00010000,
    .Media = &medium,
    .ReadBlocks = blocos_lege,
    .WriteBlocks = blocos_scribe,
    .FlushBlocks = blocos_expurga,
};

static EFI_STATUS EFIAPI manubria_inveni(U32 modus, EFI_GUID *guid, void *clavis,
                                         UINTN *numerus, EFI_HANDLE **manubria) {
    static EFI_HANDLE inventa[1];
    (void)guid;
    (void)clavis;
    if (modus != 2) return 1;
    inventa[0] = manubrium_fictum;
    *numerus = 1;
    *manubria = inventa;
    return EFI_SUCCESS;
}

static EFI_STATUS EFIAPI protocollum_accipe(EFI_HANDLE manubrium, EFI_GUID *guid,
                                             void **protocollum) {
    (void)guid;
    if (manubrium != manubrium_fictum) return 1;
    *protocollum = &blocos;
    return EFI_SUCCESS;
}

static EFI_STATUS EFIAPI memoria_libera(void *p) {
    (void)p;
    return EFI_SUCCESS;
}

static int exige(int conditio, const char *nuntius) {
    if (conditio) return 0;
    fprintf(stderr, "ERRATUM: %s\n", nuntius);
    return 1;
}

int main(void) {
    EFI_BOOT_SERVICES officia = {0};
    EFI_SYSTEM_TABLE systema = {0};
    U8 *tabula;
    UINTN i;

    tabula = mmap((void *)(UINTN)COMMUNIS, 0x19000,
                  PROT_READ | PROT_WRITE,
                  MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED_NOREPLACE, -1, 0);
    if (tabula == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    memcpy(discus, "VINDEXV0", 8);
    *(U32 *)(void *)(discus + 8) = 1;
    *(U32 *)(void *)(discus + 12) = MENSURA_FS;
    officia.FreePool = memoria_libera;
    officia.HandleProtocol = protocollum_accipe;
    officia.LocateHandleBuffer = manubria_inveni;
    systema.BootServices = &officia;
    tabula_systematis = &systema;

    if (exige(volumen_crudum_inveni() == EFI_SUCCESS,
              "partitio VINDEX non inventa")) return 1;
    for (i = 0; i < MENSURA_FS; i++)
        ((U8 *)(UINTN)TABULA_FS)[i] = (U8)((i * 29 + 7) & 255);
    memcpy(exspectatum, (void *)(UINTN)TABULA_FS, MENSURA_FS);

    if (exige(volumen_scribe() == EFI_SUCCESS, "scriptura comprobata defecit")) return 1;
    if (exige(scripturae == 1 && expurgationes == 1,
              "scriptura aut expurgatio non vocata")) return 1;
    if (exige(memcmp(discus + 512, exspectatum, MENSURA_FS) == 0,
              "discus contentum falsum habet")) return 1;

    memset((void *)(UINTN)TABULA_FS, 0, MENSURA_FS);
    volumen_crudum = 0;
    volumen_mutabile = 0;
    if (exige(volumen_crudum_inveni() == EFI_SUCCESS,
              "partitio post initium novum non inventa")) return 1;
    if (exige(memcmp((void *)(UINTN)TABULA_FS, exspectatum, MENSURA_FS) == 0,
              "contentum post initium novum mutatum est")) return 1;

    corrumpe = 1;
    if (exige(volumen_scribe() != EFI_SUCCESS,
              "corruptio pro successu accepta est")) return 1;

    munmap((void *)(UINTN)COMMUNIS, 0x19000);
    puts("RECTE: volumen post initium novum permanet.");
    return 0;
}
