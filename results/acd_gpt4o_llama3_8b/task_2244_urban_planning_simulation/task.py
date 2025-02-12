class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "high population density, limited space, need for green spaces",
                "goals": "maximize residential areas, include parks and recreational areas, ensure efficient public transportation"
            },
            "2": {
                "constraints": "coastal city, prone to flooding, high tourism",
                "goals": "develop tourist attractions, ensure flood defenses, maintain environmental sustainability"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an urban development plan based on the following constraints and goals.

Constraints: {t['constraints']}
Goals: {t['goals']}

Your response should include:
1. A description of the overall plan.
2. Specific areas designated for residential, commercial, and recreational purposes.
3. Infrastructure plans, including transportation and utilities.
4. Environmental considerations and sustainability measures.

Example response format:
- Overall Plan: [Your overall plan description]
- Residential Areas: [Description of residential areas]
- Commercial Areas: [Description of commercial areas]
- Recreational Areas: [Description of parks and green spaces]
- Infrastructure: [Transportation and utilities plan]
- Environmental Considerations: [Sustainability measures]

Note: Ensure your plan is comprehensive, clear, well-structured, and adheres to the given constraints and goals. Highlight any innovative and logical aspects of your plan. Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should adhere to the specified constraints.",
            "The plan should aim to achieve the specified goals.",
            "The plan should be clear and well-structured.",
            "The plan should include specific areas designated for residential, commercial, and recreational purposes.",
            "The plan should include infrastructure plans for transportation and utilities.",
            "The plan should consider environmental sustainability measures.",
            "The plan should be practical and feasible.",
            "The plan should be innovative and logical.",
            "The submission should be comprehensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
