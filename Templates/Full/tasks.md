# Tasks

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / ativo / revisando / estabilização / concluído]

**Documentos base:**  
[referência ao Docs/plan.md, Docs/project.md, Docs/contract.yaml, Docs/architecture.md, Docs/deploy.md]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
Este documento organiza a execução do projeto em fases, módulos, tarefas, sub-tarefas, metas e critérios de aceite, permitindo rastreabilidade, implementação modular, testes, CI/CD, deploy, release e acompanhamento operacional por Dev e AI.

**Estrutura adotada:**  
- Fase
- Módulo
- Tarefa
- Sub-tarefa
- Meta
- Critério de aceite

**Regra de marcação:**  
- `( )` não concluído
- `(x)` concluído

---

## 3. Regras Gerais

- Toda tarefa deve pertencer a uma fase.
- Toda tarefa deve pertencer a um módulo ou frente de entrega.
- Toda tarefa deve ter pelo menos uma meta.
- Toda tarefa deve ter critério de aceite.
- Sempre que fizer sentido, testes devem existir como sub-tarefa.
- CI/CD, deploy, release e observabilidade podem existir como módulos próprios.
- Mudanças estruturais relevantes devem refletir o Docs/plan.md.
- O andamento consolidado deve ser refletido no Docs/control.md.
- A primeira task de execução deve ter política `bootstrap_estrutural`.
- Apenas task com política `bootstrap_estrutural` pode criar diretórios e arquivos.
- Tasks com política `edição` devem apenas editar arquivos já existentes.
- Cada task concluída deve gerar exatamente 1 commit.
- Toda task deve registrar hash do commit e lista de arquivos tocados.
- Toda task deve registrar status do Quality Gate e evidências de validação.
- Testes devem seguir a política de fidelidade realista definida em Quality/validation-rules.md.
- Mock, stub e placeholder são proibidos por padrão, conforme Quality/validation-rules.md.

---

## 4. Bloco obrigatório de qualidade por task

Cada task deve conter os campos abaixo, preenchidos conforme [Quality/gate-evidence.md](../Quality/gate-evidence.md):

- `Quality Gate`: aprovado ou reprovado.
- `Evidências de qualidade`: formato canônico por tipo — lint, typecheck, build, testes, contrato de API, e2e, mobile, lockfile e rastreabilidade.
  - Campos não aplicáveis devem ser marcados como `N/A` com justificativa objetiva.
  - Critério de aplicabilidade por ferramenta está definido em `Quality/gate-evidence.md`.
  - Campos aplicáveis sem evidência registrada são bloqueadores de fechamento.

---

## 5. Estrutura das Fases

# FASE 01 — Fundação Estrutural

## MÓDULO: Base do Projeto

### TASK-001 — Inicializar base do repositório
**Tipo:** estrutura  
**Prioridade:** alta  
**Milestone:** M1  
**Dependências:** nenhuma
**Política de alteração:** bootstrap_estrutural  
**Permite criar diretórios/arquivos:** sim  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Repositório com estrutura inicial coerente com Docs/structure.md
- ( ) Configuração base pronta para desenvolvimento

**Sub-tarefas:**
- ( ) Criar estrutura inicial de diretórios
- ( ) Configurar package manager e workspace, se aplicável
- ( ) Configurar arquivos base do projeto
- ( ) Validar convenções iniciais

**Critérios de aceite:**
- ( ) Estrutura inicial criada conforme Docs/structure.md
- ( ) Projeto instala dependências sem erro
- ( ) Organização inicial está coerente com Docs/architecture.md

**Observações:**
[preencher]

---

### TASK-002 — Configurar qualidade local
**Tipo:** ci_cd  
**Prioridade:** alta  
**Milestone:** M1  
**Dependências:** TASK-001
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Fluxo local mínimo de qualidade definido
- ( ) Commits protegidos contra erro básico

**Sub-tarefas:**
- ( ) Configurar Husky
- ( ) Configurar pre-commit
- ( ) Configurar lint
- ( ) Configurar formatter, se aplicável
- ( ) Configurar typecheck, se aplicável
- ( ) Validar execução local

