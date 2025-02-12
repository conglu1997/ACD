class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "Two friends are discussing their future plans over coffee.",
                "mood": "optimistic",
                "elements": "mention travel, career goals, and personal growth"
            },
            "2": {
                "context": "A detective is interrogating a suspect in a dimly lit room.",
                "mood": "tense",
                "elements": "include suspicion, denial, and a revelation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to generate a fictional dialogue based on the given context, mood, and required elements. "
            "Ensure that the dialogue is coherent, fits the specified context, and conveys the intended mood. "
            "Your response should be in plain text format, structured as follows:\n\n"
            "Context: [Provided context]\n"
            "Mood: [Provided mood]\n"
            "Elements to include: [Provided elements]\n"
            "Dialogue:\n"
            "[Character 1]: [Their dialogue line]\n"
            "[Character 2]: [Their dialogue line]\n"
            "... (continue the dialogue for at least 10 exchanges)"
            "\nSample Structure:\n"
            "Context: Two friends are discussing their future plans over coffee.\n"
            "Mood: Optimistic\n"
            "Elements to include: mention travel, career goals, and personal growth\n"
            "Dialogue:\n"
            "[Friend 1]: I'm really excited about our upcoming trip to Europe!\n"
            "[Friend 2]: Me too! I think it'll be a great opportunity to explore new cultures and maybe even find some inspiration for my career.\n"
            "... (continue the dialogue for at least 10 exchanges)"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be coherent and contextually appropriate.",
            "The dialogue should convey the specified mood.",
            "The dialogue should fit the given context.",
            "The dialogue should contain at least 10 exchanges between characters.",
            "The dialogue should include the specified elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
