# Nebu CLI

CLI Python para inicializar a estrutura documental do Nebula.

## Comandos

- `nebu start`
- `nebu version`
- `nebu update`

## Instalação

```bash
python -m pip install nebula-spec-kit-cli
```

## Desenvolvimento local

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip pytest build twine
PYTHONPATH=src python -m pytest -q
python -m build
python -m twine check dist/*
```

## CI/CD

Workflows criados em `.github/workflows`:

- `ci.yml`: roda testes, build e `twine check`.
- `release-pypi.yml`: publica no PyPI por `workflow_dispatch` e por tag `vX.Y.Z`.

Autenticacao de publish:

- Trusted Publishers (OIDC), sem token no workflow.
- Configurar publisher no PyPI:
  - owner/repo: `MolinariBR/NebulaSpecKit`
  - workflow: `.github/workflows/cli-release-pypi.yml`
  - ambiente PyPI: `pypi`
