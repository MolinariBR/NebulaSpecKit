# Prototype

Pasta raiz para protótipos em HTML.

## Objetivo

Centralizar protótipos navegáveis usados para validar fluxo, estrutura de tela e comportamento antes da implementação final.

## Guia operacional

1. Mantenha protótipos HTML versionados e rastreáveis por página e fluxo.
2. Relacione cada protótipo com `Docs/pages.md` e `Docs/flow.md`.
3. Trate o protótipo como base de validação antes da implementação final.

## Convenção de nomes

- Use nomes de arquivos em kebab-case.
- Prefixe com código de página quando existir em `Docs/pages.md`.

Exemplos:

- `pg-login.html`
- `pg-dashboard.html`
- `fl-checkout-step-1.html`

## Regras de uso

1. O protótipo deve refletir `Docs/pages.md` e `Docs/flow.md` vigentes.
2. Mudanças de fluxo devem atualizar o protótipo correspondente.
3. `Docs/design-system.md` e `Docs/tokens.json` devem ser coerentes com o que foi aprovado no protótipo.
4. Não usar esta pasta para código de produção.

## Estrutura sugerida

- `index.html`: ponto de entrada opcional para navegação entre protótipos.
- `assets/`: css, js e imagens usadas apenas para prototipagem.
- `pages/`: telas isoladas quando o volume crescer.
