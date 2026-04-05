# Manual

Manual operacional consolidado do Nébula Framework para execução real com governança, rastreabilidade e qualidade de produção.

## Objetivo

Este documento unifica as regras e práticas do framework para uso diário do time, reduzindo ambiguidades entre:

1. Metodologia (`README.md`, `GUIDE.md`)
2. Pilares (`Docs`, `Skills`, `Workflows`, `Quality`, `Templates`, `agents`)
3. Modo de operação (com agentes e sem agentes)
4. Ferramentas de AI (Copilot, Cursor, Windsurf, Claude Code, Zed, etc.)

> [!IMPORTANT]
> Este manual não substitui o `GUIDE.md`. Ele operacionaliza o método em cenários reais.

## Fontes de referência usadas

- Núcleo: `README.md`, `GUIDE.md`
- Docs: `Docs/README.md`
- Manual: `Manual/00README.md`, `Manual/01GUIDE.md`
- Skills: `Skills/00README.md`, `Skills/01GUIDE.md`
- Workflows: `Workflows/00README.md`, `Workflows/01GUIDE.md`
- Quality: `Quality/00README.md`, `Quality/01GUIDE.md`
- Templates: `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`, `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- Agentes: `agents/00README.md`, `agents/01GUIDE.md`, `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`
- Manual web atual: `NebulaWeb/content/docs/manual.md`

## Princípios operacionais

1. `Docs/` é fonte de verdade do projeto.
2. `Templates/` é modelo de preenchimento, nunca entrega final.
3. Primeira task sempre `bootstrap_estrutural`.
4. Após bootstrap, somente edição de arquivos existentes.
5. Exatamente 1 commit por task concluída.
6. Quality Gate obrigatório para fechamento.
7. Evidências e rastreabilidade sempre em `Docs/tasks.md` e `Docs/control.md`.

> [!WARNING]
> Fechar task sem evidência + gate aprovado viola governança do Nébula.

## Arquitetura do manual: baseline + delta

Regra de leitura: sempre ler baseline antes do delta.

| Categoria | Baseline | Delta |
|---|---|---|
| Execução | `Manual/17EXECUTION-BASELINE.md` | `Manual/02AGENTS.md` ou `Manual/03NO-AGENTS.md` |
| Cenários | `Manual/16SCENARIOS-BASELINE.md` | `Manual/05SCENARIOS-AGENTS.md` ou `Manual/06SCENARIOS-NO-AGENTS.md` |
| Componentes | `Manual/18COMPONENTS-BASELINE.md` | `Manual/19` a `Manual/22` |
| Criação de agentes | `Manual/15CREATE-AGENT-BASELINE.md` | `Manual/07` a `Manual/14` |

## Trilha de leitura por objetivo

### Quero executar com agentes

1. `GUIDE.md`
2. `Manual/17EXECUTION-BASELINE.md`
3. `Manual/02AGENTS.md`
4. `agents/02CATALOG.md`
5. `Manual/16SCENARIOS-BASELINE.md`
6. `Manual/05SCENARIOS-AGENTS.md`

### Quero executar sem agentes

1. `GUIDE.md`
2. `Manual/17EXECUTION-BASELINE.md`
3. `Manual/03NO-AGENTS.md`
4. `Manual/16SCENARIOS-BASELINE.md`
5. `Manual/06SCENARIOS-NO-AGENTS.md`

### Quero criar/agregar agentes por ferramenta

1. `Manual/15CREATE-AGENT-BASELINE.md`
2. Escolher um delta: `Manual/07` a `Manual/14`
3. Validar contrato canônico em `agents/00README.md` e `agents/01GUIDE.md`

## Fluxo oficial de execução por task

```text
1. Definir objetivo, escopo e restrições
2. Selecionar 1 workflow principal em Workflows/
3. Carregar contexto base e contexto de execução em Docs/
4. Executar mudança técnica
5. Aplicar Quality Gate
6. Registrar evidências e status
7. Fechar com 1 commit
8. Atualizar Docs/tasks.md e Docs/control.md
```

### Contexto mínimo obrigatório antes de executar

- `GUIDE.md`
- `Workflows/01GUIDE.md`
- `Quality/01GUIDE.md`
- `Docs/plan.md`
- `Docs/tasks.md`
- `Docs/control.md`

> [!NOTE]
> Em modo com agentes, incluir também o contexto especializado definido no arquivo do papel em `agents/`.

## Bootstrap estrutural e modo edição

### Task inicial obrigatória

```text
TASK-001
Política: bootstrap_estrutural
Permissão: criar diretórios e arquivos
```

### Tasks seguintes

```text
Política: edição
Permissão: apenas alterar arquivos existentes
Se faltar arquivo obrigatório: abrir task de ajuste estrutural
```

## Integração entre pilares

### Docs

- Guarda artefatos oficiais e estado real da execução.
- Todo fechamento de task precisa atualizar `Docs/tasks.md` e `Docs/control.md`.

### Workflows

- Orquestra sequência por tipo de demanda.
- Toda task tem 1 workflow principal.

### Skills

- Apoio especializado por domínio.
- Não substitui workflow nem Quality Gate.

### Templates

- Estrutura de preenchimento (Full e Quick).
- Quick acelera; Full reduz ambiguidade.
- Se Quick gerar dúvida, migrar para Full na mesma task.

### Quality

- Define critérios de validação.
- Sem gate aprovado, task aberta.

### Agentes

- Papéis canônicos em `agents/`.
- Runtime de ferramenta é adaptador, não fonte de verdade.

## Mapa de cenários para decisão rápida

| Situação                                     | Caminho recomendado                                       |
|----------------------------------------------|-----------------------------------------------------------|
| Nova feature com impacto UI/API              | `new-feature` + agentes especializados (quando aplicável) |
| Nova tela                                    | `new-screen`                                              |
| Integração externa                           | `new-integration`                                         |
| Bug em produção                              | `hotfix`                                                  |
| Refatoração de módulo                        | `module-refactoring`                                      |
| Mudança visual sem nova tela                 | `ui-change`                                               |
| Mudança de contrato                          | `contract-change`                                         |
| Fechamento de entrega                        | `release`                                                 |

## Regra de precedência em conflitos

1. Contrato vigente
2. Documento-fonte do domínio em `Docs/`
3. `Docs/plan.md` e `Docs/tasks.md`
4. Implementação atual

## Definition of Done (task)

Uma task só pode ser concluída quando:

1. Workflow executado sem pular etapa obrigatória.
2. Artefatos oficiais em `Docs/` atualizados.
3. Quality Gate aprovado.
4. Evidências e hash de commit registrados.
5. Estado real registrado em `Docs/control.md`.

## Antipadrões que devem ser evitados

1. Usar `Templates/` como saída final.
2. Criar arquivos em task de edição.
3. Fechar task sem evidência objetiva.
4. Fechar task sem Quality Gate.
5. Agrupar múltiplas tasks em um único commit.
6. Omitir handoff e riscos no `Docs/control.md`.

> [!CAUTION]
> Se qualquer regra acima for quebrada, a entrega perde auditabilidade e deve ser tratada como não concluída.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# localizar guias e readmes do framework
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar artefatos oficiais de execução
ls Docs

# revisar workflows disponíveis
ls Workflows
```

## Encerramento

Este Manual consolida a proposta operacional do Nébula para manter previsibilidade em qualquer contexto: com agentes, sem agentes, com qualquer ferramenta de runtime.

Use este arquivo como referência de operação diária e os documentos baseline/delta para execução detalhada por cenário.
