# Pages

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / revisando / aprovado]

**Documento base:**  
[referência ao Docs/user-stories.md]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
[explique que este documento define o inventário oficial de telas e páginas do projeto, seus propósitos e relação com histórias e perfis]

**O que este documento cobre:**  
- páginas e telas do sistema
- propósito funcional de cada tela
- perfis com acesso
- histórias atendidas
- estados esperados
- dependências visuais e funcionais

**O que este documento não cobre:**  
- layout visual detalhado
- fluxo de navegação completo
- implementação técnica
- contrato de API detalhado
- arquitetura de componentes

---

## 3. Regras de Definição das Páginas

Cada página ou tela deve conter:
- nome claro
- tipo de tela
- objetivo funcional
- perfis com acesso
- histórias atendidas
- estados esperados
- dependências relevantes

**Tipos possíveis:**  
- página pública
- página autenticada
- tela administrativa
- tela operacional
- modal
- drawer
- etapa de fluxo
- tela de detalhe
- tela de listagem
- tela de formulário
- tela de confirmação
- estado especial

---

## 4. Inventário de Páginas

### PG-001 — [nome da página]

**Nome da página:**  
[preencher]

**Tipo:**  
[página pública / autenticada / modal / listagem / detalhe / formulário / etc.]

**Objetivo da página:**  
[explique para que essa página existe]

**Resumo funcional:**  
[descreva o que o usuário faz ou obtém nessa página]

**Perfis com acesso:**  
- [perfil 1]
- [perfil 2]

**Histórias relacionadas:**  
- US-001
- US-002

**Origem de navegação:**  
[de onde o usuário normalmente chega]

**Destinos principais:**  
- [destino 1]
- [destino 2]

**Ações principais disponíveis:**  
- [ação 1]
- [ação 2]
- [ação 3]

**Informações exibidas:**  
- [informação 1]
- [informação 2]
- [informação 3]

**Entradas esperadas do usuário:**  
- [input 1]
- [input 2]

**Estados obrigatórios:**  
- loading
- vazio
- erro
- sucesso
- sem permissão
- sem dados
- indisponibilidade externa
- [outro estado específico]

**Regras ou restrições relevantes:**  
- [regra 1]
- [regra 2]

**Dependências funcionais:**  
- [endpoint / módulo / integração / permissão]
- [dependência 2]

**Observações visuais ou de UX:**  
[preencher]

**Observações adicionais:**  
[preencher]

---

### PG-002 — [nome da página]

**Nome da página:**  
[preencher]

**Tipo:**  
[preencher]

**Objetivo da página:**  
[preencher]

**Resumo funcional:**  
[preencher]

**Perfis com acesso:**  
- [perfil 1]

**Histórias relacionadas:**  
- US-003

**Origem de navegação:**  
[preencher]

**Destinos principais:**  
- [destino 1]

**Ações principais disponíveis:**  
- [ação 1]
- [ação 2]

**Informações exibidas:**  
- [informação 1]
- [informação 2]

**Entradas esperadas do usuário:**  
- [input 1]

**Estados obrigatórios:**  
- loading
- erro
- sucesso

**Regras ou restrições relevantes:**  
- [regra 1]

**Dependências funcionais:**  
- [dependência 1]

**Observações visuais ou de UX:**  
[preencher]

**Observações adicionais:**  
[preencher]

---

### PG-003 — [nome da página]

**Nome da página:**  
[preencher]

**Tipo:**  
[preencher]

**Objetivo da página:**  
[preencher]

**Resumo funcional:**  
[preencher]

**Perfis com acesso:**  
- [perfil 1]

**Histórias relacionadas:**  
- US-004

**Origem de navegação:**  
[preencher]

**Destinos principais:**  
- [destino 1]

**Ações principais disponíveis:**  
- [ação 1]

**Informações exibidas:**  
- [informação 1]

**Entradas esperadas do usuário:**  
- [input 1]

**Estados obrigatórios:**  
- loading
- erro
- vazio
- sucesso

**Regras ou restrições relevantes:**  
- [regra 1]

**Dependências funcionais:**  
- [dependência 1]

**Observações visuais ou de UX:**  
[preencher]

**Observações adicionais:**  
[preencher]

---

## 5. Agrupamento por Área / Módulo

### Área / módulo: [nome]
**Objetivo da área:**  
[descreva]

**Páginas relacionadas:**  
- PG-001
- PG-002

**Perfis impactados:**  
- [perfil 1]
- [perfil 2]

**Observações:**  
[preencher]

---

### Área / módulo: [nome]
**Objetivo da área:**  
[descreva]

**Páginas relacionadas:**  
- PG-003
- PG-004

**Perfis impactados:**  
- [perfil 1]

**Observações:**  
[preencher]

---

## 6. Estados Transversais Esperados

**Estados que devem ser considerados em múltiplas páginas:**  
- loading
- vazio
- erro
- sucesso
- sem permissão
- sem conexão
- indisponibilidade externa
- sessão expirada
- conteúdo restrito

**Diretriz geral:**  
[explique como esses estados devem ser tratados de forma consistente]

---

## 7. Convenções de Nomeação e Organização

**Padrão de identificação das páginas:**  
[ex.: PG-001, PG-002]

**Convenção de nome:**  
[ex.: verbo + objeto / área + ação / entidade + operação]

**Critério para separar página, modal e componente:**  
[explique]

---

## 8. Dependências e Observações Funcionais

**Dependências relevantes entre páginas:**  
- PG-002 depende de PG-001
- PG-004 depende de autenticação prévia

**Restrições por perfil ou permissão:**  
- [restrição 1]
- [restrição 2]

**Páginas críticas do sistema:**  
- [página 1]
- [página 2]

**Páginas opcionais ou futuras:**  
- [página 1]
- [página 2]

---

## 9. Diretrizes para os Próximos Documentos

### 9.1 Para o Docs/flow.md
[quais relações de navegação e jornadas precisam ser descritas]

### 9.2 Para o Prototype/
[quais páginas devem ser prototipadas primeiro]

### 9.3 Para o Docs/design-system.md
[quais componentes e padrões parecem recorrentes entre páginas]

### 9.4 Para o Docs/tokens.json
[quais necessidades de consistência visual, responsividade ou semântica de interface aparecem]

### 9.5 Para o Docs/contract.yaml
[quais páginas sugerem endpoints, operações ou necessidades de integração]

### 9.6 Para o Docs/plan.md e Docs/tasks.md
[quais páginas parecem prioritárias, fundacionais ou dependentes]

---

## 10. Síntese Operacional para Dev e AI

### 10.1 Páginas prioritárias
- PG-001
- PG-002
- PG-003

### 10.2 Páginas críticas para o MVP
- [página 1]
- [página 2]

### 10.3 O que cada página precisa garantir
- [garantia 1]
- [garantia 2]
- [garantia 3]

### 10.4 Estados que não podem ser esquecidos
- [estado 1]
- [estado 2]
- [estado 3]

### 10.5 O que ainda está indefinido
- [ponto 1]
- [ponto 2]

---

## 11. Aprovação

**Status de aprovação:**  
[pendente / aprovado / revisando]

**Aprovado por:**  
[preencher]

**Data de aprovação:**  
[dd/mm/aaaa]

**Observações finais:**  
[preencher]