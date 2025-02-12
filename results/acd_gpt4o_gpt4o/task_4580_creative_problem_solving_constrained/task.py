class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instruction": "Design a piece of furniture that can be used both as a chair and a table. The design must meet the following constraints:\n1. The furniture must be made of wood.\n2. It must be able to support a weight of at least 100 kg.\n3. It should have a contemporary aesthetic.\n\nProvide your design in a written format, clearly describing how it meets each of the constraints. Your response should be structured as follows:\n\nDesign Description: [Your description here]\nConstraints Met: [Explanation of how each constraint is met]\n", "criteria": ["The design should be dual-purpose (chair and table)", "The design should specify that it is made of wood", "The design should include details on how it supports 100 kg", "The design should have a contemporary aesthetic"]},
            "2": {"instruction": "Create a meal plan for a day that meets the following constraints:\n1. The total calorie intake for the day should not exceed 2000 calories.\n2. The meals should include ingredients from at least three different cuisines.\n3. The plan should include breakfast, lunch, and dinner.\n\nProvide your meal plan in a written format, detailing the meals and how they meet each constraint. Your response should be structured as follows:\n\nMeal Plan: [Your meal plan here]\nConstraints Met: [Explanation of how each constraint is met]\n", "criteria": ["The total calorie intake should not exceed 2000 calories", "The meal plan should include ingredients from at least three different cuisines", "The plan should include breakfast, lunch, and dinner"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['instruction']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
