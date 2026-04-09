# Fluxo

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / revisando / aprovado]

**Documento base:**  
[referência ao Docs/pages.md e Docs/user-stories.md]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
[explique que este documento descreve os fluxos de navegação e interação do sistema, as jornadas dos usuários, as transições entre páginas e os estados condicionais relevantes]

**O que este documento cobre:**  
- jornadas por perfil
- pontos de entrada
- transições entre páginas
- decisões e condicionais
- desvios e exceções
- estados de bloqueio, erro ou permissão

**O que este documento não cobre:**  
- layout visual detalhado
- implementação técnica da navegação
- arquitetura interna
- contrato detalhado de API
- definição completa de componentes visuais

---

## 3. Regras Gerais dos Fluxos

Cada fluxo deve conter:
- nome claro
- perfil principal
- objetivo da jornada
- ponto de entrada
- pré-condições
- sequência principal
- desvios
- estados excepcionais
- resultado esperado

**Tipos de fluxo possíveis:**  
- fluxo principal
- fluxo alternativo
- fluxo de erro
- fluxo administrativo
- fluxo de autenticação
- fluxo de recuperação
- fluxo de confirmação
- fluxo de saída
- fluxo restrito por permissão

---

## 4. Visão Geral das Jornadas

### Jornada JN-001 — [nome da jornada]

**Perfil principal:**  
[perfil]

**Objetivo da jornada:**  
[o que o usuário quer alcançar]

**Histórias relacionadas:**  
- US-001
- US-002

**Páginas relacionadas:**  
- PG-001
- PG-002
- PG-003

**Ponto de entrada:**  
[onde o fluxo começa]

**Resultado esperado:**  
[qual resultado deve existir ao fim da jornada]

**Observações gerais:**  
[preencher]

---

### Jornada JN-002 — [nome da jornada]

**Perfil principal:**  
[perfil]

**Objetivo da jornada:**  
[preencher]

**Histórias relacionadas:**  
- US-003

**Páginas relacionadas:**  
- PG-004
- PG-005

**Ponto de entrada:**  
[preencher]

**Resultado esperado:**  
[preencher]

**Observações gerais:**  
[preencher]

---

## 5. Fluxos Detalhados

### FL-001 — [nome do fluxo]

**Tipo:**  
[fluxo principal / alternativo / erro / autenticação / administrativo / etc.]

**Perfil principal:**  
[perfil]

**Objetivo do fluxo:**  
[descreva]

**Histórias relacionadas:**  
- US-001

**Páginas envolvidas:**  
- PG-001
- PG-002
- PG-003

**Pré-condições:**  
- [pré-condição 1]
- [pré-condição 2]

**Ponto de entrada:**  
[onde o usuário entra nesse fluxo]

**Sequência principal:**  
1. Usuário acessa [PG-001].
2. Sistema exibe [estado inicial esperado].
3. Usuário executa [ação].
4. Sistema valida [condição].
5. Usuário é direcionado para [PG-002].
6. Sistema processa [evento].
7. Usuário conclui [ação final] em [PG-003].

**Decisões e condicionais:**  
- Se [condição], seguir para [página / estado].
- Se [condição], bloquear ação e exibir [mensagem / estado].
- Se [condição], redirecionar para [página].

**Desvios possíveis:**  
- [desvio 1]
- [desvio 2]

**Estados excepcionais:**  
- erro de validação
- indisponibilidade externa
- sessão expirada
- sem permissão
- dados inexistentes
- [outro]

**Saídas possíveis do fluxo:**  
- [saída 1]
- [saída 2]

**Resultado esperado:**  
[descreva o fim ideal do fluxo]

**Observações:**  
[preencher]

---

### FL-002 — [nome do fluxo]

**Tipo:**  
[preencher]

**Perfil principal:**  
[preencher]

**Objetivo do fluxo:**  
[preencher]

**Histórias relacionadas:**  
- US-002

**Páginas envolvidas:**  
- PG-004
- PG-005

**Pré-condições:**  
- [pré-condição 1]

**Ponto de entrada:**  
[preencher]

**Sequência principal:**  
1. [passo 1]
2. [passo 2]
3. [passo 3]

**Decisões e condicionais:**  
- [condição 1]
- [condição 2]

**Desvios possíveis:**  
- [desvio 1]

