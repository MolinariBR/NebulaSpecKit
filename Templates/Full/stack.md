# Stack

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / revisando / aprovado]

**Responsável pela definição técnica:**  
[preencher]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

**Documento base:**  
[referência ao Docs/project.md]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
[explique que este documento define a stack oficial do projeto, suas justificativas, restrições e diretrizes de uso]

**O que este documento cobre:**  
- linguagens
- frameworks
- banco de dados
- bibliotecas principais
- infraestrutura e serviços
- padrões técnicos
- critérios de escolha

**O que este documento não cobre:**  
- modelagem detalhada de entidades
- arquitetura completa de módulos
- endpoints da API
- tasks de implementação
- plano de execução

---

## 3. Contexto Técnico do Projeto

**Resumo técnico do projeto:**  
[explique o tipo de sistema que será construído]

**Natureza do projeto:**  
[web app / backend api / painel admin / app híbrido / microserviço / automação / sistema interno / SaaS / marketplace / outro]

**Tipo de operação esperada:**  
[baixa escala / média escala / alta escala / uso interno / uso público / tempo real / processamento assíncrono / transacional / analítico]

**Plataformas-alvo:**  
- [web]
- [mobile]
- [api]
- [admin]
- [worker]
- [cli]
- [outro]

**Contexto que influencia a stack:**  
- [restrição de prazo]
- [restrição de equipe]
- [restrição de custo]
- [experiência do time]
- [necessidade de velocidade]
- [necessidade de escala]
- [legado existente]

---

## 4. Princípios de Escolha da Stack

**Princípios que guiam as decisões técnicas:**  
- [ex.: simplicidade operacional]
- [ex.: rapidez de desenvolvimento]
- [ex.: baixo custo inicial]
- [ex.: facilidade de manutenção]
- [ex.: escalabilidade progressiva]
- [ex.: boa experiência do desenvolvedor]
- [ex.: forte ecossistema]
- [ex.: aderência ao conhecimento do time]

**O que tem prioridade maior nas escolhas:**  
[descreva]

**O que será evitado tecnicamente:**  
- [complexidade desnecessária]
- [dependência excessiva de serviços difíceis de operar]
- [stack desalinhada com a equipe]
- [ferramentas imaturas]
- [overengineering]

---

## 5. Stack Oficial

### 5.1 Linguagens
- **Principal:** [ex.: TypeScript]
- **Secundárias:** [ex.: SQL, Bash]

**Justificativa:**  
[por que essas linguagens foram escolhidas]

---

### 5.2 Frontend
**Framework principal:**  
[ex.: Next.js]

**Bibliotecas principais:**  
- [ex.: React]
- [ex.: TanStack Query]
- [ex.: Zod]
- [ex.: React Hook Form]

**Estratégia de UI:**  
[SSR / CSR / híbrido / componentes reutilizáveis / design system próprio / etc.]

**Justificativa:**  
[explique]

---

### 5.3 Backend
**Framework principal:**  
[ex.: Node.js + NestJS / Fastify / Express]

**Responsabilidades do backend:**  
- [autenticação]
- [regras de negócio]
- [integrações]
- [persistência]
- [fila]
- [arquivos]
- [notificações]

**Justificativa:**  
[explique]

---

### 5.4 Banco de Dados
**Banco principal:**  
[ex.: PostgreSQL]

**Bancos auxiliares, se houver:**  
- [Redis]
- [Elastic]
- [outro]

**ORM / Query Builder:**  
[ex.: Prisma / Drizzle / Knex / SQL puro]

**Justificativa:**  
[explique]

---

### 5.5 Infraestrutura e Hospedagem
**Ambiente principal:**  
[ex.: VPS / Docker / Vercel / Railway / AWS / GCP / Azure]

**Serviços previstos:**  
- [app]
- [banco]
- [cache]
- [fila]
- [storage]
- [cdn]
- [proxy]
- [monitoramento]

**Justificativa:**  
[explique]

---

### 5.6 Autenticação e Autorização
**Estratégia escolhida:**  
[JWT / sessão / OAuth / auth provider / RBAC / ACL / etc.]

**Justificativa:**  
[explique]

---

### 5.7 Comunicação e API
**Padrão principal:**  
[REST / GraphQL / RPC / WebSocket / eventos]

**Formato de contrato:**  
[OpenAPI / Contract-first / code-first / híbrido]

**Justificativa:**  
[explique]

---

### 5.8 Testes
**Ferramentas principais:**  
- [ex.: Vitest / Jest]
- [ex.: Playwright / Cypress]
- [ex.: Supertest]

**Estratégia de testes:**  
[unitário / integração / contrato / e2e]

