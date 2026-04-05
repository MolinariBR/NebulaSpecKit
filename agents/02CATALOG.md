# Catálogo de Agentes

Este documento descreve cada agente, suas responsabilidades, quando chamar, o que deve entregar e quando fazer handoff.

## Como usar este catálogo

1. Identifique o tipo de demanda.
2. Escolha o agente principal na matriz de roteamento.
3. Chame o agente com contexto obrigatório (base + especialidade + execução quando aplicável).
4. Se a demanda cruzar domínios, execute handoff explícito para o agente seguinte.

## Matriz de roteamento rápido

- Descoberta de escopo e objetivos: ScopeAgent
- Definição de produto, telas e fluxo: ProductAgent
- Arquitetura, contrato e integrações: SystemAgent
- Planejamento e execução por tasks: ExecutionAgent
- Qualidade e validação de fechamento: QualityAgent
- Deploy, release e rollout: ReleaseAgent
- Incidentes, hotfix e estabilização: RecoveryAgent

## ScopeAgent

- Função principal: definir problema, escopo e objetivos mensuráveis.
- Responsabilidades:
  - Consolidar contexto de negócio e restrições.
  - Definir objetivo, escopo in e escopo out.
  - Produzir base para plan e tasks.
- Chamar quando:
  - O pedido ainda está vago.
  - O time precisa alinhar sucesso e limites antes de implementar.
- Entregas esperadas:
  - Escopo aprovado.
  - Objetivos mensuráveis.
  - Backlog inicial priorizado.
- Handoff comum:
  - Para ProductAgent (quando houver fluxo/tela).
  - Para SystemAgent (quando houver arquitetura/contrato).
  - Para ExecutionAgent (quando iniciar implementação).

## ProductAgent

- Função principal: transformar necessidade de negócio em fluxo e especificação de interface.
- Responsabilidades:
  - Definir user stories, páginas e fluxo.
  - Conectar design-system e tokens.
  - Garantir clareza para implementação.
- Chamar quando:
  - Há nova tela, mudança de UI ou necessidade de protótipo.
- Entregas esperadas:
  - User stories e critérios de aceite funcionais.
  - Páginas e fluxo mapeados.
  - Impacto de UI documentado para execução.
- Handoff comum:
  - Para SystemAgent (impactos técnicos).
  - Para ExecutionAgent (quebra em tasks).
  - Para QualityAgent (validação E2E/interface).

## SystemAgent

- Função principal: modelar arquitetura, entidades, contrato e integrações.
- Responsabilidades:
  - Definir estrutura técnica e fronteiras.
  - Modelar contrato de API e entidades.
  - Planejar integrações externas.
- Chamar quando:
  - Há mudança de contrato.
  - Há nova integração.
  - Há decisão arquitetural relevante.
- Entregas esperadas:
  - Arquitetura e estrutura atualizadas.
  - Contrato consistente e versionado.
  - Riscos técnicos e mitigações.
- Handoff comum:
  - Para ExecutionAgent (implementação em tasks).
  - Para QualityAgent (validação técnica e de compatibilidade).

## ExecutionAgent

- Função principal: planejar e executar entrega por task com rastreabilidade.
- Responsabilidades:
  - Manter plan, tasks e control consistentes.
  - Executar workflow adequado por tipo de demanda.
  - Garantir governança de commit por task.
- Chamar quando:
  - Há implementação, bug fix, refatoração ou evolução de módulo.
- Entregas esperadas:
  - Tasks atualizadas com evidências.
  - Progresso registrado no control.
  - Artefatos técnicos editados conforme governança.
- Handoff comum:
  - Para QualityAgent (aprovação final).
  - Para ReleaseAgent (quando pronto para deploy/release).

## QualityAgent

- Função principal: validar qualidade e aprovar/reprovar fechamento de task.
- Responsabilidades:
  - Aplicar Quality Gate obrigatório.
  - Exigir testes realistas, e2e e política anti-mock.
  - Validar padrão de código e dependências.
- Chamar quando:
  - Uma task está pronta para fechamento.
  - Há dúvida sobre cobertura e fidelidade de produção.
- Entregas esperadas:
  - Decisão de gate (aprovado/reprovado).
  - Evidências de testes e critérios faltantes.
  - Lista objetiva de bloqueios.
- Handoff comum:
  - Para ExecutionAgent (ajustes de implementação).
  - Para ReleaseAgent (se aprovado para entrega).

## ReleaseAgent

- Função principal: conduzir deploy/release com evidências e rollback.
- Responsabilidades:
  - Executar plano de deploy.
  - Validar observabilidade e estabilidade pós-release.
  - Registrar evidências operacionais.
- Chamar quando:
  - O escopo passou no Quality Gate e vai para entrega.
- Entregas esperadas:
  - Release executado com checklist completo.
  - Evidências de monitoramento.
  - Plano de rollback pronto e validado.
- Handoff comum:
  - Para RecoveryAgent (se incidente ocorrer).
  - Para ExecutionAgent (ajustes pós-release).

## RecoveryAgent

- Função principal: responder incidentes e executar hotfix com segurança.
- Responsabilidades:
  - Conter incidente.
  - Corrigir causa principal com rastreabilidade.
  - Estabilizar e registrar aprendizado.
- Chamar quando:
  - Existe incidente em produção.
  - É necessário hotfix emergencial.
- Entregas esperadas:
  - Correção aplicada e validada.
  - Evidências de estabilização.
  - Causa raiz e ação preventiva registradas.
- Handoff comum:
  - Para QualityAgent (validação de fechamento).
  - Para ReleaseAgent (publicação do hotfix).

## Protocolo de chamada

Para manter padrão único e evitar divergência:

1. Use o prompt base canônico em `Manual/15CREATE-AGENT-BASELINE.md`.
2. Substitua apenas o `<AgentName>` e os arquivos de especialidade conforme este catálogo.
3. Em cada ferramenta, aplique somente o delta descrito em `Manual/07...14`.

## Regra de handoff entre agentes

- O agente atual deve encerrar com:
  - Status do que foi concluído.
  - Pendências objetivas.
  - Nome do próximo agente recomendado.
  - Lista mínima de contexto que o próximo agente precisa carregar.

## Checklist de definição de agente

Antes de criar um novo agente:

1. O novo agente tem responsabilidade que não cabe nos 7 atuais.
2. O novo agente usa conjunto de contexto realmente diferente.
3. O novo agente reduz risco de sobreposição operacional.
4. O novo agente tem workflow e entrega claramente distintos.
