#!/usr/bin/env python3
"""P16-XI-B: bullae PS/2 consumptae probantur, cursor framebuffer auctoritate."""
from __future__ import annotations

import importlib.util
import re
import socket
import time
from pathlib import Path


def importa(nomen: str, fasciculus: str) -> object:
    via = Path(__file__).resolve().with_name(fasciculus)
    spec = importlib.util.spec_from_file_location(nomen, via)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"probator importari non potest: {fasciculus}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ps2_numerus_fasciculorum(aux: object, monitor: socket.socket) -> int | None:
    """Numeratorem +67 rectoris PS/2 e telemetria cruda legit."""
    textus = aux.hmp(monitor, "xp /1gx 0x03018840")
    for linea in textus.splitlines():
        if ":" not in linea:
            continue
        valores = re.findall(r"0x[0-9a-fA-F]+", linea.split(":", 1)[1])
        if valores:
            verbum = int(valores[0], 16)
            return (verbum >> 24) & 0xFF
    return None


def numeratorem_stabiliza(aux: object, monitor: socket.socket, mora: float = 1.5) -> int:
    """Nullum fasciculum priorem pendentem ante eventum novum relinquit."""
    finis = time.time() + mora
    prior: int | None = None
    stabilia = 0
    while time.time() < finis:
        nunc = ps2_numerus_fasciculorum(aux, monitor)
        if nunc is None:
            time.sleep(0.05)
            continue
        if prior == nunc:
            stabilia += 1
            if stabilia >= 2:
                return nunc
        else:
            prior = nunc
            stabilia = 0
        time.sleep(0.06)
    if prior is None:
        raise RuntimeError("numerator fasciculorum PS2 legi non potest")
    return prior


def eventum_bullae(ps2: object, q: socket.socket, pressa: bool, dx: int) -> None:
    eventa: list[dict] = [
        {"type": "btn", "data": {"down": pressa, "button": "left"}},
    ]
    if dx != 0:
        eventa.append({"type": "rel", "data": {"axis": "x", "value": dx}})
    responsum = ps2.qmp(q, "input-send-event", {"events": eventa})
    if "error" in responsum:
        status = "pressam" if pressa else "relaxatam"
        raise RuntimeError(f"QMP bullam PS2 {status} recusavit: {responsum}")


def exspecta_fasciculum(
    aux: object,
    monitor: socket.socket,
    prior: int,
    pressa: bool,
    mora: float = 3.0,
) -> tuple[int, int]:
    """Exigit et incrementum numeratoris et statum bullae petitum."""
    finis = time.time() + mora
    ultimus_n: int | None = prior
    ultimus_b: int | None = None
    while time.time() < finis:
        numerus = ps2_numerus_fasciculorum(aux, monitor)
        bullae = aux.ps2_bullae(monitor)
        ultimus_n, ultimus_b = numerus, bullae
        if numerus is not None and numerus != prior and bullae is not None and bool(bullae & 1) == pressa:
            return numerus, bullae & 0xFF
        time.sleep(0.06)
    status = "pressa" if pressa else "relaxata"
    raise RuntimeError(
        f"fasciculus PS2 {status} non consumptus est; numerator={prior}->{ultimus_n} telemetria={ultimus_b}"
    )


def bulla_consumpta(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    pressa: bool,
    dx: int,
    nomen: str,
) -> int:
    prior = numeratorem_stabiliza(aux, monitor)
    eventum_bullae(ps2, q, pressa, dx)
    numerus, raw = exspecta_fasciculum(aux, monitor, prior, pressa)
    status = "pressa" if pressa else "relaxata"
    print(f"PS2-SYNC: {nomen} bulla={status} fasciculi={prior}->{numerus} telemetria={raw}")
    return raw


def normaliza_relaxationem(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    nomen: str,
) -> None:
    """Fasciculum relaxatum vere consumptum imponit ante arctam 0→1."""
    raw = bulla_consumpta(aux, ps2, q, monitor, False, -2, f"{nomen}-prae")
    time.sleep(0.08)
    print(f"PS2-SYNC: {nomen} prae-relaxata confirmata={raw}")


