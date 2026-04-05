# Quality

Guia operacional consolidado de Quality do Nébula Framework.

## Objetivo

Este documento define o padrão de qualidade obrigatório para garantir fidelidade de produção, reduzir falso-positivo e manter previsibilidade de entrega por task.

## Proposta do pilar

Quality responde **como validar de forma confiável** uma entrega antes de fechar uma task.

Ele não substitui:

1. Workflow (sequência de execução)
2. Skill (especialidade técnica)
3. Artefatos oficiais em `Docs/` (fonte de verdade)

> [!IMPORTANT]
> Nenhuma task pode ser concluída sem Quality Gate aprovado e evidências registradas.

## Fontes analisadas

### Núcleo do framework

- `README.md`
- `GUIDE.md`
- `Docs/README.md`

### Guides e readmes do framework

- `Manual/00README.md`, `Manual/01GUIDE.md`
- `Skills/00README.md`, `Skills/01GUIDE.md`
- `Workflows/00README.md`, `Workflows/01GUIDE.md`
- `Quality/00README.md`, `Quality/01GUIDE.md`
- `Templates/Full/00README.md`, `Templates/Full/01GUIDE.md`
- `Templates/Quick/00README.md`, `Templates/Quick/01GUIDE.md`
- `agents/00README.md`, `agents/01GUIDE.md`
- `agents/behavior/00README.md`, `agents/behavior/01GUIDE.md`
- `Prototype/00README.md`, `Prototype/01GUIDE.md`
- `NebulaWeb/README.md`

### Documentação de quality

- `Quality/gate.md`
- `Quality/realistic-tests.md`
- `Quality/anti-mock.md`
- `Quality/code-style.md`
- `Quality/dependencies.md`

### Documento web atual

- `NebulaWeb/content/docs/quality.md`

## Regras canônicas de qualidade

1. Toda task encerra com Quality Gate aprovado.
2. Sem evidência objetiva, a task permanece aberta.
3. Testes devem priorizar ambiente realista e comportamento observável.
4. Mock/stub/placeholder é proibido por padrão, com exceção formal controlada.
5. Mudança com impacto de UI exige teste e2e.
6. Mudança de API exige validação com Curl e scripts reproduzíveis.
7. Mudança mobile crítica exige BrowserStack (ou alternativa) e dispositivo físico local.
8. Dependências devem manter lockfile e compatibilidade comprovada.
9. Resultado de qualidade deve ser registrado em `Docs/tasks.md` e refletido em `Docs/control.md`.

> [!WARNING]
> Fechar task sem gate aprovado quebra governança do framework e invalida a rastreabilidade da entrega.

## Quality Gate

Arquivo-fonte: `Quality/gate.md`.

### Critérios obrigatórios

| #     | Critério                                              | Aplicação                        |
|-------|-------------------------------------------------------|----------------------------------|
| 1     | Lint aprovado                                         | Sempre                           |
| 2     | Typecheck aprovado                                    | Quando aplicável                 |
| 3     | Build aprovado                                        | Quando aplicável                 |
| 4     | Testes realistas executados                           | Sempre                           |
| 5     | Sem mock/stub/placeholder fora de exceção formal      | Sempre                           |
| 6     | Validação de API com Curl/scripts reproduzíveis       | Quando há API                    |
| 7     | Validação e2e dos fluxos críticos                     | Quando há UI                     |
| 8     | Validação mobile em BrowserStack + dispositivo físico | Quando há app mobile             |
| 9     | Dependências e lockfile consistentes                  | Sempre                           |
| 10    | Evidências completas registradas na task              | Sempre                           |

### Evidências mínimas por task

```text
- Resultado de lint, typecheck e build
- Resultado de testes (suite, ambiente e versões)
- Comandos Curl/scripts executados (quando há API)
- Relatório e2e dos fluxos críticos (quando há UI)
- Evidência de validação mobile (quando há app mobile)
- Hash do commit da task e lista de arquivos tocados
```

> [!CAUTION]
> Se qualquer critério falhar, a task não fecha. O gate é binário: aprovado ou reprovado.

## Testes realistas

Arquivo-fonte: `Quality/realistic-tests.md`.

Princípio: validar com componentes reais e infraestrutura realista, evitando simulações que escondem comportamento de produção.

### Backend e API

