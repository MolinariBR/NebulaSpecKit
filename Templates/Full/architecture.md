# Architecture
## 1. Identificação
- **Nome do projeto:** [preencher]
- **Versão do documento:** [v1, v2, etc.]
- **Status:** [rascunho / revisando / aprovado]
- **Documentos base:**
  `Docs/project.md` · `Docs/stack.md` · `Docs/user-stories.md` ·
  `Docs/entities.md`
- **Data de criação:** [dd/mm/aaaa]
- **Última atualização:** [dd/mm/aaaa]
---
## 2. Objetivo do Documento
- **Finalidade:**
  [definir arquitetura do sistema: estrutura, camadas, módulos,
  responsabilidades, fluxos técnicos e diretrizes de evolução]
- **Cobre:**
  estilo arquitetural · camadas · módulos · dependências · integrações ·
  fluxo de dados · regras estruturais de implementação
- **Não cobre:**
  contrato detalhado de API · estrutura final de diretórios · migrations/SQL ·
  layout visual · tasks detalhadas de implementação
---
## 3. Visão Geral da Arquitetura
- **Resumo arquitetural:** [descreva em poucas linhas]
- **Estilo adotado:**
  modular · MVC · Clean · hexagonal · monólito modular · microserviços ·
  frontend/backend desacoplados · BFF · event-driven · híbrido
- **Justificativa da escolha:** [por que o estilo faz sentido]
- **Estratégia de evolução:**
  [começar simples e modularizar / preparado para escala / foco em manutenção]
---
## 4. Princípios Arquiteturais
- **Princípios base:**
  separação de responsabilidades · baixo acoplamento · alta coesão ·
  previsibilidade estrutural · domínio antes de framework ·
  infraestrutura isolada · contratos explícitos · testabilidade
- **Aplicação por princípio:**
  separação de responsabilidades: [como aplicar]
  baixo acoplamento: [como aplicar]
  alta coesão: [como aplicar]
  previsibilidade estrutural: [como aplicar]
  domínio antes de framework: [como aplicar]
  infraestrutura isolada: [como aplicar]
  contratos explícitos: [como aplicar]
  testabilidade: [como aplicar]
  evolução incremental: [como aplicar]
---
## 5. Contexto Arquitetural do Sistema
- **Tipo de sistema:**
  [web app / API / admin / worker / interno / plataforma / marketplace / SaaS]
- **Partes principais:**
  frontend · backend · banco · fila · cache · workers ·
  integrações externas · painel administrativo · outro
- **Visão macro do ecossistema:** [como as partes se comunicam]
---
## 6. Camadas da Arquitetura
- **Interface:**
  responsabilidade: [descreva]
  inclui: páginas · componentes · formulários · navegação ·
  interação com usuário
  não deve conter: regra de negócio complexa · persistência ·
  acoplamento indevido
- **Aplicação:**
  responsabilidade: [descreva]
  inclui: casos de uso · orquestração · validação de entrada · coordenação
  não deve conter: detalhes de banco · acoplamento forte de framework ·
  regra visual
- **Domínio:**
  responsabilidade: [descreva]
  inclui: entidades · regras centrais · invariantes · serviços de domínio
  não deve conter: transporte · persistência · dependência de interface
- **Infraestrutura:**
  responsabilidade: [descreva]
  inclui: banco · ORM/query builder · serviços externos · cache · fila ·
  storage
  não deve conter: regra central de negócio espalhada ·
  decisão funcional de UI
---
## 7. Módulos do Sistema
### Módulo 1 — [nome do módulo]
- **Objetivo:** [descreva]
- **Responsabilidades:** [responsabilidade 1] · [responsabilidade 2]
- **Entidades:** [entidade 1] · [entidade 2]
- **Casos de uso:** [caso 1] · [caso 2]
- **Dependências internas:** [dependência 1] · [dependência 2]
- **Dependências externas:** [integração 1] · [integração 2]
- **Observações:** [preencher]
### Módulo 2 — [nome do módulo]
- **Objetivo:** [preencher]
- **Responsabilidades:** [responsabilidade 1] · [responsabilidade 2]
- **Entidades:** [entidade 1]
- **Casos de uso:** [caso 1]
- **Dependências internas:** [dependência 1]
- **Dependências externas:** [integração 1]
- **Observações:** [preencher]
### Módulo 3 — [nome do módulo]
- **Objetivo:** [preencher]
- **Responsabilidades:** [responsabilidade 1]
- **Entidades:** [entidade 1]
- **Casos de uso:** [caso 1]
- **Dependências internas:** [dependência 1]
- **Dependências externas:** [integração 1]
- **Observações:** [preencher]
---
## 8. Fluxo Técnico de Dados
- **Fluxo técnico principal:** [descreva a jornada técnica do dado]
- **Exemplo textual:**
  1. Interface recebe ação do usuário.
  2. Aplicação valida entrada e orquestra o caso de uso.
  3. Domínio aplica regras de negócio.
  4. Infraestrutura persiste ou consulta dados.
  5. Integrações externas são acionadas, se necessário.
  6. Resultado retorna de forma estruturada para a interface.
