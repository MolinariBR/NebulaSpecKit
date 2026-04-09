# Create Agents In Zed

## Escopo Deste Documento

Este manual cobre apenas o delta nativo do Zed.
O padrão comum de governança, contexto e validação esta em [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md).

## Leitura Obrigatória

1. [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
2. [../agents/00README.md](../agents/00README.md)
3. [../agents/02CATALOG.md](../agents/02CATALOG.md)

## Implementação Nativa No Zed

1. O Zed usa Agent Panel nativo para execução agentica.
2. Regras principais do projeto ficam em `.rules`.
3. Rules Library pode manter regras por perfil e tornar default.
4. Zed reconhece AGENTS.md como arquivo compativel de regras.
5. Tambem suporta agentes externos via ACP.

## Setup Rápido

1. Criar `.rules` na raiz com guardrails do Nébula.
2. Abrir Agent Panel e iniciar thread.
3. Opcional: criar regras adicionais na Rules Library.
4. Opcional: configurar agentes externos via ACP.

## Exemplo Mínimo

Arquivo: `.rules`

```md
# Nébula Guardrails

- Sempre carregar GUIDE.md, Skills/01GUIDE.md, Workflows/01GUIDE.md, Quality/README.md e Templates/Full/01GUIDE.md
- Bootstrap estrutural apenas na primeira task
- Depois do bootstrap, apenas editar arquivos existentes
- 1 commit por task
- Quality Gate obrigatório
```

## Validação Específica Do Zed

1. Rules ativas no Agent Panel.
2. Contexto carregado com @mentions quando necessário.
3. Ferramentas com permissões adequadas ao risco da task.

## Referências Externas

1. https://zed.dev/docs/ai/agent-panel.html
2. https://zed.dev/docs/ai/rules.html
3. https://zed.dev/docs/ai/tool-permissions.html
4. https://zed.dev/docs/ai/external-agents.html
