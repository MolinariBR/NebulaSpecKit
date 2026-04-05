# Deploy

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / revisando / aprovado]

**Documentos base:**  
[referência ao Docs/stack.md, Docs/architecture.md, Docs/structure.md e Docs/contract.yaml]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
[explique que este documento define a estratégia operacional e de entrega do projeto: hospedagem, infraestrutura, ambientes, qualidade de merge, CI/CD, versionamento, branches, release, logs, rollback e critérios de operação]

**O que este documento cobre:**  
- ambientes
- hospedagem
- infraestrutura
- capacidade inicial
- variáveis de ambiente
- segredos
- qualidade antes de merge
- CI/CD
- estratégia de branches
- versionamento
- release
- rollback
- logs e observabilidade
- operação mínima

**O que este documento não cobre:**  
- arquitetura detalhada de módulos
- contrato da API em profundidade
- estrutura de diretórios detalhada
- tasks específicas de implementação

---

## 3. Estratégia Operacional do Projeto

**Resumo operacional:**  
[descreva em poucas linhas como o projeto será hospedado, entregue e operado]

**Estratégia de hospedagem:**  
[VPS / cloud provider / PaaS / serverless / híbrido]

**Estratégia de operação inicial:**  
[simples, enxuta, baixo custo, manual assistida, automatizada, progressiva]

**Princípios operacionais:**  
- [ex.: simplicidade operacional]
- [ex.: previsibilidade]
- [ex.: baixo custo inicial]
- [ex.: facilidade de rollback]
- [ex.: visibilidade rápida de falhas]
- [ex.: automação progressiva]

---

## 4. Ambientes

**Ambientes previstos:**  
- local
- development
- staging
- production

### Local
**Objetivo:**  
[descreva]

**Responsabilidade:**  
[desenvolvimento individual]

**Características:**  
- execução local
- variáveis locais
- dependências simuladas ou reais, conforme necessidade

---

### Development
**Objetivo:**  
[descreva]

**Responsabilidade:**  
[validação contínua de desenvolvimento]

**Características:**  
- ambiente compartilhado ou não
- integração inicial
- testes internos

---

### Staging
**Objetivo:**  
[descreva]

**Responsabilidade:**  
[validação pré-produção]

**Características:**  
- comportamento o mais próximo possível de produção
- testes de smoke
- validação de release

---

### Production
**Objetivo:**  
[descreva]

**Responsabilidade:**  
[ambiente real do usuário]

**Características:**  
- estabilidade
- observabilidade
- controle de release
- rollback definido

---

## 5. Hospedagem e Infraestrutura

**Plataforma de hospedagem principal:**  
[ex.: Hostinger VPS / DigitalOcean / AWS / Railway / Vercel / outro]

**Modelo de hospedagem:**  
[VPS única / múltiplas instâncias / container / serverless / híbrido]

**Infraestrutura principal prevista:**  
- aplicação
- banco de dados
- proxy reverso
- storage
- cache
- fila
- worker
- CDN
- monitoramento
- [outros]

**Topologia inicial:**  
[descreva resumidamente como os serviços estarão distribuídos]

**Serviços gerenciados previstos:**  
- [serviço 1]
- [serviço 2]

**Serviços autogerenciados previstos:**  
- [serviço 1]
- [serviço 2]

---

## 6. Capacidade Inicial da Infra

### Aplicação principal
**CPU:**  
[preencher]

**Memória:**  
[preencher]

**Armazenamento:**  
[preencher]

**Banda / tráfego previsto:**  
[preencher]

**Concorrência esperada:**  
[preencher]

**Observações:**  
[preencher]

---

### Banco de dados
**CPU:**  
[preencher]

**Memória:**  
[preencher]

**Armazenamento:**  
[preencher]

**Estratégia de crescimento:**  
[preencher]

**Observações:**  
[preencher]

---

### Serviços auxiliares
**Cache:**  
[sim/não + capacidade prevista]

**Fila / worker:**  
[sim/não + capacidade prevista]

**Storage:**  
[sim/não + capacidade prevista]

**CDN:**  
[sim/não + observações]

---

## 7. Variáveis de Ambiente e Segredos

**Estratégia de configuração por ambiente:**  
[descreva]

**Onde as variáveis ficam armazenadas:**  
[ex.: GitHub Secrets / VPS env file / painel do provedor / vault / outro]

**Onde segredos não devem ficar:**  
- código-fonte
- arquivo versionado indevidamente
- documentação pública
- logs

**Categorias de variáveis:**  
- aplicação
- banco
- autenticação
- integrações externas
- observabilidade
- build/deploy

