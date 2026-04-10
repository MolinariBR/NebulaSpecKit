#!/usr/bin/env bash
set -euo pipefail

MODE="ci"
WORKFLOW=""

usage() {
  cat <<'EOF'
Usage: check-context.sh [--mode <startup|task|release|ci>] [--workflow <name>]

Read-only context pre-check for Nebula projects.

Options:
  --mode       Validation profile (default: ci)
  --workflow   Optional workflow file name without extension (e.g. new-feature)
  --help, -h   Show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --mode requires a value" >&2
        exit 1
      fi
      MODE="$2"
      shift 2
      ;;
    --workflow)
      if [[ $# -lt 2 ]]; then
        echo "ERROR: --workflow requires a value" >&2
        exit 1
      fi
      WORKFLOW="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown argument '$1'" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ! -f "instructions.md" || ! -f "GUIDE.md" ]]; then
  echo "ERROR: run this script from project root." >&2
  exit 1
fi

declare -a missing=()
declare -a warnings=()

add_missing() {
  local path="$1"
  missing+=("$path")
}

check_file() {
  local path="$1"
  [[ -f "$path" ]] || add_missing "$path"
}

check_placeholder_warning() {
  local path="$1"
  [[ -f "$path" ]] || return 0
  if grep -Eq "Preencha este arquivo a partir do template|Documento oficial do projeto em Docs\." "$path"; then
    warnings+=("$path: ainda contém conteúdo placeholder")
  fi
}

common_required=(
  "instructions.md"
  "GUIDE.md"
  "Workflows/README.md"
  "Skills/README.md"
  "Quality/validation-rules.md"
  "Docs/README.md"
  "Docs/plan.md"
  "Docs/tasks.md"
  "Docs/control.md"
)

for path in "${common_required[@]}"; do
  check_file "$path"
done

mode_required=()
case "$MODE" in
  startup)
    mode_required=(
      "Docs/get-started.md"
      "Docs/brief.md"
      "Docs/project.md"
      "Docs/stack.md"
      "Docs/plan.md"
    )
    ;;
  task|ci)
    mode_required=(
      "Docs/plan.md"
      "Docs/tasks.md"
      "Docs/control.md"
    )
    ;;
  release)
    mode_required=(
      "Docs/plan.md"
      "Docs/tasks.md"
      "Docs/control.md"
      "Docs/deploy.md"
      "Workflows/release.md"
    )
    ;;
  *)
    echo "ERROR: invalid mode '$MODE'. Use startup, task, release or ci." >&2
    exit 1
    ;;
esac

for path in "${mode_required[@]}"; do
  check_file "$path"
done

if [[ -n "$WORKFLOW" ]]; then
  check_file "Workflows/${WORKFLOW}.md"
fi

check_placeholder_warning "Docs/plan.md"
check_placeholder_warning "Docs/tasks.md"
check_placeholder_warning "Docs/control.md"

echo "Nebula Context Pre-Check"
echo "- mode: ${MODE}"
if [[ -n "$WORKFLOW" ]]; then
  echo "- workflow: ${WORKFLOW}"
fi

if [[ ${#warnings[@]} -gt 0 ]]; then
  echo
  echo "Warnings:"
  for item in "${warnings[@]}"; do
    echo "- ${item}"
  done
fi

if [[ ${#missing[@]} -gt 0 ]]; then
  echo
  echo "Missing required files:"
  for path in "${missing[@]}"; do
    echo "- ${path}"
  done
  exit 1
fi

echo
echo "Context pre-check passed."