**Critérios de aceite:**
- ( ) Pre-commit executa checagens mínimas
- ( ) Lint falha corretamente quando há erro
- ( ) Ferramentas de qualidade funcionam localmente

**Observações:**
[preencher]

---

## MÓDULO: CI/CD e Versionamento

### TASK-003 — Configurar CI de pull request
**Tipo:** ci_cd  
**Prioridade:** alta  
**Milestone:** M1  
**Dependências:** TASK-002
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Pull requests validados automaticamente
- ( ) Quebras básicas impedem merge

**Sub-tarefas:**
- ( ) Editar arquivo de workflow de GitHub Actions para PR
- ( ) Rodar instalação de dependências
- ( ) Rodar lint
- ( ) Rodar testes definidos
- ( ) Rodar build
- ( ) Validar status do workflow

**Critérios de aceite:**
- ( ) PR dispara pipeline automaticamente
- ( ) Pipeline falha quando lint, teste ou build falham
- ( ) Pipeline passa quando validações mínimas são atendidas

**Observações:**
[preencher]

---

### TASK-004 — Definir estratégia de branches
**Tipo:** versionamento  
**Prioridade:** alta  
**Milestone:** M1  
**Dependências:** nenhuma
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Fluxo de branches formalizado e aplicável ao projeto

**Sub-tarefas:**
- ( ) Definir branch `main`
- ( ) Definir branch `deploy`
- ( ) Definir padrão `feature/*`
- ( ) Definir padrão `task/*`
- ( ) Definir padrão `hotfix/*`
- ( ) Definir regras de merge

**Critérios de aceite:**
- ( ) Estratégia de branches documentada em Docs/deploy.md
- ( ) Convenção pode ser seguida sem ambiguidade

**Observações:**
[preencher]

---

# FASE 02 — Contratos e Base Funcional

## MÓDULO: Core do Produto

### TASK-005 — Implementar caso de uso principal
**Tipo:** implementação  
**Prioridade:** alta  
**Milestone:** M2  
**Dependências:** TASK-003, TASK-004
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Fluxo principal do produto esta operacional
- ( ) Caso de uso critico esta validado ponta a ponta

**Sub-tarefas:**
- ( ) Implementar contrato do caso de uso principal
- ( ) Implementar endpoint principal
- ( ) Implementar validações de entrada
- ( ) Implementar tela/fluxo principal
- ( ) Implementar tratamento de erro
- ( ) Implementar persistencia e recuperacao de estado, se aplicável
- ( ) Editar arquivos de testes unitários
- ( ) Editar arquivos de testes de integração
- ( ) Validar fluxo manualmente

**Critérios de aceite:**
- ( ) Fluxo principal executa com dados validos
- ( ) Entrada invalida retorna erro consistente
- ( ) Fluxo respeita Docs/contract.yaml
- ( ) Testes principais passam

**Observações:**
[preencher]

---

## MÓDULO: Testes

### TASK-006 — Consolidar base de testes do módulo core
**Tipo:** testes  
**Prioridade:** alta  
**Milestone:** M2  
**Dependências:** TASK-005
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Cobertura mínima do módulo definida
- ( ) Regressão básica protegida

**Sub-tarefas:**
- ( ) Revisar cenários críticos
- ( ) Adicionar testes faltantes
- ( ) Validar cenários de erro
- ( ) Validar cenários de sessão expirada, se aplicável

**Critérios de aceite:**
- ( ) Fluxos críticos do módulo possuem testes
- ( ) Erros relevantes estão cobertos

**Observações:**
[preencher]

---

# FASE 03 — MVP Operacional

## MÓDULO: Deploy e Release

### TASK-007 — Configurar deploy automatizado para branch deploy
**Tipo:** deploy  
**Prioridade:** alta  
**Milestone:** M2  
**Dependências:** TASK-003, TASK-004
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Build e deploy realizados via pipeline
- ( ) VPS não depende de ajustes manuais hardcoded

