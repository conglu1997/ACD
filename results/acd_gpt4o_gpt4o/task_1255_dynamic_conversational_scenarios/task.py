class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_scenario": "A customer is calling technical support because their internet is not working.", "criteria": "The support agent should be helpful, polite, and attempt to diagnose the issue through at least three different troubleshooting steps."},
            "2": {"initial_scenario": "Two friends are discussing their weekend plans.", "criteria": "The conversation should be friendly and include at least three suggestions for activities, with reasons why each activity would be enjoyable."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a dialogue based on the following scenario and criteria.

Scenario: {t['initial_scenario']}

Criteria: {t['criteria']}

Ensure the dialogue is coherent, follows the given scenario, and meets the specified criteria. Provide the dialogue in plain text format, with each line of dialogue prefixed by the speaker's name (e.g., 'Customer: My internet is not working.')."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be coherent and follow the given scenario.", "The dialogue should meet the specified criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
