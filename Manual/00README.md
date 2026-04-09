# Manual

Este diretório centraliza manuais práticos de uso do framework Nébula.

Objetivos:
- orientar o uso com e sem agentes
- explicar como aplicar Skills, Workflows, Quality e Templates
- fornecer exemplos de uso por situações reais
- padronizar criação e manutenção de agentes em ferramentas de AI

## Ordem recomendada de leitura

1. [01GUIDE.md](01GUIDE.md)
2. Execução: [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md) + delta [02AGENTS.md](02AGENTS.md) ou [03NO-AGENTS.md](03NO-AGENTS.md)
3. Componentes: [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md) + índice [04COMPONENTS.md](04COMPONENTS.md) + delta (19 a 22)
4. Cenários: [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md) + delta [05SCENARIOS-AGENTS.md](05SCENARIOS-AGENTS.md) ou [06SCENARIOS-NO-AGENTS.md](06SCENARIOS-NO-AGENTS.md)
5. Criação de agentes: [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md) + delta por ferramenta (07 a 14)

## Relação com o framework

- Método base: [../GUIDE.md](../GUIDE.md)
- Agentes: [../agents/00README.md](../agents/00README.md)
- Catálogo de agentes: [../agents/02CATALOG.md](../agents/02CATALOG.md)
- Skills: [../Skills/00README.md](../Skills/00README.md)
- Workflows: [../Workflows/00README.md](../Workflows/00README.md)
- Quality: [../Quality/README.md](../Quality/README.md)
- Templates Full: [../Templates/Full/01GUIDE.md](../Templates/Full/01GUIDE.md)
- Templates Quick: [../Templates/Quick/01GUIDE.md](../Templates/Quick/01GUIDE.md)

## Regra de uso obrigatória

1. Primeira task de execução deve ser bootstrap estrutural.
2. Após bootstrap, somente edição de arquivos existentes.
3. Uma task concluída deve gerar exatamente 1 commit.
4. Nenhuma task pode ser concluída sem aprovação do Quality Gate.

## Padrão para Manuais 07-14

1. O manual [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md) define o padrão comum.
2. Os manuais 07-14 descrevem apenas o delta nativo de cada ferramenta.

## Padrão para Cenários 05-06

1. O manual [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md) define o fluxo comum de cenários.
2. O manual [05SCENARIOS-AGENTS.md](05SCENARIOS-AGENTS.md) descreve apenas o delta com agentes.
3. O manual [06SCENARIOS-NO-AGENTS.md](06SCENARIOS-NO-AGENTS.md) descreve apenas o delta sem agentes.

## Padrão para Execução 02-03

1. O manual [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md) define o fluxo comum de execução.
2. O manual [02AGENTS.md](02AGENTS.md) descreve apenas o delta com agentes.
3. O manual [03NO-AGENTS.md](03NO-AGENTS.md) descreve apenas o delta sem agentes.

## Padrão para Componentes 04, 18-22

1. O manual [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md) define o fluxo comum de componentes.
2. O manual [04COMPONENTS.md](04COMPONENTS.md) atua como índice rápido.
3. Os manuais 19-22 descrevem apenas o delta por pilar.