**Justificativa:**  
[explique]

---

### 5.9 Observabilidade e Logs
**Estratégia inicial:**  
- [logs estruturados]
- [monitoramento]
- [alertas]
- [health checks]
- [rastreamento]

**Ferramentas previstas:**  
- [ferramenta 1]
- [ferramenta 2]

**Justificativa:**  
[explique]

---

### 5.10 Dev Experience e Qualidade
**Ferramentas de qualidade e produtividade:**  
- [ESLint]
- [Prettier]
- [TypeScript strict]
- [Husky]
- [lint-staged]
- [commitlint]
- [turbo / nx / pnpm workspace / etc.]

**Justificativa:**  
[explique]

---

## 6. Decisões Técnicas Estruturais

**Padrões técnicos adotados:**  
- [ex.: tipagem forte]
- [ex.: validação de entrada]
- [ex.: separação entre domínio e infraestrutura]
- [ex.: componentes reutilizáveis]
- [ex.: contratos centralizados]
- [ex.: tratamento padronizado de erro]
- [ex.: logs estruturados]
- [ex.: configuração por ambiente]

**Convenções obrigatórias:**  
- [convenção 1]
- [convenção 2]
- [convenção 3]

**Diretrizes de código relevantes:**  
- [diretriz 1]
- [diretriz 2]
- [diretriz 3]

---

## 7. Alternativas Consideradas

### Alternativa 1
**Opção avaliada:**  
[preencher]

**Vantagens percebidas:**  
- [vantagem 1]
- [vantagem 2]

**Desvantagens percebidas:**  
- [desvantagem 1]
- [desvantagem 2]

**Motivo de não adoção:**  
[explique]

### Alternativa 2
**Opção avaliada:**  
[preencher]

**Vantagens percebidas:**  
- [vantagem 1]
- [vantagem 2]

**Desvantagens percebidas:**  
- [desvantagem 1]
- [desvantagem 2]

**Motivo de não adoção:**  
[explique]

---

## 8. Restrições Técnicas

**Restrições que impactaram a stack:**  
- [restrição 1]
- [restrição 2]
- [restrição 3]

**Limitações assumidas conscientemente:**  
- [limitação 1]
- [limitação 2]

**Riscos técnicos da stack escolhida:**  
- [risco 1]
- [risco 2]

**Mitigações iniciais:**  
- [mitigação 1]
- [mitigação 2]

---

## 9. Dependências Principais

**Dependências críticas do projeto:**  
- [dependência 1]
- [dependência 2]
- [dependência 3]

**Serviços externos previstos:**  
- [serviço 1]
- [serviço 2]

**Dependências com maior risco operacional:**  
- [dependência 1]
- [dependência 2]

---

## 10. Estratégia Inicial de Ambientes

**Ambientes previstos:**  
- [local]
- [dev]
- [staging]
- [prod]

**Diferenças relevantes entre ambientes:**  
[descreva]

**Diretriz para configuração por ambiente:**  
[descreva]

---

## 11. Diretrizes para os Próximos Documentos

### 11.1 Para o Docs/architecture.md
[quais decisões de stack impactam a arquitetura]

### 11.2 Para o Docs/entities.md
[restrições e expectativas sobre persistência e modelagem]

### 11.3 Para o Docs/contract.yaml
[padrões técnicos que devem ser refletidos no contrato]

### 11.4 Para o Docs/structure.md
[organização de pastas e camadas influenciada pela stack]

### 11.5 Para o Docs/deploy.md
[restrições e necessidades operacionais da stack]

### 11.6 Para o Docs/plan.md
[impactos da stack na ordem de execução]

### 11.7 Para o Docs/tasks.md
[áreas técnicas que devem virar tarefas logo no início]

---

## 12. Síntese Operacional para Dev e AI

### 12.1 Stack oficial resumida
- **Frontend:** [preencher]
- **Backend:** [preencher]
- **Banco:** [preencher]
- **Infraestrutura:** [preencher]
- **Testes:** [preencher]

### 12.2 O que motivou essa stack
- [motivo 1]
- [motivo 2]
- [motivo 3]

### 12.3 O que deve ser respeitado na implementação
- [regra 1]
- [regra 2]
- [regra 3]

### 12.4 O que deve ser evitado
- [erro 1]
- [erro 2]

### 12.5 O que ainda pode mudar
- [ponto 1]
- [ponto 2]

---

## 13. Aprovação

**Status de aprovação:**  
[pendente / aprovado / revisando]

**Aprovado por:**  
[preencher]

**Data de aprovação:**  
[dd/mm/aaaa]

**Observações finais:**  
[preencher]