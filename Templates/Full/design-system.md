# Design System
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão do documento:** [v1, v2, etc.]
- **Status:** [rascunho / revisando / aprovado]
- **Documentos base:**
  `Docs/pages.md` · `Docs/flow.md` · `Docs/Prototype/` · `Docs/project.md`
- **Data de criação:** [dd/mm/aaaa]
- **Última atualização:** [dd/mm/aaaa]
---
## 2. Objetivo do Documento
- **Finalidade:**
  definir contrato do design system: princípios visuais, padrões de interface,
  comportamento dos componentes, regras de composição e consistência
- **Cobre:**
  princípios visuais · linguagem de interface · composição ·
  layout · tipografia · cores semânticas · componentes/estados · feedback ·
  acessibilidade · consistência
- **Não cobre:**
  valores brutos de token · implementação final de componentes · protótipos
  completos · fluxos completos · arquitetura técnica de frontend
---
## 3. Princípios do Design System
- **Princípios:**
  clareza · consistência · legibilidade · previsibilidade · eficiência ·
  acessibilidade · baixo ruído visual · escalabilidade
- **Descrição por princípio:**
  clareza: [explique]
  consistência: [explique]
  legibilidade: [explique]
  eficiência: [explique]
  acessibilidade: [explique]
---
## 4. Linguagem Visual
- **Direção visual:**
  [minimalista / sóbria / técnica / premium / institucional / amigável]
- **Personalidade da interface:** [descreva]
- **Sensação desejada:** [sensação 1] · [sensação 2] · [sensação 3]
- **Evitar:** excesso visual · ambiguidade · poluição · contraste ruim ·
  interações inesperadas
---
## 5. Regras Gerais de Layout
- **Estrutura base:**
  [header + conteúdo + ações / sidebar + área principal / dashboard / etapas]
- **Diretrizes de composição:** [regra 1] · [regra 2] · [regra 3]
- **Regras de espaçamento:** [lógica de espaçamento, valores em Docs/tokens.json]
- **Regras de alinhamento:** [descreva]
- **Regras de responsividade:** [regra 1] · [regra 2] · [regra 3]
- **Larguras, containers e grid:** [lógica estrutural]
---
## 6. Tipografia — Regras de Uso
- **Papel da tipografia:** [explique]
- **Hierarquia textual:**
  título de página · título de seção · subtítulo · corpo principal ·
  corpo secundário · legenda · rótulo · ajuda · feedback · ação
- **Regras gerais:** [regra 1] · [regra 2] · [regra 3]
- **Boas práticas:**
  contraste adequado · evitar excesso de pesos · evitar blocos longos ·
  priorizar legibilidade
---
## 7. Cores — Regras Semânticas
- **Papel das cores:** [explique]
- **Semânticas principais:**
  primária · secundária · neutra · sucesso · aviso · erro · informação ·
  destaque · superfície · borda · texto · estado desabilitado
- **Regras gerais:** [regra 1] · [regra 2] · [regra 3]
- **Não fazer:**
  usar cor sem papel semântico · depender só de cor · contraste insuficiente ·
  misturar semânticas
---
## 8. Feedback e Estados de Interface
- **Estados obrigatórios:**
  default · hover · active · focus · disabled · loading · success · error ·
  empty · selected · pressed · readonly · invalid
- **Regras por estado:** [descreva]
- **Feedbacks esperados:**
  confirmação · erro de validação · erro sistêmico · sucesso ·
  indisponibilidade · espera/processamento · ausência de conteúdo ·
  restrição de permissão
- **Diretrizes gerais:** [regra 1] · [regra 2] · [regra 3]
---
## 9. Padrões de Interação
- **Princípios de interação:**
  previsibilidade · tempo de resposta claro · baixo esforço cognitivo ·
  continuidade · ação com feedback
- **Padrões esperados:**
  formulários com validação clara · botões com hierarquia definida ·
  confirmação em ações destrutivas · navegação consistente · feedback imediato
- **Padrões a evitar:**
  interação sem feedback · ação destrutiva sem confirmação · navegação
  inconsistente · labels ambíguos · estados invisíveis
