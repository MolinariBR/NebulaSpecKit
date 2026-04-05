```text
    _   __     __          __         _____                    __ __ _ __ 
   / | / /__  / /_  __  __/ /___ _   / ___/____  ___  _____   / //_/(_) /_
  /  |/ / _ \/ __ \/ / / / / __ `/   \__ \/ __ \/ _ \/ ___/  / ,<  / / __/
 / /|  /  __/ /_/ / /_/ / / /_/ /   ___/ / /_/ /  __/ /__   / /| |/ / /_  
/_/ |_/\___/_.___/\__,_/_/\__,_/   /____/ .___/\___/\___/  /_/ |_/_/\__/  
                                       /_/                                
```
* Author: Maurício Molinari
* License: MIT
* Repository: https://github.com/molinariBR/nebula-spec-kit
* Website: https://molinari.dev/nebula-spec-kit
* Version: 1.0.0
* Last update: 2026-04-05

# Nébula

> Framework de governança documental, execução por tasks e validação técnica com foco em fidelidade de produção.

---

## O que é o Nébula?

A maioria dos projetos falha não por falta de talento, mas por falta de estrutura: decisões sem rastreabilidade, documentação desatualizada, execução inconsistente entre devs e IAs, e qualidade improvisada.

**O Nébula resolve isso.**

Ele padroniza como um projeto é **descoberto, definido, planejado, executado e validado** — com suporte nativo a agentes de AI sem abrir mão de governança, previsibilidade e qualidade de produção.

---

## Pilares

| Pilar        |                        Arquivo                         |      Responsabilidade             | 
|--------------|--------------------------------------------------------|-----------------------------------|
| Metodologia  | [GUIDE.md](GUIDE.md)                                   | Referência central de método      |
| Documentação | [Docs/README.md](Docs/README.md)                       | Artefatos oficiais do projeto     |
| Skills       | [Skills/00README.md](Skills/00README.md)               | Capacidades técnicas mapeadas     |
| Workflows    | [Workflows/00README.md](Workflows/00README.md)         | Fluxos de execução padronizados   |
| Quality      | [Quality/00README.md](Quality/00README.md)             | Gates e políticas de qualidade    |
| Templates    | [Templates/Full/01GUIDE.md](Templates/Full/01GUIDE.md) | Modelos de preenchimento          |
| Agentes      | [agents/00README.md](agents/00README.md)               | Contrato e catálogo de agentes AI |
| Manual       | [Manual/00README.md](Manual/00README.md)               | Guia operacional completo         |
| Protótipos   | [Prototype/00README.md](Prototype/00README.md)         | Interfaces HTML de referência     |

---

## Estrutura do Repositório

```
.
├── README.md
├── GUIDE.md                  # Metodologia central
├── Docs/                     # Artefatos oficiais (saída de produção)
├── Templates/
│   ├── Full/                 # Templates completos por artefato
│   └── Quick/                # Templates de uso rápido
├── Skills/                   # Capacidades técnicas
├── Workflows/                # Fluxos executáveis
├── Quality/                  # Gates, testes e políticas
├── agents/                   # Agentes especializados
├── Prototype/                # Protótipos de interface
└── Manual/                   # Documentação operacional
```

---

## Fluxo de Trabalho

```
Brief → Projeto & Stack → UX & Design → Protótipos → Técnico → Execução → Validação
```

1. **Brief** — Preencher `Templates/Full/brief.md` → salvar em `Docs/brief.md`
2. **Projeto & Stack** — Usar os templates de projeto e stack → salvar em `Docs/`
3. **UX & Design** — User stories, páginas, fluxo, design system → salvar em `Docs/`
4. **Protótipos** — Construir interfaces HTML em `Prototype/`
5. **Técnico** — Entidades, arquitetura, contrato, estrutura, deploy → salvar em `Docs/`
6. **Execução** — Operar com `Docs/plan.md`, `Docs/tasks.md` e `Docs/control.md`
7. **Validação** — Fechar cada task com [Quality/gate.md](Quality/gate.md)

### Mapa Templates → Docs

Cada template tem exatamente um destino oficial:

```
Templates/Full/brief.md          →  Docs/brief.md
Templates/Full/project.md        →  Docs/project.md
Templates/Full/stack.md          →  Docs/stack.md
Templates/Full/user-stories.md   →  Docs/user-stories.md
Templates/Full/pages.md          →  Docs/pages.md
Templates/Full/flow.md           →  Docs/flow.md
Templates/Full/design-system.md  →  Docs/design-system.md
Templates/Full/tokens.json       →  Docs/tokens.json
Templates/Full/entities.md       →  Docs/entities.md
Templates/Full/architecture.md   →  Docs/architecture.md
Templates/Full/contract.yaml     →  Docs/contract.yaml
Templates/Full/structure.md      →  Docs/structure.md
Templates/Full/deploy.md         →  Docs/deploy.md
Templates/Full/plan.md           →  Docs/plan.md
Templates/Full/tasks.md          →  Docs/tasks.md
Templates/Full/control.md        →  Docs/control.md
```

---

## Política de Execução por Task

O Nébula define regras estritas de execução para garantir rastreabilidade total:

- **Task 1 é sempre bootstrap estrutural** — única task autorizada a criar diretórios e arquivos
- **Tasks seguintes apenas editam** — se um arquivo obrigatório estiver ausente, abrir task de ajuste estrutural
- **1 task = 1 commit** — cada task concluída gera exatamente um commit
- **Todo commit deve registrar** hash, arquivos tocados e resultado do gate de qualidade

Referências: 
[Workflows/bootstrap-structure.md](Workflows/bootstrap-structure.md)
[Docs/tasks.md](Docs/tasks.md)
[Quality/gate.md](Quality/gate.md)

---

## Qualidade

O framework adota **qualidade orientada a produção realista** — sem mocks, sem atalhos que não escalam.

|                       Arquivo                            |           Conteúdo             |
|----------------------------------------------------------|--------------------------------|
| [Quality/01GUIDE.md](Quality/01GUIDE.md)                 | Guia geral de qualidade        |
| [Quality/gate.md](Quality/gate.md)                       | Gate obrigatório por task      |
| [Quality/realistic-tests.md](Quality/realistic-tests.md) | Testes realistas               |
| [Quality/anti-mock.md](Quality/anti-mock.md)             | Política anti-mock             |
| [Quality/code-style.md](Quality/code-style.md)           | Padrão de código               |
| [Quality/dependencies.md](Quality/dependencies.md)       | Dependências e compatibilidade |

---

## Agentes Especializados

Cada agente opera sob contrato único e carregamento de contexto obrigatório:

1. Carregar metodologia e guides dos pilares
2. Carregar artefatos oficiais de execução em `Docs/`
3. Usar `Templates/` apenas como referência de estrutura — nunca como saída

Referências: 
[agents/00README.md](agents/00README.md)
[agents/01GUIDE.md](agents/01GUIDE.md)
[agents/02CATALOG.md](agents/02CATALOG.md)

---

## Manual Operacional

O manual é organizado em camadas **baseline + delta**: cada baseline define o comportamento padrão, e os deltas especificam variações por modo de operação (com agentes, sem agentes) ou por ferramenta.

### Navegação

|                 Arquivo                    |     Conteúdo      |
|--------------------------------------------|-------------------|
| [Manual/00README.md](Manual/00README.md)   | Entrada do manual |
| [Manual/01GUIDE.md](Manual/01GUIDE.md)     | Guia de navegação |

### Execução

|                           Arquivo                                |           Conteúdo           |
|------------------------------------------------------------------|------------------------------|
| [Manual/17EXECUTION-BASELINE.md](Manual/17EXECUTION-BASELINE.md) | Execução baseline            |
| [Manual/02AGENTS.md](Manual/02AGENTS.md)                         | Delta — execução com agentes |
| [Manual/03NO-AGENTS.md](Manual/03NO-AGENTS.md)                   | Delta — execução sem agentes |

### Cenários

|                           Arquivo                                  |          Conteúdo            |
|--------------------------------------------------------------------|------------------------------|
| [Manual/16SCENARIOS-BASELINE.md](Manual/16SCENARIOS-BASELINE.md)   | Cenários baseline            |
| [Manual/05SCENARIOS-AGENTS.md](Manual/05SCENARIOS-AGENTS.md)       | Delta — cenários com agentes |
| [Manual/06SCENARIOS-NO-AGENTS.md](Manual/06SCENARIOS-NO-AGENTS.md) | Delta — cenários sem agentes |

### Componentes

|                            Arquivo                                   |          Conteúdo    |
|----------------------------------------------------------------------|----------------------|
| [Manual/18COMPONENTS-BASELINE.md](Manual/18COMPONENTS-BASELINE.md)   | Componentes baseline |
| [Manual/19COMPONENTS-SKILLS.md](Manual/19COMPONENTS-SKILLS.md)       | Delta — Skills       |
| [Manual/20COMPONENTS-WORKFLOWS.md](Manual/20COMPONENTS-WORKFLOWS.md) | Delta — Workflows    |
| [Manual/21COMPONENTS-QUALITY.md](Manual/21COMPONENTS-QUALITY.md)     | Delta — Quality      |
| [Manual/22COMPONENTS-TEMPLATES.md](Manual/22COMPONENTS-TEMPLATES.md) | Delta — Templates    |

### Criação de Agentes

|                            Arquivo                               |          Conteúdo            |
|------------------------------------------------------------------|------------------------------|
| [Manual/15CREATE-AGENT-BASELINE.md](Manual/15CREATE-AGENT-BASELINE.md) | Criação de agentes baseline |
| [Manual/07CREATE-AGENT-GITHUB-COPILOT.md](Manual/07CREATE-AGENT-GITHUB-COPILOT.md) → [Manual/14CREATE-AGENT-ZED.md](Manual/14CREATE-AGENT-ZED.md) | Delta por ferramenta (Copilot, Cursor, Zed...) |

---

## Princípios

- **Fidelidade** — o que está documentado é o que vai para produção
- **Rastreabilidade** — cada decisão e entrega tem registro
- **Consistência** — documentação, execução e validação falam a mesma língua
- **Governança** — Dev e AI operam com as mesmas regras
- **Previsibilidade** — prazo, qualidade e manutenção deixam de ser variáveis aleatórias

---