**Sub-tarefas:**
- ( ) Editar workflow para branch `deploy`
- ( ) Preparar build do projeto
- ( ) Publicar artefato no ambiente alvo
- ( ) Configurar variáveis e segredos no ambiente correto
- ( ) Executar restart seguro da aplicação
- ( ) Validar health check pós-deploy
- ( ) Validar logs pós-deploy

**Critérios de aceite:**
- ( ) Push ou merge na branch `deploy` dispara pipeline
- ( ) Aplicação sobe corretamente no ambiente alvo
- ( ) Deploy não exige intervenção manual hardcoded na VPS
- ( ) Logs e health check validam a publicação

**Observações:**
[preencher]

---

### TASK-008 — Configurar release de app mobile
**Tipo:** release  
**Prioridade:** média  
**Milestone:** M2  
**Dependências:** TASK-003, TASK-004
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Release mobile padronizada via GitHub

**Sub-tarefas:**
- ( ) Definir estratégia de build mobile
- ( ) Definir estratégia de versionamento
- ( ) Configurar workflow de release
- ( ) Gerar artefato de release
- ( ) Publicar release no GitHub
- ( ) Validar rastreabilidade da versão

**Critérios de aceite:**
- ( ) Release mobile pode ser gerada de forma reprodutível
- ( ) Versionamento está coerente com Docs/deploy.md
- ( ) Artefato publicado pode ser rastreado

**Observações:**
[preencher]

---

# FASE 04 — Validação, Release e Estabilização

## MÓDULO: Estabilização Operacional

### TASK-009 — Executar rodada final de validação realista
**Tipo:** validação  
**Prioridade:** alta  
**Milestone:** M3  
**Dependências:** TASK-007, TASK-008
**Política de alteração:** edição  
**Permite criar diretórios/arquivos:** não  
**Commit da task:** [preencher após concluir]  
**Arquivos tocados:** [listar caminhos alterados]
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:** [preencher conforme Quality/gate-evidence.md]

**Meta(s):**
- ( ) Garantir fidelidade de execução próxima ao ambiente de produção
- ( ) Validar fluxos críticos com evidências reprodutiveis

**Sub-tarefas:**
- ( ) Executar testes de integração com Testcontainers
- ( ) Executar testes de contrato com curl/scripts
- ( ) Executar e2e de interface para fluxos críticos
- ( ) Executar validação mobile (BrowserStack/alternativa/dispositivo físico)
- ( ) Consolidar evidências e resultados no Docs/control.md

**Critérios de aceite:**
- ( ) Testes críticos executados sem bloqueio grave
- ( ) Evidências de validação registradas e rastreaveis
- ( ) Quality Gate aprovado para encerramento da fase

**Observações:**
[preencher]

---

## 6. Resumo por Fase

### FASE 01 — Fundação Estrutural
- ( ) concluída

### FASE 02 — Base Funcional
- ( ) concluída

### FASE 03 — MVP Operacional
- ( ) concluída

### FASE 04 — Validação, Release e Estabilização
- ( ) concluída

---

## 7. Resumo por Milestone

### M1
- ( ) concluído

### M2
- ( ) concluído

### M3
- ( ) concluído

---

## 8. Diretrizes de Uso

- Tasks devem ser pequenas o suficiente para execução clara.
- Sub-tarefas devem representar passos reais de implementação.
- Testes devem aparecer como sub-tarefa ou task própria.
- CI/CD, versionamento, deploy e release devem ser rastreados como trabalho real.
- Toda task deve poder ser lida e executada por Dev ou AI sem depender de contexto implícito.
- Quando a ordem macro mudar, revisar o Docs/plan.md.
- Quando o status operacional mudar, refletir em Docs/control.md.

---

## 9. Síntese Operacional para Dev e AI

**O que este arquivo organiza:**  
- fases
- módulos
- tarefas
- sub-tarefas
- metas
- critérios de aceite

**Como interpretar:**  
- fase = contexto macro
- módulo = frente de implementação
- task = entrega concreta
- sub-tarefa = passo executável
- meta = resultado esperado
- critério = prova de conclusão

**O que precisa ser respeitado:**  
- modularidade
- rastreabilidade
- vínculo com milestone
- critérios verificáveis
- compatibilidade com testes, CI/CD, deploy e release