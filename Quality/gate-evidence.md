# Gate Evidence

## Objetivo

Operacionalizar o Quality Gate definindo:

1. formato padrao de evidencia por tipo de validacao;
2. criterio de aplicabilidade ("quando aplicavel") por ferramenta;
3. definicao de "fluxo critico";
4. classificacao de severidade dos criterios de bloqueio;
5. template de quality gate pronto para uso em `Docs/tasks.md`.

Este arquivo complementa `validation-rules.md`, que define o que validar.
Este arquivo define como registrar e quando cada criterio se aplica.

## Regra de ownership

1. Formato de evidencia por tipo: aqui.
2. O que validar e criterios de bloqueio: `validation-rules.md`.
3. Thresholds numericos: `metrics.md`.
4. Checklist de revisao de codigo: `review-checklist.md`.

## Definicao de fluxo critico

Um fluxo e considerado critico quando sua falha em producao:

1. impede o usuario de completar a acao principal do produto;
2. envolve autenticacao, autorizacao ou acesso a dados sensiveis;
3. envolve transacao financeira ou operacao irreversivel;
4. e parte do core do negocio sem substituto imediato no contexto do usuario.

Exemplos de fluxos criticos:

1. login, logout, recuperacao de senha;
2. checkout, pagamento, confirmacao de pedido;
3. onboarding de usuario com criacao de conta;
4. envio de formulario com dados sensiveis;
5. acoes de administracao com impacto irreversivel.

Exemplos de fluxos nao criticos:

1. pagina de perfil somente leitura;
2. listagem de historico sem acao;
3. configuracoes cosmeticas de interface.

## Criterio de aplicabilidade por ferramenta

### Typecheck

Aplicavel quando o projeto usa linguagem com tipagem estatica: TypeScript, Go, Java, Kotlin, Swift, Dart, Rust, C#.

Nao aplicavel para projetos exclusivamente em JavaScript sem tipagem, Python sem mypy configurado, ou linguagens dinamicas sem checagem estatica ativa no projeto.

### Build

Aplicavel quando o projeto tem:

1. etapa de compilacao (TypeScript para JS, Go, Java, Kotlin, etc.);
2. bundling (Vite, Webpack, Rollup, esbuild, etc.);
3. geracao de artefato de deploy (Docker image, APK, IPA, binary).

Nao aplicavel para projetos de script puro sem etapa de build definida.

### Testcontainers

Aplicavel quando a task envolve integracao com:

1. banco de dados (PostgreSQL, MySQL, MongoDB, Redis, etc.);
2. fila de mensagens (RabbitMQ, Kafka, etc.);
3. servico de cache;
4. qualquer dependencia de infraestrutura com estado.

Nao aplicavel em tasks exclusivamente de interface sem chamada de infraestrutura real.

### E2e

Aplicavel quando a task afeta:

1. fluxo critico de interface web (conforme definicao acima);
2. mudanca visual em tela com acao de usuario de alto impacto.

Nao aplicavel em tasks exclusivamente de backend sem impacto de interface.

### Mobile (BrowserStack / dispositivo fisico)

Aplicavel quando a task afeta:

1. fluxo critico em interface mobile (iOS ou Android);
2. comportamento especifico de plataforma mobile.

Nao aplicavel em tasks exclusivamente de backend ou web sem equivalente mobile.

### Curl / scripts

Aplicavel quando a task:

1. cria ou altera endpoint HTTP;
2. altera contrato de API (request, response, status code, headers);
3. implementa integracao com API externa.

Nao aplicavel em tasks sem exposicao ou consumo de endpoint HTTP.

## Classificacao de severidade dos criterios de bloqueio

### Blocker

Trava fechamento da task em qualquer contexto. Sem excecao valida.

1. Ausencia de evidencia registrada quando o criterio era aplicavel.
2. Mock, stub ou placeholder sem excecao formal completa em `Docs/tasks.md`.
3. Validacao de API sem curl reproduzivel quando ha endpoint HTTP afetado.
4. Lockfile inconsistente ou com conflito nao resolvido.
5. Risco critico sem mitigacao ou plano de acao documentado.

### Contextual

Trava fechamento quando o criterio de aplicabilidade for atendido.
Quando nao aplicavel, registrar "N/A" com justificativa objetiva.

1. Typecheck ausente quando ha linguagem tipada no projeto.
2. Build ausente quando ha etapa de compilacao ou bundling.
3. Testcontainers ausente quando ha dependencia de infraestrutura na task.
4. E2e ausente quando ha fluxo critico de interface web afetado.
5. Mobile ausente quando ha fluxo critico mobile afetado.
6. Curl/scripts ausentes quando ha endpoint HTTP criado ou alterado.

### Advisory

Nao bloqueia o fechamento, mas deve ser registrado na task.

1. Lint com warnings sem erros.
2. Risco residual identificado com plano de acompanhamento.
3. Excecao de mock aprovada com prazo de remocao documentado.

## Formato de evidencia por tipo

### Lint

```
Lint: <aprovado / reprovado> | <comando> | <resultado resumido>

Exemplo:
Lint: aprovado | npm run lint | 0 erros, 0 warnings
Lint: reprovado | npm run lint | 3 erros, 2 warnings — bloqueador ativo
```

### Typecheck

```
Typecheck: <aprovado / reprovado / N/A> | <comando> | <resultado> | aplicavel: <sim/nao — motivo>

Exemplos:
Typecheck: aprovado | npx tsc --noEmit | sem erros de tipo | aplicavel: sim — TypeScript
Typecheck: N/A | aplicavel: nao — projeto JavaScript sem tipagem estatica
```

