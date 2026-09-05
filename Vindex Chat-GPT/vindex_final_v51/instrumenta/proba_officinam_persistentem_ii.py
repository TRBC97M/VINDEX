#!/usr/bin/env python3
"""P19-II: OFFICINA persistens in Sylvia per QEMU exercetur."""
from __future__ import annotations

import importlib.util
import socket
import sys
import time
from pathlib import Path


def importa_modulum(nomen: str, fasciculus: str) -> object:
    via = Path(__file__).resolve().with_name(fasciculus)
    spec = importlib.util.spec_from_file_location(nomen, via)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'probator importari non potest: {fasciculus}')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mitte(aux: object, monitor: socket.socket, clavis: str, mora: float = 0.13) -> None:
    responsum = aux.hmp(monitor, f'sendkey {clavis}')
    if 'unknown command' in responsum.lower():
        raise RuntimeError(f'HMP sendkey deest: {clavis}')
    time.sleep(mora)


def scribe_maiusculas(aux: object, monitor: socket.socket, textus: str) -> None:
    for c in textus:
        if 'A' <= c <= 'Z':
            mitte(aux, monitor, f'shift-{c.lower()}')
        elif '0' <= c <= '9':
            mitte(aux, monitor, c)
        else:
            raise ValueError(f'littera probationis non sustenta: {c!r}')


def numerus_coloris(aux: object, pix: bytes, w: int, regio: tuple[int, int, int, int], color: tuple[int, int, int]) -> int:
    x0, y0, x1, y1 = regio
    return sum(aux.pixel(pix, w, x, y) == color for y in range(y0, y1) for x in range(x0, x1))


def focus_officina(aux: object, pix: bytes, w: int, h: int) -> str | None:
    """Focus historicus aut chrome XII-E OFFICINAE apertae comprobatur."""
    bronzeum_vetus = (185, 138, 82)
    if aux.pixel(pix, w, 500, 64) == bronzeum_vetus:
        return 'historicus'

    regio = (130, 50, min(w, 1120), min(h - 40, 690))
    bronzeum = (181, 138, 84)
    aqua = (104, 202, 210)
    ebur = (242, 244, 247)
    aes = numerus_coloris(aux, pix, w, regio, bronzeum)
    aq = numerus_coloris(aux, pix, w, regio, aqua)
    eb = numerus_coloris(aux, pix, w, regio, ebur)
    if aes >= 80 and aq >= 20 and eb >= 500:
        return 'XII-E'
    return None


def move_ad_firmus(
    aux: object,
    monitor: socket.socket,
    out: Path,
    nomen: str,
    x: int,
    y: int,
    w: int,
    h: int,
) -> tuple[int, int]:
    """Paquetum HMP perditum tolerat, sed framebuffer cursorem probare semper debet."""
    ultimus: RuntimeError | None = None
    for tentamen in range(4):
        try:
            return aux.move_ad(monitor, out, f'{nomen}-t{tentamen}', x, y, w, h)
        except RuntimeError as exc:
            ultimus = exc
            textus = str(exc)
            if 'motus muris non consumptus' not in textus and 'cursor scopum' not in textus:
                raise
            time.sleep(0.18)
    if ultimus is not None:
        raise ultimus
    raise RuntimeError(f'cursor ad {nomen} moveri non potest')


def qmp_bulla(
    ps2: object,
    q: socket.socket,
    pressa: bool,
    dx: int,
) -> None:
    """Bullam sinistram per QMP input-send-event cum fasciculo relativo PS/2 vehit."""
    eventa: list[dict] = [
        {'type': 'btn', 'data': {'down': pressa, 'button': 'left'}},
    ]
    if dx != 0:
        eventa.append({'type': 'rel', 'data': {'axis': 'x', 'value': dx}})
    responsum = ps2.qmp(q, 'input-send-event', {'events': eventa})
    if 'error' in responsum:
        status = 'pressam' if pressa else 'relaxatam'
        raise RuntimeError(f'QMP bullam {status} recusavit: {responsum}')


