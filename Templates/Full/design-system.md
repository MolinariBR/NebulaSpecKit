# Design System

## 1. Identificação

**Nome do projeto:**  
[preencher]

**Versão do documento:**  
[v1, v2, etc.]

**Status:**  
[rascunho / revisando / aprovado]

**Documentos base:**  
[referência ao Docs/pages.md, Docs/flow.md, Prototype/ e Docs/project.md]

**Data de criação:**  
[dd/mm/aaaa]

**Última atualização:**  
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**  
[explique que este documento define o contrato do design system do projeto: princípios visuais, padrões de interface, comportamento dos componentes, regras de composição e critérios de consistência]

**O que este documento cobre:**  
- princípios visuais
- linguagem de interface
- regras de composição
- estrutura de layout
- tipografia como regra de uso
- cores como papel semântico
- componentes e seus estados
- padrões de feedback
- acessibilidade
- consistência visual e comportamental

**O que este documento não cobre:**  
- valores brutos de token em detalhe
- implementação final de componentes
- protótipos completos
- fluxos de navegação completos
- arquitetura técnica do frontend

---

## 3. Princípios do Design System

**Princípios que devem guiar a interface:**  
- [ex.: clareza]
- [ex.: consistência]
- [ex.: legibilidade]
- [ex.: previsibilidade]
- [ex.: eficiência]
- [ex.: acessibilidade]
- [ex.: baixo ruído visual]
- [ex.: escalabilidade]

**Descrição dos princípios:**  

### Clareza
[explique o que significa clareza neste projeto]

### Consistência
[explique]

### Legibilidade
[explique]

### Eficiência
[explique]

### Acessibilidade
[explique]

---

## 4. Linguagem Visual

**Direção visual do produto:**  
[ex.: minimalista, sóbria, técnica, premium, institucional, amigável, operacional]

**Personalidade da interface:**  
[descreva]

**Sensação desejada ao usar o sistema:**  
- [sensação 1]
- [sensação 2]
- [sensação 3]

**O que a interface deve evitar:**  
- [excesso visual]
- [ambiguidade]
- [poluição]
- [contraste ruim]
- [interações inesperadas]

---

## 5. Regras Gerais de Layout

**Estrutura base de layout:**  
[ex.: header + conteúdo + ações contextuais / sidebar + área principal / dashboard modular / formulário em etapas]

**Diretrizes de composição:**  
- [regra 1]
- [regra 2]
- [regra 3]

**Regras de espaçamento:**  
[descreva a lógica de espaçamento; os valores concretos ficam em Docs/tokens.json]

**Regras de alinhamento:**  
[descreva]

**Regras de responsividade:**  
- [regra 1]
- [regra 2]
- [regra 3]

**Larguras, containers e grid:**  
[descreva a lógica estrutural]

---

## 6. Tipografia — Regras de Uso

**Papel da tipografia na interface:**  
[explique]

**Hierarquia textual esperada:**  
- título de página
- título de seção
- subtítulo
- corpo principal
- corpo secundário
- legenda
- rótulo
- ajuda
- feedback
- ação

**Regras gerais de uso:**  
- [regra 1]
- [regra 2]
- [regra 3]

**Boas práticas:**  
- [manter contraste adequado]
- [evitar excesso de pesos]
- [evitar blocos longos sem hierarquia]
- [priorizar legibilidade]

---

## 7. Cores — Regras Semânticas

**Papel das cores no sistema:**  
[explique]

**Semânticas principais:**  
- primária
- secundária
- neutra
- sucesso
- aviso
- erro
- informação
- destaque
- superfície
- borda
- texto
- estado desabilitado

**Regras gerais de uso:**  
- [regra 1]
- [regra 2]
- [regra 3]

**O que não fazer com cores:**  
- [usar cor sem papel semântico]
- [depender só de cor para transmitir estado]
- [usar contraste insuficiente]
- [misturar semânticas]

---

## 8. Feedback e Estados de Interface

**Estados que devem existir de forma consistente:**  
- default
- hover
- active
- focus
- disabled
- loading
- success
- error
- empty
- selected
- pressed
- readonly
- invalid

**Regras de comportamento por estado:**  
[descreva como a interface responde]

**Feedbacks esperados ao usuário:**  
- confirmação de ação
- erro de validação
- erro sistêmico
- sucesso
- indisponibilidade
- espera/processamento
- ausência de conteúdo
- restrição de permissão

**Diretrizes gerais:**  
- [regra 1]
- [regra 2]
- [regra 3]

---

## 9. Padrões de Interação

**Princípios de interação:**  
- [previsibilidade]
- [tempo de resposta claro]
- [baixo esforço cognitivo]
- [continuidade]
- [ação com feedback]

**Padrões esperados:**  
- formulários com validação clara
- botões com hierarquia bem definida
- confirmação em ações destrutivas
- navegação consistente
- feedback imediato em ações do usuário

**Padrões a evitar:**  
- interação sem feedback
- ação destrutiva sem confirmação
- navegação inconsistente
- labels ambíguos
- estados invisíveis

---

## 10. Componentes do Sistema

