class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "genre1": "science fiction",
                "genre2": "fantasy",
                "prompt": "A scientist discovers a portal to a magical world where mythical creatures exist."
            },
            "2": {
                "genre1": "mystery",
                "genre2": "romance",
                "prompt": "A detective investigating a series of thefts at a museum finds unexpected love." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a short story that combines elements from the following two genres:

1. {t['genre1']}
2. {t['genre2']}

Prompt: {t['prompt']}

Ensure that your story is coherent, creatively blends elements from both genres, and is engaging. Provide your story in plain text format as follows:

Story: [Your story]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should creatively blend elements from both genres.",
            "The narrative should be coherent and engaging.",
            "The story should be relevant to the given prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
