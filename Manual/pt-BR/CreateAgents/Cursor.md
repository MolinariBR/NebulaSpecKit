# Criação de Agentes no Cursor

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do Cursor.
O padrão comum de governança, contexto e validação está em [Baseline.md](Baseline.md).

## Leitura Obrigatória

1. [Baseline.md](Baseline.md)
2. [../agents/README.md](../../../agents/README.md)
3. [Agents.md](../Agents.md)

## Implementação Nativa No Cursor

1. O mecanismo nativo principal é Rules em `.cursor/rules`.
2. Formatos suportados: `.md` e `.mdc`.
3. `Agents.md` na raiz também pode ser usado como camada de instruções.
4. Regras podem ser criadas via `/create-rule`.

## Setup Rápido

1. Criar `.cursor/rules`.
2. Criar uma regra por papel (ex.: quality.mdc).
3. Definir frontmatter com `description`, `alwaysApply` e globs quando necessário.
4. Referenciar os arquivos canônicos do Nébula.

## Exemplo Mínimo

Arquivo: `.cursor/rules/quality.mdc`

```md
---
description: "Use when validating Quality Gate before task closure"
alwaysApply: false
---

# Nébula Quality Rule

Load:
- Guide-Started.md
- Quality/README.md
- Quality/validation-rules.md
- Docs/tasks.md
```

## Validação Específica Do Cursor

1. A regra é carregada em contexto quando aplicável.
2. O comportamento final respeita o baseline do Nébula.
3. Não há conflito entre Rules e Agents.md.

## Referências Externas

1. https://cursor.com/docs/rules
2. https://cursor.com/docs/rules#agentsmd
