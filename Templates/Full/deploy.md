# Deploy
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão do documento:** [v1, v2, etc.]
- **Status:** [rascunho / revisando / aprovado]
- **Documentos base:**
  `Docs/stack.md` · `Docs/architecture.md` · `Docs/structure.md`· `Docs/contract.yaml`
- **Data de criação:** [dd/mm/aaaa]
- **Última atualização:** [dd/mm/aaaa]
## 2. Objetivo do Documento
- **Finalidade:**
  definir estratégia operacional e de entrega: hospedagem, infra, ambientes,
  qualidade de merge, CI/CD, versionamento, branches, release, rollback e logs
- **Cobre:**
  ambientes · hospedagem · infraestrutura · capacidade inicial · variáveis ·
  segredos · qualidade pré-merge · CI/CD · branches · versionamento · release ·
  rollback · logs/observabilidade · operação mínima
- **Não cobre:**
  arquitetura detalhada de módulos · contrato de API em profundidade ·
  estrutura detalhada de diretórios · tasks específicas de implementação
## 3. Estratégia Operacional do Projeto
- **Resumo operacional:** [como será hospedado, entregue e operado]
- **Estratégia de hospedagem:** [VPS / cloud provider / PaaS / serverless / híbrido]
- **Estratégia operacional inicial:**
  [simples / enxuta / baixo custo / manual assistida / automatizada / progressiva]
- **Princípios operacionais:**
  simplicidade · previsibilidade · baixo custo inicial · rollback fácil ·
  visibilidade rápida de falhas · automação progressiva
## 4. Ambientes
- **Ambientes previstos:** local · development · staging · production
### Local
- **Objetivo:** [descreva]
- **Responsabilidade:** [desenvolvimento individual]
- **Características:** execução local · variáveis locais · deps sob demanda
### Development
- **Objetivo:** [descreva]
- **Responsabilidade:** [validação contínua de desenvolvimento]
- **Características:** compartilhado ou não · integração inicial · testes internos
### Staging
- **Objetivo:** [descreva]
- **Responsabilidade:** [validação pré-produção]
- **Características:** próximo de produção · smoke tests · validação de release
### Production
- **Objetivo:** [descreva]
- **Responsabilidade:** [ambiente real do usuário]
- **Características:** estabilidade · observabilidade · release controlado · rollback
## 5. Hospedagem e Infraestrutura
- **Plataforma principal:**
  [Hostinger VPS / DigitalOcean / AWS / Railway / Vercel / outro]
- **Modelo de hospedagem:** [VPS única / múltiplas instâncias / container / híbrido]
- **Infra:** aplicação · banco · proxy reverso · storage · cache · fila ·
  worker · CDN · monitoramento · outros
- **Topologia inicial:** [como os serviços estarão distribuídos]
- **Serviços gerenciados:** [serviço 1] · [serviço 2]
- **Serviços autogerenciados:** [serviço 1] · [serviço 2]
## 6. Capacidade Inicial da Infra
### Aplicação principal
- **CPU:** [preencher]
- **Memória:** [preencher]
- **Armazenamento:** [preencher]
- **Banda/tráfego previsto:** [preencher]
- **Concorrência esperada:** [preencher]
- **Observações:** [preencher]
### Banco de dados
- **CPU:** [preencher]
- **Memória:** [preencher]
- **Armazenamento:** [preencher]
- **Estratégia de crescimento:** [preencher]
- **Observações:** [preencher]
### Serviços auxiliares
- **Cache:** [sim/não + capacidade]
- **Fila/worker:** [sim/não + capacidade]
- **Storage:** [sim/não + capacidade]
- **CDN:** [sim/não + observações]
## 7. Variáveis de Ambiente e Segredos
- **Estratégia de configuração por ambiente:** [descreva]
- **Onde variáveis ficam:** [GitHub Secrets / env file / painel / vault / outro]
- **Onde segredos não devem ficar:** código-fonte · arquivo versionado ·
  documentação pública · logs
- **Categorias:** aplicação · banco · autenticação · integrações ·
  observabilidade · build/deploy
- **Regras importantes:** [regra 1] · [regra 2] · [regra 3]
## 8. Qualidade Antes do Merge e do Deploy
- **Mínimo obrigatório pré-merge:** lint ok · testes obrigatórios ok · build ok ·
  validação de contrato quando aplicável · revisão mínima definida
- **Hooks locais previstos:** `husky` · `pre-commit` · `pre-push` (se aplicável)
- **No pre-commit:** lint · formatação quando aplicável · checks leves ·
  validação dos arquivos alterados
- **No pre-push:** testes relevantes · typecheck · validações mais pesadas
- **Ferramentas previstas:** Husky · lint-staged · ESLint · formatter · typecheck ·
  testes automatizados
- **Bloqueio de merge:** falha em CI/lint/testes/build/contrato relevante/segurança
## 9. Estratégia de Branches
- **Branch principal:** `main`
- **Branch de deploy/release:** [`staging` / `release` / `production` / `deploy`]
- **Branches de feature/módulo/task:**
  [`feature/...` / `task/TASK-001-...` / `module/...`]
- **Padrão recomendado:** `main` estável · `[deploy-branch]` entrega alvo ·
  `feature/...` · `fix/...` · `hotfix/...` · `refactor/...` · `chore/...` ·
  `task/...`
- **Regras de uso:** sem desenvolvimento direto em `main` · merge validado ·
  deploy pela branch definida · hotfix rastreável · evitar branches longas
## 10. Estratégia de CI/CD
- **Plataforma:** [GitHub Actions]
- **Objetivo do pipeline:** [validar, buildar, testar e publicar com segurança]
- **Etapas mínimas de CI:** checkout · setup ambiente · dependências · lint ·
  typecheck · testes · build · validações extras quando aplicável
