"""
Script para fazer push de prompts otimizados ao LangSmith Prompt Hub.

Este script:
1. Lê os prompts otimizados de prompts/bug_to_user_story_v2.yml
2. Valida os prompts
3. Faz push PÚBLICO para o LangSmith Hub
4. Adiciona metadados (tags, descrição, técnicas utilizadas)

SIMPLIFICADO: Código mais limpo e direto ao ponto.
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate
from utils import load_yaml, check_env_vars, print_section_header

HANDLE_NAME = "acsdev"
PROMPT_REPO = f"{HANDLE_NAME}/bug_to_user_story_v2"
PROMPT_FILE = Path("prompts/bug_to_user_story_v2.yml")
REQUIRED_FIELDS = ["system_prompt", "user_prompt"]

load_dotenv()

def push_prompt_to_langsmith(prompt_name: str, prompt_data: dict) -> bool:
    """
    Faz push do prompt otimizado para o LangSmith Hub (PÚBLICO).

    Args:
        prompt_name: Nome do prompt
        prompt_data: Dados do prompt

    Returns:
        True se sucesso, False caso contrário
    """
    template = ChatPromptTemplate.from_messages([
        ("system", prompt_data["system_prompt"]),
        ("human",  prompt_data["user_prompt"]),
    ])

    print(f"⬆️  Pushing: {prompt_name}")
    anwser = hub.push(prompt_name, template, new_repo_is_public=True)
    print(f"Resposta do push: {anwser}")
    return True

def validate_prompt(prompt_data: dict) -> tuple[bool, list]:
    """
    Valida estrutura básica de um prompt (versão simplificada).

    Args:
        prompt_data: Dados do prompt

    Returns:
        (is_valid, errors) - Tupla com status e lista de erros
    """
    ...
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in prompt_data:
            errors.append(f"Campo obrigatorio ausente: '{field}'")
        elif not prompt_data[field].strip():
            errors.append(f"Campo '{field}' esta vazio")

    return len(errors) == 0, errors

def main():
    """Função principal"""
    print_section_header("Push de Prompts — LangSmith Hub")

    check_env_vars(["LANGSMITH_ENDPOINT", "LANGSMITH_API_KEY", "LANGSMITH_PROJECT"])

    if not PROMPT_FILE.exists():
        print(f"❌  Arquivo nao encontrado: {PROMPT_FILE}")
        return 1


    raw = load_yaml(PROMPT_FILE)
    prompt_name = next(iter(raw))
    prompt_data = raw[prompt_name]

    
    is_valid, errors = validate_prompt(prompt_data)
    if not is_valid:
        print("❌  Prompt invalido:")
        for err in errors:
            print(f"    • {err}")
        return 1

    print(f"✅  Prompt valido: {prompt_name}")

    try:
        push_prompt_to_langsmith(PROMPT_REPO, prompt_data)
        print(f"✅  Push concluido: {PROMPT_REPO}")
    except Exception as e:
        print(f"❌  Erro ao fazer push: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