**Regras importantes:**  
- [regra 1]
- [regra 2]
- [regra 3]

---

## 8. Qualidade Antes do Merge e do Deploy

**Regras mínimas obrigatórias antes de mergear:**  
- lint sem erro
- testes obrigatórios passando
- build válido
- validação de contrato, quando aplicável
- revisão mínima definida

**Hooks locais previstos:**  
- `husky`
- `pre-commit`
- `pre-push`, se aplicável

**No pre-commit deve rodar:**  
- lint
- formatação, se aplicável
- checagens leves e rápidas
- validação de arquivos alterados

**No pre-push pode rodar:**  
- testes relevantes
- typecheck
- validações mais pesadas

**Ferramentas previstas:**  
- Husky
- lint-staged
- ESLint
- formatter
- typecheck
- testes automatizados

**Critérios de bloqueio de merge:**  
- falha em CI
- lint quebrado
- testes obrigatórios falhando
- build inválido
- quebra de contrato relevante
- falha de segurança crítica detectada, se houver scanner

---

## 9. Estratégia de Branches

**Branch principal:**  
`main`

**Branch de deploy / release:**  
[ex.: `staging` / `release` / `production` / `deploy`]

**Branches de feature / módulo / task:**  
[ex.: `feature/nome-da-feature`, `task/TASK-001-nome`, `module/pedidos`]

**Padrão de branches recomendado:**  
- `main` → fonte principal estável
- `[deploy-branch]` → branch de entrega para ambiente alvo
- `feature/...` → novas features
- `fix/...` → correções
- `hotfix/...` → correções urgentes
- `refactor/...` → refatorações
- `chore/...` → manutenção técnica
- `task/...` → implementação derivada de Docs/tasks.md

**Regras de uso:**  
- não desenvolver direto em `main`
- merges para `main` devem passar por validação
- deploy deve sair da branch definida para deploy
- hotfix deve ter rastreabilidade
- branches longas devem ser evitadas sem necessidade

---

## 10. Estratégia de CI/CD

**Plataforma de CI/CD:**  
[GitHub Actions]

**Objetivo do pipeline:**  
[validar, buildar, testar e publicar com segurança]

### Etapas mínimas de CI
- checkout
- setup do ambiente
- instalação de dependências
- lint
- typecheck
- testes
- build
- validações adicionais, se aplicável

### Etapas mínimas de CD
- autenticação no ambiente alvo
- preparação do artefato
- deploy
- migração, se aplicável
- health check
- validação pós-deploy

**Workflows previstos no GitHub Actions:**  
- CI em pull request
- CI em merge para branch principal
- Deploy para staging
- Deploy para produção
- Release tagging, se aplicável

**Gatilhos principais:**  
- pull request aberto/atualizado
- merge em branch específica
- tag de release
- dispatch manual, se necessário

**Critérios de bloqueio de deploy:**  
- CI falhou
- testes críticos falharam
- build falhou
- migração não validada
- health check pós-deploy falhou

---

## 11. Versionamento e Release

**Estratégia de versionamento:**  
[semver / simplificado / tag incremental]

**Formato de versão:**  
[ex.: `v1.0.0`]

**Quando gerar nova versão:**  
- release de produção
- milestone relevante
- hotfix publicado
- mudança significativa de contrato, se aplicável

**Estratégia de release:**  
- manual
- semiautomática
- automática
- por tag
- por branch
- por milestone

**Notas de release:**  
[sim/não + como devem ser feitas]

**Changelog:**  
[sim/não + onde fica]

**Responsável por aprovar release:**  
[preencher]

---

## 12. Logs e Observabilidade

**Estratégia de logs:**  
[descreva]

**Padrão esperado dos logs:**  
- estruturados
- consistentes
- legíveis
- parseáveis
- com contexto mínimo
- sem ruído excessivo

**Campos mínimos esperados em logs normalizados:**  
- timestamp
- nível
- serviço
- ambiente
- mensagem
- contexto
- requestId / correlationId, quando aplicável
- usuário / ator, quando aplicável e seguro
- módulo ou fluxo
- erro padronizado, quando houver

**Parser / padronização:**  
[descreva como os logs devem ser formatados para fácil leitura por Dev]

**Níveis de log:**  
- debug
- info
- warn
- error

**Onde os logs serão visíveis:**  
- terminal
- arquivos
- painel do provedor
- agregador externo
- ferramenta de monitoramento

