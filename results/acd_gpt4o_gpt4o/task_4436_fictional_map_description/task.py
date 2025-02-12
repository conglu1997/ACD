class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe a fictional map of a lost kingdom. The map should include at least five distinct regions (e.g., forests, mountains, rivers, cities) and notable landmarks. Describe each region and landmark in detail, focusing on their characteristics and spatial relationships. Your description should be at least 300 words long."},
            "2": {"prompt": "Describe a fictional map of an alien planet. The map should include at least five distinct regions (e.g., craters, alien cities, lakes, deserts, forests) and notable landmarks. Describe each region and landmark in detail, focusing on their characteristics and spatial relationships. Your description should be at least 300 words long."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the following fictional map in vivid detail:

Prompt: {t['prompt']}

Your description should include at least five distinct regions and notable landmarks. Focus on the characteristics of each region and landmark, as well as their spatial relationships. The goal is to create a vivid and coherent description that allows the reader to visualize the map clearly. Your description should be at least 300 words long and well-structured. Provide your response in plain text format.

Example response format:
Region 1: [Description]
Region 2: [Description]
Landmark 1: [Description]
Landmark 2: [Description]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should include at least five distinct regions.", "The description should mention notable landmarks.", "The description should focus on the characteristics and spatial relationships of regions and landmarks.", "The description should be at least 300 words long.", "The description should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
