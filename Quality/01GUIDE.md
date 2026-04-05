# Guia do Pilar Quality

Guia oficial do pilar de qualidade.

## Princípio operacional

Fidelidade máxima para produção com pragmatismo controlado.

## Escopo

1. Definir requisitos de validação para task.
2. Definir evidências mínimas para fechamento.
3. Definir critério de reprovação e reabertura.

## Regras nucleares

1. Toda task deve encerrar com Quality Gate aprovado.
2. Sem evidência de qualidade, a task não pode ser marcada como concluída.
3. Testes devem priorizar ambiente realista e comportamento observável.
4. Política anti-mock/stub/placeholder é obrigatória, com exceção formal.
5. Mudanças com impacto em interface devem possuir teste e2e.
6. Mudanças mobile devem validar BrowserStack (ou alternativa) e dispositivo físico local para fluxos críticos.
7. Mudanças de API devem usar Curl e scripts reproduzíveis.
8. Dependências devem ter versões compatíveis e lockfile atualizado.
9. Todo resultado de qualidade deve ser registrado em `Docs/tasks.md`.

## Entradas obrigatórias

1. `Docs/plan.md`
2. `Docs/tasks.md`
3. `Docs/control.md`
4. `Quality/gate.md`

## Saída obrigatória

1. Task concluída com gate aprovado e evidência registrada em `Docs/tasks.md`.

## Fontes oficiais

1. `gate.md`
2. `realistic-tests.md`
3. `anti-mock.md`
4. `code-style.md`
5. `dependencies.md`

## Regra de precedência

1. Contrato vigente
2. Documento-fonte do domínio
3. `gate.md`
4. `Docs/plan.md` e `Docs/tasks.md`
5. Implementação atual
