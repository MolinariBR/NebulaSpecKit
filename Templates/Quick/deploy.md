# Deploy

## Nome do projeto
[preencher]

## Estratégia operacional
[resuma como o projeto será hospedado, entregue e operado]

## Ambientes
- local
- development
- staging
- production

## Hospedagem
**Plataforma:** [preencher]  
**Modelo:** [VPS / PaaS / serverless / outro]

## Infraestrutura inicial
### Aplicação
- CPU: [preencher]
- Memória: [preencher]
- Armazenamento: [preencher]
- Banda: [preencher]

### Banco
- CPU: [preencher]
- Memória: [preencher]
- Armazenamento: [preencher]

### Serviços auxiliares
- cache: [sim/não]
- fila: [sim/não]
- storage: [sim/não]

## Variáveis e segredos
- onde ficam: [preencher]
- onde não devem ficar:
  - código
  - logs
  - arquivos versionados indevidos

## Qualidade antes do merge
- husky
- pre-commit
- lint
- typecheck
- testes mínimos
- build válido

## Branches
- main
- [deploy-branch]
- feature/*
- fix/*
- hotfix/*
- task/*

## CI/CD
**Plataforma:** GitHub Actions

**CI:**  
- install
- lint
- typecheck
- testes
- build

**CD:**  
- deploy
- migração, se aplicável
- health check
- validação pós-deploy

## Versionamento e release
- estratégia: [semver / outro]
- release por: [tag / branch / manual]
- changelog: [sim/não]

## Logs e observabilidade
- logs estruturados
- parser normalizado
- níveis: info, warn, error, debug
- campos mínimos:
  - timestamp
  - nível
  - serviço
  - ambiente
  - mensagem
  - contexto

## Pós-deploy
- health check
- smoke tests
- validação de endpoints críticos

## Banco e backup
- migração: [manual / automática / híbrida]
- backup: [sim/não]
- restauração: [como será feita]

## Rollback
- estratégia: [preencher]
- quando usar:
  - falha crítica
  - indisponibilidade
  - quebra de fluxo principal

## Segurança operacional
- segredos fora do código
- acesso restrito
- logs sem vazamento
- rastreabilidade de deploy

## Síntese para Dev e AI
**Infra e hospedagem:**  
[resumo]

**Pipeline e branches:**  
[resumo]

**Regras que devem ser respeitadas:**  
- [regra 1]
- [regra 2]

**O que ainda está indefinido:**  
- [ponto 1]
- [ponto 2]