# Briefing

## 0. Limites Obrigatórios
- Ao gerar o documento oficial `Docs/brief.md`, respeitar os limites abaixo.
- **Máximo de linhas:** `200`
- **Máximo por linha:** `89` caracteres
- Se ultrapassar, condensar sem remover seções, perguntas e intenção do template.
- **Checagem direta (shell):**
  `wc -l Docs/brief.md`
  `awk 'length>89{print NR ":" length ":" $0}' Docs/brief.md`

---

## 1. Identificação do Projeto
- **Nome do projeto:** [preencher]
- **Resumo em 1 frase:** [descreva em uma frase clara e objetiva]
- **Responsável principal:** [preencher]
- **Stakeholders envolvidos:** [nome / papel] · [nome / papel]
- **Data de criação do briefing:** [dd/mm/aaaa]
- **Versão:** [v1, v2, etc.]

---

## 2. Contexto
- **Qual é o contexto do projeto?**
  [cenário atual, problema percebido, oportunidade ou demanda que originou o projeto]
- **Por que esse projeto está sendo criado agora?** [motivo do timing]
- **Existe histórico anterior relevante?**
  [projetos antigos, tentativas, legado, processos atuais, problemas recorrentes]

---

## 3. Problema
- **Qual problema principal o projeto resolve?** [problema central]
- **Quais dores específicas existem hoje?** [dor 1] · [dor 2] · [dor 3]
- **Quem é impactado por esse problema?** [perfis afetados]
- **O que acontece se não for resolvido?**
  [impacto operacional, financeiro, estratégico ou de experiência]

---

## 4. Objetivo
- **Objetivo principal do projeto:** [resultado principal esperado]
- **Objetivos secundários:** [objetivo 1] · [objetivo 2] · [objetivo 3]
- **Transformação esperada após a entrega:**
  [como o cenário muda depois que o projeto estiver pronto]

---

## 5. Público-Alvo / Usuários
- **Quem vai usar ou ser impactado?** [perfil 1] · [perfil 2] · [perfil 3]
- **Qual é o perfil desses usuários?**
  [nível técnico, contexto de uso, comportamento, necessidades]
- **Qual problema cada perfil quer resolver?**
  [perfil]: [problema/necessidade] · [perfil]: [problema/necessidade]

---

## 6. Escopo Inicial
- **O que este projeto deve fazer?** [item 1] · [item 2] · [item 3]
- **O que é obrigatório no MVP / primeira versão?**
  [item obrigatório 1] · [item obrigatório 2] · [item obrigatório 3]
- **O que é desejável, mas não obrigatório agora?**
  [item desejável 1] · [item desejável 2]
- **O que está explicitamente fora de escopo?**
  [fora de escopo 1] · [fora de escopo 2] · [fora de escopo 3]

---

## 7. Mercado / Nicho
- **Em qual nicho ou mercado se encaixa?**
  [educação, saúde, logística, financeiro, SaaS interno, marketplace, delivery]
- **Como esse mercado funciona hoje?** [contexto resumido]
- **Particularidades do nicho que afetam o projeto?**
  [regras, comportamento, sazonalidade, operação, linguagem do setor]

---

## 8. Concorrência / Referências
- **Concorrentes, referências ou soluções parecidas?**
  [nome / link / observação] · [nome / link / observação]
- **O que essas referências fazem bem?** [ponto positivo 1] · [ponto positivo 2]
- **O que fazem mal ou deixam a desejar?** [ponto fraco 1] · [ponto fraco 2]
- **Que experiência queremos seguir, evitar ou superar?** [descreva]

---

## 9. Regras de Negócio
- **Existem regras de negócio já conhecidas?** [regra 1] · [regra 2] · [regra 3]
- **Existem validações, permissões ou restrições por perfil?** [descreva]
- **Existem etapas obrigatórias, aprovações ou condicionais?** [descreva]

---

## 10. Requisitos e Expectativas
- **Quais resultados mínimos são esperados?** [resultado 1] · [resultado 2]
- **O que define este projeto como bem-sucedido?** [descreva]
- **Quais expectativas importantes precisam ser respeitadas?**
  [expectativa 1] · [expectativa 2]

---

## 11. Restrições
- **Restrições técnicas:** [restrição 1] · [restrição 2]
- **Restrições de negócio:** [restrição 1] · [restrição 2]
- **Restrições operacionais:** [restrição 1] · [restrição 2]
- **Restrições legais ou regulatórias:** [restrição 1] · [restrição 2]
- **Restrições de prazo:** [descreva]
- **Restrições de orçamento:** [descreva]

---

## 12. Plataformas e Canais
- **Onde o projeto será usado?**
  [web] · [mobile] · [admin] · [api] · [interno] · [outro]
- **Existe plataforma prioritária?** [descreva]
- **Existe limitação de dispositivo, navegador ou ambiente?** [descreva]

---

## 13. Integrações e Dependências Conhecidas
- **O projeto depende de serviços externos?**
  [serviço / motivo] · [serviço / motivo]
- **Integrações definidas ou esperadas?** [integração 1] · [integração 2]
- **Dependências internas entre times, sistemas ou pessoas?** [descreva]

---

## 14. Riscos e Incertezas
- **Quais são os principais riscos conhecidos?** [risco 1] · [risco 2] · [risco 3]
- **Quais pontos ainda estão indefinidos?**
  [ponto indefinido 1] · [ponto indefinido 2]
- **Quais decisões ainda precisam ser tomadas?** [decisão 1] · [decisão 2]

---

## 15. Critérios de Sucesso
- **Como será medido o sucesso do projeto?**
  [métrica 1] · [métrica 2] · [métrica 3]
- **Quais indicadores importam mais?** [descreva]
- **Existe meta de adoção, conversão, redução de erro, tempo ou receita?**
  [descreva]

---

## 16. Prioridade
- **Qual é a prioridade do projeto?** [alta / média / baixa]
- **Qual é a urgência do projeto?** [alta / média / baixa]
- **Existe deadline relevante?** [descreva]
- **Existe algum marco importante?** [marco 1] · [marco 2]

---

## 17. Resumo Executivo
- **Resumo objetivo do projeto:** [resuma o projeto em 5 a 10 linhas]
- **Problema central:** [resuma]
- **Objetivo central:** [resuma]
- **Escopo inicial:** [resuma]
- **Restrições mais importantes:** [resuma]

---

## 18. Síntese Operacional para Dev e AI
- **18.1 Entendimento do projeto:**
  [descreva em linguagem direta o que está sendo construído]
- **18.2 O que parece ser mais importante:**
  [prioridade 1] · [prioridade 2] · [prioridade 3]
- **18.3 O que não pode ser perdido de vista:**
  [restrição crítica 1] · [restrição crítica 2]
- **18.4 O que ainda está em aberto:** [aberto 1] · [aberto 2]
- **18.5 Próximos documentos que devem nascer deste briefing:**
  `Docs/project.md` · `Docs/stack.md` · `Docs/user-stories.md`

---

## 19. Aprovação
- **Briefing aprovado por:** [preencher]
- **Data de aprovação:** [dd/mm/aaaa]
- **Observações finais:** [preencher]
