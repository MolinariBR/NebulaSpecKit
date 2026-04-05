# Guide

Este guia explica como navegar pelo diretório Manual e como escolher o tipo de manual para cada necessidade.

Regra de leitura: sempre carregar o baseline primeiro e, depois, apenas o delta do modo ou da ferramenta.

## Mapa de decisões

1. Quero usar agentes na execução
- Ler [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md)
- Ler [02AGENTS.md](02AGENTS.md)
- Ler [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
- Ler [05SCENARIOS-AGENTS.md](05SCENARIOS-AGENTS.md)

2. Quero executar sem agentes
- Ler [17EXECUTION-BASELINE.md](17EXECUTION-BASELINE.md)
- Ler [03NO-AGENTS.md](03NO-AGENTS.md)
- Ler [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
- Ler [06SCENARIOS-NO-AGENTS.md](06SCENARIOS-NO-AGENTS.md)

3. Quero entender o papel de Skills, Workflows, Quality e Templates
- Ler [18COMPONENTS-BASELINE.md](18COMPONENTS-BASELINE.md)
- Ler [04COMPONENTS.md](04COMPONENTS.md)
- Ler o delta do pilar desejado (19 a 22)

4. Quero criar ou adaptar agentes em uma ferramenta específica
- Ler primeiro [15CREATE-AGENT-BASELINE.md](15CREATE-AGENT-BASELINE.md)
- Depois ler o documento da ferramenta alvo (07 a 14)

5. Quero aplicar cenários com menos repetição
- Ler primeiro [16SCENARIOS-BASELINE.md](16SCENARIOS-BASELINE.md)
- Depois ler apenas o delta do modo escolhido (05 ou 06)

6. Quero aplicar componentes com menos repetição
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

## Convenções de referência

- Caminhos de arquivo sempre relativos ao root do repositório.
- Evitar fontes duplicadas de verdade.
- Em conflito de instruções, seguir a precedência definida em [../GUIDE.md](../GUIDE.md).