**O que deve ser logado:**  
- inicialização
- falhas
- integrações externas
- ações críticas
- deploy
- migrações
- autenticação relevante, sem vazar segredos
- eventos importantes do domínio, quando fizer sentido

**O que não deve ser logado:**  
- segredos
- tokens
- senhas
- dados sensíveis desnecessários
- payload completo sem critério

---

## 13. Health Check, Readiness e Pós-Deploy

**Health check obrigatório:**  
[sim/não]

**Endpoint ou mecanismo de health check:**  
[descreva]

**Readiness check:**  
[sim/não + como funciona]

**Smoke tests pós-deploy:**  
- [teste 1]
- [teste 2]
- [teste 3]

**Checklist mínimo pós-deploy:**  
- aplicação sobe corretamente
- health check responde
- logs sem erro crítico inesperado
- endpoints críticos respondem
- autenticação funciona, se aplicável
- integração crítica responde, se aplicável

---

## 14. Banco, Migrações e Dados

**Banco principal:**  
[preencher]

**Estratégia de migração:**  
[manual / automatizada / validada em pipeline / etapa separada]

**Quando rodar migrações:**  
[descreva]

**Seed inicial:**  
[sim/não + como]

**Política de backup:**  
[descreva]

**Frequência de backup:**  
[preencher]

**Política de restauração:**  
[descreva]

**Cuidados importantes:**  
- validar migração antes de produção
- evitar migração destrutiva sem plano
- garantir rollback ou plano de contingência
- proteger dados sensíveis

---

## 15. Rollback e Contingência

**Estratégia de rollback:**  
[descreva]

**Quando rollback deve acontecer:**  
- falha crítica pós-deploy
- indisponibilidade
- quebra de fluxo principal
- aumento crítico de erros
- falha de migração sem recuperação rápida

**Como rollback será executado:**  
[descreva]

**Dependências críticas para rollback:**  
- artefato anterior
- versão anterior
- backup
- comando documentado
- acesso ao ambiente

**Plano de contingência quando rollback não for possível:**  
[descreva]

---

## 16. Segurança Operacional

**Regras mínimas de segurança operacional:**  
- acesso restrito aos ambientes
- segredos fora do código
- permissões mínimas necessárias
- logs sem vazamento sensível
- revisão antes de produção
- rastreabilidade de quem fez deploy

**Controle de acesso:**  
[descreva]

**Riscos operacionais conhecidos:**  
- [risco 1]
- [risco 2]

**Mitigações previstas:**  
- [mitigação 1]
- [mitigação 2]

---

## 17. Responsabilidades Operacionais

**Quem pode fazer deploy:**  
[preencher]

**Quem aprova release:**  
[preencher]

**Quem responde por incidente inicial:**  
[preencher]

**Quem mantém a infraestrutura:**  
[preencher]

**Observações:**  
[preencher]

---

## 18. Relação com Outros Documentos

### Docs/stack.md
[como a stack influencia hospedagem, pipeline e operação]

### Docs/architecture.md
[como a arquitetura impacta deploy, observabilidade e rollback]

### Docs/structure.md
[como a organização do repositório impacta CI/CD e build]

### Docs/contract.yaml
[como contratos podem ser validados no pipeline]

### Docs/plan.md / Docs/tasks.md
[como a estratégia operacional afeta ordem de entrega e tarefas técnicas]

---

## 19. Diretrizes de Implementação

**O que Dev e AI devem respeitar obrigatoriamente:**  
- [diretriz 1]
- [diretriz 2]
- [diretriz 3]

**O que deve ser evitado:**  
- deploy manual sem rastreio
- logs sem padronização
- merge sem validação mínima
- segredos versionados
- release sem rollback definido

**O que exige atualização deste documento:**  
- mudança de hospedagem
- mudança de infraestrutura
- mudança de pipeline
- mudança de estratégia de release
- mudança de branches
- mudança de observabilidade
- mudança de política de backup ou rollback

---

## 20. Síntese Operacional para Dev e AI

### 20.1 Hospedagem e infra
[resuma]

### 20.2 Pipeline e branches
[resuma]

### 20.3 Regras que não podem ser quebradas
- [regra 1]
- [regra 2]
- [regra 3]

### 20.4 Pontos críticos de operação
- [ponto 1]
- [ponto 2]
- [ponto 3]

### 20.5 O que ainda está indefinido
- [ponto 1]
- [ponto 2]

---

## 21. Aprovação

**Status de aprovação:**  
[pendente / aprovado / revisando]

**Aprovado por:**  
[preencher]

**Data de aprovação:**  
[dd/mm/aaaa]

**Observações finais:**  
[preencher]