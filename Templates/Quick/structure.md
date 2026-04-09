# Estrutura

## Nome do projeto
[preencher]

## Objetivo
Definir a estrutura mínima de diretórios e arquivos para bootstrap estrutural e rastreabilidade da implementação.

## Estrutura raiz (base)

```txt
.
├── README.md
├── GUIDE.md
├── Docs/
│   ├── README.md
│   ├── brief.md
│   ├── project.md
│   ├── stack.md
│   ├── user-stories.md
│   ├── pages.md
│   ├── flow.md
│   ├── design-system.md
│   ├── tokens.json
│   ├── entities.md
│   ├── architecture.md
│   ├── contract.yaml
│   ├── structure.md
│   ├── deploy.md
│   ├── plan.md
│   ├── tasks.md
│   └── control.md
├── Manual/
│   ├── 00README.md
│   ├── 01GUIDE.md
│   └── 02..14 *.md
├── Prototype/
│   ├── 00README.md
│   ├── 01GUIDE.md
│   ├── index.html
│   ├── pages/
│   └── assets/
├── Quality/
│   ├── README.md
│   ├── execution-policy.md
│   ├── structure-rules.md
│   ├── clean-rules.md
│   ├── metrics.md
│   ├── review-checklist.md
│   ├── realistic-tests.md
│   ├── anti-mock.md
│   ├── dependencies.md
│   └── validation-rules.md
├── Skills/
│   ├── 00README.md
│   ├── 01GUIDE.md
│   └── *.md
├── Workflows/
│   ├── 00README.md
│   ├── 01GUIDE.md
│   └── *.md
├── Templates/
│   ├── Full/
│   └── Quick/
├── src/
├── tests/
├── scripts/
└── .github/workflows/
```

## Regras operacionais
- A primeira task deve ser `bootstrap_estrutural`.
- No bootstrap, criar a estrutura completa definida neste documento.
- Todo artefato oficial de governança, execução e qualidade deve ser salvo em `Docs/`.
- A partir da segunda task, apenas editar arquivos existentes.
- Cada task concluída gera exatamente 1 commit.
- Toda task deve registrar hash, arquivos tocados e status do Quality Gate.

## Vinculo com fases e milestones
- FASE 01 (M1): bootstrap estrutural completo e validado.
- FASE 02 (M2): implementação de funcionalidades nucleares com qualidade aprovada.
- FASE 03 (M2): consolidação técnica e cobertura de validações realistas.
- FASE 04 (M3): estabilização final e readiness para release.

## Checklist rápido
- ( ) Estrutura raiz criada integralmente
- ( ) Prototype pronto para validação de UI/fluxo
- ( ) Pastas de governança criadas e completas
- ( ) Estrutura de código definida (src/, tests/, scripts/)
- ( ) Regra bootstrap + edição respeitada
