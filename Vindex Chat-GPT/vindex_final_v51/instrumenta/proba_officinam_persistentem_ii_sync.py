#!/usr/bin/env python3
"""P19-II: bullae PS/2 consumptae probantur, cursor framebuffer auctoritate."""
from __future__ import annotations

import importlib.util
import re
import socket
import time
from pathlib import Path

_BASE = None


def importa(nomen: str, fasciculus: str) -> object:
    via = Path(__file__).resolve().with_name(fasciculus)
    spec = importlib.util.spec_from_file_location(nomen, via)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"probator importari non potest: {fasciculus}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ps2_numerus_fasciculorum(aux: object, monitor: socket.socket) -> int | None:
    """Numeratorem +67 rectoris PS/2 e verbo telemetriae legit."""
    textus = aux.hmp(monitor, "xp /1gx 0x03018840")
    for linea in textus.splitlines():
        if ":" not in linea:
            continue
        valores = re.findall(r"0x[0-9a-fA-F]+", linea.split(":", 1)[1])
        if valores:
            verbum = int(valores[0], 16)
            return (verbum >> 24) & 0xFF
    return None


def acervus_proximum(aux: object, monitor: socket.socket) -> int | None:
    """Proximam sedem allocatoris VINDEX legit sine telemetria nucleari."""
    textus = aux.hmp(monitor, "xp /1gx 0x02000000")
    for linea in textus.splitlines():
        if ":" not in linea:
            continue
        valores = re.findall(r"0x[0-9a-fA-F]+", linea.split(":", 1)[1])
        if valores:
            return int(valores[0], 16)
    return None


def acervum_certifica(aux: object, monitor: socket.socket, nomen: str) -> None:
    """Acervus numquam fines segmenti ELF VINDEX transgredi debet."""
    proximum = acervus_proximum(aux, monitor)
    if proximum is None:
        raise RuntimeError("proxima sedes acervi VINDEX legi non potest")
    if not 0x02000008 <= proximum < 0x03000000:
        raise RuntimeError(f"acervus VINDEX fines transgressus est: 0x{proximum:08x}")
    print(f"XIIE-ACERVUS: {nomen}=0x{proximum:08x} limen=0x03000000")


def numeratorem_stabiliza(aux: object, monitor: socket.socket, mora: float = 1.5) -> int:
    finis = time.time() + mora
    prior: int | None = None
    stabilia = 0
    while time.time() < finis:
        nunc = ps2_numerus_fasciculorum(aux, monitor)
        if nunc is None:
            time.sleep(0.05)
            continue
        if nunc == prior:
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
    mora: float = 12.0,
) -> tuple[int, int]:
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
    """Release vere consumptum s[13] ad 0 reducit ante novam arctam 0→1."""
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
    """Post cliccum positio cursoris ex imagine reali restituitur."""
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


def bronzeum_compositum(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return 120 <= r <= 220 and 75 <= g <= 185 and 35 <= b <= 150 and r > g > b


def aqua_activa_composita(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return 35 <= r <= 145 and 70 <= g <= 215 and 75 <= b <= 225 and g >= r + 18 and b >= g - 12


def clara_materia(c: tuple[int, int, int]) -> bool:
    r, g, b = c
    return r >= 205 and g >= 205 and b >= 190


def focus_officina_compositum(
    originalis: object,
    aux: object,
    pix: bytes,
    w: int,
    h: int,
) -> str | None:
    """Contractum exactum primum servat; deinde compositionem XII-E tolerat."""
    vetus = originalis(aux, pix, w, h)
    if vetus is not None:
        return str(vetus)

    x0, y0, x1, y1 = 130, 50, min(w, 1120), min(h - 40, 690)
    clara = 0
    aqua = 0
    aes = 0
    for y in range(y0, y1):
        for x in range(x0, x1):
            c = aux.pixel(pix, w, x, y)
            if clara_materia(c):
                clara += 1
            if aqua_activa_composita(c):
                aqua += 1
            if bronzeum_compositum(c):
                aes += 1
    if clara >= 1200 and aqua >= 500 and aes >= 40:
        return "XII-E"
    return None


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
    if _BASE is None:
        raise RuntimeError("probator OFFICINAE basis deest")

    bulla_sync(aux, ps2, q, monitor, True, 1, "officina-initium-linea")
    time.sleep(0.10)
    bulla_sync(aux, ps2, q, monitor, False, -1, "officina-initium-linea")
    time.sleep(0.12)
    acervum_certifica(aux, monitor, "officina-post-cliccum")

    testa: str | None = None
    for i in range(40):
        effectus = out / f"officina-sync-effectus-{i}.ppm"
        aux.captura(monitor, effectus)
        _, _, pix = aux.ppm(effectus)
        menu = aux.initium_top_quaere(pix, w, h, nox, bronzeum, ebur)
        if menu is None:
            testa = _BASE.focus_officina(aux, pix, w, h)
            if testa is not None:
                break
        time.sleep(0.12)

    aux.captura(monitor, via)
    _, _, pix_finalis = aux.ppm(via)
    if aux.initium_top_quaere(pix_finalis, w, h, nox, bronzeum, ebur) is not None:
        testa = None
    else:
        testa = _BASE.focus_officina(aux, pix_finalis, w, h)
    positio = aux.cursor_quaere(pix_finalis, w, h)
    return testa, (positio if positio is not None else prior)


def principale() -> int:
    global _BASE
    base = importa("proba_officina_base", "proba_officinam_persistentem_ii.py")
    _BASE = base
    originalis_focus = base.focus_officina
    base.focus_officina = lambda aux, pix, w, h: focus_officina_compositum(
        originalis_focus, aux, pix, w, h
    )
    base.click_ps2 = click_ps2
    base.elige_officinam_effectu = elige_officinam_effectu
    return int(base.principale())


if __name__ == "__main__":
    raise SystemExit(principale())
