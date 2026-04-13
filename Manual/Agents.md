# Execução com Agentes

> Este manual cobre apenas o **delta** de execução com agentes.  
> O fluxo comum está em [Execution.md](Execution.md).

---

## Leitura Obrigatória

| # | Documento | Finalidade |
|---|-----------|------------|
| 1 | [Execution.md](Execution.md) | Fluxo base de execução |
| 2 | [../agents/README.md](../agents/README.md) | Catálogo de agentes |
| 3 | [CreateAgents/Baseline.md](CreateAgents/Baseline.md) | Contexto base de qualquer agente |

---

## Delta do Modo com Agentes

1. Selecionar o agente principal conforme o objetivo da task.
2. Carregar contexto base **e** contexto de especialidade do agente.
3. Declarar o formato de saída esperado **antes** da execução.
4. Quando necessário, fazer handoff para agente complementar.

---

## Escolha Rápida de Agente

```mermaid
flowchart TD
    START([Qual é o objetivo?]) --> Q1{Pedido vago\nou descoberta?}

    Q1 -->|Sim| SCOPE[🔍 Scope\ndescoberta e escopo]
    Q1 -->|Não| Q2{Envolve tela,\nUX ou protótipo?}

    Q2 -->|Sim| PRODUCT[🎨 Product\nproduto, fluxo e protótipo]
    Q2 -->|Não| Q3{Arquitetura,\ncontrato ou integração?}

    Q3 -->|Sim| SYSTEM[🏗️ System\narquitetura e contrato]
    Q3 -->|Não| Q4{Implementação,\nbug ou refatoração?}

    Q4 -->|Sim| EXECUTION[⚙️ Execution\nplan, tasks e implementação]
    Q4 -->|Não| Q5{Gate de qualidade\nou validação?}

    Q5 -->|Sim| QUALITY[✅ Quality\ngate e validação]
    Q5 -->|Não| Q6{Pronto para\ndeploy ou release?}

    Q6 -->|Sim| RELEASE[🚀 Release\nentrega e estabilização]
    Q6 -->|Não| RECOVERY[🔥 Recovery\nincidente e hotfix]
```

---

## Matriz de Papéis

| Agente | Chamar quando | Entrega esperada | Handoff comum |
|--------|---------------|------------------|---------------|
| **Scope** | Pedido vago, descoberta inicial, definição de limite | Escopo aprovado, objetivos mensuráveis, backlog inicial | Product · System · Execution |
| **Product** | Nova tela, mudança de UX/UI, necessidade de protótipo | User stories, páginas e fluxo claros para execução | System · Execution · Quality |
| **System** | Mudança de contrato, integração externa, decisão arquitetural | Arquitetura atualizada, contrato consistente, riscos técnicos | Execution · Quality |
| **Execution** | Implementação, bug fix, refatoração, evolução de módulo | Tasks com evidências, progresso em control, entrega rastreável | Quality · Release |
| **Quality** | Fechamento de task, dúvida de cobertura ou fidelidade | Decisão de gate, evidências, bloqueios objetivos | Execution · Release |
| **Release** | Escopo aprovado no gate e pronto para deploy | Release com checklist, monitoramento e rollback validado | Recovery · Execution |
| **Recovery** | Incidente em produção, hotfix emergencial | Correção validada, estabilização, causa raiz e prevenção | Quality · Release |

---

## Fluxo de Handoff Entre Agentes

```mermaid
flowchart LR
    SCOPE -->|"backlog definido"| PRODUCT
    SCOPE -->|"escopo técnico"| SYSTEM
    SCOPE -->|"direto para execução"| EXECUTION

    PRODUCT -->|"contrato/estrutura"| SYSTEM
    PRODUCT -->|"stories prontas"| EXECUTION
    PRODUCT -->|"validação de UX"| QUALITY

    SYSTEM -->|"estrutura aprovada"| EXECUTION
    SYSTEM -->|"risco técnico"| QUALITY

    EXECUTION -->|"task concluída"| QUALITY
    EXECUTION -->|"pronto para deploy"| RELEASE

    QUALITY -->|"gate reprovado"| EXECUTION
    QUALITY -->|"gate aprovado"| RELEASE

    RELEASE -->|"incidente pós-deploy"| RECOVERY
    RECOVERY -->|"estabilizado"| QUALITY
    RECOVERY -->|"correção validada"| RELEASE
```

### Registro obrigatório em todo handoff

1. O que foi **concluído**.
2. O que ficou **pendente**.
3. Qual agente deve **assumir**.
4. Quais **arquivos** devem ser carregados no próximo ciclo.

---

## Prompt Mínimo

```text
Use o agente: <AgentName>
Objetivo: <objetivo>
Workflow: Workflows/<workflow>.md
Contexto de execução: Docs/plan.md, Docs/tasks.md, Docs/control.md
Saída: plano, execução, evidências, riscos e pendências
```

---

## Checklist — Modo com Agentes

- [ ] Agente principal correto para a demanda
- [ ] Contexto base e contexto especializado carregados
- [ ] Handoff definido quando houver dependência entre papéis
- [ ] Saída registrada em `Docs/tasks.md` e `Docs/control.md`, quando aplicável