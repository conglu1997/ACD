class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'excerpt': "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."},
            '2': {'theme': "The conflict between personal desire and societal expectations in Jane Austen's Pride and Prejudice."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'excerpt' in t:
            return f"Read the following excerpt from a classic literary work and generate a detailed summary and analysis: {t['excerpt']}\n\nYour response should include:\n1. A brief summary of the excerpt.\n2. An analysis of the themes, characters, and stylistic elements.\n3. Your interpretation of the significance of this passage within the context of the entire work.\n\nSubmit your response as a plain text string in the following format:\n\nSummary: [Your summary]\nAnalysis: [Your analysis]\nInterpretation: [Your interpretation]"
        elif 'theme' in t:
            return f"Analyze the following theme from a classic literary work: {t['theme']}\n\nYour response should include:\n1. An explanation of the theme and its significance.\n2. An analysis of how the theme is developed through characters, plot, and literary devices.\n3. Your interpretation of the author's message regarding this theme.\n\nSubmit your response as a plain text string in the following format:\n\nExplanation: [Your explanation]\nAnalysis: [Your analysis]\nInterpretation: [Your interpretation]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should accurately summarize and analyze the excerpt or theme.", "The response should be detailed, coherent, and logically structured.", "The interpretation should be insightful and relevant to the context of the work."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
