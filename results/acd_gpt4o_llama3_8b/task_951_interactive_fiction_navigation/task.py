class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You find yourself in a dark forest. There are paths leading to the north and east. To the west, you hear the sound of running water. As you contemplate your options, you hear a distant howl."
            },
            "2": {
                "scenario": "You enter a small village. There is a market to the south, an inn to the west, and a blacksmith to the north. The villagers seem to be whispering about a recent event."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are navigating through a text-based adventure game. Read the scenario and choose an action to take. Your response should be a clear and logical decision based on the given narrative. Provide a brief explanation of why you chose that action and what you hope to achieve. Consider any potential outcomes of your chosen action.

Submit your response in the following format:

Action: [Your chosen action]
Explanation: [Your explanation]

Scenario: {t['scenario']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The action should be clear and logical.", "The explanation should be coherent and based on the scenario.", "The explanation should consider potential outcomes of the chosen action."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
