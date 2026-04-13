# Tasks

## 1. Identificacao
- **Projeto:** Nebula CLI Bootstrap
- **Versao:** v3
- **Status:** revisando
- **Base:** `plan.md` + `contrato.yaml`

## 2. Regras Operacionais
- Uma task por commit
- Nao quebrar contrato definido em `contrato.yaml`
- `nebu start` nao pode preencher conteudo em `Docs/`
- Validar idempotencia em toda mudanca de filesystem
- Nao substituir `release.yml` existente do NebulaSpecKit
- Publicacao PyPI em workflow dedicado

## 3. Fase 01 - Contrato e Compatibilidade
### TASK-001 - Revisar contrato multi-comando
- **Objetivo:** consolidar `start`, `version` e `update`
- **Aceite:** contrato sem ambiguidade e alinhado ao repo atual
- **Dependencia:** nenhuma
- **Status:** concluida
- **Checklist:**
  - [x] Definir inputs/outputs por comando
  - [x] Definir regra de `update --apply`
  - [x] Definir politica de release por tag
  - [x] Definir regra de compatibilidade com `release.yml`

### TASK-002 - Congelar spec de estrutura do `start`
- **Objetivo:** mapear diretorios e arquivos canonicos
- **Aceite:** spec fechada com regra de arquivos vazios em `Docs/`
- **Dependencia:** TASK-001
- **Status:** concluida
- **Checklist:**
  - [x] Listar diretorios obrigatorios
  - [x] Listar arquivos obrigatorios em `Docs/`
  - [x] Confirmar regra de arquivos vazios

## 4. Fase 02 - Implementacao da CLI
### TASK-003 - Criar entrypoint e parser principal
- **Objetivo:** rotear `start`, `version` e `update`
- **Aceite:** `nebu --help` funcional com subcomandos
- **Dependencia:** TASK-002
- **Status:** concluida
- **Checklist:**
  - [x] Parser principal implementado
  - [x] Subcomandos registrados
  - [x] Help validado

### TASK-004 - Implementar `nebu start`
- **Objetivo:** bootstrap idempotente da estrutura Nebula
- **Aceite:** primeira execucao cria; segunda sem `--force` preserva
- **Dependencia:** TASK-003
- **Status:** concluida
- **Checklist:**
  - [x] Criar diretorios canonicos
  - [x] Criar arquivos vazios em `Docs/`
  - [x] Implementar `--dry-run`
  - [x] Implementar `--force`
  - [x] Garantir que `GUIDE.md` so seja criado se ausente

### TASK-005 - Implementar `nebu version`
- **Objetivo:** exibir versao instalada da CLI
- **Aceite:** comando retorna versao sem erro
- **Dependencia:** TASK-003
- **Status:** concluida
- **Checklist:**
  - [x] Ler versao do pacote
  - [x] Exibir em saida padrao
  - [x] Cobrir fallback quando metadado faltar

### TASK-006 - Implementar `nebu update`
- **Objetivo:** verificar release no PyPI e orientar atualizacao
- **Aceite:** check-only funcional + `--apply` funcional
- **Dependencia:** TASK-003
- **Status:** concluida
- **Checklist:**
  - [x] Consultar ultima versao no PyPI
  - [x] Comparar com versao local
  - [x] Exibir comando manual de upgrade
  - [x] Implementar `--apply` via `pip install --upgrade nebu`

### TASK-007 - Implementar `.nebula/manifest.json`
- **Objetivo:** persistir metadados minimos de bootstrap
- **Aceite:** manifesto criado e atualizado em execucoes validas
- **Dependencia:** TASK-004
- **Status:** concluida
- **Checklist:**
  - [x] Criar manifesto no primeiro bootstrap
  - [x] Atualizar `last_run_at`
  - [x] Garantir consistencia com contrato

## 5. Fase 03 - Empacotamento
### TASK-008 - Estruturar pacote Python para PyPI
- **Objetivo:** configurar `pyproject.toml` e build
- **Aceite:** `python -m build` gera `sdist` e `wheel`
- **Dependencia:** TASK-003
- **Status:** concluida
- **Checklist:**
  - [x] Definir metadata do pacote
  - [x] Definir entrypoint `nebu`
  - [x] Validar build local
  - [x] Validar `twine check dist/*`

## 6. Fase 04 - CI/CD sem quebra
### TASK-009 - Ajustar CI para incluir Python
- **Objetivo:** ampliar validacoes sem remover o quality gate atual
- **Aceite:** CI valida docs e codigo Python da CLI
- **Dependencia:** TASK-008
- **Status:** em validacao
- **Checklist:**
  - [x] Incluir paths Python no gatilho do CI
  - [x] Adicionar job/lint/test para CLI
  - [x] Preservar job de quality gate documental
  - [ ] Validar execucao do workflow em PR real

### TASK-010 - Criar workflow de publish PyPI dedicado
- **Objetivo:** publicar pacote sem alterar `release.yml`
- **Aceite:** publish por tag semver em workflow separado
- **Dependencia:** TASK-009
- **Status:** validada com bloqueio externo
- **Checklist:**
  - [x] Criar `release-pypi.yml` separado
  - [x] Configurar Trusted Publisher (OIDC) no fluxo
  - [x] Garantir permissao `id-token: write` no workflow
  - [x] Definir environment: `pypi`
  - [x] Validar `workflow_dispatch` no GitHub Actions
  - [x] Validar trigger por tag (`vX.Y.Z`)
  - [ ] Resolver bloqueio de publish real no PyPI para o nome `nebu`

## 7. Fase 05 - Testes e Documentacao
### TASK-011 - Testes unitarios e integracao
- **Objetivo:** cobrir parser, filesystem e comandos
- **Aceite:** suite passando em CI
- **Dependencia:** TASK-004, TASK-005, TASK-006, TASK-007
- **Status:** nao iniciada
- **Checklist:**
  - [ ] Cobrir `start`
  - [ ] Cobrir `version`
  - [ ] Cobrir `update`
  - [ ] Cobrir `start --dry-run`
  - [ ] Cobrir idempotencia

### TASK-012 - Guia operacional de release e rollback
- **Objetivo:** guiar mantenedor com fluxo completo
- **Aceite:** documento claro para build, publish e rollback
- **Dependencia:** TASK-010, TASK-011
- **Status:** nao iniciada
- **Checklist:**
  - [ ] Comandos basicos documentados
  - [ ] Fluxo de publish PyPI via OIDC documentado
  - [ ] Procedimento de rollback documentado
  - [ ] Troubleshooting basico documentado

## 8. Checklist de Fechamento
- [ ] Contrato respeitado integralmente
- [ ] Arquivos `Docs/*` criados vazios
- [ ] Idempotencia comprovada
- [ ] `version` funcionando
- [ ] `update` funcionando
- [ ] `release.yml` atual preservado
- [ ] Publish PyPI funcionando em workflow dedicado
- [ ] Testes passando
- [ ] Documentacao atualizada
