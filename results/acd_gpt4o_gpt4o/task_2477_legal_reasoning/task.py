class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'scenario': 'You are a tenant in an apartment building. Recently, the landlord has increased the rent significantly, and you believe this increase is unreasonable. Provide legal advice on what steps you can take.'
            },
            '2': {
                'legal_text': 'In the event of a breach of contract, the non-breaching party shall be entitled to seek damages, including but not limited to, compensatory, consequential, and incidental damages, as well as specific performance, injunctive relief, and any other remedies available under the law.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'scenario' in t:
            return f"""Your task is to provide legal advice based on the following scenario:

Scenario: {t['scenario']}

Provide your advice in plain text format, clearly stating the legal steps the tenant can take and any relevant laws or regulations that apply. Your response should be well-structured and consider the potential consequences of each step."""
        else:
            return f"""Your task is to interpret the following legal text and explain its meaning in plain language:

Legal Text: {t['legal_text']}

Your response should be at least 150 words and include an analysis of the different types of damages mentioned and the remedies available to the non-breaching party. Provide your response in plain text format. Use clear paragraphs to structure your analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'scenario' in t:
            criteria = [
                "The advice should address the tenant's issue.",
                "The advice should include relevant legal steps and laws.",
                "The advice should be clear and well-structured.",
                "The advice should consider the consequences of each step."
            ]
        else:
            criteria = [
                "The interpretation should include an analysis of the different types of damages mentioned.",
                "The interpretation should explain the remedies available to the non-breaching party.",
                "The interpretation should be at least 150 words.",
                "The interpretation should use clear paragraphs to structure the analysis."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
