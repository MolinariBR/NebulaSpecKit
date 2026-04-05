# Prototype

Pasta raiz para protótipos em HTML.

## Objetivo

Centralizar protótipos navegáveis usados para validar fluxo, estrutura de tela e comportamento antes da implementação final.

## Convencao de nomes

- Use nomes de arquivos em kebab-case.
- Prefixe com código de pagina quando existir em Docs/pages.md.

Exemplos:

- `pg-login.html`
- `pg-dashboard.html`
- `fl-checkout-step-1.html`

## Regras de uso

1. O protótipo deve refletir Docs/pages.md e Docs/flow.md vigentes.
2. Mudanças de fluxo devem atualizar o protótipo correspondente.
3. Docs/design-system.md e Docs/tokens.json devem ser coerentes com o que foi aprovado no protótipo.
4. Não usar esta pasta para código de produção.

## Estrutura sugerida

- `index.html`: ponto de entrada opcional para navegação entre protótipos.
- `assets/`: css, js e imagens usadas apenas para prototipagem.
- `pages/`: telas isoladas quando o volume crescer.