def click_ps2(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    out: Path,
    nomen: str,
    prior: tuple[int, int],
    w: int,
    h: int,
) -> tuple[int, int]:
    """Cliccum QMP per PS/2 mittit; framebuffer post effectum cursorem reperit."""
    qmp_bulla(ps2, q, True, 1)
    time.sleep(0.32)
    qmp_bulla(ps2, q, False, -1)
    time.sleep(0.24)
    via = out / f'click-{nomen}-post.ppm'
    aux.captura(monitor, via)
    _, _, pix = aux.ppm(via)
    positio = aux.cursor_quaere(pix, w, h)
    return positio if positio is not None else prior


def elige_officinam_effectu(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    out: Path,
    via: Path,
    prior: tuple[int, int],
    w: int,
    h: int,
    nox: tuple[int, int, int],
    bronzeum: tuple[int, int, int],
    ebur: tuple[int, int, int],
) -> tuple[str | None, tuple[int, int]]:
    """Bullam QMP tenet donec OFFICINA in framebuffer vere appareat."""
    qmp_bulla(ps2, q, True, 1)

    testa: str | None = None
    try:
        for i in range(40):
            effectus = out / f'officina-electio-effectus-{i}.ppm'
            aux.captura(monitor, effectus)
            _, _, pix = aux.ppm(effectus)
            menu = aux.initium_top_quaere(pix, w, h, nox, bronzeum, ebur)
            if menu is None:
                testa = focus_officina(aux, pix, w, h)
                if testa is not None:
                    break
            time.sleep(0.14)
    finally:
        qmp_bulla(ps2, q, False, -1)
        time.sleep(0.18)

    aux.captura(monitor, via)
    _, _, pix_finalis = aux.ppm(via)
    if aux.initium_top_quaere(pix_finalis, w, h, nox, bronzeum, ebur) is not None:
        testa = None
    else:
        testa = focus_officina(aux, pix_finalis, w, h)
    positio = aux.cursor_quaere(pix_finalis, w, h)
    return testa, (positio if positio is not None else prior)


def aperi_officinam_per_initium(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    out: Path,
    via: Path,
    w: int,
    h: int,
) -> tuple[str | None, tuple[int, int]]:
    """INITIUM aperit, OFFICINAM eligit, deinde fenestram ipsam ut auctoritatem habet."""
    nox = (28, 31, 32)
    bronzeum = (185, 138, 82)
    ebur = (241, 238, 228)

    pos_initium = move_ad_firmus(aux, monitor, out, 'officina-initium', 50, h - 30, w, h)
    pos_initium = click_ps2(aux, ps2, q, monitor, out, 'officina-initium', pos_initium, w, h)

    menu = out / 'officina-initium-apertum.ppm'
    aux.captura(monitor, menu)
    _, _, pix_menu = aux.ppm(menu)
    top = aux.initium_top_quaere(pix_menu, w, h, nox, bronzeum, ebur)
    if top is None:
        return None, pos_initium

    # Quarta applicatio canonica: PROGRAMMATA, TABULA, TERMINALE, OFFICINA.
    officina_y = top + 92 + 3 * 54 + 22
    pos_officina = move_ad_firmus(aux, monitor, out, 'officina-initium-linea', 150, officina_y, w, h)
    return elige_officinam_effectu(
        aux, ps2, q, monitor, out, via, pos_officina, w, h, nox, bronzeum, ebur
    )


def cursorem_excita(
    aux: object,
    ps2: object,
    monitor: socket.socket,
    q: socket.socket,
    out: Path,
    modus: int,
    w: int,
    h: int,
    pix_initialis: bytes,
) -> tuple[int, int] | None:
    """Primum fasciculum PS/2 mittit donec cursor stabilis in framebuffer appareat."""
    positio = aux.cursor_quaere(pix_initialis, w, h)
    if positio is not None:
        return positio

    motus = ((4, 3), (8, 5), (-3, 7), (12, -4))
    for tentamen, (dx, dy) in enumerate(motus):
        responsum = ps2.qmp(
            q,
            'input-send-event',
            {
                'events': [
                    {'type': 'rel', 'data': {'axis': 'x', 'value': dx}},
                    {'type': 'rel', 'data': {'axis': 'y', 'value': dy}},
                ]
            },
        )
        if 'error' in responsum:
            raise RuntimeError(f'QMP motum PS/2 recusavit: {responsum}')
        aux.hmp(monitor, f'mouse_move {dx} {dy}')
        time.sleep(0.35)
        positio = aux.cursor_ex_captura_stabili(
            monitor, out, f'officina-p19-ii-{modus}-primus', tentamen, w, h
        )
        if positio is not None:
            print(f'OFFICINA-P19-II: cursor_primus={positio} tentamen={tentamen + 1}')
            return positio
    return None


