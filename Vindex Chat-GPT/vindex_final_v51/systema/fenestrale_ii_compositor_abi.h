#ifndef VINDEX_FENESTRALE_II_COMPOSITOR_ABI_H
#define VINDEX_FENESTRALE_II_COMPOSITOR_ABI_H

/* Sylvia OS — Fenestrale II, Gradus G.
 * Extensio experimentalis ABI ad superficies privatas clientium.
 * Nucleus et firmamentum canonicum 0.51 hoc fasciculo non mutantur.
 */

#include "fenestrale_ii_abi.h"

#define FENESTRALE2_COMPOSITOR_BASIS   0x03000E00ULL
#define FENESTRALE2_COMPOSITOR_MAGIC   0x0032504D434C5953ULL /* "SYLCMP2\0" LE */
#define FENESTRALE2_COMPOSITOR_VERSIO  1ULL
#define FENESTRALE2_COMPOSITOR_MENSURA 256ULL

/* Status mailbox serialis. */
#define FII_CMP_STATUS_VACUUM           0ULL
#define FII_CMP_STATUS_PETITUM          1ULL
#define FII_CMP_STATUS_PERFECTUM        2ULL
#define FII_CMP_STATUS_ERRATUM          3ULL

/* Operationes clientis. */
#define FII_CMP_OP_NULLUM               0ULL
#define FII_CMP_OP_CREA                 1ULL
#define FII_CMP_OP_DELE                 2ULL
#define FII_CMP_OP_PRAESENTA            3ULL
#define FII_CMP_OP_MOVE                  4ULL
#define FII_CMP_OP_OSTENDE               5ULL
#define FII_CMP_OP_CELA                  6ULL
#define FII_CMP_OP_FOCUS                 7ULL

/* Vexilla superficiei. */
#define FII_CMP_SUPERFICIES_ALPHA       (1ULL << 0)
#define FII_CMP_SUPERFICIES_RESIZABILIS (1ULL << 1)
#define FII_CMP_SUPERFICIES_FENESTRA    (1ULL << 2)

#ifndef __ASSEMBLER__

typedef struct {
    FII_U64 magic;                /* +0x00 */
    FII_U64 versio;               /* +0x08 */
    FII_U64 mensura;              /* +0x10 */
    FII_U64 status;               /* +0x18 */
    FII_U64 operatio;             /* +0x20 */
    FII_U64 client;               /* +0x28 */
    FII_U64 superficies_id;       /* +0x30 */
    FII_U64 vexilla;              /* +0x38 */
    FII_U64 petita_latitudo;      /* +0x40 */
    FII_U64 petita_altitudo;      /* +0x48 */
    FII_U64 basis_pixelorum;      /* +0x50 */
    FII_U64 pixel_per_lineam;     /* +0x58 */
    FII_U64 formatum_pixelorum;   /* +0x60 */
    FII_U64 x;                    /* +0x68 */
    FII_U64 y;                    /* +0x70 */
    FII_U64 damnum_x;             /* +0x78 */
    FII_U64 damnum_y;             /* +0x80 */
    FII_U64 damnum_latitudo;      /* +0x88 */
    FII_U64 damnum_altitudo;      /* +0x90 */
    FII_U64 responsum;            /* +0x98 */
    FII_U64 seriale_petitionis;   /* +0xA0 */
    FII_U64 seriale_responsi;     /* +0xA8 */
    FII_U64 reservata[10];        /* +0xB0 .. +0xF8 */
} FENESTRALE2_COMPOSITOR_MAILBOX;

_Static_assert(sizeof(FENESTRALE2_COMPOSITOR_MAILBOX) ==
               FENESTRALE2_COMPOSITOR_MENSURA,
               "FENESTRALE2_COMPOSITOR_MAILBOX mensura mutata est");
_Static_assert(FENESTRALE2_COMPOSITOR_BASIS >= 0x03000DA0ULL,
               "mailbox eventa Gradus D non tangat");
_Static_assert(FENESTRALE2_COMPOSITOR_BASIS + FENESTRALE2_COMPOSITOR_MENSURA
               <= 0x03001000ULL,
               "mailbox UMBRAM hereditariam non tangat");

#endif /* !__ASSEMBLER__ */

#endif /* VINDEX_FENESTRALE_II_COMPOSITOR_ABI_H */
