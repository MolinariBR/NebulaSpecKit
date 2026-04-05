# Testes Realistas

Política de testes para maximizar fidelidade de produção.

## Regras centrais

1. Priorizar testes contra componentes reais e infraestrutura realista.
2. Evitar simulações que escondam comportamento de produção.
3. Registrar ambiente, dados e comandos para reprodução.

## Backend e API

1. Testes de integração devem usar Testcontainers por padrão.
2. Contrato de API deve ser validado com Curl e scripts versionados.
3. Cobrir cenários de erro realista: timeout, indisponibilidade e validação.

## Interface Web

1. Fluxos críticos devem ter teste e2e obrigatório.
2. Mudança visual relevante deve ser validada com Prototype e e2e.

## Mobile

1. Testes de fluxo critico devem executar em BrowserStack ou alternativa gratuita viavel.
2. Deve haver validação em pelo menos um dispositivo físico local para fluxos críticos.

## Evidências obrigatórias

1. Comandos executados.
2. Resultado final (pass/fail) por suite.
3. Ambiente e versões utilizadas.
4. Vinculo com TASK-ID.