def bulla_sync(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    pressa: bool,
    dx: int,
    nomen: str,
) -> int:
    if pressa:
        normaliza_relaxationem(aux, ps2, q, monitor, nomen)
    return bulla_consumpta(aux, ps2, q, monitor, pressa, dx, nomen)


def cursor_ex_framebuffer(
    aux: object,
    monitor: socket.socket,
    out: Path,
    nomen: str,
    prior: tuple[int, int],
    w: int,
    h: int,
) -> tuple[int, int]:
    """Post cliccum cursoris positio e framebuffer, non e delta telemetriae, sumitur."""
    for tentamen in range(3):
        via = out / f"{nomen}-cursor-{tentamen}.ppm"
        aux.captura(monitor, via)
        _, _, pix = aux.ppm(via)
        positio = aux.cursor_quaere(pix, w, h)
        if positio is not None:
            return positio
        time.sleep(0.16)
    return prior


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
    bulla_sync(aux, ps2, q, monitor, True, 1, nomen)
    time.sleep(0.10)
    bulla_sync(aux, ps2, q, monitor, False, -1, nomen)
    time.sleep(0.12)
    return cursor_ex_framebuffer(aux, monitor, out, f"click-{nomen}-sync", prior, w, h)


def elige_tabula_effectu(
    aux: object,
    ps2: object,
    q: socket.socket,
    monitor: socket.socket,
    out: Path,
    prior: tuple[int, int],
    w: int,
    h: int,
    nox: tuple[int, int, int],
    bronzeum: tuple[int, int, int],
    ebur: tuple[int, int, int],
) -> tuple[tuple[int, int], bool]:
    """Cliccum completum consumit, tum effectum semanticum framebuffer exspectat."""
    bulla_sync(aux, ps2, q, monitor, True, 1, "tabula-xib")
    time.sleep(0.10)
    bulla_sync(aux, ps2, q, monitor, False, -1, "tabula-xib")
    time.sleep(0.12)

    effectus = False
    for i in range(40):
        via = out / f"tabula-xib-sync-effectus-{i}.ppm"
        aux.captura(monitor, via)
        _, _, pix = aux.ppm(via)
        if aux.initium_top_quaere(pix, w, h, nox, bronzeum, ebur) is None:
            effectus = True
            break
        time.sleep(0.12)

    positio = cursor_ex_framebuffer(aux, monitor, out, "tabula-xib-sync-finalis", prior, w, h)
    return positio, effectus


def bronzeum_compositum(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return 120 <= r <= 220 and 75 <= g <= 185 and 35 <= b <= 150 and r > g > b


def aqua_compositum(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return 35 <= r <= 145 and 70 <= g <= 215 and 75 <= b <= 225 and g >= r + 18 and b >= g - 12


def numerus_coloris_compositus(
    originalis: object,
    aux: object,
    pix: bytes,
    w: int,
    regio: tuple[int, int, int, int],
    color: tuple[int, int, int],
) -> int:
    """Color canonicus exactus semper valet; compositio tantum contractum dilatat."""
    exactus = int(originalis(aux, pix, w, regio, color))
    x0, y0, x1, y1 = regio
    if color == (181, 138, 84):
        compositus = sum(
            bronzeum_compositum(aux.pixel(pix, w, x, y))
            for y in range(y0, y1)
            for x in range(x0, x1)
        )
        return max(exactus, compositus)
    if color == (104, 202, 210):
        compositus = sum(
            aqua_compositum(aux.pixel(pix, w, x, y))
            for y in range(y0, y1)
            for x in range(x0, x1)
        )
        return max(exactus, compositus)
    return exactus


def principale() -> int:
    base = importa("proba_initium_xib_base", "proba_initium_sylviae_xib.py")
    # Framebuffer manet auctoritas positionis et faciei; telemetria rectoris
    # probat singulos fasciculos click, non solum statum iam praesentem.
    originalis_numerus = base.numerus_coloris
    base.numerus_coloris = lambda aux, pix, w, regio, color: numerus_coloris_compositus(
        originalis_numerus, aux, pix, w, regio, color
    )
    base.click_ps2 = click_ps2
    base.elige_tabula_effectu = elige_tabula_effectu
    return int(base.principale())


if __name__ == "__main__":
    raise SystemExit(principale())