- **Etapas mínimas de CD:** autenticação alvo · artefato · deploy · migração ·
  health check · validação pós-deploy
- **Workflows previstos:** CI em PR · CI em merge principal · deploy staging ·
  deploy produção · release tagging quando aplicável
- **Gatilhos:** PR aberto/atualizado · merge em branch específica · tag de release ·
  dispatch manual
- **Bloqueio de deploy:** falha em CI/teste/build/migração/health check
## 11. Versionamento e Release
- **Estratégia de versionamento:** [semver / simplificado / tag incremental]
- **Formato da versão:** [ex.: `v1.0.0`]
- **Quando gerar versão:** release de produção · milestone relevante ·
  hotfix publicado · mudança significativa de contrato quando aplicável
- **Estratégia de release:** manual · semiautomática · automática · por tag ·
  por branch · por milestone
- **Notas de release:** [sim/não + como]
- **Changelog:** [sim/não + onde fica]
- **Responsável por aprovar release:** [preencher]
## 12. Logs e Observabilidade
- **Estratégia de logs:** [descreva]
- **Padrão esperado:** estruturados · consistentes · legíveis · parseáveis ·
  contexto mínimo · baixo ruído
- **Campos mínimos:** timestamp · nível · serviço · ambiente · mensagem ·
  contexto · requestId/correlationId quando aplicável · ator quando seguro ·
  módulo/fluxo · erro padronizado
- **Parser/padronização:** [como formatar para leitura por Dev]
- **Níveis:** debug · info · warn · error
- **Onde logs serão visíveis:** terminal · arquivos · painel do provedor ·
  agregador externo · monitoramento
- **Deve ser logado:** inicialização · falhas · integrações · ações críticas ·
  deploy · migrações · autenticação relevante · eventos importantes do domínio
- **Não logar:** segredos · tokens · senhas · dados sensíveis sem critério
## 13. Health Check, Readiness e Pós-Deploy
- **Health check obrigatório:** [sim/não]
- **Endpoint ou mecanismo de health check:** [descreva]
- **Readiness check:** [sim/não + como funciona]
- **Smoke tests pós-deploy:** [teste 1] · [teste 2] · [teste 3]
- **Checklist pós-deploy:** app sobe · health responde · logs sem erro crítico ·
  endpoints críticos respondem · auth ok quando aplicável · integração crítica ok
## 14. Banco, Migrações e Dados
- **Banco principal:** [preencher]
- **Estratégia de migração:** [manual / automatizada / pipeline / etapa separada]
- **Quando rodar migrações:** [descreva]
- **Seed inicial:** [sim/não + como]
- **Política de backup:** [descreva]
- **Frequência de backup:** [preencher]
- **Política de restauração:** [descreva]
- **Cuidados importantes:** validar migração pré-produção · evitar destrutiva sem
  plano · garantir rollback/contingência · proteger dados sensíveis
## 15. Rollback e Contingência
- **Estratégia de rollback:** [descreva]
- **Quando rollback deve acontecer:** falha crítica pós-deploy · indisponibilidade ·
  quebra de fluxo principal · aumento crítico de erros · falha de migração
- **Como rollback será executado:** [descreva]
- **Dependências críticas:** artefato anterior · versão anterior · backup ·
  comando documentado · acesso ao ambiente
- **Plano de contingência sem rollback:** [descreva]
## 16. Segurança Operacional
- **Regras:** acesso restrito · segredos fora do código · permissões mínimas ·
  logs sem vazamento · revisão antes de produção · rastreabilidade de deploy
- **Controle de acesso:** [descreva]
- **Riscos operacionais conhecidos:** [risco 1] · [risco 2]
- **Mitigações previstas:** [mitigação 1] · [mitigação 2]
## 17. Responsabilidades Operacionais
- **Quem pode fazer deploy:** [preencher]
- **Quem aprova release:** [preencher]
- **Quem responde por incidente inicial:** [preencher]
- **Quem mantém a infraestrutura:** [preencher]
- **Observações:** [preencher]
## 18. Relação com Outros Documentos
- **`Docs/stack.md`:** [como stack influencia hospedagem, pipeline e operação]
- **`Docs/architecture.md`:** [como arquitetura impacta deploy e rollback]
- **`Docs/structure.md`:** [como repositório impacta CI/CD e build]
- **`Docs/contract.yaml`:** [como contratos podem ser validados no pipeline]
- **`Docs/plan.md` / `Docs/tasks.md`:**
  [como estratégia operacional afeta ordem de entrega e tarefas técnicas]
## 19. Diretrizes de Implementação
- **Dev e AI devem respeitar obrigatoriamente:**
  [diretriz 1] · [diretriz 2] · [diretriz 3]
- **Deve ser evitado:** deploy manual sem rastreio · logs sem padrão · merge sem
  validação mínima · segredos versionados · release sem rollback definido
- **Exige atualização deste documento:** mudança de hospedagem · infraestrutura ·
  pipeline · estratégia de release · branches · observabilidade · backup/rollback
## 20. Síntese Operacional para Dev e AI
- **20.1 Hospedagem e infra:** [resuma]
- **20.2 Pipeline e branches:** [resuma]
- **20.3 Regras que não podem ser quebradas:** [regra 1] · [regra 2] · [regra 3]
- **20.4 Pontos críticos de operação:** [ponto 1] · [ponto 2] · [ponto 3]
- **20.5 O que ainda está indefinido:** [ponto 1] · [ponto 2]
## 21. Aprovação
- **Status de aprovação:** [pendente / aprovado / revisando]
- **Aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