---
## 10. Componentes do Sistema
- **Lista de componentes base:**
  botão · input · textarea · select · checkbox · radio · switch ·
  badge · card · modal · drawer · tooltip · alert · toast · tabela ·
  tabs · pagination · breadcrumb · avatar · skeleton · spinner · empty state
- **Observação:** [ajuste a lista ao projeto]
### 10.2 Contrato por componente
#### Button
- **Objetivo:** [para que serve]
- **Variações:** primário · secundário · ghost · link · destrutivo · outras
- **Tamanhos:** pequeno · médio · grande
- **Estados:** default · hover · active · focus · disabled · loading
- **Regras de uso:** [regra 1] · [regra 2]
- **Restrições:**
  não usar para navegação quando o correto for link · não competir com ação
  primária da tela
- **Acessibilidade:** [regras]
#### Input
- **Objetivo:** [preencher]
- **Variações:** texto · senha · email · número · busca · outras
- **Estados:** default · focus · disabled · readonly · invalid ·
  loading se aplicável
- **Regras de uso:** [regra 1] · [regra 2]
- **Feedbacks obrigatórios:** erro de validação · ajuda contextual · label claro
- **Acessibilidade:** [regras]
#### Modal
- **Objetivo:** [preencher]
- **Quando usar:** [caso 1] · [caso 2]
- **Quando não usar:** [caso 1] · [caso 2]
- **Estados:** aberto · fechado · loading · erro se aplicável
- **Regras de comportamento:** [regra 1] · [regra 2]
- **Acessibilidade:** [foco, escape, aria, etc.]
---
## 11. Padrões de Página
- **Estruturas recorrentes:**
  listagem · detalhe · formulário simples · formulário multi-etapas ·
  dashboard · autenticação · tela vazia · tela de erro · confirmação
### Página de listagem
- **Objetivo:** [descreva]
- **Partes esperadas:**
  título · filtros · ações · tabela/lista · paginação · estados
- **Regras:** [regra 1] · [regra 2]
### Página de formulário
- **Objetivo:** [descreva]
- **Partes esperadas:**
  título · descrição opcional · campos · validação · ações · feedback
- **Regras:** [regra 1] · [regra 2]
---
## 12. Acessibilidade
- **Objetivo:** [descreva]
- **Regras mínimas:**
  contraste adequado · foco visível · labels claros · teclado quando aplicável ·
  feedback não depende só de cor · semântica correta · erros compreensíveis
- **Cuidados específicos:** [cuidado 1] · [cuidado 2]
---
## 13. Consistência entre Design System e Tokens
- **Regra principal:** valores visuais estruturados devem nascer/refletir
  `Docs/tokens.json`
- **Este documento define:** papéis · regras · semânticas · comportamento ·
  composição
- **`Docs/tokens.json` define:** valores · escalas · aliases · categorias
- **Precedência:**
  regra visual/comportamental → `Docs/design-system.md` ·
  valor estruturado reutilizável → `Docs/tokens.json`
---
## 14. Relação com Outros Documentos
- **`Docs/pages.md`:** [como orientar páginas]
- **`Docs/flow.md`:** [como orientar estados e interação]
- **`Docs/Prototype/`:** [como orientar prototipagem]
- **`Docs/tokens.json`:** [como orientar estrutura de tokens]
- **`Docs/tasks.md`:** [impacto em tarefas de UI]
---
## 15. Diretrizes para Implementação
- **Dev e AI devem respeitar:** [diretriz 1] · [diretriz 2] · [diretriz 3]
- **Pode variar com segurança:** [item 1] · [item 2]
- **Exige atualização:**
  novo padrão recorrente · nova variação relevante · mudança semântica ·
  mudança visual recorrente
---
## 16. Síntese Operacional para Dev e AI
- **16.1 Direção visual resumida:** [descreva em poucas linhas]
- **16.2 Princípios inegociáveis:** [princípio 1] · [princípio 2] · [princípio 3]
- **16.3 Componentes críticos:** [componente 1] · [componente 2] · [componente 3]
- **16.4 Estados críticos:** [estado 1] · [estado 2] · [estado 3]
- **16.5 Indefinições:** [ponto 1] · [ponto 2]
---
## 17. Aprovação
- **Status de aprovação:** [pendente / aprovado / revisando]
- **Aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
