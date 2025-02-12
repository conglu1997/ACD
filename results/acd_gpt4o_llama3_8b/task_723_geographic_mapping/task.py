class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "identification", "map_description": "A map featuring a large river flowing from north to south, with a mountain range to the west and a forest to the east. There are three cities: one near the river's source in the north, one by the river in the central region, and one at the river's mouth in the south.", "question": "Identify the geographic features and their spatial relationships described. Submit your answer in the following format: 'River: [direction], Mountain Range: [relative position], Forest: [relative position], Cities: [description of locations]'."},
            "2": {"task_type": "generation", "geographic_features": ["a large lake in the center", "a desert to the north", "a forest to the south", "three towns: one on the lake's western shore, one in the desert, and one in the forest"], "constraints": "Generate a detailed map description based on the given geographic features. The description should include the relative positions of the features and any notable spatial relationships among them.", "example": "The map showcases a large lake situated centrally, with a vast desert sprawling to the north and a dense forest covering the southern region. Three towns are marked: one on the western shore of the lake, another in the heart of the desert, and the last nestled within the forest."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "identification":
            return f"Read the following map description and identify the geographic features and their spatial relationships: {t['map_description']}\nQuestion: {t['question']}"
        elif t["task_type"] == "generation":
            features = ', '.join(t['geographic_features'])
            return f"Generate a detailed map description based on the following geographic features: {features}. {t['constraints']}\nExample: {t['example']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "identification":
            criteria = ["The response should correctly identify the river's direction.", "The response should correctly identify the relative positions of the mountain range and the forest.", "The response should correctly describe the locations of the cities."]
        elif t["task_type"] == "generation":
            criteria = ["The description should include all specified geographic features.", "The description should accurately describe the relative positions of the features.", "The description should mention any notable spatial relationships among the features."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
