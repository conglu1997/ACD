class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Nature", "form": "Haiku", "requirements": "A haiku is a three-line poem with a syllable pattern of 5-7-5."},
            "2": {"theme": "Love", "form": "Sonnet", "requirements": "A sonnet is a 14-line poem written in iambic pentameter, typically with a rhyme scheme of ABABCDCDEFEFGG."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a poem based on the following theme and form:\nTheme: {t['theme']}\nForm: {t['form']}\n\nEnsure your poem adheres to the conventions of the specified form. Here are the requirements for the form:\n{t['requirements']}\n\nAfter generating the poem, analyze its adherence to the form's conventions, including structure, meter, and rhyme scheme (if applicable). Submit your response as a plain text string in the following format:\n\nPoem: [Your poem]\nAnalysis: [Your analysis]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The poem should adhere to the specified form's conventions, including structure, meter, and rhyme scheme (if applicable). The analysis should accurately reflect the poem's adherence to these conventions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
