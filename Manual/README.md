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

1. Execução: [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md) + delta [02AGENTS.md](02AGENTS.md) ou [03NO-AGENTS.md](03NO-AGENTS.md)
2. Componentes: [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md) + índice [04COMPONENTS.md](04COMPONENTS.md) + delta (19 a 22)
3. Cenários: [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md) + delta [05SCENARIOS-AGENTS.md](05SCENARIOS-AGENTS.md) ou [06SCENARIOS-NO-AGENTS.md](06SCENARIOS-NO-AGENTS.md)
4. Criação de agentes: [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md) + delta por ferramenta (07 a 14)

## Mapa de decisões

1. Quero usar agentes na execução:
- Ler [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md)
- Ler [02AGENTS.md](02AGENTS.md)
- Ler [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
- Ler [05SCENARIOS-AGENTS.md](05SCENARIOS-AGENTS.md)

2. Quero executar sem agentes:
- Ler [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md)
- Ler [03NO-AGENTS.md](03NO-AGENTS.md)
- Ler [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
- Ler [06SCENARIOS-NO-AGENTS.md](06SCENARIOS-NO-AGENTS.md)

3. Quero entender o papel de Skills, Workflows, Quality e Templates:
- Ler [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md)
- Ler [04COMPONENTS.md](04COMPONENTS.md)
- Ler o delta do pilar desejado (19 a 22)

4. Quero criar ou adaptar agentes em uma ferramenta específica:
- Ler primeiro [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
- Depois ler o documento da ferramenta alvo (07 a 14)

5. Quero aplicar cenários com menos repetição:
- Ler primeiro [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
- Depois ler apenas o delta do modo escolhido (05 ou 06)

6. Quero aplicar componentes com menos repetição:
- Ler primeiro [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md)
- Ler [04COMPONENTS.md](04COMPONENTS.md) para índice rápido
- Ler somente o delta necessário: 19, 20, 21 ou 22

## Fluxo recomendado de trabalho

1. Definir objetivo e escopo.
2. Editar os artefatos da demanda em `Docs/` usando `Templates/` como modelo.
3. Selecionar workflow adequado ao tipo de mudança.
4. Escolher modo de execução: com agente ou sem agente.
5. Aplicar Quality Gate antes de concluir a task.
6. Registrar 1 commit por task.

## Relação com o framework

- Método base: [../GUIDE.md](../GUIDE.md)
- Agentes: [../agents/README.md](../agents/README.md)
- Catálogo de agentes: [../agents/02CATALOG.md](../agents/02CATALOG.md)
- Skills: [../Skills/README.md](../Skills/README.md)
- Workflows: [../Workflows/README.md](../Workflows/README.md)
- Quality: [../Quality/README.md](../Quality/README.md)
- Templates Full: [../Templates/Full/README.md](../Templates/Full/README.md)
- Templates Quick: [../Templates/Quick/README.md](../Templates/Quick/README.md)

## Regra de uso obrigatória

1. Primeira task de execução deve ser bootstrap estrutural.
2. Após bootstrap, somente edição de arquivos existentes.
3. Uma task concluída deve gerar exatamente 1 commit.
4. Nenhuma task pode ser concluída sem aprovação do Quality Gate.

## Padrões baseline + delta

### Cenários (05-06)

1. O manual [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md) define o fluxo comum de cenários.
2. O manual [05SCENARIOS-AGENTS.md](05SCENARIOS-AGENTS.md) descreve apenas o delta com agentes.
3. O manual [06SCENARIOS-NO-AGENTS.md](06SCENARIOS-NO-AGENTS.md) descreve apenas o delta sem agentes.

### Execução (02-03)

1. O manual [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md) define o fluxo comum de execução.
2. O manual [02AGENTS.md](02AGENTS.md) descreve apenas o delta com agentes.
3. O manual [03NO-AGENTS.md](03NO-AGENTS.md) descreve apenas o delta sem agentes.

### Componentes (04, 18-22)

1. O manual [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md) define o fluxo comum de componentes.
2. O manual [04COMPONENTS.md](04COMPONENTS.md) atua como índice rápido.
3. Os manuais 19-22 descrevem apenas o delta por pilar.

### Criação de agentes (07-14)

1. O manual [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md) define o padrão comum.
2. Os manuais 07-14 descrevem apenas o delta nativo de cada ferramenta.

## Convenções de referência

- Caminhos de arquivo sempre relativos ao root do repositório.
- Evitar fontes duplicadas de verdade.
- Em conflito de instruções, seguir a precedência definida em [../GUIDE.md](../GUIDE.md).
