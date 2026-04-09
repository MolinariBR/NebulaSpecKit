# Templates Full

Template set completo para planejamento, execução e governança de projeto.

## Objetivo

Garantir consistência entre projetos, separação clara de responsabilidades e rastreabilidade na execução, com baixa ambiguidade.

## Regra de uso

1. Arquivos em `Templates/Full/` são modelos.
2. Artefatos oficiais do projeto devem ser salvos em `Docs/`.
3. Protótipos HTML devem ser salvos em `Docs/Prototype/`.

## Leitura recomendada

1. `README.md` deste diretório
2. `Manual/18COMPONENTS-BASELINE.md`
3. `Manual/22COMPONENTS-TEMPLATES.md`

## Full vs Quick

Use Full quando:

- houver maior risco de ambiguidade
- existir integração relevante entre módulos
- o projeto exigir governança forte
- a documentação for base principal para Dev e AI

Use Quick quando:

- o escopo for pequeno e claro
- a velocidade for prioridade
- o risco de decisão errada for baixo

Se houver ambiguidade durante o uso de Quick, migrar para Full na mesma task.

## Ordem recomendada de criação

1. Usar `Templates/Full/brief.md` e salvar em `Docs/brief.md`
2. Usar `Templates/Full/project.md` e salvar em `Docs/project.md`
3. Usar `Templates/Full/stack.md` e salvar em `Docs/stack.md`
4. Usar `Templates/Full/user-stories.md` e salvar em `Docs/user-stories.md`
5. Usar `Templates/Full/pages.md` e salvar em `Docs/pages.md`
6. Usar `Templates/Full/flow.md` e salvar em `Docs/flow.md`
7. Protótipos HTML em `Docs/Prototype/`
8. Usar `Templates/Full/design-system.md` e salvar em `Docs/design-system.md`
9. Usar `Templates/Full/tokens.json` e salvar em `Docs/tokens.json`
10. Usar `Templates/Full/entities.md` e salvar em `Docs/entities.md`
11. Usar `Templates/Full/architecture.md` e salvar em `Docs/architecture.md`
12. Usar `Templates/Full/contract.yaml` e salvar em `Docs/contract.yaml`
13. Usar `Templates/Full/structure.md` e salvar em `Docs/structure.md`
14. Usar `Templates/Full/deploy.md` e salvar em `Docs/deploy.md`
15. Usar `Templates/Full/plan.md` e salvar em `Docs/plan.md`
16. Usar `Templates/Full/tasks.md` e salvar em `Docs/tasks.md`
17. Usar `Templates/Full/control.md` e salvar em `Docs/control.md`

## Referência de componentes

1. Baseline comum: `Manual/18COMPONENTS-BASELINE.md`.
2. Delta de templates: `Manual/22COMPONENTS-TEMPLATES.md`.

## Regras de preenchimento

1. Não preencher sem base documental.
2. Não duplicar conteúdo entre arquivos sem necessidade.
3. Não improvisar detalhes técnicos sem sustentação.
4. Marcar indefinições explicitamente.
5. Atualizar documentos quando a fonte de verdade mudar.
6. Manter os protótipos HTML em `Docs/Prototype/` coerentes com `Docs/pages.md` e `Docs/flow.md`.
7. Iniciar execução com task obrigatória de bootstrap estrutural para criar toda a árvore de diretórios e arquivos prevista.
8. Após o bootstrap, executar tarefas apenas em modo de edição de arquivos existentes.
9. Registrar 1 commit por task concluída, com hash e lista de arquivos tocados em `Docs/tasks.md`.
10. Encerrar toda task com Quality Gate aprovado conforme `Quality/validation-rules.md`.
11. Aplicar política anti-mock/stub/placeholder e testes realistas definidos na pasta `Quality/`.

## Critério de pronto do uso de template

1. Documento correspondente em `Docs/` atualizado.
2. Rastreabilidade registrada em `Docs/tasks.md` e `Docs/control.md`.
3. Quality Gate aprovado para a task.

## Regra de precedência

1. Contrato vigente
2. Documento-fonte do domínio
3. `Docs/plan.md` e `Docs/tasks.md`
4. Implementação atual

## Mapa de referência

1. Guia Full: `Templates/Full/README.md`.
2. Guia Quick: `Templates/Quick/README.md`.
