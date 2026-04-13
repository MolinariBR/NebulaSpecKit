# Manual

Este diretório centraliza manuais práticos de uso do framework Nébula.

## Objetivos

- orientar o uso com e sem agentes;
- explicar como aplicar Skills, Workflows, Quality e Templates;
- fornecer exemplos de uso por situações reais;
- padronizar criação e manutenção de agentes em ferramentas de IA.

## Regra de leitura

Sempre carregar o baseline primeiro e, depois, apenas o delta do modo ou da ferramenta.

## Ordem recomendada de leitura

1. Execução: [Execution.md](Execution.md) + delta [Agents.md](Agents.md) ou [NoAgents.md](NoAgents.md)
2. Componentes: [Components-Base.md](Components-Base.md) + índice [Components.md](Components.md) + delta [Skills.md](Skills.md), [Workflows.md](Workflows.md), [Quality.md](Quality.md) ou [Templates.md](Templates.md)
3. Cenários: [Scenarios-Base.md](Scenarios-Base.md) + delta [Scenarios-Agents.md](Scenarios-Agents.md) ou [Scenarios-NoAgents.md](Scenarios-NoAgents.md)
4. Criação de agentes: [Baseline.md](CreateAgents/Baseline.md) + delta por ferramenta (`CreateAgents/*.md`)

## Mapa de decisões

1. Quero usar agentes na execução:
- Ler [Execution.md](Execution.md)
- Ler [Agents.md](Agents.md)
- Ler [Scenarios-Base.md](Scenarios-Base.md)
- Ler [Scenarios-Agents.md](Scenarios-Agents.md)

2. Quero executar sem agentes:
- Ler [Execution.md](Execution.md)
- Ler [NoAgents.md](NoAgents.md)
- Ler [Scenarios-Base.md](Scenarios-Base.md)
- Ler [Scenarios-NoAgents.md](Scenarios-NoAgents.md)

3. Quero entender o papel de Skills, Workflows, Quality e Templates:
- Ler [Components-Base.md](Components-Base.md)
- Ler [Components.md](Components.md)
- Ler o delta do pilar desejado:
- [Skills.md](Skills.md)
- [Workflows.md](Workflows.md)
- [Quality.md](Quality.md)
- [Templates.md](Templates.md)

4. Quero criar ou adaptar agentes em uma ferramenta específica:
- Ler primeiro [Baseline.md](CreateAgents/Baseline.md)
- Depois ler o documento da ferramenta alvo:
- [Copilot.md](CreateAgents/Copilot.md)
- [Cursor.md](CreateAgents/Cursor.md)
- [Antigravity.md](CreateAgents/Antigravity.md)
- [Windsurf.md](CreateAgents/Windsurf.md)
- [Trae.md](CreateAgents/Trae.md)
- [Claude.md](CreateAgents/Claude.md)
- [OpenCode.md](CreateAgents/OpenCode.md)
- [Zed.md](CreateAgents/Zed.md)

5. Quero aplicar cenários com menos repetição:
- Ler primeiro [Scenarios-Base.md](Scenarios-Base.md)
- Depois ler apenas o delta do modo escolhido:
- [Scenarios-Agents.md](Scenarios-Agents.md)
- [Scenarios-NoAgents.md](Scenarios-NoAgents.md)

6. Quero aplicar componentes com menos repetição:
- Ler primeiro [Components-Base.md](Components-Base.md)
- Ler [Components.md](Components.md) para índice rápido
- Ler somente o delta necessário:
- [Skills.md](Skills.md)
- [Workflows.md](Workflows.md)
- [Quality.md](Quality.md)
- [Templates.md](Templates.md)

## Fluxo recomendado de trabalho

1. Definir objetivo e escopo.
2. Editar os artefatos da demanda em `Docs/` usando `Templates/` como modelo.
3. Selecionar workflow adequado ao tipo de mudança.
4. Escolher modo de execução: com agente ou sem agente.
5. Aplicar Quality Gate antes de concluir a task.
6. Registrar 1 commit por task.

## Relação com o framework

- Método base: [../Guide-Started.md](../../Guide-Started.md)
- Agentes: [../agents/README.md](../../agents/README.md)
- Catálogo de agentes: [Agents.md](Agents.md)
- Skills: [../Skills/README.md](../../Skills/README.md)
- Workflows: [../Workflows/README.md](../../Workflows/README.md)
- Quality: [../Quality/README.md](../../Quality/README.md)
- Templates Full: [../Templates/Full/README.md](../../Templates/Full/README.md)
- Templates Quick: [../Templates/Quick/README.md](../../Templates/Quick/README.md)

## Regra de uso obrigatória

1. Primeira task de execução deve ser bootstrap estrutural.
2. Após bootstrap, somente edição de arquivos existentes.
3. Uma task concluída deve gerar exatamente 1 commit.
4. Nenhuma task pode ser concluída sem aprovação do Quality Gate.

## Padrões baseline + delta

### Cenários (baseline + delta)

1. O manual [Scenarios-Base.md](Scenarios-Base.md) define o fluxo comum de cenários.
2. O manual [Scenarios-Agents.md](Scenarios-Agents.md) descreve apenas o delta com agentes.
3. O manual [Scenarios-NoAgents.md](Scenarios-NoAgents.md) descreve apenas o delta sem agentes.

### Execução (baseline + delta)

1. O manual [Execution.md](Execution.md) define o fluxo comum de execução.
2. O manual [Agents.md](Agents.md) descreve apenas o delta com agentes.
3. O manual [NoAgents.md](NoAgents.md) descreve apenas o delta sem agentes.

### Componentes (baseline + delta)

1. O manual [Components-Base.md](Components-Base.md) define o fluxo comum de componentes.
2. O manual [Components.md](Components.md) atua como índice rápido.
3. Os manuais de delta descrevem apenas o ajuste por pilar:
- [Skills.md](Skills.md)
- [Workflows.md](Workflows.md)
- [Quality.md](Quality.md)
- [Templates.md](Templates.md)

### Criação de agentes (baseline + delta)

1. O manual [Baseline.md](CreateAgents/Baseline.md) define o padrão comum.
2. Os manuais `CreateAgents/*.md` descrevem apenas o delta nativo de cada ferramenta.

## Convenções de referência

- Caminhos de arquivo sempre relativos ao root do repositório.
- Evitar fontes duplicadas de verdade.
- Em conflito de instruções, seguir a precedência definida em [../Guide-Started.md](../../Guide-Started.md).
