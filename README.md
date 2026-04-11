```text
           _   __     __          __         _____                    __ __ _ __
          / | / /__  / /_  __  __/ /___ _   / ___/____  ___  _____   / //_/(_) /_
         /  |/ / _ \/ __ \/ / / / / __ `/   \__ \/ __ \/ _ \/ ___/  / ,<  / / __/
        / /|  /  __/ /_/ / /_/ / / /_/ /   ___/ / /_/ /  __/ /__   / /| |/ / /_
       /_/ |_|\___/_.___/\__,_/_/\__,_/   /____/ .___/\___/\___/  /_/ |_/_/\__/
                                              /_/
```

- Autor: Maurício Molinari
- Licença: MIT
- Repositório: https://github.com/MolinariBR/NebulaSpecKit
- Site: https://nebulaweb.vercel.app/
- Versão: 1.0.3
- Última atualização: 2026-04-09

# Nébula Spec Kit

> Framework de governança documental, execução por tasks e validação técnica, com foco em fidelidade de produção.

---

## O que é o Nébula?

A maioria dos projetos falha não por falta de talento, mas por falta de estrutura: decisões sem rastreabilidade, documentação desatualizada, execução inconsistente entre devs e IAs e qualidade improvisada.

**O Nébula resolve esse problema.**

Ele padroniza como um projeto é **descoberto, definido, planejado, executado e validado**, com suporte nativo a agentes de IA, sem abrir mão de governança, previsibilidade e qualidade de produção.

---

## Estado Atual do Fluxo

Mudanças estruturais recentes já refletidas neste repositório:

- Agentes renomeados para padrão curto: `agents/<role>.md` (sem sufixo `-agent`).
- Arquivo legado removido: `agents/02CATALOG.md`.
- `Manual/` permanece como guia para dev humano e não compõe o contexto mínimo de IA.
- Contexto mínimo de execução com IA centralizado em:
  - `instructions.md`
  - `GUIDE.md`
  - `Workflows/README.md`
  - `Skills/README.md`
  - `Quality/validation-rules.md`

---

## Pilares

| Pilar | Arquivo | Responsabilidade |
| --- | --- | --- |
| Instruções | [instructions.md](instructions.md) | Raiz operacional e precedência de execução |
| Metodologia | [GUIDE.md](GUIDE.md) | Referência central do método |
| Documentação | [Docs/README.md](Docs/README.md) | Artefatos oficiais do projeto |
| Skills | [Skills/README.md](Skills/README.md) | Capacidades técnicas mapeadas |
| Workflows | [Workflows/README.md](Workflows/README.md) | Fluxos de execução padronizados |
| Quality | [Quality/README.md](Quality/README.md) | Gates e políticas de qualidade |
| Templates | [Templates/Full/README.md](Templates/Full/README.md) | Modelos de preenchimento |
| Agentes | [agents/README.md](agents/README.md) | Contrato e papéis de agentes de IA |
| Manual | [Manual/README.md](Manual/README.md) | Guia de uso para dev humano (fora do contexto mínimo de IA) |
| Protótipos | [Docs/Prototype/README.md](Docs/Prototype/README.md) | Interfaces HTML de referência |

---

## Estrutura do Repositório

```text
.
├── README.md
├── GUIDE.md                  # Metodologia central
├── instructions.md           # Raiz operacional
├── Docs/                     # Artefatos oficiais (saída de produção)
│   └── Prototype/            # Protótipos de interface
├── Templates/
│   ├── Full/                 # Templates completos por artefato
│   └── Quick/                # Templates de uso rápido
├── Skills/                   # Capacidades técnicas
├── Workflows/                # Fluxos executáveis
├── Quality/                  # Gates, testes e políticas
├── agents/                   # Agentes especializados
└── Manual/                   # Documentação operacional
```

---

## Fluxo de Trabalho

```text
Brief → Projeto e Stack → UX e Design → Protótipos → Técnico → Execução → Validação
```

1. **Brief**: preencha `Templates/Full/brief.md` e salve em `Docs/brief.md`.
2. **Projeto e Stack**: use os templates de projeto e stack e salve em `Docs/`.
3. **UX e Design**: documente user stories, páginas, fluxo e design system em `Docs/`.
4. **Protótipos**: construa interfaces HTML em `Docs/Prototype/`.
5. **Técnico**: documente entidades, arquitetura, contrato, estrutura e deploy em `Docs/`.
6. **Execução**: opere com `Docs/plan.md`, `Docs/tasks.md` e `Docs/control.md`.
7. **Validação**: feche cada task com [Quality/validation-rules.md](Quality/validation-rules.md).

### Mapa Templates -> Docs

Cada template tem exatamente um destino oficial:

```text
Templates/Full/brief.md          -> Docs/brief.md
Templates/Full/project.md        -> Docs/project.md
Templates/Full/stack.md          -> Docs/stack.md
Templates/Full/user-stories.md   -> Docs/user-stories.md
Templates/Full/pages.md          -> Docs/pages.md
Templates/Full/flow.md           -> Docs/flow.md
Templates/Full/design-system.md  -> Docs/design-system.md
Templates/Full/tokens.json       -> Docs/tokens.json
Templates/Full/entities.md       -> Docs/entities.md
Templates/Full/architecture.md   -> Docs/architecture.md
Templates/Full/contract.yaml     -> Docs/contract.yaml
Templates/Full/structure.md      -> Docs/structure.md
Templates/Full/deploy.md         -> Docs/deploy.md
Templates/Full/plan.md           -> Docs/plan.md
Templates/Full/tasks.md          -> Docs/tasks.md
Templates/Full/control.md        -> Docs/control.md
```

---

## Política de Execução por Task

O Nébula define regras estritas de execução para garantir rastreabilidade total:

- **A Task 1 é sempre de bootstrap estrutural**: é a única task autorizada a criar diretórios e arquivos.
- **As tasks seguintes apenas editam**: se um arquivo obrigatório estiver ausente, abra uma task de ajuste estrutural.
- **1 task = 1 commit**: cada task concluída gera exatamente um commit.
- **Todo commit deve registrar**: hash, arquivos tocados e resultado do gate de qualidade.

Referências:

- [Workflows/bootstrap-structure.md](Workflows/bootstrap-structure.md)
- [Docs/tasks.md](Docs/tasks.md)
- [Quality/validation-rules.md](Quality/validation-rules.md)

---

## Qualidade

O framework adota **qualidade orientada à produção realista**: sem mocks e sem atalhos que não escalam.

| Arquivo | Conteúdo |
| --- | --- |
| [Quality/README.md](Quality/README.md) | Guia geral de qualidade |
| [Quality/validation-rules.md](Quality/validation-rules.md) | Gate obrigatório por task |
| [Quality/gate-evidence.md](Quality/gate-evidence.md) | Formato de evidência e critérios de aplicabilidade |
| [Quality/realistic-tests.md](Quality/realistic-tests.md) | Testes realistas |
| [Quality/anti-mock.md](Quality/anti-mock.md) | Política anti-mock |
| [Quality/clean-rules.md](Quality/clean-rules.md) | Regras de código limpo |
| [Quality/structure-rules.md](Quality/structure-rules.md) | Regras de estrutura de arquivos e módulos |
| [Quality/metrics.md](Quality/metrics.md) | Métricas, limites e bandas de risco |
| [Quality/review-checklist.md](Quality/review-checklist.md) | Checklist de revisão técnica |
| [Quality/dependencies.md](Quality/dependencies.md) | Dependências e compatibilidade |
| [Quality/execution-policy.md](Quality/execution-policy.md) | Política de execução e escopo |

---

## Agentes Especializados

Cada agente opera sob contrato único e carregamento obrigatório de contexto
definido em `instructions.md` e `agents/README.md`:

1. Carregar contexto base:
- `GUIDE.md`
- `Skills/README.md`
- `Workflows/README.md`
- `Quality/validation-rules.md`
2. Carregar contexto condicional quando aplicável:
- `Templates/Full/README.md`
- políticas complementares em `Quality/*.md`
3. Carregar artefatos oficiais de execução em `Docs/`.
4. Usar `Templates/` apenas como referência de estrutura, nunca como saída final.

Papéis atuais de agente:

| Papel | Arquivo |
| --- | --- |
| Scope | [agents/scope.md](agents/scope.md) |
| Product | [agents/product.md](agents/product.md) |
| System | [agents/system.md](agents/system.md) |
| Execution | [agents/execution.md](agents/execution.md) |
| Quality | [agents/quality.md](agents/quality.md) |
| Release | [agents/release.md](agents/release.md) |
| Recovery | [agents/recovery.md](agents/recovery.md) |

Referências:

- [agents/README.md](agents/README.md)
- [instructions.md](instructions.md)

---

## Manual Operacional

O manual é organizado em camadas de **baseline + delta**: cada baseline define o comportamento padrão, e os deltas especificam variações por modo de operação (com agentes ou sem agentes) e por ferramenta.

### Navegação

| Arquivo | Conteúdo |
| --- | --- |
| [Manual/README.md](Manual/README.md) | Entrada do manual |

### Execução

| Arquivo | Conteúdo |
| --- | --- |
| [Manual/17EXECUTION-BASELINE.md](Manual/17EXECUTION-BASELINE.md) | Execução baseline |
| [Manual/02AGENTS.md](Manual/02AGENTS.md) | Delta: execução com agentes |
| [Manual/03NO-AGENTS.md](Manual/03NO-AGENTS.md) | Delta: execução sem agentes |

### Cenários

| Arquivo | Conteúdo |
| --- | --- |
| [Manual/16SCENARIOS-BASELINE.md](Manual/16SCENARIOS-BASELINE.md) | Cenários baseline |
| [Manual/05SCENARIOS-AGENTS.md](Manual/05SCENARIOS-AGENTS.md) | Delta: cenários com agentes |
| [Manual/06SCENARIOS-NO-AGENTS.md](Manual/06SCENARIOS-NO-AGENTS.md) | Delta: cenários sem agentes |

### Componentes

| Arquivo | Conteúdo |
| --- | --- |
| [Manual/18COMPONENTS-BASELINE.md](Manual/18COMPONENTS-BASELINE.md) | Componentes baseline |
| [Manual/19COMPONENTS-SKILLS.md](Manual/19COMPONENTS-SKILLS.md) | Delta: Skills |
| [Manual/20COMPONENTS-WORKFLOWS.md](Manual/20COMPONENTS-WORKFLOWS.md) | Delta: Workflows |
| [Manual/21COMPONENTS-QUALITY.md](Manual/21COMPONENTS-QUALITY.md) | Delta: Quality |
| [Manual/22COMPONENTS-TEMPLATES.md](Manual/22COMPONENTS-TEMPLATES.md) | Delta: Templates |

### Criação de Agentes

| Arquivo | Conteúdo |
| --- | --- |
| [Manual/15CREATE-AGENT-BASELINE.md](Manual/15CREATE-AGENT-BASELINE.md) | Criação de agentes baseline |
| [Manual/07CREATE-AGENT-GITHUB-COPILOT.md](Manual/07CREATE-AGENT-GITHUB-COPILOT.md) até [Manual/14CREATE-AGENT-ZED.md](Manual/14CREATE-AGENT-ZED.md) | Delta por ferramenta (Copilot, Cursor, Zed etc.) |

---

## Princípios

- **Fidelidade**: o que está documentado é o que vai para produção.
- **Rastreabilidade**: cada decisão e entrega têm registro.
- **Consistência**: documentação, execução e validação falam a mesma língua.
- **Governança**: dev e IA operam com as mesmas regras.
- **Previsibilidade**: prazo, qualidade e manutenção deixam de ser variáveis aleatórias.
