# Entidades

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / revisando / aprovado]

**Documentos base:**  
[referência ao Docs/project.md, Docs/user-stories.md, Docs/pages.md e Docs/flow.md]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
[explique que este documento define o modelo de domínio do projeto: entidades, atributos, relações, regras, estados e validações que sustentam o sistema]

**O que este documento cobre:**  
- entidades do domínio
- significado de cada entidade
- atributos e tipos lógicos
- identificadores
- regras e validações
- relacionamentos
- estados e ciclo de vida
- dependências conceituais

**O que este documento não cobre:**  
- SQL final
- migrations
- implementação de ORM
- contrato detalhado da API
- arquitetura de módulos em profundidade

---

## 3. Regras Gerais de Modelagem

**Princípios da modelagem do projeto:**  
- [ex.: modelar conceitos do domínio antes da estrutura técnica]
- [ex.: evitar duplicidade conceitual]
- [ex.: nomear entidades de forma clara e estável]
- [ex.: separar entidade de apoio de entidade central]
- [ex.: refletir regras reais de negócio]

**Convenções gerais:**  
- nomes de entidades no singular
- atributos com nomes claros e sem ambiguidade
- identificadores explícitos
- estados relevantes modelados
- relações descritas de forma legível

**Diretriz importante:**  
[explique como Dev e AI devem interpretar o documento antes de modelar banco, contrato ou código]

---

## 4. Visão Geral do Domínio

**Resumo do domínio:**  
[descreva em poucas linhas o domínio funcional do projeto]

**Entidades centrais do sistema:**  
- [entidade 1]
- [entidade 2]
- [entidade 3]

**Entidades auxiliares ou de apoio:**  
- [entidade 1]
- [entidade 2]

**Observações gerais do domínio:**  
[preencher]

---

## 5. Entidades do Projeto

### ENT-001 — [nome da entidade]

**Nome da entidade:**  
[preencher]

**Descrição:**  
[explique o que essa entidade representa]

**Tipo da entidade:**  
[central / apoio / associação / configuração / evento / histórico / transacional / catálogo]

**Responsabilidade no domínio:**  
[qual papel ela cumpre no sistema]

**Origem funcional:**  
[quais histórias, páginas ou fluxos justificam essa entidade]

**Identificador principal:**  
- `id`: [tipo lógico]

**Atributos:**  
- `id`: [tipo] — [descrição]
- `name`: [tipo] — [descrição]
- `status`: [tipo] — [descrição]
- `createdAt`: [tipo] — [descrição]
- `updatedAt`: [tipo] — [descrição]

**Atributos obrigatórios:**  
- [atributo 1]
- [atributo 2]

**Atributos opcionais:**  
- [atributo 1]
- [atributo 2]

**Regras de validação:**  
- [regra 1]
- [regra 2]
- [regra 3]

**Regras de negócio da entidade:**  
- [regra 1]
- [regra 2]

**Estados possíveis:**  
- [estado 1]
- [estado 2]
- [estado 3]

**Transições de estado relevantes:**  
- [transição 1]
- [transição 2]

**Relacionamentos:**  
- pertence a [entidade]
- possui muitos [entidade]
- depende de [entidade]
- referência [entidade]

**Observações:**  
[preencher]

---

### ENT-002 — [nome da entidade]

**Nome da entidade:**  
[preencher]

**Descrição:**  
[preencher]

**Tipo da entidade:**  
[preencher]

**Responsabilidade no domínio:**  
[preencher]

**Origem funcional:**  
[preencher]

**Identificador principal:**  
- `id`: [tipo lógico]

**Atributos:**  
- `id`: [tipo] — [descrição]
- `[campo]`: [tipo] — [descrição]
- `[campo]`: [tipo] — [descrição]

**Atributos obrigatórios:**  
- [atributo 1]

**Atributos opcionais:**  
- [atributo 1]

**Regras de validação:**  
- [regra 1]
- [regra 2]

**Regras de negócio da entidade:**  
- [regra 1]

**Estados possíveis:**  
- [estado 1]
- [estado 2]

**Transições de estado relevantes:**  
- [transição 1]

