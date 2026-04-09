# Estrutura

## 1. Identificação

**Nome do projeto:**
[preencher]

**Versão do documento:**
[v1, v2, etc.]

**Status:**
[rascunho / revisando / aprovado]

**Documentos base:**
[referência a Docs/stack.md, Docs/architecture.md, Docs/contract.yaml, Docs/deploy.md e Docs/plan.md]

**Data de criação:**
[dd/mm/aaaa]

**Ultima atualização:**
[dd/mm/aaaa]

---

## 2. Objetivo do Documento

**Finalidade deste documento:**
Definir a organização oficial de diretórios e arquivos do projeto para garantir previsibilidade, rastreabilidade e coerência com a arquitetura.

**O que este documento cobre:**
- arvore raiz do repositório
- organização por área e responsabilidade
- convenções de nomeação
- regras de localização de código, testes e scripts
- limites entre documentação, implementação e operação

**O que este documento não cobre:**
- implementação detalhada de casos de uso
- regras visuais detalhadas (DesignSystem/Tokens)
- contrato funcional específico de cada endpoint

---

## 3. Princípios Estruturais

- A estrutura fisica deve refletir a arquitetura lógica.
- Cada pasta deve ter responsabilidade clara.
- Arquivos devem ser localizados por domínio e não por conveniência momentanea.
- Testes, scripts e automações devem ter local proprio.
- Evitar pasta genérica sem dono funcional.
- Evitar duplicacao de fonte de verdade.

---

## 4. Estrategia de Organização

**Estrategia recomendada:**
[modular por domínio] + [camadas internas por responsabilidade]

**Modelo operacional:**
- Documentação de governança na raiz e em pastas dedicadas (Skills, Workflows, Quality).
- Documentação oficial do projeto em Docs/.
- Protótipos navegáveis em Docs/Prototype/.
- Templates em Templates/.
- Código de execução em apps/, services/, packages/ ou src/, conforme stack do projeto.

---

## 5. Arvore Estrutural Canônica (Raiz)

```text
.
├── README.md
├── GUIDE.md
├── Docs/
│   ├── README.md
│   ├── brief.md
│   ├── project.md
│   ├── stack.md
│   ├── user-stories.md
│   ├── pages.md
│   ├── flow.md
│   ├── design-system.md
│   ├── tokens.json
│   ├── entities.md
│   ├── architecture.md
│   ├── contract.yaml
│   ├── structure.md
│   ├── deploy.md
│   ├── plan.md
│   ├── tasks.md
│   ├── control.md
│   └── Prototype/
│       ├── README.md
│       ├── index.html
│       ├── pages/
│       └── assets/
├── Quality/
│   ├── README.md
│   ├── execution-policy.md
│   ├── structure-rules.md
│   ├── clean-rules.md
│   ├── metrics.md
│   ├── review-checklist.md
│   ├── realistic-tests.md
│   ├── anti-mock.md
│   ├── dependencies.md
│   └── validation-rules.md
├── Skills/
│   ├── README.md
│   └── *.md
├── Workflows/
│   ├── 00README.md
│   ├── 01GUIDE.md
│   └── *.md
├── Templates/
│   ├── Full/
│   └── Quick/
├── apps/                # opcional, conforme stack
├── services/            # opcional, conforme stack
├── packages/            # opcional, conforme stack
├── src/                 # opcional, conforme stack
├── tests/               # opcional, conforme stack
├── scripts/             # opcional, conforme stack
└── .github/
    └── workflows/
```

---

## 6. Responsabilidade por Pasta

- Docs/Prototype/: protótipos HTML de validação de interface e fluxo.
- Docs/: fonte de verdade de governança, execução e qualidade do projeto.
- Quality/: políticas obrigatórias de qualidade e gate.
- Skills/: conhecimento reutilizável por domínio técnico.
- Workflows/: fluxo operacional por tipo de mudança.
- Templates/: modelos oficiais de artefatos Full e Quick.
- apps/, services/, packages/, src/: implementação de produto.
- tests/: testes automatizados por nível (unitário, integração, e2e).
- scripts/: automações executáveis (build, teste, verificacao, release).
- .github/workflows/: pipelines de CI/CD.

---

## 7. Convenções de Nomeacao

### 7.1 Arquivos

- Raiz: README.md e GUIDE.md.
- Pastas de governança: README.md (preferencial) ou 00README.md + 01GUIDE.md (legado).
- Artefatos oficiais do projeto em Docs/: nomes curtos em minúsculo (ex.: project.md, plan.md, tasks.md).
- Skills: README.md e nome.md.
- Workflows: nome.md.
- Templates Full: nome-curto-em-ingles.md|yaml|json.
- Templates Quick: mesmo nome do Full, em Templates/Quick/.

### 7.2 Pastas

- Nome sem espaco, com maiuscula inicial para pastas de governança.
- Nome em minúsculo para pastas de código executável.

### 7.3 IDs de rastreio

- Tasks: TASK-001, TASK-002, ...
- Fases: FASE-01, FASE-02, ...
- Milestones: M1, M2, ...

---

## 8. Regras de Localização de Conteúdo

- Não armazenar documento de governança dentro de pasta de código.
- Não salvar documento oficial do projeto fora de Docs/.
- Não armazenar script operacional dentro de pasta de testes sem justificativa.
- Não misturar contrato de API com descrição de regra de negócio fora de Docs/contract.yaml e documentos-fonte.
- Não duplicar o mesmo conteúdo em arquivos diferentes sem declaracao de fonte de verdade.

---

## 9. Regras de Criação e Edição

- A primeira task deve ser de bootstrap_estrutural.
- No bootstrap, criar toda a arvore prevista para o projeto.
- A partir da task seguinte, somente editar arquivos já existentes.
- Cada task concluída deve gerar exatamente 1 commit.
- Toda task deve registrar hash do commit, arquivos tocados e Quality Gate.

---

## 10. Regras de Qualidade Estrutural

- Estrutura deve ser verificavel por script.
- Alteração estrutural deve atualizar structure.md e, quando necessário, plan.md e tasks.md.
- Não concluir task com Quality Gate reprovado.
- Manter compatibilidade de dependências conforme Quality/dependencies.md.

---

## 11. Regras para Dev e AI

- Antes de editar, localizar arquivo oficial da responsabilidade.
- Não criar novos caminhos em task de edição.
- Toda alteração estrutural deve ser explicita e rastreavel.
- Em caso de conflito entre documentos, seguir a regra de precedência do framework.

---

## 12. Checklist de Aderencia Estrutural

- ( ) A arvore raiz esta coerente com o framework.
- ( ) Pastas de governança (Quality, Skills, Workflows) existem e estão completas.
- ( ) Docs/Prototype/ existe para validação visual de fluxos.
- ( ) Estrutura de código executável esta definida (apps/, services/, packages/ ou src/).
- ( ) tests/ e scripts/ estão definidos quando aplicável.
- ( ) Regra de bootstrap e regra de edição foram respeitadas.

---

## 13. Síntese Operacional

**Este documento define:**
- onde cada coisa deve existir
- como nomear
- como evoluir sem degradar organização

**Este documento evita:**
- crescimento desordenado
- acoplamento estrutural acidental
- perda de rastreabilidade em tarefas

**Este documento exige:**
- consistência com arquitetura
- consistência com metodologia
- consistência com qualidade
