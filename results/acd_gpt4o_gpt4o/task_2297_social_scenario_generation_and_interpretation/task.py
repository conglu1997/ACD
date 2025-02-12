class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a social scenario where a person feels left out at a party and describe their emotions and reactions.", "scenario": "At a friend's birthday party, John notices that everyone is talking and laughing in groups, but he is standing alone, feeling awkward and ignored."},
            "2": {"criteria": "Create a social scenario where a person receives unexpected praise at work and describe their emotions and reactions.", "scenario": "During a team meeting, Sarah's manager unexpectedly praises her for her recent project, which she thought went unnoticed."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: first, generate a realistic social scenario based on the given criteria; second, interpret the provided social scenario to understand the emotions and motivations of the characters involved.

Criteria for scenario generation: {t['criteria']}

Provide your generated scenario and interpretation in the format 'Generated Scenario: [your scenario], Interpretation: [your interpretation]'.

Here is a scenario for you to interpret:

Scenario: {t['scenario']}

Provide your interpretation of the scenario in plain text format. Ensure you address the emotions and motivations of the characters involved. For the provided scenario, write 'Interpretation: [your interpretation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should correctly identify the emotions of the characters.",
            "The interpretation should explain the motivations of the characters.",
            "The generated scenario should be realistic and align with the given criteria."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
