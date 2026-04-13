# Release e Rollback da CLI

Este guia cobre build, publicacao e recuperacao da `nebula-spec-kit-cli`.

## 1. Pre-check local

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip pytest build twine
PYTHONPATH=src python -m pytest -q
python -m build
python -m twine check dist/*
```

## 2. Publicacao recomendada (GitHub Actions + Trusted Publisher)

1. Garanta que o `pyproject.toml` tem a versao correta.
2. Garanta que a branch `main` tem os checks obrigatorios verdes.
3. Crie e envie tag semver:

```bash
git tag -a vX.Y.Z -m "release: cli vX.Y.Z"
git push origin vX.Y.Z
```

4. Acompanhe o workflow `CLI Release PyPI` no GitHub Actions.
5. Valide no PyPI:
   - `https://pypi.org/project/nebula-spec-kit-cli/`

## 3. Fluxo TestPyPI -> PyPI (opcional)

Se houver conta no TestPyPI:

1. Rode `workflow_dispatch` apontando para TestPyPI (ou job separado).
2. Instale e valide:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple nebula-spec-kit-cli
nebu version
```

3. Publicar no PyPI oficial por tag semver.

Sem conta no TestPyPI, siga direto o fluxo de publicacao oficial por tag.

## 4. Rollback

PyPI nao permite remover e reutilizar a mesma versao. O rollback pratico e:

1. Corrigir problema no codigo.
2. Bump de versao (ex.: `0.1.0` -> `0.1.1`).
3. Publicar nova versao por tag.
4. Comunicar versao corrigida no changelog/release notes.

## 5. Hotfix rapido

```bash
# 1) corrigir codigo
# 2) atualizar versao no pacote
git commit -am "fix(cli): hotfix"
git tag -a vX.Y.Z -m "release: hotfix cli vX.Y.Z"
git push origin main --follow-tags
```

## 6. Troubleshooting

### Erro: "Non-user identities cannot create new projects"
- Causa comum: pending publisher configurado com nome de projeto diferente.
- Validar no PyPI:
  - project name: `nebula-spec-kit-cli`
  - owner: `MolinariBR`
  - repository: `NebulaSpecKit`
  - workflow: `cli-release-pypi.yml`
  - environment: `Any` (vazio), se workflow nao define environment.

### Erro: arquivo ja existe no PyPI
- Causa: tentativa de republicar mesma versao.
- Solucao: bump de versao e novo release.

### Erro de permissao no workflow
- Validar `permissions` do workflow:
  - `contents: read`
  - `id-token: write`

### CLI nao atualiza localmente
- Rode:

```bash
python -m pip install --upgrade nebula-spec-kit-cli
nebu version
```
