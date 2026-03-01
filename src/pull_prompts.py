"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
import json
import yaml
from datetime import date
from pathlib import Path
from dotenv import load_dotenv
from httpx import Client
from langchain import hub
from langchain.load import dumps

from utils import save_yaml, check_env_vars, print_section_header

load_dotenv()

PROMPT_REPO   = "leonanluppi/bug_to_user_story_v1"
PROMPT_OUTPUT = Path("prompts/raw_prompts.yml")
ROLE_MAP = {
    "SystemMessagePromptTemplate": "system",
    "HumanMessagePromptTemplate":  "human"
}

def pull_prompts_from_langsmith() -> dict:

    prompt = hub.pull(PROMPT_REPO)

    # Use para verificar a estrutura de dados retornada pelo pull
    # show_data_structure(prompt)    

    # Extrai as mensagens por role
    templates = {
        ROLE_MAP[type(msg).__name__]: msg.prompt.template
        for msg in prompt.messages
    }

    repo = prompt.metadata["lc_hub_repo"]

    return {
        repo: {
            "description":   'Prompt para converter relatos de bugs em User Stories',
            "system_prompt": templates["system"],
            "user_prompt":   templates["human"],
            "version":       'v1',
            "create_at":     date.today(),
            "tags":          ["bug-analysis", "user-story", "product-management"],
        }
    }

def show_data_structure(prompt):
    print(type(prompt))  # apresentar o tipo do objeto retornado
    print(vars(prompt))  # apresentar o dictionary com atributos do prompt
    data = json.loads(dumps(prompt))
    yaml_string = yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(yaml_string)  # apresentar a string JSON resultante da serialização

def main():
    """Função principal"""
    print_section_header("Pull de Prompts — LangSmith Hub")

    if not check_env_vars(["LANGSMITH_ENDPOINT","LANGSMITH_API_KEY"]):
        return 1

    try:
        data = pull_prompts_from_langsmith()
        save_yaml(data, PROMPT_OUTPUT)
        print(f"✅  Salvo em: {PROMPT_OUTPUT}")
    except Exception as e:
        print(f"❌  Erro: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
