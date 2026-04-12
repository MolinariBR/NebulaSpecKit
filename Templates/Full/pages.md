# Páginas
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão do documento:** [v1, v2, etc.]
- **Status:** [rascunho / revisando / aprovado]
- **Documentos base:**
  `Docs/project.md` · `Docs/user-stories.md` · `Docs/flow.md` · `Docs/brief.md`
- **Data de criação:** [dd/mm/aaaa]
- **Última atualização:** [dd/mm/aaaa]
---
## 2. Objetivo do Documento
- **Finalidade:**
  definir o inventário oficial de telas e páginas, seus propósitos e relação
  com histórias e perfis
- **Cobre:**
  lista de páginas · objetivo de cada página · perfil principal ·
  relação com histórias e fluxos · estado principal e variações
- **Não cobre:**
  layout visual final · regras detalhadas de componentes · implementação técnica
---
## 3. Regras Gerais
- **Cada página deve conter:**
  nome · id · perfil principal · objetivo · estado principal ·
  histórias relacionadas · fluxos relacionados
- **Tipos de página:**
  listagem · detalhe · formulário · dashboard · autenticação · confirmação ·
  erro · vazio · administrativo · onboarding
---
## 4. Inventário de Páginas
### PG-001 — [nome da página]
- **Tipo:** [listagem / detalhe / formulário / dashboard / auth / etc.]
- **Perfil principal:** [perfil]
- **Objetivo:** [o que a página entrega]
- **Histórias relacionadas:** US-001 · US-002
- **Fluxos relacionados:** FL-001 · FL-002
- **Ponto de entrada:** [rota, menu ou ação]
- **Estado principal:** [descreva o estado padrão]
- **Estados alternativos:**
  loading · vazio · erro · sem permissão · sucesso · parcial
- **Ações principais:** [ação 1] · [ação 2] · [ação 3]
- **Saídas possíveis:** [para onde o usuário pode ir]
- **Observações:** [preencher]
### PG-002 — [nome da página]
- **Tipo:** [preencher]
- **Perfil principal:** [preencher]
- **Objetivo:** [preencher]
- **Histórias relacionadas:** US-003
- **Fluxos relacionados:** FL-003
- **Ponto de entrada:** [preencher]
- **Estado principal:** [preencher]
- **Estados alternativos:** [preencher]
- **Ações principais:** [preencher]
- **Saídas possíveis:** [preencher]
- **Observações:** [preencher]
### PG-003 — [nome da página]
- **Tipo:** [preencher]
- **Perfil principal:** [preencher]
- **Objetivo:** [preencher]
- **Histórias relacionadas:** [preencher]
- **Fluxos relacionados:** [preencher]
- **Ponto de entrada:** [preencher]
- **Estado principal:** [preencher]
- **Estados alternativos:** [preencher]
- **Ações principais:** [preencher]
- **Saídas possíveis:** [preencher]
- **Observações:** [preencher]
<!-- duplicar bloco PG conforme necessário -->
---
## 5. Mapa de Navegação por Perfil
### Perfil: [nome do perfil]
- **Páginas principais:** PG-001 · PG-002
- **Páginas secundárias:** PG-003
- **Restrições:** [restrição 1] · [restrição 2]
- **Observações:** [preencher]
### Perfil: [nome do perfil]
- **Páginas principais:** PG-004
- **Páginas secundárias:** PG-005
- **Restrições:** [restrição 1]
- **Observações:** [preencher]
---
## 6. Estados de Página e Variações
- **Estados transversais:**
  loading · vazio · erro · sem permissão · sucesso · parcial ·
  sessão expirada · indisponibilidade externa
- **Regras de tratamento:** [como cada estado deve se comportar]
---
## 7. Dependências e Prioridades
- **Páginas críticas para MVP:** PG-001 · PG-002
- **Páginas opcionais ou futuras:** PG-005 · PG-006
- **Dependências entre páginas:** PG-002 depende de PG-001
- **Dependências de fluxo:** PG-003 depende de FL-002
---
## 8. Diretrizes para Próximos Documentos
- **Docs/flow.md:**
  [como as páginas informam fluxos e transições]
- **Docs/design-system.md:**
  [padrões recorrentes de UI nas páginas]
- **Docs/Prototype/:**
  [quais páginas precisam de protótipo primeiro]
- **Docs/contract.yaml:**
  [páginas que exigem endpoints específicos]
- **Docs/entities.md:**
  [entidades que aparecem nas páginas]
- **Docs/plan.md / Docs/tasks.md:**
  [páginas prioritárias, bloqueantes ou fundacionais]
---
## 9. Síntese Operacional para Dev e AI
- **Páginas principais:** PG-001 · PG-002 · PG-003
- **Páginas mais críticas:** PG-001 · PG-002
- **Estados críticos:** [estado 1] · [estado 2] · [estado 3]
- **Regras inegociáveis:** [regra 1] · [regra 2]
- **Indefinições:** [ponto 1] · [ponto 2]
---
## 10. Aprovação
- **Status de aprovação:** [pendente / aprovado / revisando]
- **Aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