**Relacionamentos:**  
- [relacionamento 1]
- [relacionamento 2]

**Observações:**  
[preencher]

---

### ENT-003 — [nome da entidade]

**Nome da entidade:**  
[preencher]

**Descrição:**  
[preencher]

**Tipo da entidade:**  
[preencher]

**Responsabilidade no domínio:**  
[preencher]

**Origem funcional:**  
[preencher]

**Identificador principal:**  
- `id`: [tipo lógico]

**Atributos:**  
- `id`: [tipo] — [descrição]
- `[campo]`: [tipo] — [descrição]

**Atributos obrigatórios:**  
- [atributo 1]

**Atributos opcionais:**  
- [atributo 1]

**Regras de validação:**  
- [regra 1]

**Regras de negócio da entidade:**  
- [regra 1]

**Estados possíveis:**  
- [estado 1]

**Transições de estado relevantes:**  
- [transição 1]

**Relacionamentos:**  
- [relacionamento 1]

**Observações:**  
[preencher]

---

## 6. Relações Entre Entidades

**Mapa textual das relações principais:**  
- [entidade A] 1:N [entidade B]
- [entidade A] N:N [entidade C]
- [entidade D] 1:1 [entidade E]

**Entidades agregadoras ou pivôs:**  
- [entidade 1]
- [entidade 2]

**Relações críticas do sistema:**  
- [relação 1]
- [relação 2]

**Restrições relevantes de relacionamento:**  
- [restrição 1]
- [restrição 2]

---

## 7. Regras Transversais do Domínio

**Regras que afetam múltiplas entidades:**  
- [regra 1]
- [regra 2]
- [regra 3]

**Validações transversais:**  
- [validação 1]
- [validação 2]

**Restrições por perfil, permissão ou contexto:**  
- [restrição 1]
- [restrição 2]

---

## 8. Estados e Ciclos de Vida

**Entidades com ciclo de vida importante:**  
- [entidade 1]
- [entidade 2]

### Ciclo de vida: [entidade]
**Estados:**  
- [estado 1]
- [estado 2]
- [estado 3]

**Eventos que causam transição:**  
- [evento 1]
- [evento 2]

**Estados inválidos ou proibidos:**  
- [estado inválido 1]
- [estado inválido 2]

---

## 9. Campos Sensíveis, Críticos ou Auditáveis

**Campos sensíveis:**  
- [campo 1]
- [campo 2]

**Campos críticos para operação:**  
- [campo 1]
- [campo 2]

**Campos auditáveis:**  
- [campo 1]
- [campo 2]

**Observações sobre privacidade, rastreabilidade ou compliance:**  
[preencher]

---

## 10. Dependências Funcionais

**Entidades fundamentais para o MVP:**  
- [entidade 1]
- [entidade 2]

**Entidades que dependem de outras para existir:**  
- [entidade 1 depende de entidade 2]
- [entidade 3 depende de entidade 4]

**Entidades futuras ou opcionais:**  
- [entidade 1]
- [entidade 2]

---

## 11. Diretrizes para os Próximos Documentos

### 11.1 Para o Docs/architecture.md
[como as entidades impactam módulos, serviços, agregados ou camadas]

### 11.2 Para o Docs/contract.yaml
[quais entidades provavelmente serão expostas ou trafegadas na API]

### 11.3 Para o Docs/structure.md
[como o domínio pode influenciar a organização de pastas e responsabilidades]

### 11.4 Para o Docs/deploy.md
[se houver dependência operacional relevante por causa de persistência ou consistência]

### 11.5 Para o Docs/plan.md e Docs/tasks.md
[quais entidades são fundacionais e devem orientar a ordem de implementação]

---

## 12. Síntese Operacional para Dev e AI

### 12.1 Entidades centrais
- [entidade 1]
- [entidade 2]
- [entidade 3]

### 12.2 Relações mais importantes
- [relação 1]
- [relação 2]

### 12.3 Regras que não podem ser quebradas
- [regra 1]
- [regra 2]
- [regra 3]

### 12.4 Estados críticos do domínio
- [estado 1]
- [estado 2]

### 12.5 O que ainda está indefinido
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