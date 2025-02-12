class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Three friends, Alice, Bob, and Carol, are planning a surprise birthday party for their friend Dave. Alice is in charge of the decorations, Bob is handling the guest list, and Carol is responsible for the cake."
            },
            "2": {
                "scenario": "Two colleagues, Emma and Frank, are discussing how to solve a complex problem at work. Emma is proposing a solution that requires additional resources, while Frank is concerned about the budget constraints."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to generate a coherent and contextually appropriate dialogue between the characters based on the given scenario.

Scenario:
{scenario}

Your dialogue should include:
1. Clear and consistent voices for each character.
2. Contextually appropriate responses that fit the scenario.
3. A logical progression of the dialogue that maintains coherence.

Provide your response in plain text format, with each character's lines clearly labeled.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should include clear and consistent voices for each character.",
            "The dialogue responses should be contextually appropriate and fit the given scenario.",
            "The dialogue should have a logical progression and maintain coherence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