### 10.1 Lista de componentes base
- botão
- input
- textarea
- select
- checkbox
- radio
- switch
- badge
- card
- modal
- drawer
- tooltip
- alert
- toast
- tabela
- tabs
- pagination
- breadcrumb
- avatar
- skeleton
- spinner
- empty state

**Observação:**  
[ajuste a lista ao projeto]

---

### 10.2 Contrato por componente

#### Componente: Button

**Objetivo:**  
[para que serve]

**Variações previstas:**  
- primário
- secundário
- ghost
- link
- destrutivo
- [outras]

**Tamanhos previstos:**  
- pequeno
- médio
- grande

**Estados obrigatórios:**  
- default
- hover
- active
- focus
- disabled
- loading

**Regras de uso:**  
- [regra 1]
- [regra 2]

**Restrições:**  
- [não usar para navegação quando o elemento correto for link]
- [não competir com ação primária da tela]

**Acessibilidade:**  
- [regras]

---

#### Componente: Input

**Objetivo:**  
[preencher]

**Variações previstas:**  
- texto
- senha
- email
- número
- busca
- [outras]

**Estados obrigatórios:**  
- default
- focus
- disabled
- readonly
- invalid
- loading, se aplicável

**Regras de uso:**  
- [regra 1]
- [regra 2]

**Feedbacks obrigatórios:**  
- erro de validação
- ajuda contextual
- label claro

**Acessibilidade:**  
- [regras]

---

#### Componente: Modal

**Objetivo:**  
[preencher]

**Quando usar:**  
- [caso 1]
- [caso 2]

**Quando não usar:**  
- [caso 1]
- [caso 2]

**Estados obrigatórios:**  
- aberto
- fechado
- loading
- erro, se aplicável

**Regras de comportamento:**  
- [regra 1]
- [regra 2]

**Acessibilidade:**  
- [foco, escape, aria, etc.]

---

## 11. Padrões de Página

**Estruturas recorrentes esperadas:**  
- página de listagem
- página de detalhe
- formulário simples
- formulário multi-etapas
- dashboard
- tela de autenticação
- tela vazia
- tela de erro
- tela de confirmação

### Padrão: Página de listagem
**Objetivo:**  
[descreva]

**Partes esperadas:**  
- título
- filtros
- ações
- tabela/lista
- paginação
- estados

**Regras:**  
- [regra 1]
- [regra 2]

### Padrão: Página de formulário
**Objetivo:**  
[descreva]

**Partes esperadas:**  
- título
- descrição opcional
- campos
- validação
- ações
- feedback

**Regras:**  
- [regra 1]
- [regra 2]

---

## 12. Acessibilidade

**Objetivo de acessibilidade do sistema:**  
[descreva]

**Regras mínimas obrigatórias:**  
- contraste adequado
- foco visível
- labels claros
- navegação por teclado quando aplicável
- feedback não dependente apenas de cor
- semântica correta dos elementos
- mensagens de erro compreensíveis

**Cuidados específicos do projeto:**  
- [cuidado 1]
- [cuidado 2]

---

## 13. Consistência entre Design System e Tokens

**Regra principal:**  
Todos os valores visuais estruturados devem nascer ou ser refletidos em `Docs/tokens.json`.

**Este documento define:**  
- papéis
- regras
- semânticas
- comportamento
- composição

**Docs/tokens.json define:**  
- valores
- escalas
- aliases
- categorias consumíveis por código

**Regra de precedência:**  
- regra visual e comportamental → `Docs/design-system.md`
- valor estruturado reutilizável → `Docs/tokens.json`

---

## 14. Relação com Outros Documentos

### Docs/pages.md
[como este documento deve orientar as páginas]

### Docs/flow.md
[como deve orientar estados e interação]

### Prototype/
[como deve orientar a prototipagem]

### Docs/tokens.json
[como deve orientar a estrutura de tokens]

### Docs/tasks.md
[como este documento impacta tarefas de UI]

---

## 15. Diretrizes para Implementação

**O que Dev e AI devem respeitar obrigatoriamente:**  
- [diretriz 1]
- [diretriz 2]
- [diretriz 3]

**O que pode variar com segurança:**  
- [item 1]
- [item 2]

**O que exige atualização deste documento:**  
- novo padrão recorrente
- nova variação relevante de componente
- mudança de regra semântica
- mudança de comportamento visual recorrente

---

## 16. Síntese Operacional para Dev e AI

### 16.1 Direção visual resumida
[descreva em poucas linhas]

### 16.2 Princípios que não podem ser quebrados
- [princípio 1]
- [princípio 2]
- [princípio 3]

### 16.3 Componentes mais críticos
- [componente 1]
- [componente 2]
- [componente 3]

### 16.4 Estados que precisam existir com consistência
- [estado 1]
- [estado 2]
- [estado 3]

### 16.5 O que ainda está indefinido
- [ponto 1]
- [ponto 2]

---

## 17. Aprovação

**Status de aprovação:**  
[pendente / aprovado / revisando]

**Aprovado por:**  
[preencher]

**Data de aprovação:**  
[dd/mm/aaaa]

**Observações finais:**  
[preencher]