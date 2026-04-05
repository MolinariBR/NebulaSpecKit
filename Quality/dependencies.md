# Dependências e Compatibilidade

## Regras obrigatórias

1. Usar lockfile versionado no repositório.
2. Evitar ranges amplos para dependências criticas.
3. Garantir compatibilidade entre runtime, framework e bibliotecas.
4. Atualizacoes devem passar por Quality Gate completo.

## Validações mínimas

1. Instalacao limpa sem conflito de dependência.
2. Build e testes aprovados após atualização.
3. Registro da versão alterada e impacto em Docs/tasks.md.

## Restrições

1. Não introduzir biblioteca sem justificativa técnica.
2. Não manter dependência sem uso real.
3. Não atualizar dependência crítica sem evidências de compatibilidade.
