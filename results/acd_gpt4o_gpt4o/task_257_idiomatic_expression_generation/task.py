class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "context": "A friend who is always late to events."},
            "2": {"task_type": "interpret", "idiom": "Bite the bullet", "context": "Someone deciding to face a difficult situation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Your task is to generate an appropriate idiomatic expression for the following context:\n\nContext: {t['context']}\n\nEnsure that the idiomatic expression is relevant to the context and commonly used in English. Provide your response in the following format:\n\nIdiom: [Your idiomatic expression]\n\nExample: If the context is 'A person who is very knowledgeable about various topics.', an appropriate idiomatic expression could be 'A walking encyclopedia.'\n"""
        elif t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following idiomatic expression and explain its meaning based on the given context:\n\nIdiom: {t['idiom']}\nContext: {t['context']}\n\nEnsure that your explanation is clear and accurately conveys the meaning of the idiom in the given context. Provide your response in the following format:\n\nMeaning: [Your explanation]\n\nExample: If the idiom is 'Let the cat out of the bag' and the context is 'Someone accidentally revealing a secret', an appropriate explanation could be 'The idiom means to disclose something that was intended to be kept secret.'\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The response should be formatted as 'Idiom: [Your idiomatic expression]'.", "The idiomatic expression must be relevant to the context.", "The idiomatic expression must be commonly used in English."]
        elif t['task_type'] == 'interpret':
            criteria = ["The response should be formatted as 'Meaning: [Your explanation]'.", "The explanation must accurately convey the meaning of the idiom.", "The explanation must be clear and relevant to the context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