1. Testes de integração com Testcontainers por padrão.
2. Contrato de API validado com Curl e scripts versionados.
3. Cobertura de erro realista: timeout, indisponibilidade e validação.

### Interface web

1. Fluxos críticos com teste e2e obrigatório.
2. Mudança visual relevante validada com Prototype e e2e.

### Mobile

1. Fluxos críticos validados em BrowserStack (ou alternativa viável).
2. Fluxos críticos validados também em dispositivo físico local.

### Evidências obrigatórias de teste

```text
1. Comandos executados
2. Resultado final (pass/fail) por suite
3. Ambiente e versões utilizadas
4. Vínculo com TASK-ID
```

## Política anti-mock

Arquivo-fonte: `Quality/anti-mock.md`.

Regra geral: mock, stub e placeholder são proibidos por padrão em integração, contrato, e2e e release.

### Exceção controlada

Só é permitida com inviabilidade técnica temporária e registro completo na task:

```text
1. Justificativa técnica objetiva
2. Escopo exato da exceção
3. Prazo de remoção
4. Risco assumido
5. Plano de substituição por validação real
```

> [!IMPORTANT]
> Sem esse registro completo, o QualityAgent deve reprovar o gate.

## Padrão de código

Arquivo-fonte: `Quality/code-style.md`.

### Limites obrigatórios

| Escopo                                          | Limite                         |
|-------------------------------------------------|--------------------------------|
| Caracteres por linha                            | 120                            |
| Linhas por arquivo de regra de negócio          | 300                            |
| Linhas por função/método                        | 80 (salvo exceção justificada) |

### Regras de legibilidade

1. Nome de símbolo deve refletir responsabilidade real.
2. Evitar função com múltiplas responsabilidades.
3. Evitar comentário redundante.
4. Tratar erros com mensagens claras e acionáveis.

### Exceção de limite

Exceções devem ser registradas em `Docs/tasks.md` com justificativa técnica explícita.

## Dependências e compatibilidade

Arquivo-fonte: `Quality/dependencies.md`.

### Regras obrigatórias

1. Lockfile versionado no repositório.
2. Evitar ranges amplos em dependências críticas.
3. Garantir compatibilidade entre runtime, framework e bibliotecas.
4. Atualização de dependência passa por Quality Gate completo.

### Validações mínimas

```text
1. Instalação limpa sem conflito
2. Build e testes aprovados após atualização
3. Registro de versão alterada e impacto em Docs/tasks.md
```

### Restrições

1. Não introduzir biblioteca sem justificativa técnica.
2. Não manter dependência sem uso real.
3. Não atualizar dependência crítica sem evidências de compatibilidade.

## Integração com execução por task

```text
1. Selecionar workflow principal da task
2. Executar mudança técnica com skill adequada
3. Aplicar Quality Gate completo
4. Registrar evidências em Docs/tasks.md
5. Atualizar status em Docs/control.md
6. Fechar com 1 commit por task
```

> [!NOTE]
> Quality valida a saída técnica, mas também valida disciplina operacional (rastreabilidade, evidência e governança).

## Ordem de leitura recomendada

```text
1. Quality/01GUIDE.md
2. Quality/realistic-tests.md
3. Quality/anti-mock.md
4. Quality/code-style.md
5. Quality/dependencies.md
6. Quality/gate.md
```

## Regra de precedência

1. Contrato vigente em `Docs/contract.yaml`
2. Documento-fonte do domínio em `Docs/`
3. `Quality/gate.md`
4. `Docs/plan.md` e `Docs/tasks.md`
5. Implementação atual

## Antipadrões

1. Fechar task com checklist parcial de qualidade.
2. Marcar “aprovado” sem comando/resultado reproduzível.
3. Validar API sem Curl/scripts versionados.
4. Validar UI sem e2e em fluxos críticos.
5. Usar mock sem exceção formal registrada.
6. Atualizar dependência crítica sem evidência de compatibilidade.

## Comandos úteis

```bash
cd /home/mau/molinari/Framework

# listar documentos do pilar Quality
ls Quality

# revisar readmes/guides usados como base
rg --files | rg '(README\.md|GUIDE\.md|00README\.md|01GUIDE\.md)$' | sort

# revisar artefatos de execução e qualidade
ls Docs
```

## Encerramento

Resumo operacional: workflow organiza, skill especializa, quality valida, e `Docs/` prova a entrega.
