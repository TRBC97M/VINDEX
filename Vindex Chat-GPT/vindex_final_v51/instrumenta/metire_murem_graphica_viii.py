#!/usr/bin/env python3
"""Graphica VIII: moram PS/2 a QMP usque ad telemetriam nuclei metitur."""
from __future__ import annotations

import importlib.util
import json
import socket
import statistics
import sys
import time
from pathlib import Path


def auxilia() -> object:
    via = Path(__file__).resolve().with_name("proba_murem_uefi_053.py")
    spec = importlib.util.spec_from_file_location("aux_murus_gviii", via)
    if spec is None or spec.loader is None:
        raise RuntimeError("auxilia muris importari non possunt")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def exspecta_vias(monitor: Path, qmp: Path, mora: float = 12.0) -> bool:
    finis = time.monotonic() + mora
    while time.monotonic() < finis:
        if monitor.exists() and qmp.exists():
            return True
        time.sleep(0.02)
    return False


def exspecta_ps2(aux: object, monitor: socket.socket, mora: float = 35.0) -> tuple[int, int, int, int] | None:
    finis = time.monotonic() + mora
    ultimus = None
    while time.monotonic() < finis:
        ps2 = aux.status_ps2(monitor)
        status = aux.status_muris(monitor)
        if status is not None:
            ultimus = status
        if ps2 and ps2[0] == 9 and len(ps2) >= 3 and ps2[1] == 250 and ps2[2] == 250 and status is not None:
            return status
        time.sleep(0.025)
    return ultimus


def exspecta_eventum(aux: object, monitor: socket.socket, series_ante: int, mora: float = 0.75) -> tuple[float, tuple[int, int, int, int] | None, int]:
    initium = time.perf_counter_ns()
    finis = time.monotonic() + mora
    probationes = 0
    ultimus = None
    while time.monotonic() < finis:
        status = aux.status_muris(monitor)
        probationes += 1
        if status is not None:
            ultimus = status
            if status[3] != series_ante:
                ns = time.perf_counter_ns() - initium
                return ns / 1_000_000.0, status, probationes
        time.sleep(0.002)
    return -1.0, ultimus, probationes


def percentile_95(valores: list[float]) -> float:
    ordinati = sorted(valores)
    index = (95 * len(ordinati) + 99) // 100 - 1
    if index < 0:
        index = 0
    if index >= len(ordinati):
        index = len(ordinati) - 1
    return ordinati[index]


def principale() -> int:
    if len(sys.argv) != 3:
        print("USUS: metire_murem_graphica_viii.py MONITOR.sock QMP.sock", file=sys.stderr)
        return 2

    aux = auxilia()
    monitor_via = Path(sys.argv[1])
    qmp_via = Path(sys.argv[2])
    if not exspecta_vias(monitor_via, qmp_via):
        print("DEFECIT: monitor vel QMP non apparuit", file=sys.stderr)
        return 3

    monitor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    monitor.settimeout(0.35)
    monitor.connect(str(monitor_via))
    q = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    q.settimeout(2.0)
    q.connect(str(qmp_via))

    try:
        aux.lege_usque(monitor, b"(qemu) ", 2.0)
        salutatio = aux.qmp_linea(q)
        if "QMP" not in salutatio:
            print("DEFECIT: salutatio QMP invalida", file=sys.stderr)
            return 4
        cap = aux.qmp(q, "qmp_capabilities")
        if "error" in cap:
            print(f"DEFECIT: qmp_capabilities {cap}", file=sys.stderr)
            return 5

        mures = aux.qmp(q, "query-mice")
        candidati = [m for m in mures.get("return", []) if "PS/2 Mouse" in str(m.get("name", ""))]
        if not candidati:
            print("DEFECIT: QEMU PS/2 Mouse non invenitur", file=sys.stderr)
            print(json.dumps(mures, ensure_ascii=False), file=sys.stderr)
            return 6
        index = int(candidati[0]["index"])
        aux.hmp(monitor, f"mouse_set {index}")

        status = exspecta_ps2(aux, monitor)
        ps2 = aux.status_ps2(monitor)
        if status is None or not ps2 or ps2[0] != 9:
            print(f"DEFECIT: PS/2 paratus non est: status={status} ps2={ps2}", file=sys.stderr)
            return 7

        # Calefactio: primum eventum caches/ramulos tangere licet; in statistica non numeratur.
        ante = status[3]
        responsum = aux.qmp(q, "input-send-event", {"events": [
            {"type": "rel", "data": {"axis": "x", "value": 8}},
            {"type": "rel", "data": {"axis": "y", "value": -4}},
        ]})
        if "error" in responsum:
            print(f"DEFECIT: calefactio recusata est: {responsum}", file=sys.stderr)
            return 8
        _, status, _ = exspecta_eventum(aux, monitor, ante)
        if status is None or status[3] == ante:
            print("DEFECIT: eventus calefactionis ad nucleum non pervenit", file=sys.stderr)
            return 9

        motus = [(12, -7), (18, 5), (-9, 11), (7, -13), (15, 9), (-11, -6),
                 (9, 14), (-14, 8), (13, -10), (6, 12), (-8, -15), (16, 7),
                 (-12, 10), (10, -8), (14, 6), (-7, 13)]
        morae: list[float] = []
        polling: list[int] = []
        for n, (dx, dy) in enumerate(motus, 1):
            ante = status[3]
            t0 = time.perf_counter_ns()
            responsum = aux.qmp(q, "input-send-event", {"events": [
                {"type": "rel", "data": {"axis": "x", "value": dx}},
                {"type": "rel", "data": {"axis": "y", "value": dy}},
            ]})
            qmp_ms = (time.perf_counter_ns() - t0) / 1_000_000.0
            if "error" in responsum:
                print(f"DEFECIT: eventus {n} recusatus est: {responsum}", file=sys.stderr)
                return 10
            mora_ms, novus, probes = exspecta_eventum(aux, monitor, ante)
            if mora_ms < 0 or novus is None:
                print(f"DEFECIT: eventus {n} intra 750 ms non observatus est", file=sys.stderr)
                return 11
            # Mora finem QMP->telemetria metitur; tempus mittendi separatim nuntiatur.
            morae.append(mora_ms)
            polling.append(probes)
            status = novus
            print(f"MURUS-GVIII: specimen={n:02d} qmp={qmp_ms:.3f}ms telemetria={mora_ms:.3f}ms probes={probes}")

        mediana = statistics.median(morae)
        p95 = percentile_95(morae)
        maximum = max(morae)
        minimum = min(morae)
        print(f"MURUS-GVIII: n={len(morae)} min={minimum:.3f}ms mediana={mediana:.3f}ms p95={p95:.3f}ms max={maximum:.3f}ms")
        print(f"MURUS-GVIII: probes_mediana={statistics.median(polling):.1f} probes_max={max(polling)}")
        print("RECTE: baseline responsivitatis PS/2 Graphica VIII mensuratus est.")
        return 0
    finally:
        try:
            aux.hmp(monitor, "quit")
        except Exception:
            pass
        monitor.close()
        q.close()


if __name__ == "__main__":
    raise SystemExit(principale())
