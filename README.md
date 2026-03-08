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
seguindo o padrão YYYY-MM-MM, nome, mensagem na lista ordenada abaixo. A primeira mensagem é apenas um exemplo:

1. 2026-03-08, Allan, Message de Exemplo.