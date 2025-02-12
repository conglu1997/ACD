class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"map_type": "fantasy world", "criteria": "Include at least three distinct regions: a forest, a mountain range, and a river. Each region should have a unique name and a brief description of its characteristics and significance."},
            "2": {"map_type": "modern city", "criteria": "Include at least five different neighborhoods, a central park, and a river flowing through the city. Each neighborhood should have a unique name and a brief description of its characteristics and significance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a map based on the given criteria.

Map Type: {t['map_type']}

Criteria: {t['criteria']}

Provide your map design in the following format:

Map Design:
- Region 1: [Name and description]
- Region 2: [Name and description]
- Region 3: [Name and description]
... (Include all specified regions)
- Additional Descriptions: [Any additional elements or descriptions for your map]

Ensure that your map design is creative, coherent, and adheres to the given criteria. Use clear and concise language in your descriptions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The map design should include all specified regions with unique names and descriptions.",
            "The submission should follow the specified format.",
            "The map should demonstrate creativity and coherence.",
            "Additional elements or descriptions should align with the overall map design." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
