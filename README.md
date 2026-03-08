### A) Seção "Técnicas Aplicadas (Fase 2)": 

1. Role Prompting
A persona de "Product Manager Sênior com 10 anos de experiência em metodologias ágeis, especializada em BDD" define quem o modelo deve ser antes de qualquer instrução.

2. Chain of Thought (CoT)
O PASSO 1 — Classifique o bug instrui o modelo a raciocinar internamente sobre complexidade, ator, problemas e impacto antes de escrever qualquer linha da User Story.

3. Few-shot Learning
Os 3 exemplos completos (simples → médio → complexo) calibram entrada/saída para cada nível de complexidade, diretamente alinhados com o dataset de referência.

4. Skeleton of Thought
Os templates SIMPLES / MÉDIO / COMPLEXO estruturam a resposta em seções pré-definidas (User Story → Critérios BDD → Contexto Técnico → Tasks), garantindo que o modelo preencha um esqueleto fixo em vez de inventar estrutura livremente.

### B) Seção "Resultados Finais"

- Link Prompt V1: https://smith.langchain.com/hub/acsdev/bug_to_user_story_v1

- Link Prompt V2: https://smith.langchain.com/hub/acsdev/bug_to_user_story_v2

- Execução v1 ( FALHA )

```shell
╭─vscode@c15c76cfe8ea in /workspace/challenge-prompt-evaluation on main ✔ (origin/main +1)
╰$ python src/evaluate.py

==================================================
AVALIAÇÃO DE PROMPTS OTIMIZADOS
==================================================

Provider: openai
Modelo Principal: gpt-4o-mini
Modelo de Avaliação: gpt-4o

Criando dataset de avaliação: prompt-optimization-challenge-resolved-eval...
   ✓ Carregados 15 exemplos do arquivo datasets/bug_to_user_story.jsonl
   ✓ Dataset criado com 15 exemplos

======================================================================
PROMPTS PARA AVALIAR
======================================================================

Este script irá puxar prompts do LangSmith Hub.
Certifique-se de ter feito push dos prompts antes de avaliar:
  python src/push_prompts.py


🔍 Avaliando: bug_to_user_story_v1
   Puxando prompt do LangSmith Hub: bug_to_user_story_v1
   ✓ Prompt carregado com sucesso
   Dataset: 15 exemplos
   Avaliando exemplos...
      [1/10] F1:0.75 Clarity:0.90 Precision:0.90
      [2/10] F1:0.75 Clarity:0.90 Precision:0.90
      [3/10] F1:0.75 Clarity:0.90 Precision:0.90
      [4/10] F1:0.57 Clarity:0.85 Precision:0.83
      [5/10] F1:0.69 Clarity:0.90 Precision:0.80
      [6/10] F1:0.80 Clarity:0.85 Precision:0.90
      [7/10] F1:0.69 Clarity:0.90 Precision:0.83
      [8/10] F1:0.75 Clarity:0.90 Precision:1.00
      [9/10] F1:0.80 Clarity:0.90 Precision:1.00
      [10/10] F1:0.67 Clarity:0.80 Precision:0.67

==================================================
Prompt: bug_to_user_story_v1
==================================================

Métricas LangSmith:
  - Helpfulness: 0.88 ✗
  - Correctness: 0.80 ✗

Métricas Customizadas:
  - F1-Score: 0.72 ✗
  - Clarity: 0.88 ✗
  - Precision: 0.87 ✗

--------------------------------------------------
📊 MÉDIA GERAL: 0.8291
--------------------------------------------------

❌ STATUS: REPROVADO (média < 0.9)
⚠️  Média atual: 0.8291 | Necessário: 0.9000

==================================================
RESUMO FINAL
==================================================

Prompts avaliados: 1
Aprovados: 0
Reprovados: 1

⚠️  Alguns prompts não atingiram média >= 0.9

Próximos passos:
1. Refatore os prompts com score baixo
2. Faça push novamente: python src/push_prompts.py
3. Execute: python src/evaluate.py novamente
```


- As images estão na pasta screenshots
    - Imagens que represetam a avaliação da execução do prompt v1
        - prompt01.evaluate.execution.01.img01.png
        - prompt01.evaluate.execution.01.img02.png
        - prompt01.evaluate.execution.01.img03.png
    - Imagens que represetam a avaliação da execução do prompt v2 (primeira vez)
        - prompt02.evaluate.execution.01.img01.png
        - prompt02.evaluate.execution.01.img02.png
        - prompt02.evaluate.execution.01.img03.png

### C) Seção "Como Executar"

1. Abra o projeto no vscode

2. Ctrl + Shit + P, Dev Container: Rebuild and Reopen Container **( ou opção similar que prepare o dev container )**

3. Abrir o terminal na pasta raiz e execute `python tests/test_prompts.py`

4. Execute o comando `python src/pull_prompts.py` e veja o resultado do pull no arquivo raw_prompts.
    - ANTES DE EXECUTAR
    - Não esqueça de por suas credencias no arquivo .env
    - O arquivo é gerado em `prompts/raw_prompts.yml`

5. Execute o comando `python src/push_prompts.py` e veja o resultado no console.
    - ANTES DE EXECUTAR
    - Não esqueça de por suas credencias no arquivo .env
    - Na linha 21 do script push_prompts.py coloque o seu handle name
    - IMPORTANTE: Não é possível rodar o script duas vezes consecutivas sem alterar o prompt

6. Execute o comando `python src/evaluate.py` para rodar o evaluation no LangSmith
    - ANTES DE EXECUTAR
    - Não esqueça de por suas credencias no arquivo .env
    - Faça atenção ao array definido na linha 315 do script para decidir qual prompt será avaliado.
        - Foi um opção minha não colocar os dois prompts para serem avalidados em um unica chamada.
    - No arquivo `.env` escolha o nome o valor da variável LANGSMITH_PROJECT
        - Escolha um valor para cada execução:
        - Para o prompt inicial eu deixei o valor: `FC_Challenge_Prompt_Evaluation`
        - Para o prompt corrigido eu utilisei um padrão `FC_Challenge_Prompt_Evaluation V2.01` onde `01` é o número da execução caso seja necessário executar mais de uma vez.

### Area de comunicação com o Avaliador

Como não temos uma boa forma de nos comunicar para a avaliação e/ou discução sobre o exercício, peço por favor que coloque
seguindo o padrão YYYY-MM-MM, nome, mensagem na lista ordenada abaixo.

1. 2026-03-08, Allan, Como o prompt V1 que não possui quase detalhe algum, pode ter uma avaliação tão alta?
