#!/usr/bin/env python3
"""Validate skills, platform prompts/adapters, changelogs, and local Markdown links."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "debug-and-fix", "audit-ci-release", "github-project-operations",
    "ads-campaign-builder", "business-strategy-documents", "senior-code-refactor",
    "agent-skill-generator", "technical-documentation-writer", "commit-pr-writer",
    "automated-test-generator", "chat-task-auditor", "workflow-automation-architect",
    "project-orchestrator", "smart-task-intake", "context-handoff-manager", "evidence-verifier",
    "decision-and-risk-manager", "workflow-optimizer",
}
REQUIRED_FILES = [
    "README.md", "COMMON-INSTRUCTIONS.md", "LICENSE",
    "prompts/claude-code/CLAUDE.md",
    "prompts/claude/PROJECT-INSTRUCTIONS.md",
    "prompts/chatgpt/PROJECT-INSTRUCTIONS.md",
    "prompts/gemini/GEMINI.md", "prompts/kimi/KIMI.md",
    "adapters/README.md", "adapters/claude-code/README.md",
    "adapters/claude/README.md", "adapters/chatgpt/README.md",
    "adapters/gemini/README.md", "adapters/kimi/README.md",
    "docs/uso-claude.md", "docs/uso-chatgpt.md", "docs/uso-kimi.md",
    "docs/compatibilidad.md", "docs/instrucciones-universales.md",
    "tests/README.md", "tests/RESULTS.md", "tasks/todo.md", "tasks/lessons.md",
]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
EXPECTED_PLATFORMS = {
    "Claude Code", "Claude web/app", "ChatGPT / Proyecto", "Gemini", "Kimi",
}
VALID_STATES = {"VERDE", "ROJO", "PENDIENTE", "BLOQUEADO"}


def strip_fenced_code(text: str) -> str:
    kept: list[str] = []
    fence_char = None
    for line in text.splitlines():
        stripped = line.lstrip()
        marker = "`" * 3
        if stripped.startswith(marker) or stripped.startswith("~~~"):
            current = marker if stripped.startswith(marker) else "~~~"
            if fence_char is None:
                fence_char = current
            elif current == fence_char:
                fence_char = None
            continue
        if fence_char is None:
            kept.append(line)
    return "\n".join(kept)


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}


def check_skill_quality(skill: str, path: Path, content: str, metadata: str, desc_match) -> list[str]:
    """Checks aligned with the Agent Skills specification (agentskills.io) and repository conventions."""
    errs: list[str] = []
    rel = path.relative_to(ROOT)
    if len(skill) > 64 or not NAME_RE.match(skill):
        errs.append(f"Nombre de skill inválido según la especificación: {skill}")
    keys = set(re.findall(r"^([A-Za-z][\w-]*):", metadata, re.M))
    extra = keys - ALLOWED_KEYS
    if extra:
        errs.append(f"Claves de frontmatter no previstas en {rel}: {sorted(extra)}")
    if desc_match:
        raw = desc_match.group(1).strip()
        quoted = raw[:1] in {"\"", "'"}
        description = raw.strip("\"'")
        if len(description) > 1024:
            errs.append(f"Descripción de más de 1024 caracteres en {rel}: {len(description)}")
        if not quoted and ": " in raw:
            errs.append(f"Descripción sin comillas con ': ' (YAML inválido o ambiguo) en {rel}")
        if "use when" not in description.lower() and "use for" not in description.lower():
            errs.append(f"La descripción debe indicar cuándo usar la skill ('Use when'): {rel}")
    if len(content.splitlines()) > 500:
        errs.append(f"SKILL.md supera 500 líneas; mover detalle a archivos enlazados: {rel}")
    good = len(re.findall(r"^### Good example", content, re.M))
    bad = len(re.findall(r"^### Bad example", content, re.M))
    if good != 2 or bad != 1:
        errs.append(f"Se requieren 2 ejemplos buenos y 1 malo en {rel}; hay {good} y {bad}")
    changelog = path.parent / "CHANGELOG.md"
    if changelog.is_file() and not re.search(r"^## \d+\.\d+\.\d+", changelog.read_text(encoding="utf-8"), re.M):
        errs.append(f"CHANGELOG sin encabezado de versión 'x.y.z': {changelog.relative_to(ROOT)}")
    return errs


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Falta archivo requerido: {relative}")

    skill_root = ROOT / ".claude" / "skills"
    actual_skills = {
        path.name for path in skill_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    } if skill_root.is_dir() else set()
    if actual_skills != EXPECTED_SKILLS:
        errors.append(
            "Skills detectadas no coinciden con las esperadas. "
            f"Esperadas={sorted(EXPECTED_SKILLS)}; detectadas={sorted(actual_skills)}"
        )

    for skill in sorted(EXPECTED_SKILLS):
        path = skill_root / skill / "SKILL.md"
        if not path.is_file():
            errors.append(f"Falta archivo de skill: {path.relative_to(ROOT)}")
            continue
        changelog = path.parent / "CHANGELOG.md"
        if not changelog.is_file():
            errors.append(f"Falta changelog de skill: {changelog.relative_to(ROOT)}")
        content = path.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", content, re.S)
        if not frontmatter:
            errors.append(f"Frontmatter ausente o mal delimitado: {path.relative_to(ROOT)}")
            continue
        metadata = frontmatter.group(1)
        name_match = re.search(r"^name:\s*([^\s#]+)\s*$", metadata, re.M)
        desc_match = re.search(r"^description:\s*(.+?)\s*$", metadata, re.M)
        if not name_match:
            errors.append(f"Falta 'name' en frontmatter: {path.relative_to(ROOT)}")
        elif name_match.group(1).strip("\"'") != skill:
            errors.append(f"Nombre de skill no coincide con directorio '{skill}'")
        if not desc_match or not desc_match.group(1).strip("\"'"):
            errors.append(f"Falta 'description' en frontmatter: {path.relative_to(ROOT)}")
        errors.extend(check_skill_quality(skill, path, content, metadata, desc_match))

    results_file = ROOT / "tests" / "RESULTS.md"
    if results_file.is_file():
        matrix_rows = []
        in_matrix = False
        for line in results_file.read_text(encoding="utf-8").splitlines():
            if line.strip() == "## Matriz de cobertura":
                in_matrix = True
                continue
            if in_matrix and line.startswith("## "):
                break
            if in_matrix and line.startswith("|") and not line.startswith("|---"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if cells and cells[0] != "Plataforma":
                    matrix_rows.append(cells)
        expected_pairs = {(platform, skill) for platform in EXPECTED_PLATFORMS for skill in EXPECTED_SKILLS}
        seen_pairs = set()
        for row in matrix_rows:
            if len(row) != 5:
                errors.append(f"Fila mal formada en matriz funcional: {row}")
                continue
            platform, skill, principal, adversarial, combined = row
            pair = (platform, skill)
            if pair in seen_pairs:
                errors.append(f"Combinación plataforma-skill duplicada en matriz: {pair}")
            seen_pairs.add(pair)
            if platform not in EXPECTED_PLATFORMS:
                errors.append(f"Plataforma inesperada en matriz funcional: {platform}")
            if skill not in EXPECTED_SKILLS:
                errors.append(f"Skill inesperada en matriz funcional: {skill}")
            for state in (principal, adversarial, combined):
                if state not in VALID_STATES:
                    errors.append(f"Estado inválido en matriz funcional para {pair}: {state}")
        missing_pairs = expected_pairs - seen_pairs
        extra_pairs = seen_pairs - expected_pairs
        if missing_pairs:
            errors.append(f"Faltan {len(missing_pairs)} combinaciones en la matriz funcional")
        if extra_pairs:
            errors.append(f"Hay {len(extra_pairs)} combinaciones inesperadas en la matriz funcional")
        if len(matrix_rows) != len(expected_pairs):
            errors.append(
                f"La matriz debe tener {len(expected_pairs)} filas de datos; "
                f"se encontraron {len(matrix_rows)}"
            )

    markdown_files = sorted(ROOT.rglob("*.md"))
    for md_file in markdown_files:
        if any(part in {".git", ".venv", "node_modules"} for part in md_file.parts):
            continue
        content = strip_fenced_code(md_file.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(content):
            target = match.group(1).strip()
            if not target:
                continue
            target = target.split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith("#"):
                continue
            local_path = unquote(parsed.path)
            if not local_path:
                continue
            candidate = (md_file.parent / local_path).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                errors.append(f"Enlace sale del repositorio: {md_file.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"Enlace interno roto: {md_file.relative_to(ROOT)} -> {target}")

    if errors:
        print(f"VALIDACIÓN ROJA: {len(errors)} error(es)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "VALIDACIÓN VERDE: archivos requeridos presentes; eighteen skills, frontmatter "
        "y calidad de skills válidos; changelogs, prompts, adaptadores y enlaces Markdown internos comprobados."
    )
    print(f"Archivos Markdown inspeccionados: {len(markdown_files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
