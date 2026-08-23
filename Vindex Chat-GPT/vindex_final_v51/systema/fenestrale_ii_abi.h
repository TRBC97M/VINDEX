#ifndef VINDEX_FENESTRALE_II_ABI_H
#define VINDEX_FENESTRALE_II_ABI_H

/* Sylvia OS — Fenestrale II, Gradus D.
 * ABI memoriae inter firmamentum UEFI, nucleum VINDEX et clientes nativos.
 * Nulla structura huius fasciculi UI ipsam pingit.
 */

#ifndef __ASSEMBLER__
typedef unsigned long long FII_U64;
#endif

#define FENESTRALE2_BASIS              0x03000900ULL
#define FENESTRALE2_MAGIC              0x00324E45464C5953ULL /* "SYLFEN2\0" LE */
#define FENESTRALE2_VERSIO             1ULL
#define FENESTRALE2_MENSURA            128ULL

#define FENESTRALE2_EVENTA_CAPUT       0x03000980ULL
#define FENESTRALE2_EVENTA_BASIS       0x030009A0ULL
#define FENESTRALE2_EVENTA_CAPACITAS   32ULL
#define FENESTRALE2_EVENTUM_MENSURA    32ULL

/* Capacitas descriptoris. */
#define FII_CAP_FRAMEBUFFER_NATIVUS    (1ULL << 0)
#define FII_CAP_PIXEL_RGB_BGR          (1ULL << 1)
#define FII_CAP_MURUS_RELATIVUS        (1ULL << 2)
#define FII_CAP_MURUS_ABSOLUTUS        (1ULL << 3)
#define FII_CAP_EVENTA                 (1ULL << 4)
#define FII_CAP_COMPOSITORIUM          (1ULL << 5)

/* Typi eventuum. */
#define FII_EVENTUM_NULLUM             0ULL
#define FII_EVENTUM_MURUS_MOVETUR      1ULL
#define FII_EVENTUM_MURUS_BULLA        2ULL
#define FII_EVENTUM_CLAVIS_PREMITUR    3ULL
#define FII_EVENTUM_CLAVIS_SOLVITUR    4ULL
#define FII_EVENTUM_DISPLAY_MUTATUR    5ULL
#define FII_EVENTUM_FENESTRA           6ULL

#ifndef __ASSEMBLER__

typedef struct {
    FII_U64 magic;               /* +0x00 */
    FII_U64 versio;              /* +0x08 */
    FII_U64 mensura;             /* +0x10 */
    FII_U64 capacitates;         /* +0x18 */
    FII_U64 framebuffer;         /* +0x20 */
    FII_U64 latitudo;            /* +0x28 */
    FII_U64 altitudo;            /* +0x30 */
    FII_U64 pixel_per_lineam;    /* +0x38 */
    FII_U64 formatum_pixelorum;  /* +0x40 */
    FII_U64 bits_per_pixel;      /* +0x48 */
    FII_U64 murus_x;             /* +0x50 */
    FII_U64 murus_y;             /* +0x58 */
    FII_U64 bullae;              /* +0x60 */
    FII_U64 numerus_eventuum;    /* +0x68 */
    FII_U64 taskbar_altitudo;    /* +0x70 */
    FII_U64 scala_per_mille;     /* +0x78 */
} FENESTRALE2_DESCRIPTOR;

typedef struct {
    FII_U64 typus;
    FII_U64 vexilla;
    FII_U64 a;
    FII_U64 b;
} FENESTRALE2_EVENTUM;

typedef struct {
    FII_U64 caput_scripturae;
    FII_U64 caput_lectionis;
    FII_U64 capacitas;
    FII_U64 reservatum;
} FENESTRALE2_EVENTA_META;

_Static_assert(sizeof(FENESTRALE2_DESCRIPTOR) == FENESTRALE2_MENSURA,
               "FENESTRALE2_DESCRIPTOR mensura mutata est");
_Static_assert(sizeof(FENESTRALE2_EVENTUM) == FENESTRALE2_EVENTUM_MENSURA,
               "FENESTRALE2_EVENTUM mensura mutata est");
_Static_assert(sizeof(FENESTRALE2_EVENTA_META) == 32,
               "FENESTRALE2_EVENTA_META mensura mutata est");

#endif /* !__ASSEMBLER__ */

#endif /* VINDEX_FENESTRALE_II_ABI_H */
