class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You have been working hard on a project for weeks, but your manager criticizes your work during a team meeting, making you feel embarrassed and demotivated.", "type": "infer_and_suggest"},
            "2": {"scenario": "You recently moved to a new city for a job and feel lonely because you haven't made any friends yet.", "type": "infer_and_suggest"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following emotional scenario and suggest appropriate coping strategies. Based on the given scenario, identify the primary emotion(s) experienced by the individual and provide 2-3 practical coping strategies that can help them manage their feelings. Ensure that your suggestions are empathetic and contextually appropriate.

Scenario: {t['scenario']}

Provide your response in the following format:

- Primary Emotion(s): [Your answer]
- Coping Strategies:
  1. [Strategy 1]
  2. [Strategy 2]
  3. [Strategy 3] (if applicable)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The primary emotions identified should be relevant to the scenario.", "The suggested coping strategies should be practical, empathetic, and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
