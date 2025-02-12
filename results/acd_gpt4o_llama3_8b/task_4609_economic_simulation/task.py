class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "limited budget, high unemployment, environmental regulations",
                "goals": "reduce unemployment, increase GDP, ensure environmental sustainability"
            },
            "2": {
                "constraints": "aging population, limited natural resources, high inflation",
                "goals": "improve healthcare, stabilize inflation, promote sustainable resource use"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Optimize the economy of a city based on the following constraints and goals.

Constraints: {t['constraints']}
Goals: {t['goals']}

Your response should include:
1. An overview of your economic strategy.
2. Specific policies or actions to achieve the goals.
3. Consideration of the constraints in your plan.
4. Potential challenges and how to address them.

Example response format:
- Strategy Overview: [Your strategy overview]
- Policies/Actions: [Description of specific policies or actions]
- Constraints Consideration: [How you consider the constraints in your plan]
- Challenges: [Potential challenges and solutions]

Note: Ensure your plan is comprehensive, logical, and feasible given the constraints and goals. Highlight any innovative aspects of your plan. Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should adhere to the specified constraints.",
            "The plan should aim to achieve the specified goals.",
            "The plan should be clear and well-structured.",
            "The plan should include specific policies or actions.",
            "The plan should consider potential challenges and solutions.",
            "The plan should be practical and feasible.",
            "The plan should be innovative and logical.",
            "The submission should be comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