def principale() -> int:
    if len(sys.argv) != 6:
        print('USUS: proba_officinam_persistentem_ii.py MONITOR QMP EXITUS MORA MODUS', file=sys.stderr)
        return 2

    aux = importa_modulum('proba_initium_ii', 'proba_initium_sylviae_ii.py')
    ps2 = importa_modulum('proba_fenestrale_ps2', 'proba_fenestrale_uefi_purum.py')
    mon_via = Path(sys.argv[1])
    qmp_via = Path(sys.argv[2])
    out = Path(sys.argv[3])
    mora = float(sys.argv[4])
    modus = int(sys.argv[5])
    if modus not in (1, 2):
        print('DEFECIT: modus debet esse 1 aut 2', file=sys.stderr)
        return 2

    finis = time.time() + 15.0
    while (not mon_via.exists() or not qmp_via.exists()) and time.time() < finis:
        time.sleep(0.1)
    if not mon_via.exists() or not qmp_via.exists():
        print('DEFECIT: monitor vel QMP QEMU deest', file=sys.stderr)
        return 3

    out.mkdir(parents=True, exist_ok=True)
    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.7)
    monitor.connect(str(mon_via))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    q.settimeout(2.0)
    q.connect(str(qmp_via))
    try:
        aux.lege_usque(monitor, b'(qemu) ', 2.0)
        salutatio = ps2.qmp_linea(q)
        if 'QMP' not in salutatio:
            print('DEFECIT: salutatio QMP invalida', file=sys.stderr)
            return 4
        ps2.qmp(q, 'qmp_capabilities')
        mures = ps2.qmp(q, 'query-mice').get('return', [])
        candidati = [m for m in mures if 'PS/2 Mouse' in str(m.get('name', ''))]
        if not candidati:
            print('DEFECIT: QEMU PS/2 Mouse deest', file=sys.stderr)
            return 5
        index = int(candidati[0]['index'])
        aux.hmp(monitor, f'mouse_set {index}')
        print(f'OFFICINA-P19-II: mus_ps2_index={index}')
        time.sleep(mora)

        ante = out / f'officina-p19-ii-{modus}-ante.ppm'
        aperta = out / f'officina-p19-ii-{modus}-aperta.ppm'
        servata = out / f'officina-p19-ii-{modus}-servata.ppm'
        aux.captura(monitor, ante)
        w, h, pix_ante = aux.ppm(ante)
        if (w, h) != (1280, 800):
            print(f'DEFECIT: resolutio {w}x{h}', file=sys.stderr)
            return 6

        primus = cursorem_excita(aux, ps2, monitor, q, out, modus, w, h, pix_ante)
        if primus is None:
            print('DEFECIT: cursor PS/2 post motus primos in framebuffer non apparuit', file=sys.stderr)
            return 7

        testa, pos = aperi_officinam_per_initium(aux, ps2, q, monitor, out, aperta, w, h)
        if testa is None:
            print('DEFECIT: OFFICINA per INITIUM focus/chrome non accepit', file=sys.stderr)
            return 8

        if modus == 1:
            scribe_maiusculas(aux, monitor, 'ZEPHYR72941')
            mitte(aux, monitor, 'ret')
            scribe_maiusculas(aux, monitor, 'NOVAPERSISTET')
        else:
            mitte(aux, monitor, 'down')
            for _ in range(13):
                mitte(aux, monitor, 'right', 0.08)
            scribe_maiusculas(aux, monitor, 'X')

        mitte(aux, monitor, 'f2', 0.8)
        aux.captura(monitor, servata)
        _, _, pix_saved = aux.ppm(servata)
        testa_post = focus_officina(aux, pix_saved, w, h)
        if testa_post != testa:
            print(f'DEFECIT: F2 focum OFFICINAE amisit: {testa}->{testa_post}', file=sys.stderr)
            return 9

        print(f'OFFICINA-P19-II: initium={modus} testa={testa} cursor_initium={pos} F2=missum')
        return 0
    finally:
        try:
            aux.hmp(monitor, 'quit')
        except Exception:
            pass
        monitor.close()
        q.close()


if __name__ == '__main__':
    raise SystemExit(principale())
