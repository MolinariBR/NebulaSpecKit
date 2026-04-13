#!/usr/bin/env bash
set -euo pipefail

if [[ ! -f "instructions.md" || ! -f "Guide-Started.md" ]]; then
  echo "ERROR: run this script from project root." >&2
  exit 1
fi

declare -a failures=()
declare -a warnings=()

add_failure() {
  failures+=("$1")
}

add_warning() {
  warnings+=("$1")
}

normalize() {
  tr '[:upper:]' '[:lower:]' | sed 's/`//g; s/[[:space:]]\+/ /g; s/^[[:space:]]*//; s/[[:space:]]*$//'
}

extract_order() {
  local file="$1"
  local section="$2"
  awk -v section="$section" '
    $0 ~ section {in_section=1; next}
    in_section && /^## / {exit}
    in_section {print}
  ' "$file" | sed -n 's/^[0-9][0-9]*\. //p' | normalize
}

compare_precedence() {
  local a b
  a="$(extract_order "instructions.md" "^## 4\\. Precedência$")"
  b="$(extract_order "Guide-Started.md" "^## Regra de Precedência$")"

  if [[ -z "$a" ]]; then
    add_failure "instructions.md: seção de precedência ausente ou inválida"
    return
  fi
  if [[ -z "$b" ]]; then
    add_warning "Guide-Started.md: seção de precedência ausente (comparação de precedência foi ignorada)"
    return
  fi
  if [[ "$a" != "$b" ]]; then
    add_failure "precedência divergente entre instructions.md e Guide-Started.md"
  fi
}

check_base_stack_files() {
  local line path
  while IFS= read -r line; do
    path="$(sed -n 's/^[0-9][0-9]*\. `\([^`]*\)`.*/\1/p' <<<"$line")"
    [[ -n "$path" ]] || continue
    if [[ ! -f "$path" ]]; then
      add_failure "arquivo da Base obrigatória não encontrado: $path"
    fi
  done < <(awk '
    /^### 3\.1 Base obrigatória \(sempre\)/ {flag=1; next}
    flag && /^### / {exit}
    flag {print}
  ' instructions.md)
}

check_referenced_paths() {
  local file="$1"
  local pattern="$2"
  local ref
  while IFS= read -r ref; do
    [[ -n "$ref" ]] || continue
    if [[ ! -e "$ref" ]]; then
      add_failure "$file referencia caminho inexistente: $ref"
    fi
  done < <(grep -Eo "$pattern" "$file" | sort -u || true)
}

check_manual_isolation() {
  if ! grep -Eiq "Manual/.*(não integra|nao integra).*contexto mínimo|Manual/.*(não integra|nao integra).*contexto minimo" instructions.md; then
    add_warning "instructions.md: recomendável explicitar isolamento de Manual/ do contexto mínimo"
  fi
  if ! grep -Eiq "Manual/.*(não integra|nao integra).*contexto mínimo|Manual/.*(não integra|nao integra).*contexto minimo" Guide-Started.md; then
    add_warning "Guide-Started.md: recomendável explicitar isolamento de Manual/ do contexto mínimo"
  fi
}

check_docs_source_of_truth() {
  if ! grep -Eiq "fonte de verdade" Docs/README.md; then
    add_warning "Docs/README.md: expressão 'fonte de verdade' não encontrada"
  fi
  if ! grep -Eiq "fonte de verdade" Docs/get-started.md; then
    add_warning "Docs/get-started.md: expressão 'fonte de verdade' não encontrada"
  fi
}

compare_precedence
check_base_stack_files
check_referenced_paths "instructions.md" 'Workflows/[A-Za-z0-9._/-]+\.md'
check_referenced_paths "instructions.md" 'Skills/[A-Za-z0-9._/-]+\.md'
check_referenced_paths "instructions.md" 'Quality/[A-Za-z0-9._/-]+\.md'
check_referenced_paths "Guide-Started.md" 'Quality/[A-Za-z0-9._/-]+\.md'
check_manual_isolation
check_docs_source_of_truth

echo "Nebula Consistency Analysis (read-only)"
echo "- Failures: ${#failures[@]}"
echo "- Warnings: ${#warnings[@]}"

if [[ ${#warnings[@]} -gt 0 ]]; then
  echo
  echo "Warnings:"
  for item in "${warnings[@]}"; do
    echo "- $item"
  done
fi

if [[ ${#failures[@]} -gt 0 ]]; then
  echo
  echo "Failures:"
  for item in "${failures[@]}"; do
    echo "- $item"
  done
  exit 1
fi

echo
echo "Consistency analysis passed."
