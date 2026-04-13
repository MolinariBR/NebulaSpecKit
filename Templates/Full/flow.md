# Fluxo
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão:** [v1]
- **Status:** [rascunho | revisando | aprovado]
- **Documentos base:** project.md · user-stories.md · pages.md · entities.md
- **Criado em:** [dd/mm/aaaa] · **Atualizado em:** [dd/mm/aaaa]
---
## 2. Escopo do Documento
- **Cobre:**
  jornadas · pontos de entrada · transições de página · condicionais ·
  desvios · estados de bloqueio · restrições por permissão
- **Não cobre:**
  layout visual · implementação técnica da navegação · arquitetura interna ·
  contrato de API · definição de componentes
---
## 3. Regras Gerais de Fluxo
- **Cada fluxo deve conter:**
  nome · perfil · objetivo · ponto de entrada · pré-condições · sequência
  principal · desvios · estados excepcionais · resultado esperado
- **Tipos de fluxo:**
  principal · alternativo · erro · administrativo · autenticação ·
  recuperação · confirmação · saída · restrito por permissão
---
## 4. Visão Geral das Jornadas
### JN-001 — [nome da jornada]
- **Perfil:** [perfil]
- **Objetivo:** [o que o usuário quer alcançar]
- **Histórias relacionadas:** US-001 · US-002
- **Páginas relacionadas:** PG-001 · PG-002 · PG-003
- **Ponto de entrada:** [onde a jornada começa]
- **Resultado esperado:** [resultado ao fim da jornada]
- **Observações:** [observações / nenhum]
### JN-002 — [nome da jornada]
- **Perfil:** [perfil]
- **Objetivo:** [descreva]
- **Histórias relacionadas:** US-003
- **Páginas relacionadas:** PG-004 · PG-005
- **Ponto de entrada:** [descreva]
- **Resultado esperado:** [descreva]
- **Observações:** [observações / nenhum]
<!-- duplicar bloco JN conforme necessário -->
---
## 5. Fluxos Detalhados
### FL-001 — [nome do fluxo]
- **Tipo:** [principal | alternativo | erro | auth | admin | etc.]
- **Perfil:** [perfil]
- **Objetivo:** [descreva]
- **Histórias relacionadas:** US-001
- **Páginas envolvidas:** PG-001 · PG-002 · PG-003
- **Ponto de entrada:** [onde o usuário entra neste fluxo]
- **Pré-condições:** [condição 1] · [condição 2]
- **Sequência principal:**
  1. Usuário acessa [PG-001].
  2. Sistema exibe [estado inicial].
  3. Usuário executa [ação].
  4. Sistema valida [condição].
  5. Usuário é direcionado para [PG-002].
  6. Sistema processa [evento].
  7. Usuário conclui [ação final] em [PG-003].
- **Condicionais:**
  se [condição] → [página/estado] · se [condição] → bloquear e mostrar
  [mensagem] · se [condição] → redirecionar para [página]
- **Desvios:** [desvio 1] · [desvio 2]
- **Estados excepcionais:**
  erro de validação · indisponibilidade externa · sessão expirada ·
  sem permissão · dados inexistentes · outro
- **Saídas possíveis:** [saída 1] · [saída 2]
- **Resultado esperado:** [fim ideal do fluxo]
- **Observações:** [observações / nenhum]
### FL-002 — [nome do fluxo]
- **Tipo:** [descreva]
- **Perfil:** [descreva]
- **Objetivo:** [descreva]
- **Histórias relacionadas:** US-002
- **Páginas envolvidas:** PG-004 · PG-005
- **Ponto de entrada:** [descreva]
- **Pré-condições:** [condição 1]
- **Sequência principal:** 1. [passo 1] 2. [passo 2] 3. [passo 3]
- **Condicionais:** [condição 1] · [condição 2]
- **Desvios:** [desvio 1]
- **Estados excepcionais:** [estado 1] · [estado 2]
- **Saídas possíveis:** [saída 1]
- **Resultado esperado:** [descreva]
- **Observações:** [observações / nenhum]
### FL-003 — [nome do fluxo]
- **Tipo:** [descreva]
- **Perfil:** [descreva]
- **Objetivo:** [descreva]
- **Histórias relacionadas:** US-003
- **Páginas envolvidas:** PG-006
- **Ponto de entrada:** [descreva]
- **Pré-condições:** [condição 1]
- **Sequência principal:** 1. [passo 1] 2. [passo 2]
- **Condicionais:** [condição 1]
- **Desvios:** [desvio 1]
- **Estados excepcionais:** [estado 1]
- **Saídas possíveis:** [saída 1]
- **Resultado esperado:** [descreva]
- **Observações:** [observações / nenhum]
<!-- duplicar bloco FL conforme necessário -->
---
## 6. Fluxos por Perfil
### Perfil: [nome do perfil]
- **Fluxos principais:** FL-001 · FL-002
- **Fluxos alternativos:** FL-003
- **Restrições:** [restrição 1] · [restrição 2]
- **Observações:** [observações / nenhum]
### Perfil: [nome do perfil]
- **Fluxos principais:** FL-004
- **Fluxos alternativos:** FL-005
- **Restrições:** [restrição 1]
- **Observações:** [observações / nenhum]
---
## 7. Pontos Críticos de Decisão
- **Decisões críticas do sistema:** [decisão 1] · [decisão 2] · [decisão 3]
- **Condições de bloqueio:** [bloqueio 1] · [bloqueio 2]
- **Condições de redirecionamento:** [redirecionamento 1] · [redirecionamento 2]
- **Condições de fallback:** [fallback 1] · [fallback 2]
---
## 8. Estados Transversais de Navegação
- **Estados em múltiplos fluxos:**
  loading · erro · sucesso · vazio · sem permissão · sessão expirada ·
  indisponibilidade externa · timeout · falha de autenticação
- **Diretriz de tratamento:** [como esses estados se comportam nos fluxos]
---
## 9. Dependências e Restrições Funcionais
- **Dependências entre fluxos:**
  FL-002 depende de FL-001 · FL-004 exige autenticação prévia
- **Restrições por perfil/permissão:** [restrição 1] · [restrição 2]
- **Fluxos críticos para MVP:** FL-001 · FL-002
- **Fluxos opcionais/futuros:** FL-005 · FL-006
---
## 10. Diretrizes para Próximos Documentos

| Documento | Como os fluxos impactam |
|----------|--------------------------|
| prototype/ | [fluxos e telas a prototipar primeiro] |
| design-system.md | [padrões recorrentes de interação e estados] |
| tokens.json | [semânticas visuais e estados que exigem token] |
| contract.yaml | [fluxos que indicam endpoints/respostas] |
| entities.md | [conceitos de domínio presentes] |
| plan.md / tasks.md | [fluxos prioritários, bloqueantes, fundacionais] |

---
## 11. Síntese Operacional para Dev e AI
- **Jornadas principais:** JN-001 · JN-002
- **Fluxos mais críticos:** FL-001 · FL-002 · FL-003
- **Regras inegociáveis:** [regra 1] · [regra 2]
- **Estados críticos:** [estado 1] · [estado 2] · [estado 3]
- **Indefinições:** [ponto 1] · [ponto 2]
---
## 12. Aprovação
- **Status:** [pendente | aprovado | revisando]
- **Aprovado por:** [nome]
- **Data:** [dd/mm/aaaa]
- **Observações:** [observações]
