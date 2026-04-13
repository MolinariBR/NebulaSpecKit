# Nebu CLI

CLI Python para inicializar a estrutura documental do Nebula.

## Comandos

- `nebu start`
- `nebu version`
- `nebu update`

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
- `release-pypi.yml`: publica no TestPyPI (manual) e PyPI (tag `vX.Y.Z`).

Autenticacao de publish:

- Trusted Publishers (OIDC), sem token no workflow.
- Configurar publisher no TestPyPI e no PyPI:
  - owner/repo: `MolinariBR/NebulaSpecKit`
  - workflow: `.github/workflows/cli-release-pypi.yml`
  - ambiente TestPyPI: `testpypi`
  - ambiente PyPI: `pypi`