- **Pontos críticos do fluxo:** [ponto 1] · [ponto 2] · [ponto 3]
---
## 9. Integrações Externas e Dependências Técnicas
- **Integrações previstas:** [integração 1] · [integração 2] · [integração 3]
- **Papel de cada integração:**
  [integração]: [função] · [integração]: [função]
- **Regras de isolamento:** [regra 1] · [regra 2]
- **Riscos arquiteturais de integração:** [risco 1] · [risco 2]
---
## 10. Persistência e Consistência
- **Estratégia de persistência:** [descreva]
- **Fonte principal de verdade:** [descreva]
- **Necessidades de consistência:**
  consistência imediata · consistência eventual · auditoria · idempotência ·
  concorrência
- **Cuidados relevantes:** [cuidado 1] · [cuidado 2]
---
## 11. Comunicação Entre Partes do Sistema
- **Padrão principal:**
  [REST / eventos / fila / chamada interna / RPC / GraphQL]
- **Comunicação síncrona:** [descreva]
- **Comunicação assíncrona:** [descreva]
- **Eventos ou mensagens previstos:** [evento 1] · [evento 2]
- **Regras de comunicação:** [regra 1] · [regra 2]
---
## 12. Estratégia de Escalabilidade e Evolução
- **Escalabilidade esperada:** [baixa / média / alta / progressiva]
- **Partes com maior chance de crescimento:** [parte 1] · [parte 2]
- **Partes que devem permanecer simples:** [parte 1] · [parte 2]
- **Estratégia de evolução arquitetural:** [descreva]
- **Sinais de refatoração futura:** [sinal 1] · [sinal 2] · [sinal 3]
---
## 13. Segurança e Isolamento
- **Pontos sensíveis:**
  autenticação · autorização · dados sensíveis · integrações externas ·
  arquivos · logs · ações destrutivas
- **Regras arquiteturais de segurança:** [regra 1] · [regra 2] · [regra 3]
- **Áreas com atenção extra:** [área 1] · [área 2]
---
## 14. Observabilidade e Operação
- **Necessidades operacionais:** logs estruturados · health checks ·
  métricas · alertas · rastreabilidade
- **Pontos observáveis:** [ponto 1] · [ponto 2] · [ponto 3]
- **Falhas rastreáveis:** [falha 1] · [falha 2]
---
## 15. Restrições e Trade-offs Arquiteturais
- **Restrições assumidas:** [restrição 1] · [restrição 2]
- **Trade-offs aceitos conscientemente:**
  [trade-off 1] · [trade-off 2] · [trade-off 3]
- **Alternativas não adotadas:**
  [alternativa 1 + motivo] · [alternativa 2 + motivo]
---
## 16. Relação com Outros Documentos
- **`Docs/entities.md`:** [como domínio influencia módulos e regras]
- **`Docs/contract.yaml`:** [como arquitetura expõe ou consome contratos]
- **`Docs/structure.md`:** [como arquitetura reflete em diretórios e camadas]
- **`Docs/deploy.md`:** [como arquitetura impacta ambientes, pipeline e operação]
- **`Docs/plan.md` / `Docs/tasks.md`:**
  [como partes arquiteturais orientam a ordem de implementação]
---
## 17. Diretrizes de Implementação
- **Dev e AI devem respeitar:**
  [diretriz 1] · [diretriz 2] · [diretriz 3]
- **Dev e AI devem evitar:** [erro 1] · [erro 2] · [erro 3]
- **Exigem revisão deste documento:**
  novo módulo estrutural · mudança de responsabilidade entre camadas ·
  nova integração crítica · mudança relevante de comunicação ·
  quebra da estratégia arquitetural inicial
---
## 18. Síntese Operacional para Dev e AI
- **18.1 Estilo arquitetural:** [resuma]
- **18.2 Módulos principais:** [módulo 1] · [módulo 2] · [módulo 3]
- **18.3 Regras que não podem ser quebradas:**
  [regra 1] · [regra 2] · [regra 3]
- **18.4 Pontos críticos da arquitetura:** [ponto 1] · [ponto 2]
- **18.5 O que ainda está indefinido:** [ponto 1] · [ponto 2]
---
## 19. Aprovação
- **Status de aprovação:** [pendente / aprovado / revisando]
- **Aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
