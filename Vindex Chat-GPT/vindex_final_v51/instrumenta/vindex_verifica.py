#!/usr/bin/env python3
"""Verificatio statica levis interfaciei publicae VINDEX.

Compilator nativus sui iuris manet. Hoc instrumentum facultativum diagnostica
cum archivo, linea et columna ante generationem binarii addit.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


MAX_SOURCE_BYTES = 212_999
MAX_IDENTIFIER_CHARS = 32

IDENTIFIER_RE = re.compile(r"\b[A-Za-z_][A-Za-z_0-9]*\b")
IMPORT_RE = re.compile(r'^\s*IMPORTA\s+"([^"]+)"\s*\.\s*$')
FUNCTION_RE = re.compile(r"^\s*FUNCTIO\s+([A-Za-z_][A-Za-z_0-9]*)\b")
FORM_RE = re.compile(r"^\s*FORMA\s+([A-Za-z_][A-Za-z_0-9]*)\b")
CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z_0-9]*)\s*\(")

BUILTIN_CALLS = {
    "APERI_ADICERE",
    "APERI_LEGERE",
    "APERI_SCRIBERE",
    "CAMBIA",
    "CLAUDE",
    "CONTENTUM",
    "CURRE",
    "EXSEQUERE",
    "EXSEQUERE_CAPTURA",
    "LEGE",
    "LIBERA",
    "MITTE",
    "OCTETUS",
    "OCTETUS_AB",
    "REDDE",
    "RESERVA",
    "SCRIBE_OCTETUM_AB",
    "SEDES",
    "SI",
    "TUBUS",
    "UEFI_VOCA6",
    "VALENS",
}


@dataclass(frozen=True)
class Location:
    path: Path
    line: int
    column: int = 1


@dataclass(frozen=True)
class Diagnostic:
    location: Location
    message: str

    def render(self) -> str:
        loc = self.location
        return f"{loc.path}:{loc.line}:{loc.column}: erratum: {self.message}"


@dataclass
class SourceUnit:
    path: Path
    text: str
    lines: list[str]


def strip_literals_and_comment(line: str) -> tuple[str, list[tuple[int, str]]]:
    """Catenas litterasque tegit et errata lexicalia simplicia reddit."""
    chars = list(line)
    errors: list[tuple[int, str]] = []
    quote: str | None = None
    quote_column = 0
    index = 0

    while index < len(chars):
        char = chars[index]
        if quote is None:
            if char == "/" and index + 1 < len(chars) and chars[index + 1] == "/":
                for position in range(index, len(chars)):
                    chars[position] = " "
                break
            if char in {'"', "'"}:
                quote = char
                quote_column = index + 1
                chars[index] = " "
            index += 1
            continue

        chars[index] = " "
        if char == quote:
            quote = None
        index += 1

    if quote == '"':
        errors.append((quote_column, "catena litterarum non terminata"))
    elif quote == "'":
        errors.append((quote_column, "litterale litterae non terminatum"))
    return "".join(chars), errors


class Verifier:
    def __init__(self, root_source: Path):
        self.root_source = root_source
        self.units: list[SourceUnit] = []
        self.diagnostics: list[Diagnostic] = []
        self.total_bytes = 0
        self._visiting: list[Path] = []
        self._visited: set[Path] = set()
        self.functions: dict[str, Location] = {}
        self.forms: dict[str, Location] = {}
        self.calls: list[tuple[str, Location]] = []
        self.principalis: list[Location] = []

    def error(self, path: Path, line: int, column: int, message: str) -> None:
        self.diagnostics.append(Diagnostic(Location(path, line, column), message))

    def load(self, path: Path, import_location: Location | None = None) -> None:
        path = path.resolve()
        if path in self._visiting:
            chain = " -> ".join(item.name for item in [*self._visiting, path])
            location = import_location or Location(path, 1)
            self.error(location.path, location.line, location.column, f"cyclus IMPORTA: {chain}")
            return
        if path in self._visited:
            return
        if not path.is_file():
            location = import_location or Location(path, 1)
            self.error(location.path, location.line, location.column, "archivum non inventum")
            return

        try:
            raw = path.read_bytes()
        except OSError:
            location = import_location or Location(path, 1)
            self.error(location.path, location.line, location.column, "lectio impossibilis")
            return

        if len(raw) > MAX_SOURCE_BYTES:
            location = import_location or Location(path, 1)
            self.error(
                location.path,
                location.line,
                location.column,
                f"fons {len(raw)} octeta continet; maximum {MAX_SOURCE_BYTES}",
            )
            return
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            self.error(path, exc.start + 1, 1, "archivum textus UTF-8 validus non est")
            return

        self.total_bytes += len(raw) + (1 if import_location else 0)
        if self.total_bytes > MAX_SOURCE_BYTES:
            self.error(
                path,
                1,
                1,
                f"fontes coniuncti {self.total_bytes} octeta continent; maximum {MAX_SOURCE_BYTES}",
            )
            return

        unit = SourceUnit(path=path, text=text, lines=text.splitlines())
        self.units.append(unit)
        self._visiting.append(path)

        for number, line in enumerate(unit.lines, start=1):
            match = IMPORT_RE.match(line)
            if match:
                location = Location(path, number, line.find("IMPORTA") + 1)
                if import_location is not None:
                    self.error(
                        path,
                        number,
                        location.column,
                        "IMPORTA inclusum nondum sustinetur",
                    )
                else:
                    # Compilator fontes importatos in directorio praesenti quaerit.
                    imported = (Path.cwd() / match.group(1)).resolve()
                    self.load(imported, location)

        self._visiting.pop()
        self._visited.add(path)

    def verify_unit(self, unit: SourceUnit) -> None:
        stack: list[tuple[str, Location]] = []
        parens: list[Location] = []
        brackets: list[Location] = []

        for number, original in enumerate(unit.lines, start=1):
            code, lexical_errors = strip_literals_and_comment(original)
            for column, message in lexical_errors:
                self.error(unit.path, number, column, message)

            stripped = code.strip()
            if not stripped:
                continue

            for index, char in enumerate(code, start=1):
                if char == "(":
                    parens.append(Location(unit.path, number, index))
                elif char == ")":
                    if parens:
                        parens.pop()
                    else:
                        self.error(unit.path, number, index, "parenthesis claudens sine aperiente")
                elif char == "[":
                    brackets.append(Location(unit.path, number, index))
                elif char == "]":
                    if brackets:
                        brackets.pop()
                    else:
                        self.error(unit.path, number, index, "uncus claudens sine aperiente")

            for match in IDENTIFIER_RE.finditer(code):
                name = match.group(0)
                if len(name) > MAX_IDENTIFIER_CHARS:
                    self.error(
                        unit.path,
                        number,
                        match.start() + 1,
                        f"identificator '{name}' nimis longus ({len(name)}; maximum {MAX_IDENTIFIER_CHARS})",
                    )

            location = Location(unit.path, number, len(original) - len(original.lstrip()) + 1)
            function = FUNCTION_RE.match(stripped)
            form = FORM_RE.match(stripped)

            if IMPORT_RE.match(original):
                if stack:
                    self.error(unit.path, number, location.column, "IMPORTA in gradu supremo esse debet")
                continue

            if function:
                name = function.group(1)
                if stack:
                    self.error(unit.path, number, location.column, "FUNCTIO includi non potest")
                previous = self.functions.get(name)
                if previous:
                    self.error(unit.path, number, location.column, f"functio '{name}' iam definita apud {previous.path}:{previous.line}")
                else:
                    self.functions[name] = location
                if name == "PRINCIPALIS":
                    self.principalis.append(location)
                stack.append(("FUNCTIO", location))
            elif form:
                name = form.group(1)
                if stack:
                    self.error(unit.path, number, location.column, "FORMA includi non potest")
                previous = self.forms.get(name)
                if previous:
                    self.error(unit.path, number, location.column, f"forma '{name}' iam definita apud {previous.path}:{previous.line}")
                else:
                    self.forms[name] = location
                stack.append(("FORMA", location))
            elif stripped.startswith("SI ") and stripped.endswith(" TUNC"):
                stack.append(("SI", location))
            elif stripped.startswith("DUM ") and stripped.endswith(" PERFICE"):
                stack.append(("DUM", location))
            elif stripped.startswith("PER ") and stripped.endswith(" PERFICE"):
                stack.append(("PER", location))
            elif stripped == "ALITER":
                if not stack or stack[-1][0] != "SI":
                    self.error(unit.path, number, location.column, "ALITER sine SI congruente")
            elif stripped.startswith("FIN-"):
                match = re.fullmatch(r"FIN-(FUNCTIO|FORMA|SI|DUM|PER)\.", stripped)
                if not match:
                    self.error(unit.path, number, location.column, "clausura bloci invalida")
                else:
                    expected = match.group(1)
                    if not stack:
                        self.error(unit.path, number, location.column, f"FIN-{expected} sine apertura")
                    elif stack[-1][0] != expected:
                        opened, opened_at = stack[-1]
                        self.error(
                            unit.path,
                            number,
                            location.column,
                            f"FIN-{expected} blocum {opened} in linea {opened_at.line} apertum claudit",
                        )
                    else:
                        stack.pop()
            elif not stack:
                self.error(unit.path, number, location.column, "praeceptum in gradu supremo inexspectatum")

            opener_without_period = (
                stripped == "ALITER"
                or (stripped.startswith("SI ") and stripped.endswith(" TUNC"))
                or (stripped.startswith("DUM ") and stripped.endswith(" PERFICE"))
                or (stripped.startswith("PER ") and stripped.endswith(" PERFICE"))
            )
            continued = bool(parens or brackets) or stripped.endswith((",", "+", "-", "*", "/", "&&", "||"))
            if not opener_without_period and not continued and not stripped.endswith("."):
                self.error(unit.path, number, len(original) + 1, "punctum finale deest")

            declaration_prefix = bool(function)
            for match in CALL_RE.finditer(code):
                name = match.group(1)
                if declaration_prefix and name == function.group(1):
                    continue
                if name not in BUILTIN_CALLS:
                    self.calls.append((name, Location(unit.path, number, match.start(1) + 1)))

        for opened, location in reversed(stack):
            self.error(location.path, location.line, location.column, f"blocus {opened} numquam clausus")
        for location in parens:
            self.error(location.path, location.line, location.column, "parenthesis numquam clausa")
        for location in brackets:
            self.error(location.path, location.line, location.column, "uncus numquam clausus")

    def verify(self) -> list[Diagnostic]:
        self.load(self.root_source)
        for unit in self.units:
            self.verify_unit(unit)

        if not self.principalis:
            self.error(self.root_source, 1, 1, "FUNCTIO PRINCIPALIS deest")
        elif len(self.principalis) > 1:
            for location in self.principalis[1:]:
                self.error(location.path, location.line, location.column, "FUNCTIO PRINCIPALIS plus semel definita est")

        for name, location in self.calls:
            if name not in self.functions:
                self.error(location.path, location.line, location.column, f"functio '{name}' non definita")

        return sorted(
            self.diagnostics,
            key=lambda item: (str(item.location.path), item.location.line, item.location.column, item.message),
        )


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] in {"-h", "--help"}:
        print(f"USUS: {Path(argv[0]).name} <fons.vindex>", file=sys.stderr)
        return 64 if len(argv) != 2 else 0

    source = Path(argv[1])
    verifier = Verifier(source)
    diagnostics = verifier.verify()
    if diagnostics:
        for diagnostic in diagnostics:
            print(diagnostic.render(), file=sys.stderr)
        print(f"VINDEX: {len(diagnostics)} errata; compilatio abolita.", file=sys.stderr)
        return 1

    print(
        f"VINDEX: verificatio perfecta ({len(verifier.units)} archiva, {verifier.total_bytes} octeta)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
