# Plan

## 1. Identificacao
- **Projeto:** Nebula CLI Bootstrap
- **Versao:** v3
- **Status:** revisando
- **Escopo tecnico:** CLI Python distribuida via PyPI
- **Data:** [dd/mm/aaaa]

## 2. Objetivo
Implementar e publicar a CLI `nebu` para inicializar a estrutura Nebula
no projeto alvo, sem quebrar o CI/release ja existente do NebulaSpecKit.

## 3. Escopo
- Comandos: `start`, `version`, `update`, `--help`
- Bootstrap idempotente sem preencher conteudo em `Docs/`
- Suporte a `--root`, `--profile`, `--dry-run`, `--force`
- Manifesto em `.nebula/manifest.json`
- Pipeline de publicacao em PyPI separado do release atual
- Documentacao de uso para usuario e mantenedor

## 4. Fora de Escopo
- Geracao automatica de conteudo dentro de `Docs/`
- Wizard interativo
- Plugin system
- Comandos avancados (`doctor`, `migrate`, `repair`)

## 5. Comandos Basicos
- `nebu start`: cria estrutura fisica Nebula
- `nebu version`: mostra versao instalada da CLI
- `nebu update`: consulta ultima versao no PyPI
- `nebu update --apply`: executa upgrade do pacote
- `nebu --help`: lista comandos e flags

## 6. Regras de Compatibilidade
- Nao remover ou substituir `.github/workflows/release.yml`
- Nao alterar o contrato atual de quality gate documental
- Adicionar workflow PyPI de forma complementar
- Preservar gatilhos atuais de release de artefato GitHub
- Tratar mudancas de CI Python como incrementais e reversiveis

## 7. Workflow Atual Observado
- `ci.yml`: roda para `*.md`, `*.yaml`, `*.json` e workflows
- `_quality-gate.yml`: valida estrutura documental, JSON e YAML
- `release.yml`: cria tag e GitHub Release com zip/tar.gz
- `links-scheduled.yml`: rotina agendada de links

## 8. Estrategia de Release PyPI sem Quebra
- Manter `release.yml` como esta
- Criar `release-pypi.yml` separado
- Trigger recomendado:
  - `workflow_dispatch` para testes iniciais
  - tag semver (`vX.Y.Z`) apos validacao
- Metodo de autenticacao:
  - Trusted Publishers (OIDC) para TestPyPI e PyPI
  - sem `PYPI_API_TOKEN` no workflow de publish
- Publicar primeiro em TestPyPI, depois PyPI

## 9. Arquitetura Proposta da CLI
- `src/nebu_cli/__main__.py`
- `src/nebu_cli/commands/start.py`
- `src/nebu_cli/commands/version.py`
- `src/nebu_cli/commands/update.py`
- `src/nebu_cli/core/fs.py`
- `src/nebu_cli/core/manifest.py`
- `src/nebu_cli/specs/structure.py`

## 10. Estrutura Criada por `nebu start`
- `.nebula/`
- `GUIDE.md` (se ausente)
- `Docs/Prototype/`
- Arquivos vazios em `Docs/`:
  - `brief.md`, `project.md`, `stack.md`, `user-stories.md`
  - `pages.md`, `flow.md`, `design-system.md`, `tokens.json`
  - `entities.md`, `architecture.md`, `contract.yaml`, `structure.md`
  - `deploy.md`, `plan.md`, `tasks.md`, `control.md`

## 11. Fases de Implementacao
### Fase 01 - Contrato
- Fechar contrato CLI multi-comando
- Validar regra de arquivos `Docs/` vazios
- Congelar regra de idempotencia

### Fase 02 - Implementacao
- Parser e roteamento
- `start`, `version`, `update`
- Manifesto `.nebula/manifest.json`

### Fase 03 - Empacotamento
- `pyproject.toml`
- `python -m build`
- Teste local de instalacao

### Fase 04 - CI/CD
- Ajustar CI para incluir Python sem remover cobertura atual
- Adicionar workflow dedicado de publish PyPI
- Validar fluxo por `workflow_dispatch`

### Fase 05 - Release
- Publicar em TestPyPI
- Publicar em PyPI
- Documentar rollback e hotfix de pacote

## 12. Comandos Operacionais Minimos
- Build local:
  - `python -m pip install --upgrade build twine`
  - `python -m build`
- Validacao local:
  - `python -m twine check dist/*`
- Publicacao via GitHub Actions:
  - `workflow_dispatch` com `target=testpypi`
  - tag `vX.Y.Z` para publish em PyPI
- Uso usuario:
  - `python -m pip install nebu`
  - `nebu start`
  - `nebu update --apply`

## 13. Criterios de Aceite
- `nebu start` cria estrutura esperada sem conteudo em `Docs/`
- Reexecucao sem `--force` nao sobrescreve arquivos existentes
- `--dry-run` nao grava nada em disco
- `nebu version` retorna versao instalada
- `nebu update` compara local x PyPI
- Workflow PyPI funciona sem impactar `release.yml`

## 14. Riscos e Mitigacoes
- **Risco:** sobrescrever arquivo do usuario
  - **Mitigacao:** sem overwrite por padrao + resumo final
- **Risco:** colisao com release atual
  - **Mitigacao:** workflow PyPI separado
- **Risco:** CI deixar de validar docs
  - **Mitigacao:** manter quality gate atual e adicionar checks Python
- **Risco:** falha de update automatico
  - **Mitigacao:** modo check-only e comando manual de fallback

## 15. Dependencias
- Python 3.11+
- stdlib: `argparse`, `pathlib`, `json`, `subprocess`, `urllib`
- `pytest` para testes
- `build` e `twine` para empacotamento/publicacao

## 16. Aprovacao
- **Status:** pendente
- **Aprovado por:** [preencher]
- **Data:** [dd/mm/aaaa]
