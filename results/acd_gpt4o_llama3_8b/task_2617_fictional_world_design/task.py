class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "world_name": "Aetheria",
                "requirements": "Create a detailed description of the fictional world 'Aetheria'. Include the following elements: Geography (landscapes, climate), Culture (traditions, languages, art), Technology (level of technological advancement, key inventions), and Societal Structure (governance, social classes). Ensure that all elements are coherent and fit well together."
            },
            "2": {
                "world_name": "Nexon",
                "requirements": "Design the fictional world 'Nexon'. Describe its Geography (landscapes, climate), Culture (traditions, languages, art), Technology (level of technological advancement, key inventions), and Societal Structure (governance, social classes). Ensure that all elements are coherent, fit well together, and are creatively engaging."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return r"""Design the fictional world '{t['world_name']}' based on the following requirements: {t['requirements']}. Ensure that your description is detailed, coherent, and creatively engaging. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should include detailed elements of geography, culture, technology, and societal structure.",
            "The elements should be coherent and fit well together.",
            "The submission should be creatively engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