### Build

```
Build: <aprovado / reprovado / N/A> | <comando> | <resultado resumido>

Exemplos:
Build: aprovado | npm run build | artefato gerado em /dist sem erros
Build: N/A | aplicavel: nao — projeto de script sem etapa de build
```

### Testes

```
Testes: <X passed, Y failed> | suite: <nome> | ambiente: <descricao> | <comando>

Exemplos:
Testes: 14 passed, 0 failed | suite: integracao | ambiente: Testcontainers + PostgreSQL 15 | npm run test:integration
Testes: 8 passed, 0 failed | suite: unitarios | ambiente: Node 20 | npm test
```

### Contrato de API

```
Contrato de API: <aprovado / reprovado / N/A> | endpoint: <METHOD /caminho> | resultado: <HTTP status + resumo>
Comando: <curl completo e reproduzivel>
Script versionado: <caminho no repositorio>

Exemplo:
Contrato de API: aprovado | endpoint: POST /api/users | resultado: HTTP 201 com id gerado
Comando: curl -s -X POST http://localhost:3000/api/users -H "Content-Type: application/json" -d '{"name":"test","email":"test@example.com"}' | jq .
Script versionado: scripts/validate-users.sh
```

### E2e

```
E2e: <aprovado / reprovado / N/A> | ferramenta: <nome> | fluxo: <descricao> | resultado: <X passed, Y failed>

Exemplos:
E2e: aprovado | ferramenta: Playwright | fluxo: cadastro de usuario | resultado: 3 passed, 0 failed
E2e: N/A | aplicavel: nao — task sem impacto em interface web
```

### Mobile

```
Mobile: <aprovado / reprovado / N/A> | ferramenta: <nome> | dispositivo: <modelo + OS> | fluxo: <descricao> | resultado: <resumo>

Exemplos:
Mobile: aprovado | ferramenta: BrowserStack | dispositivo: iPhone 14, iOS 17 | fluxo: login e checkout | sem regressao
Mobile: N/A | aplicavel: nao — task sem impacto em interface mobile
```

### Lockfile

```
Lockfile: <consistente / atualizado / inconsistente>

Exemplos:
Lockfile: consistente | sem alteracao pos-instalacao
Lockfile: atualizado | dependencia axios atualizada de 1.6.0 para 1.7.2
```

### Rastreabilidade

```
Rastreabilidade: TASK-ID: <id> | commit: <hash> | arquivos: <lista de caminhos tocados>

Exemplo:
Rastreabilidade: TASK-ID: TASK-005 | commit: abc1234 | arquivos: src/users/handler.ts, src/users/service.ts
```

## Template de quality gate para tasks.md

Copiar e preencher em cada task concluida:

```markdown
**Quality Gate:** [aprovado / reprovado]
**Evidências de qualidade:**
- Lint: [aprovado / reprovado] | `<comando>` | <resultado>
- Typecheck: [aprovado / reprovado / N/A] | `<comando>` | <resultado> | aplicável: <sim/não — motivo>
- Build: [aprovado / reprovado / N/A] | `<comando>` | <resultado>
- Testes: [X passed, Y failed] | suite: <nome> | ambiente: <descrição> | `<comando>`
- Contrato de API: [aprovado / N/A] | endpoint: <METHOD /caminho> | resultado: <HTTP status> | script: <caminho>
- E2e: [aprovado / N/A] | ferramenta: <nome> | fluxo: <descrição> | resultado: <X passed>
- Mobile: [aprovado / N/A] | ferramenta: <nome> | dispositivo: <modelo> | fluxo: <descrição>
- Lockfile: [consistente / atualizado]
- Rastreabilidade: TASK-ID: <id> | commit: <hash> | arquivos: <lista>
```

### Exemplo preenchido

```markdown
**Quality Gate:** aprovado
**Evidências de qualidade:**
- Lint: aprovado | `npm run lint` | 0 erros, 0 warnings
- Typecheck: aprovado | `npx tsc --noEmit` | sem erros de tipo | aplicável: sim — TypeScript
- Build: aprovado | `npm run build` | artefato gerado em /dist sem erros
- Testes: 14 passed, 0 failed | suite: integração | ambiente: Testcontainers + PostgreSQL 15 | `npm run test:integration`
- Contrato de API: aprovado | endpoint: POST /api/users | resultado: HTTP 201 com id gerado | script: `scripts/validate-users.sh`
- E2e: aprovado | ferramenta: Playwright | fluxo: cadastro de usuário | resultado: 3 passed, 0 failed
- Mobile: N/A | aplicável: não — task sem impacto em interface mobile
- Lockfile: consistente | sem alteração pós-instalação
- Rastreabilidade: TASK-ID: TASK-005 | commit: abc1234 | arquivos: src/users/handler.ts, src/users/service.ts
```

## Integracao operacional

1. `validation-rules.md` define o que validar e os criterios de bloqueio por perfil de mudanca.
2. `gate-evidence.md` define como registrar evidencia e quando cada criterio se aplica.
3. O template deste arquivo e o formato de referencia para o campo `Evidencias de qualidade` em `Docs/tasks.md`.
4. `metrics.md` define thresholds numericos de qualidade estrutural, referenciados em `review-checklist.md`.
5. `review-checklist.md` e o gate de revisao de codigo; este arquivo e o gate de fechamento de task.
