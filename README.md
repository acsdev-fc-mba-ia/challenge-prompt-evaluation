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

### C) Seção "Como Executar"

1. Abra o projeto no vscode

2. Ctrl + Shit + P, Dev Container: Rebuild and Reopen Container **( ou opção similar que prepare o dev container )**

3. Abrir o terminal na pasta raiz e execute `python tests/test_prompts.py`

4. Execute o comando `python src/pull_prompts.py` e veja o resultado do pull no arquivo raw_prompts.
    - ANTES DE EXECUTAR
    - Não esqueça de por suas credencias no arquivo .env

5. Execute o comando `python src/push_prompts.py` e veja o resultado no console.
    - ANTES DE EXECUTAR
    - Não esqueça de por suas credencias no arquivo .env
    - Na linha 21 do script push_prompts.py coloque o seu handle name
    - IMPORTANTE: Não é possível rodar o script duas vezes consecutivas sem alterar o prompt

6. Execute o comando `python src/evaluate.py` para rodar o evaluation no LangSmith
    - ANTES DE EXECUTAR
    - Não esqueça de por suas credencias no arquivo .env
    - Remova o código para que força o delay, linhas 204, 221, 222, 223 que usei para não estourar free-tier do Gemini

## Observações

Foi necessário adicionar um delay de execução no script evalution para evitar o erro abaixo:
```google.api_core.exceptions.ResourceExhausted: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash

```

Foi necessário tb alterar versões de biblioteca.
- langchain-google-genai>=2.1.0
- google-genai>=0.1.0