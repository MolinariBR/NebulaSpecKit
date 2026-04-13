# Scenarios Baseline

Este manual define o fluxo comum para executar cenários no Framework Nébula, com ou sem agentes.

Use este documento como base obrigatória antes de [Scenarios-Agents.md](Scenarios-Agents.md) ou [Scenarios-NoAgents.md](Scenarios-NoAgents.md).

## Objetivo

Padronizar a execução de cenários com o menor nível de repetição, mantendo rastreabilidade e qualidade.

## Regra de Ouro

1. Templates em `Templates/` são modelo.
2. Artefatos oficiais do projeto são editados em `Docs/`.
3. Protótipos HTML ficam em `Docs/Prototype/`.

## Estrutura comum de cenário

1. Contexto e gatilho
- O que motivou o cenário.

2. Objetivo e limite
- O que deve ser entregue e o que fica fora de escopo.

3. Entradas obrigatórias
- Workflow aplicável.
- Skills necessárias.
- Artefatos de Docs que serão editados.

4. Execução por etapas
- Planejar
- Executar
- Validar
- Encerrar

5. Evidências de saída
- Atualização em Docs.
- Evidências de qualidade.
- Registro de commit por task.

## Artefatos oficiais mínimos por cenário

1. Docs/plan.md
2. Docs/tasks.md
3. Docs/control.md
4. Docs/deploy.md quando houver entrega operacional

## Governança obrigatória

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Quality Gate obrigatório antes de fechar task.

## Card de cenário (template)

```md
# <Nome do cenário>

## Contexto
<resumo>

## Objetivo
<resultado esperado>

## Workflow
Workflows/<workflow>.md

## Skills
- Skills/<skill>.md

## Docs editados
- Docs/plan.md
- Docs/tasks.md
- Docs/control.md

## Etapas
1. Planejar
2. Executar
3. Validar
4. Encerrar

## Evidências
- Quality Gate aprovado
- hash do commit
- riscos e pendências
```

## Checklist de fechamento comum

1. Workflow correto foi aplicado.
2. Docs oficiais foram atualizados.
3. Quality Gate foi aprovado.
4. Commit da task foi registrado.
5. Riscos e pendências foram atualizados no control.

## Referências

1. [../Guide-Started.md](../Guide-Started.md)
2. [../Docs/README.md](../Docs/README.md)
3. [../Workflows/README.md](../Workflows/README.md)
4. [../Quality/validation-rules.md](../Quality/validation-rules.md)
