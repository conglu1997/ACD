class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": ["must be eco-friendly", "accommodate 500,000 residents", "use renewable energy sources"],
                "goals": ["reduce carbon footprint", "promote community engagement", "ensure accessibility for all"]
            },
            "2": {
                "constraints": ["must be disaster-resilient", "accommodate 1,000,000 residents", "integrate advanced transportation systems"],
                "goals": ["maximize green spaces", "foster economic growth", "enhance public safety"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed plan for a futuristic city based on the following constraints and goals:

Constraints: {', '.join(t['constraints'])}
Goals: {', '.join(t['goals'])}

Your plan should include the following sections:
1. Overview: A brief introduction to the city and its vision.
2. Infrastructure: Details on the layout, buildings, and key structures.
3. Energy: Explanation of how the city will use and manage renewable energy sources.
4. Transportation: Description of the transportation systems and how they integrate with the city's design.
5. Community: How the city will promote community engagement and accessibility for all residents.
6. Sustainability: Strategies to reduce the carbon footprint and enhance environmental sustainability.
7. Safety: Measures to ensure public safety and disaster resilience.

Ensure that each section is covered in detail and is logically sequenced. Provide concrete examples where applicable. Submit your plan as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should address all specified constraints and goals.",
            "The plan should be coherent, well-structured, and detailed.",
            "The plan should demonstrate creativity and practical reasoning.",
            "The response should be clear and logically sequenced.",
            "The plan should include concrete examples where applicable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
