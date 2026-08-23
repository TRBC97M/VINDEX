#!/usr/bin/env python3
"""Firmamentum 0.51 ad ABI Fenestralis II Gradus E sine fonte canonico mutando transformat."""

from __future__ import annotations

from pathlib import Path
import sys


def substitue(textus: str, vetus: str, novus: str, nomen: str) -> str:
    numerus = textus.count(vetus)
    if numerus != 1:
        raise RuntimeError(f"ANCORA {nomen}: expectata I, inventae {numerus}")
    return textus.replace(vetus, novus, 1)


def principale() -> int:
    if len(sys.argv) != 3:
        print("USUS: genera_firmamentum_fenestrale_e.py FONS.c EXITUS.c", file=sys.stderr)
        return 64

    fons = Path(sys.argv[1])
    exitus = Path(sys.argv[2])
    textus = fons.read_text(encoding="utf-8")

    textus = substitue(
        textus,
        "typedef unsigned char      U8;",
        '#include "fenestrale_ii_abi.h"\n\ntypedef unsigned char      U8;',
        "caput ABI",
    )

    textus = substitue(
        textus,
        "static U8 murus_paratus;",
        """static U8 murus_paratus;
static I64 murus_x_nativus;
static I64 murus_y_nativus;
""",
        "status muris nativi",
    )

    auxilia = r'''
/* Fenestrale II Gradus E — contractus novus iuxta viam hereditariam. */
static volatile FENESTRALE2_DESCRIPTOR *fenestrale2_descriptor(void) {
    return (volatile FENESTRALE2_DESCRIPTOR *)(UINTN)FENESTRALE2_BASIS;
}

static volatile FENESTRALE2_EVENTA_META *fenestrale2_eventa_meta(void) {
    return (volatile FENESTRALE2_EVENTA_META *)(UINTN)FENESTRALE2_EVENTA_CAPUT;
}

static volatile FENESTRALE2_EVENTUM *fenestrale2_eventa(void) {
    return (volatile FENESTRALE2_EVENTUM *)(UINTN)FENESTRALE2_EVENTA_BASIS;
}

static void fenestrale2_eventum(U64 typus, U64 vexilla, U64 a, U64 b) {
    volatile FENESTRALE2_DESCRIPTOR *d = fenestrale2_descriptor();
    volatile FENESTRALE2_EVENTA_META *m = fenestrale2_eventa_meta();
    volatile FENESTRALE2_EVENTUM *e = fenestrale2_eventa();
    U64 scriptura;
    U64 lectio;
    U64 index;
    if (d->magic != FENESTRALE2_MAGIC || m->capacitas != FENESTRALE2_EVENTA_CAPACITAS)
        return;
    scriptura = m->caput_scripturae;
    lectio = m->caput_lectionis;
    if (scriptura - lectio >= FENESTRALE2_EVENTA_CAPACITAS)
        m->caput_lectionis = scriptura - FENESTRALE2_EVENTA_CAPACITAS + 1;
    index = scriptura & (FENESTRALE2_EVENTA_CAPACITAS - 1);
    e[index].typus = typus;
    e[index].vexilla = vexilla;
    e[index].a = a;
    e[index].b = b;
    m->caput_scripturae = scriptura + 1;
    d->numerus_eventuum++;
}

static void fenestrale2_murum_scribe(I64 x, I64 y, U64 bullae) {
    volatile FENESTRALE2_DESCRIPTOR *d = fenestrale2_descriptor();
    U64 vetus_x;
    U64 vetus_y;
    U64 veteres_bullae;
    if (d->magic != FENESTRALE2_MAGIC) return;
    if (x < 0) x = 0;
    if (y < 0) y = 0;
    if ((U64)x >= d->latitudo) x = d->latitudo ? (I64)d->latitudo - 1 : 0;
    if ((U64)y >= d->altitudo) y = d->altitudo ? (I64)d->altitudo - 1 : 0;
    vetus_x = d->murus_x;
    vetus_y = d->murus_y;
    veteres_bullae = d->bullae;
    d->murus_x = (U64)x;
    d->murus_y = (U64)y;
    d->bullae = bullae;
    if (vetus_x != (U64)x || vetus_y != (U64)y)
        fenestrale2_eventum(FII_EVENTUM_MURUS_MOVETUR, 0, (U64)x, (U64)y);
    if (veteres_bullae != bullae)
        fenestrale2_eventum(FII_EVENTUM_MURUS_BULLA, 0, bullae, veteres_bullae);
}

static void fenestrale2_para(EFI_GRAPHICS_OUTPUT_PROTOCOL *graphica) {
    volatile FENESTRALE2_DESCRIPTOR *d = fenestrale2_descriptor();
    volatile FENESTRALE2_EVENTA_META *m = fenestrale2_eventa_meta();
    U64 capacitates = FII_CAP_FRAMEBUFFER_NATIVUS |
                      FII_CAP_PIXEL_RGB_BGR |
                      FII_CAP_EVENTA;
    memoria_vacua((void *)(UINTN)FENESTRALE2_BASIS,
                  (UINTN)(FENESTRALE2_EVENTA_BASIS - FENESTRALE2_BASIS +
                          FENESTRALE2_EVENTA_CAPACITAS * FENESTRALE2_EVENTUM_MENSURA));
    if (murus_relativus) capacitates |= FII_CAP_MURUS_RELATIVUS;
    if (murus_absolutus) capacitates |= FII_CAP_MURUS_ABSOLUTUS;
    d->magic = FENESTRALE2_MAGIC;
    d->versio = FENESTRALE2_VERSIO;
    d->mensura = FENESTRALE2_MENSURA;
    d->capacitates = capacitates;
    d->framebuffer = graphica->Mode->FrameBufferBase;
    d->latitudo = graphica->Mode->Info->HorizontalResolution;
    d->altitudo = graphica->Mode->Info->VerticalResolution;
    d->pixel_per_lineam = graphica->Mode->Info->PixelsPerScanLine;
    d->formatum_pixelorum = graphica->Mode->Info->PixelFormat;
    d->bits_per_pixel = 32;
    murus_x_nativus = (I64)d->latitudo / 2;
    murus_y_nativus = (I64)d->altitudo / 2;
    d->murus_x = (U64)murus_x_nativus;
    d->murus_y = (U64)murus_y_nativus;
    d->bullae = 0;
    d->numerus_eventuum = 0;
    d->taskbar_altitudo = 28;
    d->scala_per_mille = 1000;
    m->caput_scripturae = 0;
    m->caput_lectionis = 0;
    m->capacitas = FENESTRALE2_EVENTA_CAPACITAS;
    m->reservatum = 0;
    fenestrale2_eventum(FII_EVENTUM_DISPLAY_MUTATUR, 0, d->latitudo, d->altitudo);
}

'''
    textus = substitue(
        textus,
        "U64 firmamentum_polle(void) {",
        auxilia + "U64 firmamentum_polle(void) {",
        "auxilia Gradus E",
    )

    textus = substitue(
        textus,
        """        if (clavis.UnicodeChar != 0) unicode_inpone(clavis.UnicodeChar);
        else {""",
        """        fenestrale2_eventum(FII_EVENTUM_CLAVIS_PREMITUR,
                             clavis.UnicodeChar != 0 ? 1 : 0,
                             (U64)clavis.UnicodeChar, (U64)clavis.ScanCode);
        if (clavis.UnicodeChar != 0) unicode_inpone(clavis.UnicodeChar);
        else {""",
        "eventum clavis",
    )

    textus = substitue(
        textus,
        """                I64 x = (I64)((status.CurrentX - m->AbsoluteMinX) * 306 / dx);
                I64 y = (I64)((status.CurrentY - m->AbsoluteMinY) * 186 / dy);
                muri_statum_para(x, y, status.ActiveButtons & 1);
                muri_statum_confirma();
                return 0;""",
        """                I64 x_nativus = (I64)((status.CurrentX - m->AbsoluteMinX) *
                    (graphica_globalis->Mode->Info->HorizontalResolution - 1) / dx);
                I64 y_nativus = (I64)((status.CurrentY - m->AbsoluteMinY) *
                    (graphica_globalis->Mode->Info->VerticalResolution - 1) / dy);
                I64 x = (I64)((status.CurrentX - m->AbsoluteMinX) * 306 / dx);
                I64 y = (I64)((status.CurrentY - m->AbsoluteMinY) * 186 / dy);
                murus_x_nativus = x_nativus;
                murus_y_nativus = y_nativus;
                muri_statum_para(x, y, status.ActiveButtons & 1);
                muri_statum_confirma();
                fenestrale2_murum_scribe(murus_x_nativus, murus_y_nativus,
                                         bullae_stabiles);
                return 0;""",
        "murus absolutus",
    )

    textus = substitue(
        textus,
        """            I64 x = (I64)communis[0] + motus_normalis(status.RelativeMovementX, murus_relativus->Mode->ResolutionX);
            I64 y = (I64)communis[1] + motus_normalis(status.RelativeMovementY, murus_relativus->Mode->ResolutionY);
            muri_statum_para(x, y, status.LeftButton ? 1 : 0);""",
        """            I64 mx = motus_normalis(status.RelativeMovementX,
                                     murus_relativus->Mode->ResolutionX);
            I64 my = motus_normalis(status.RelativeMovementY,
                                     murus_relativus->Mode->ResolutionY);
            I64 x = (I64)communis[0] + mx;
            I64 y = (I64)communis[1] + my;
            murus_x_nativus += mx * (I64)graphica_globalis->Mode->Info->HorizontalResolution / 320;
            murus_y_nativus += my * (I64)graphica_globalis->Mode->Info->VerticalResolution / 200;
            muri_statum_para(x, y, status.LeftButton ? 1 : 0);""",
        "murus relativus",
    )

    textus = substitue(
        textus,
        """    muri_statum_confirma();
    return 0;
}""",
        """    muri_statum_confirma();
    fenestrale2_murum_scribe(murus_x_nativus, murus_y_nativus,
                             bullae_stabiles);
    return 0;
}""",
        "confirmatio muris",
    )

    textus = substitue(
        textus,
        """    if (murus_absolutus) murus_absolutus->Reset(murus_absolutus, 0);
    if (murus_relativus) murus_relativus->Reset(murus_relativus, 0);
    systema->ConIn->Reset(systema->ConIn, 0);""",
        """    if (murus_absolutus) murus_absolutus->Reset(murus_absolutus, 0);
    if (murus_relativus) murus_relativus->Reset(murus_relativus, 0);
    fenestrale2_para(graphica);
    systema->ConIn->Reset(systema->ConIn, 0);""",
        "initium descriptoris",
    )

    exitus.write_text(textus, encoding="utf-8")
    print("RECTE: firmamentum Gradus E generatum est.")
    return 0


if __name__ == "__main__":
    raise SystemExit(principale())
