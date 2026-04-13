# Histórias de Usuário
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão do documento:** [v1, v2, etc.]
- **Status:** [rascunho / revisando / aprovado]
- **Documento base:** `Docs/project.md`
- **Data de criação:** [dd/mm/aaaa]
- **Última atualização:** [dd/mm/aaaa]
---
## 2. Objetivo do Documento
- **Finalidade:**
  definir histórias de usuário, critérios de aceite e valor funcional esperado
- **Cobre:**
  perfis de usuário · histórias · objetivos funcionais · critérios de aceite ·
  dependências funcionais · prioridades iniciais
- **Não cobre:**
  layout detalhado · arquitetura técnica · modelagem profunda de entidades ·
  contrato detalhado da API · tasks técnicas de implementação
---
## 3. Perfis de Usuário
### Perfil 1 — [nome do perfil]
- **Descrição:** [quem é esse usuário]
- **Objetivo principal:** [o que quer alcançar]
- **Contexto de uso:** [quando, como e em qual situação usa o sistema]
- **Dores/necessidades principais:** [dor 1] · [dor 2] · [dor 3]
### Perfil 2 — [nome do perfil]
- **Descrição:** [quem é esse usuário]
- **Objetivo principal:** [o que quer alcançar]
- **Contexto de uso:** [quando, como e em qual situação usa o sistema]
- **Dores/necessidades principais:** [dor 1] · [dor 2] · [dor 3]
### Perfil 3 — [nome do perfil]
- **Descrição:** [quem é esse usuário]
- **Objetivo principal:** [o que quer alcançar]
- **Contexto de uso:** [quando, como e em qual situação usa o sistema]
- **Dores/necessidades principais:** [dor 1] · [dor 2] · [dor 3]
---
## 4. Regras de Escrita das Histórias
- **Estrutura padrão:**
  Como [perfil], quero [ação/capacidade], para [benefício/valor]
- **Cada história deve conter:**
  contexto · valor entregue · critério de aceite · observações/dependências
---
## 5. Histórias de Usuário
### US-001 — [título da história]
- **Perfil:** [perfil principal]
- **História:** Como **[perfil]**, quero **[ação]**, para **[benefício]**.
- **Objetivo funcional:** [o que precisa entregar na prática]
- **Valor gerado:** [valor ao usuário ou negócio]
- **Contexto:** [quando a necessidade aparece]
- **Pré-condições:** [pré-condição 1] · [pré-condição 2]
- **Pós-condições esperadas:** [resultado 1] · [resultado 2]
- **Critérios de aceite:** [critério 1] · [critério 2] · [critério 3]
- **Exceções/edge cases:** [edge case 1] · [edge case 2]
- **Dependências:** [dependência 1] · [dependência 2]
- **Prioridade:** [alta / média / baixa]
- **Observações:** [preencher]
### US-002 — [título da história]
- **Perfil:** [perfil principal]
- **História:** Como **[perfil]**, quero **[ação]**, para **[benefício]**.
- **Objetivo funcional:** [explique]
- **Valor gerado:** [explique]
- **Contexto:** [descreva]
- **Pré-condições:** [pré-condição 1]
- **Pós-condições esperadas:** [resultado 1]
- **Critérios de aceite:** [critério 1] · [critério 2]
- **Exceções/edge cases:** [edge case 1]
- **Dependências:** [dependência 1]
- **Prioridade:** [alta / média / baixa]
- **Observações:** [preencher]
### US-003 — [título da história]
- **Perfil:** [perfil principal]
- **História:** Como **[perfil]**, quero **[ação]**, para **[benefício]**.
- **Objetivo funcional:** [explique]
- **Valor gerado:** [explique]
- **Contexto:** [descreva]
- **Pré-condições:** [pré-condição 1]
- **Pós-condições esperadas:** [resultado 1]
- **Critérios de aceite:** [critério 1] · [critério 2]
- **Exceções/edge cases:** [edge case 1]
- **Dependências:** [dependência 1]
- **Prioridade:** [alta / média / baixa]
- **Observações:** [preencher]
---
## 6. Agrupamento por Jornada / Módulo
### Jornada / Módulo: [nome]
- **Objetivo da jornada:** [descreva]
- **Histórias relacionadas:** US-001 · US-002
- **Observações:** [preencher]
### Jornada / Módulo: [nome]
- **Objetivo da jornada:** [descreva]
- **Histórias relacionadas:** US-003 · US-004
- **Observações:** [preencher]
---
## 7. Priorização Inicial
- **Alta prioridade:** US-001 — [título] · US-002 — [título]
- **Média prioridade:** US-003 — [título]
- **Baixa prioridade:** US-004 — [título]
- **Justificativa da priorização:** [explique]
---
## 8. Dependências Funcionais Entre Histórias
- **Dependências conhecidas:** US-002 depende de US-001 · US-004 depende de US-003
- **Bloqueios potenciais:** [bloqueio 1] · [bloqueio 2]
---
## 9. Regras Funcionais Transversais
- **Regras multi-histórias:** [regra 1] · [regra 2] · [regra 3]
- **Permissões/perfis/restrições transversais:** [regra 1] · [regra 2]
- **Estados comuns esperados:**
  loading · vazio · erro · sucesso · sem permissão · indisponibilidade externa
---
## 10. Diretrizes para os Próximos Documentos
- **Docs/pages.md:** [quais telas devem nascer das histórias]
- **Docs/flow.md:** [quais jornadas/transições precisam ser modeladas]
- **Docs/design-system.md:** [componentes, padrões ou variações necessárias]
- **Docs/tokens.json:**
  [necessidade de tema, escala, semântica visual ou consistência]
- **Docs/entities.md:** [conceitos de domínio e dados que surgem]
- **Docs/contract.yaml:** [capacidades de API ou integração sugeridas]
- **Docs/plan.md / Docs/tasks.md:**
  [histórias fundacionais, críticas ou dependentes]
---
## 11. Síntese Operacional para Dev e AI
- **Perfis principais:** [perfil 1] · [perfil 2]
- **Jornadas principais:** [jornada 1] · [jornada 2]
- **Histórias de maior prioridade:** US-001 · US-002 · US-003
- **Garantias da implementação:** [garantia 1] · [garantia 2] · [garantia 3]
- **O que ainda está indefinido:** [ponto 1] · [ponto 2]
---
## 12. Aprovação
- **Status de aprovação:** [pendente / aprovado / revisando]
- **Aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
