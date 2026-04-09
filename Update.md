# Roadmap de Atualizações (Futuro)

## Visão

Transformar o Nebula Spec Kit em uma base de documentação mais eficiente para IA e
para devs, com menor custo de tokens, comandos mais diretos e melhor desempenho
operacional.

## Contexto

Em testes, modelos legados (ainda amplamente usados) interpretam pior documentação
em português e textos excessivamente verbosos. Isso aumenta o consumo de tokens e
reduz a performance.

Modelos mais recentes já evoluíram nesse ponto, mas o framework precisa atender bem
os dois cenários:
- modelos atuais;
- modelos legados.

## Objetivos Estratégicos

1. Migrar a documentação para inglês de forma gradual, priorizando arquivos de alto
impacto no contexto carregado.
2. Reduzir a verbosidade sem perder governança, rastreabilidade e qualidade.
3. Padronizar a escrita orientada a comandos diretos, com menos ambiguidade.
4. Preparar o Nebula para evolução em produto CLI/UI de documentação de projetos.

## Frentes de Atualização

### 1) Internacionalização (EN-first)
- Status: planejado.
- Prioridade: alta.
- Objetivo: reduzir custo de tokens e melhorar interpretação em modelos legados.
- Ação inicial: migrar os pilares principais (`instructions`, `Workflows`, `Skills`,
`Quality` e `Templates`) para inglês.

### 2) Compressão e Clareza
- Status: em andamento.
- Prioridade: alta.
- Objetivo: substituir textos explicativos longos por instruções operacionais curtas
e objetivas.
- Diretriz: manter 100% das responsabilidades com menos linhas.

### 3) Arquitetura de Templates
- Status: adiado (fase posterior).
- Prioridade: média.
- Escopo: consolidar e refatorar templates longos, com foco em performance de
contexto.
- Nota: a refatoração de `Templates/Full/architecture.md` foi analisada e ficará para
a próxima leva.

### 4) Productização (CLI/UI)
- Status: planejamento estratégico.
- Prioridade: média-alta.
- Objetivo: evoluir o framework para uma experiência CLI/UI nativa de documentação e
execução operacional.

## Critérios de Sucesso

1. Redução mensurável de tokens nos arquivos mais carregados pelo fluxo.
2. Menor ambiguidade em prompts e handoffs.
3. Melhor aderência de execução em modelos legados e atuais.
4. Manutenção da qualidade e da governança, sem perda de cobertura funcional.

## Próximos Passos

1. Definir a ordem oficial de migração `PT -> EN` por pasta.
2. Criar a baseline de medição (linhas, tokens e tempo de execução por task).
3. Aplicar refatoração incremental em lotes pequenos, com validação por etapa.
4. Revisitar `Templates/Full/architecture.md` na fase de templates.
