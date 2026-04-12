# Entidades
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão do documento:** [v1, v2, etc.]
- **Status:** [rascunho / revisando / aprovado]
- **Documentos base:**
  `Docs/project.md` · `Docs/user-stories.md` · `Docs/pages.md` · `Docs/flow.md`
- **Data de criação:** [dd/mm/aaaa]
- **Última atualização:** [dd/mm/aaaa]
---
## 2. Objetivo do Documento
- **Finalidade:**
  definir o modelo de domínio: entidades, atributos, relações, regras, estados e
  validações que sustentam o sistema
- **Cobre:**
  entidades · significado · atributos/tipos · identificadores · regras ·
  validações · relacionamentos · estados/ciclo de vida · dependências conceituais
- **Não cobre:**
  SQL final · migrations · ORM · contrato detalhado de API ·
  arquitetura de módulos em profundidade
---
## 3. Regras Gerais de Modelagem
- **Princípios:**
  modelar domínio antes da estrutura técnica · evitar duplicidade conceitual ·
  nomear entidades com clareza · separar apoio de entidade central ·
  refletir regras reais de negócio
- **Convenções gerais:**
  nomes no singular · atributos claros · identificadores explícitos ·
  estados relevantes · relações legíveis
- **Diretriz importante:**
  [como Dev e AI devem interpretar o documento antes de modelar banco/contrato]
---
## 4. Visão Geral do Domínio
- **Resumo do domínio:** [descreva em poucas linhas]
- **Entidades centrais:** [entidade 1] · [entidade 2] · [entidade 3]
- **Entidades auxiliares:** [entidade 1] · [entidade 2]
- **Observações gerais:** [preencher]
---
## 5. Entidades do Projeto
### ENT-001 — [nome da entidade]
- **Nome:** [preencher]
- **Descrição:** [o que representa]
- **Tipo:** [central / apoio / associação / configuração / evento / histórico]
- **Responsabilidade:** [papel no domínio]
- **Origem funcional:** [histórias, páginas ou fluxos]
- **Identificador principal:** `id` — [tipo lógico]
- **Atributos:**
  `id`: [tipo] — [descrição] · `name`: [tipo] — [descrição] ·
  `status`: [tipo] — [descrição] · `createdAt`: [tipo] — [descrição] ·
  `updatedAt`: [tipo] — [descrição]
- **Atributos obrigatórios:** [atributo 1] · [atributo 2]
- **Atributos opcionais:** [atributo 1] · [atributo 2]
- **Regras de validação:** [regra 1] · [regra 2] · [regra 3]
- **Regras de negócio:** [regra 1] · [regra 2]
- **Estados possíveis:** [estado 1] · [estado 2] · [estado 3]
- **Transições relevantes:** [transição 1] · [transição 2]
- **Relacionamentos:**
  pertence a [entidade] · possui muitos [entidade] · depende de [entidade] ·
  referência [entidade]
- **Observações:** [preencher]
### ENT-002 — [nome da entidade]
- **Nome:** [preencher]
- **Descrição:** [preencher]
- **Tipo:** [preencher]
- **Responsabilidade:** [preencher]
- **Origem funcional:** [preencher]
- **Identificador principal:** `id` — [tipo lógico]
- **Atributos:**
  `id`: [tipo] — [descrição] · `[campo]`: [tipo] — [descrição] ·
  `[campo]`: [tipo] — [descrição]
- **Atributos obrigatórios:** [atributo 1]
- **Atributos opcionais:** [atributo 1]
- **Regras de validação:** [regra 1] · [regra 2]
- **Regras de negócio:** [regra 1]
- **Estados possíveis:** [estado 1] · [estado 2]
- **Transições relevantes:** [transição 1]
- **Relacionamentos:** [relacionamento 1] · [relacionamento 2]
- **Observações:** [preencher]
### ENT-003 — [nome da entidade]
- **Nome:** [preencher]
- **Descrição:** [preencher]
- **Tipo:** [preencher]
- **Responsabilidade:** [preencher]
- **Origem funcional:** [preencher]
- **Identificador principal:** `id` — [tipo lógico]
- **Atributos:** `id`: [tipo] — [descrição] · `[campo]`: [tipo] — [descrição]
- **Atributos obrigatórios:** [atributo 1]
- **Atributos opcionais:** [atributo 1]
- **Regras de validação:** [regra 1]
- **Regras de negócio:** [regra 1]
- **Estados possíveis:** [estado 1]
- **Transições relevantes:** [transição 1]
- **Relacionamentos:** [relacionamento 1]
- **Observações:** [preencher]
---
## 6. Relações Entre Entidades
- **Mapa textual:**
  [entidade A] 1:N [entidade B] · [entidade A] N:N [entidade C] ·
  [entidade D] 1:1 [entidade E]
- **Entidades agregadoras/pivôs:** [entidade 1] · [entidade 2]
- **Relações críticas:** [relação 1] · [relação 2]
- **Restrições relevantes:** [restrição 1] · [restrição 2]
---
## 7. Regras Transversais do Domínio
- **Regras multi-entidade:** [regra 1] · [regra 2] · [regra 3]
- **Validações transversais:** [validação 1] · [validação 2]
- **Restrições por perfil/permissão/contexto:** [restrição 1] · [restrição 2]
---
## 8. Estados e Ciclos de Vida
- **Entidades com ciclo de vida importante:** [entidade 1] · [entidade 2]
### Ciclo de vida: [entidade]
- **Estados:** [estado 1] · [estado 2] · [estado 3]
- **Eventos que causam transição:** [evento 1] · [evento 2]
- **Estados inválidos/proibidos:** [estado inválido 1] · [estado inválido 2]
---
## 9. Campos Sensíveis, Críticos ou Auditáveis
- **Campos sensíveis:** [campo 1] · [campo 2]
- **Campos críticos:** [campo 1] · [campo 2]
- **Campos auditáveis:** [campo 1] · [campo 2]
- **Observações:** [privacidade, rastreabilidade, compliance]
---
## 10. Dependências Funcionais
- **Entidades fundamentais (MVP):** [entidade 1] · [entidade 2]
- **Dependem de outras:**
  [entidade 1 depende de entidade 2] · [entidade 3 depende de entidade 4]
- **Futuras ou opcionais:** [entidade 1] · [entidade 2]
---
## 11. Diretrizes para os Próximos Documentos
- **Docs/architecture.md:**
  [como entidades impactam módulos, serviços, agregados ou camadas]
- **Docs/contract.yaml:**
  [quais entidades serão expostas ou trafegadas na API]
- **Docs/structure.md:**
  [como o domínio influencia organização de pastas e responsabilidades]
- **Docs/deploy.md:**
  [dependência operacional por persistência ou consistência, se houver]
- **Docs/plan.md / Docs/tasks.md:**
  [entidades fundacionais que orientam ordem de implementação]
---
## 12. Síntese Operacional para Dev e AI
- **12.1 Entidades centrais:** [entidade 1] · [entidade 2] · [entidade 3]
- **12.2 Relações mais importantes:** [relação 1] · [relação 2]
- **12.3 Regras inegociáveis:** [regra 1] · [regra 2] · [regra 3]
- **12.4 Estados críticos:** [estado 1] · [estado 2]
- **12.5 O que ainda está indefinido:** [ponto 1] · [ponto 2]
---
## 13. Aprovação
- **Status de aprovação:** [pendente / aprovado / revisando]
- **Aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
