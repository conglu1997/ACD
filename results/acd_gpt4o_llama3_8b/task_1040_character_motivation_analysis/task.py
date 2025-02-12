class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"character": "John", "scenario": "John decides to leave his high-paying job in the city to move to a small rural town and start a farm."},
            "2": {"character": "Emily", "scenario": "Emily breaks off her engagement with her long-time partner just a month before the wedding."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the motivations behind the following character's actions and provide a detailed explanation:
Character: {t["character"]}
Scenario: {t["scenario"]}

Your analysis should include:
1. A description of the character's possible emotional state and personal background.
2. An exploration of external factors that might have influenced the character's decision.
3. A coherent narrative that ties together the character's motivations and actions.

Submit your analysis as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should include a description of the character's possible emotional state and personal background.", "The analysis should explore external factors that might have influenced the character's decision.", "The analysis should provide a coherent narrative that ties together the character's motivations and actions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
