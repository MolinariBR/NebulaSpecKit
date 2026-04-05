# Create Agents Baseline

Este manual define o padrão comum para criar e usar agentes no framework Nébula, independente da ferramenta.

Use este documento como base obrigatória antes dos manuais 07 a 14.

## Objetivo

Padronizar a execução para evitar divergências entre ferramentas e manter o framework minimalista.

## Fonte Canônica

1. Agentes canônicos: [../agents](../agents)
2. Contrato dos agentes: [../agents/00README.md](../agents/00README.md)
3. Catálogo de papéis: [../agents/02CATALOG.md](../agents/02CATALOG.md)
4. Guia de uso: [../agents/01GUIDE.md](../agents/01GUIDE.md)

## Regra de Ouro

1. O diretório `agents/` é a única fonte de verdade dos papéis.
2. Integrações nativas de cada ferramenta são adaptadores de runtime.
3. Quando houver conflito, prevalece o contrato canonicamente versionado em `agents/`.

## Contexto obrigatório em toda chamada

1. Base:
   - GUIDE.md
   - Skills/01GUIDE.md
   - Workflows/01GUIDE.md
   - Quality/01GUIDE.md
   - Templates/Full/01GUIDE.md
2. Especialidade:
   - conforme o arquivo do agente em `agents/<role>-agent.md`
3. Execução (quando aplicável):
   - Docs/plan.md
   - Docs/tasks.md
   - Docs/control.md

## Governança Obrigatória

1. Bootstrap estrutural apenas na primeira task.
2. Após bootstrap, apenas edição de arquivos existentes.
3. Exatamente 1 commit por task concluída.
4. Quality Gate obrigatório antes de fechar task.

## Prompt Base Canônico

```text
Atue como <AgentName>.
Objetivo: <objetivo da task>
Workflow: Workflows/<workflow>.md

Carregue contexto base:
- GUIDE.md
- Skills/01GUIDE.md
- Workflows/01GUIDE.md
- Quality/01GUIDE.md
- Templates/Full/01GUIDE.md

Carregue contexto especializado conforme agents/<role>-agent.md.
Carregue contexto de execução em Docs/plan.md, Docs/tasks.md e Docs/control.md quando aplicável.

Aplique governança:
- bootstrap apenas na primeira task
- edit-only após bootstrap
- 1 commit por task
- Quality Gate obrigatório

Entregue:
1) plano
2) execução
3) evidências
4) riscos e pendências
```

## Checklist de validação comum

1. O agente correto foi invocado.
2. O contexto base foi carregado.
3. O contexto especializado foi carregado.
4. O contexto de execução em Docs foi considerado.
5. As quatro regras de governança foram aplicadas.
6. O output inclui plano, execução, evidências e pendências.

## Checklist de sincronização

Quando usar agentes nativos da ferramenta:

1. Atualizar o adaptador nativo da ferramenta.
2. Validar que o adaptador continua apontando para os arquivos canônicos.
3. Nunca duplicar regras longas em vários lugares se puder referenciar `agents/`.

## Erros comuns

1. Tratar adaptador nativo como fonte de verdade.
2. Invocar agente sem contexto base mínimo.
3. Fechar task sem Quality Gate.
4. Fazer implementação antes de editar Docs.

## Como usar com os manuais 07-14

1. Ler este manual primeiro.
2. Ler o manual da ferramenta alvo (07-14) apenas para o delta nativo.
3. Executar com o prompt base e ajustar somente o bloco nativo da ferramenta.
