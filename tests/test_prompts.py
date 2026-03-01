"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from utils import validate_prompt_structure

PROMPT_KEY="bug_to_user_story_v2"
PROMPT_FILE = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="module")
def prompt_data():
    """Carrega o YAML uma única vez para todos os testes do módulo."""
    return load_prompts(PROMPT_FILE).get(PROMPT_KEY)

class TestPrompts:
    def test_prompt_has_system_prompt(self, prompt_data):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        
        system_prompt = prompt_data.get("system_prompt")

        assert system_prompt is not None, (
            "Campo 'system_prompt' ausente no YAML. "
            "Todo prompt precisa de um system_prompt definido."
        )
        
        assert isinstance(system_prompt, str), (
            f"'system_prompt' deve ser uma string, mas é {type(system_prompt).__name__}."
        )
        
        assert system_prompt.strip(), (
            "Campo 'system_prompt' está vazio. "
            "Adicione as instruções do sistema antes de usar em produção."
        )
        
        assert len(system_prompt.strip()) >= 50, (
            f"'system_prompt' muito curto ({len(system_prompt.strip())} chars). "
            "Um prompt eficaz precisa de pelo menos 50 caracteres de instrução."
        )
        
    def test_prompt_has_role_definition(self, prompt_data):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        
        system_prompt = prompt_data.get("system_prompt")
        sp_lower = system_prompt.lower()
        has_role = any(indicator in sp_lower for indicator in ["você é um product manager"])

        assert has_role, (
            "Nenhuma definição de persona (Role Prompting) encontrada no system_prompt.\n"
            "Exemplo: 'Você é uma Product Manager Sênior com 10 anos de experiência...'"
        )

    def test_prompt_mentions_format(self, prompt_data):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        
        system_prompt = prompt_data.get("system_prompt")
        match_simple  = any(indicator in system_prompt for indicator in ["TEMPLATE DE SAÍDA SIMPLES"])
        match_medium  = any(indicator in system_prompt for indicator in ["TEMPLATE DE SAÍDA MÉDIO"])
        match_complex = any(indicator in system_prompt for indicator in ["TEMPLATE DE SAÍDA COMPLEXO"])

        assert match_simple and match_medium and match_complex, (
            "Nenhuma instrução de formato de saída encontrada no system_prompt.\n"
            f"O prompt precisa especificar os formatos SIMPLES, MÉDIO e COMPLEXO"
        )

    def test_prompt_has_few_shot_examples(self, prompt_data):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        
        system_prompt = prompt_data.get("system_prompt")
        match_simple  = any(indicator in system_prompt for indicator in ["Exemplo 1 — Complexidade SIMPLES"])
        match_medium  = any(indicator in system_prompt for indicator in ["Exemplo 2 — Complexidade MÉDIA"])
        match_complex = any(indicator in system_prompt for indicator in ["Exemplo 3 — Complexidade COMPLEXA"])

        assert match_simple and match_medium and match_complex, (
            "Nenhuma instrução de formato de saída encontrada no system_prompt.\n"
            "O prompt precisa especificar um exemplo para cada tipo de saída SIMPLES, MÉDIA e COMPLEXA"
        )

    def test_prompt_no_todos(self, prompt_data):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        
        TODO_PATTERNS = [
            "[todo]",
            "[fixme]",
            "[wip]",
            "# todo",
            "# fixme",
            "TODO:",
            "FIXME:",
        ]
        system_prompt = prompt_data.get("system_prompt")
        full_text = str(system_prompt)
        found = [p for p in TODO_PATTERNS if p.lower() in full_text.lower()]

        assert not found, (
            f"TODOs/FIXMEs encontrados no prompt: {found}\n"
            "Remova ou complete todos os marcadores antes de usar em produção."
        )

    def test_minimum_techniques(self, prompt_data):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        
        techniques = prompt_data.get('techniques_applied', [])
        invalid = len(techniques) < 2
        assert not invalid, (
            f"Foram encontradas apenas {len(techniques)} no prompt"
        )

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])