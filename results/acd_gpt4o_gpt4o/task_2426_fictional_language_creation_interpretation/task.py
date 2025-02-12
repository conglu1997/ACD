class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Create a fictional language based on the following constraints: The language must have at least 10 unique words, a simple grammar rule for forming past tense verbs, and a basic sentence structure for forming questions. Provide a vocabulary list, grammar rules, and example sentences.", "response_format": "Vocabulary List:\n[word] - [meaning]\nGrammar Rules:\n[rule description]\nExample Sentences:\n1. [sentence in fictional language] - [translation]\n2. [sentence in fictional language] - [translation]"},
            "2": {"prompt": "Interpret the following fictional language description and provide a translation of the given sentences into English. The language has the following vocabulary and grammar rules:\nVocabulary: \n- blor: tree\n- glorp: water\n- snik: to run\n- plim: to drink\n- zar: big\nGrammar Rules: \n- Past tense of verbs is formed by adding '-ed'\n- Questions are formed by placing the verb at the beginning of the sentence\nTranslate the following sentences:\n1. Snik blor zar\n2. Plim glorp-ed\n3. Glorp plim-ed zar\n4. Snik-ed blor?", "response_format": "1. [translation]\n2. [translation]\n3. [translation]\n4. [translation]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to {t['prompt']}

Provide your response in the following format:\n{t['response_format']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'Create a fictional language' in instructions:
            criteria = [
                "The language must have at least 10 unique words.",
                "The language must include a simple grammar rule for forming past tense verbs.",
                "The language must include a basic sentence structure for forming questions.",
                "The response must include a vocabulary list, grammar rules, and example sentences.",
                "The language must be coherent and logically consistent."
            ]
        elif 'Interpret the following fictional language' in instructions:
            criteria = [
                "The translations must be accurate based on the provided vocabulary and grammar rules."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