**Estados excepcionais:**  
- [estado 1]
- [estado 2]

**Saídas possíveis do fluxo:**  
- [saída 1]

**Resultado esperado:**  
[preencher]

**Observações:**  
[preencher]

---

### FL-003 — [nome do fluxo]

**Tipo:**  
[preencher]

**Perfil principal:**  
[preencher]

**Objetivo do fluxo:**  
[preencher]

**Histórias relacionadas:**  
- US-003

**Páginas envolvidas:**  
- PG-006

**Pré-condições:**  
- [pré-condição 1]

**Ponto de entrada:**  
[preencher]

**Sequência principal:**  
1. [passo 1]
2. [passo 2]

**Decisões e condicionais:**  
- [condição 1]

**Desvios possíveis:**  
- [desvio 1]

**Estados excepcionais:**  
- [estado 1]

**Saídas possíveis do fluxo:**  
- [saída 1]

**Resultado esperado:**  
[preencher]

**Observações:**  
[preencher]

---

## 6. Fluxos por Perfil

### Perfil: [nome do perfil]
**Fluxos principais:**  
- FL-001
- FL-002

**Fluxos alternativos:**  
- FL-003

**Restrições relevantes:**  
- [restrição 1]
- [restrição 2]

**Observações:**  
[preencher]

---

### Perfil: [nome do perfil]
**Fluxos principais:**  
- FL-004

**Fluxos alternativos:**  
- FL-005

**Restrições relevantes:**  
- [restrição 1]

**Observações:**  
[preencher]

---

## 7. Pontos de Decisão e Condições Críticas

**Decisões críticas do sistema:**  
- [decisão 1]
- [decisão 2]
- [decisão 3]

**Condições de bloqueio:**  
- [bloqueio 1]
- [bloqueio 2]

**Condições de redirecionamento:**  
- [redirecionamento 1]
- [redirecionamento 2]

**Condições de fallback:**  
- [fallback 1]
- [fallback 2]

---

## 8. Estados Transversais de Navegação

**Estados que podem aparecer em múltiplos fluxos:**  
- loading
- erro
- sucesso
- vazio
- sem permissão
- sessão expirada
- indisponibilidade externa
- timeout
- falha de autenticação

**Diretriz de tratamento:**  
[explique como esses estados devem se comportar ao longo dos fluxos]

---

## 9. Dependências e Restrições Funcionais

**Dependências entre fluxos:**  
- FL-002 depende de FL-001
- FL-004 exige autenticação prévia

**Restrições por perfil ou permissão:**  
- [restrição 1]
- [restrição 2]

**Fluxos críticos para o MVP:**  
- FL-001
- FL-002

**Fluxos opcionais ou futuros:**  
- FL-005
- FL-006

---

## 10. Diretrizes para os Próximos Documentos

### 10.1 Para o Docs/Prototype/
[quais fluxos e telas precisam ser prototipados primeiro]

### 10.2 Para o Docs/design-system.md
[quais padrões de interação, feedback e estado parecem recorrentes]

### 10.3 Para o Docs/tokens.json
[quais semânticas visuais e estados precisam de suporte por tokens]

### 10.4 Para o Docs/contract.yaml
[quais fluxos indicam necessidade de endpoints, operações ou respostas específicas]

### 10.5 Para o Docs/entities.md
[quais conceitos de domínio aparecem nos fluxos]

### 10.6 Para o Docs/plan.md e Docs/tasks.md
[quais fluxos são prioritários, bloqueantes ou fundacionais]

---

## 11. Síntese Operacional para Dev e AI

### 11.1 Jornadas principais
- JN-001
- JN-002

### 11.2 Fluxos mais críticos
- FL-001
- FL-002
- FL-003

### 11.3 Decisões que não podem ser esquecidas
- [decisão 1]
- [decisão 2]

### 11.4 Estados críticos que devem existir
- [estado 1]
- [estado 2]
- [estado 3]

### 11.5 O que ainda está indefinido
- [ponto 1]
- [ponto 2]

---

## 12. Aprovação

**Status de aprovação:**  
[pendente / aprovado / revisando]

**Aprovado por:**  
[preencher]

**Data de aprovação:**  
[dd/mm/aaaa]

**Observações finais:**  
[preencher]