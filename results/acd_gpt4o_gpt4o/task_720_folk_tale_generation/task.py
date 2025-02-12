class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "culture": "Japanese",
                "theme": "spirits of the forest"
            },
            "2": {
                "culture": "African",
                "theme": "talking animals"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        culture = t["culture"]
        theme = t["theme"]
        instructions = f"""Your task is to generate a folk tale based on the given cultural theme.

Culture: {culture}
Theme: {theme}

Your folk tale should:
1. Be creative and coherent.
2. Integrate cultural elements and knowledge.
3. Adhere to the given theme.
4. Be evocative and well-structured.

Provide your folk tale in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The folk tale should be creative and coherent.",
            "The folk tale should integrate cultural elements and knowledge.",
            "The folk tale should adhere to the given theme.",
            "The folk tale should be evocative and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
