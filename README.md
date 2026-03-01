# Observações

Foi necessário adicionar um delay de execução no script evalution para evitar o erro abaixo:
```google.api_core.exceptions.ResourceExhausted: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash

```

Foi necessário tb alterar versões de biblioteca.
- langchain-google-genai>=2.1.0
- google-genai>=0.1.0