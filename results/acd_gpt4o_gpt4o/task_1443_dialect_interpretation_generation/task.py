class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "interpretation",
                "dialect": "Scottish",
                "text": "Ah dinnae ken whit ye'r talkin' aboot."
            },
            "2": {
                "task": "generation",
                "dialect": "Southern American",
                "prompt": "Describe a typical day on a farm."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "interpretation":
            return (
                f"Your task is to interpret the following text written in the {t['dialect']} dialect.\n"
                f"Text: {t['text']}\n"
                "Provide a translation of the text into standard English. Your translation should be clear and accurate."
            )
        elif t["task"] == "generation":
            return (
                f"Your task is to generate a text in the {t['dialect']} dialect.\n"
                f"Prompt: {t['prompt']}\n"
                "Ensure that the generated text accurately reflects the linguistic characteristics of the dialect. The text should be at least 150 words long and relevant to the given prompt."
            )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["task"] == "interpretation":
            criteria = [
                "The translation should accurately reflect the meaning of the original text.",
                "The translation should be in standard English.",
                "The translation should be clear and accurate."
            ]
        elif t["task"] == "generation":
            criteria = [
                "The generated text should accurately reflect the linguistic characteristics of the specified dialect.",
                "The text should be coherent and relevant to the given prompt.",
                "The text should be at least 150 words long."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
    