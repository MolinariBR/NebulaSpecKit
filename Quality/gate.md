# Quality Gate

Checklist obrigatório para fechar uma task.

## Critérios obrigatórios

1. Lint aprovado.
2. Typecheck aprovado (quando aplicável).
3. Build aprovado (quando aplicável).
4. Testes realistas executados conforme `realistic-tests.md`.
5. Sem uso de mock/stub/placeholder fora de exceção formal registrada.
6. Impacto de API validado com Curl e scripts reproduzíveis (quando aplicável).
7. Impacto de interface validado com e2e (quando aplicável).
8. Impacto mobile validado em BrowserStack (ou alternativa) e dispositivo físico local para fluxos críticos.
9. Dependências e lockfile consistentes.
10. Evidências registradas na task.

## Evidências mínimas na task

- Resultado de lint/typecheck/build.
- Resultado de testes (incluindo ambiente usado).
- Comandos Curl e scripts executados (quando houver API).
- Relatório e2e de fluxos críticos (quando houver UI).
- Evidência de validação mobile (quando houver app mobile).
- Hash do commit da task e lista de arquivos tocados.

## Regra de bloqueio

Se qualquer critério obrigatório falhar, a task deve permanecer aberta.
