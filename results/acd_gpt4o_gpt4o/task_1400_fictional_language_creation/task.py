class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "creation",
                "instructions": "Create a fictional language by providing a translation guide and generating a few sentences in that language. The guide should include: 1) Basic grammar rules (e.g., sentence structure, verb conjugation), 2) A vocabulary list of at least 10 words with translations, 3) 3 sentences using these words. Ensure the grammar rules and vocabulary are detailed enough to create coherent sentences. Format your response as follows: \n\n1. Grammar Rules: [Your grammar rules]\n2. Vocabulary List: [Your vocabulary list]\n3. Sentences: [Your sentences]"
            },
            "2": {
                "task_type": "translation",
                "instructions": "Translate the following text from the fictional language back into English using the provided translation guide.\n\nFictional Language Text: 'Lomir tesh arka. Selen dor miran. Fira lomir tesh. Varek loren tesh fira. Miran dor loren tesh.'\n\nTranslation Guide: 'Lomir = Hello, tesh = friend, arka = how are you, Selen = I am, dor = doing, miran = well, Fira = goodbye, Varek = see, loren = again.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "creation":
            return (
                "Your task is to create a fictional language. Provide a translation guide that includes basic grammar rules, a vocabulary list of at least 10 words, and 3 sentences using these words. Ensure the grammar rules and vocabulary are detailed enough to create coherent sentences. Format your response as follows: \n\n1. Grammar Rules: [Your grammar rules]\n2. Vocabulary List: [Your vocabulary list]\n3. Sentences: [Your sentences]"
            )
        elif t["task_type"] == "translation":
            return (
                t["instructions"]
            )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "creation":
            criteria = [
                "The translation guide should include detailed and coherent grammar rules.",
                "The vocabulary list should contain at least 10 words with translations.",
                "The sentences should use the vocabulary words correctly and adhere to the grammar rules."
            ]
        elif t["task_type"] == "translation":
            criteria = [
                "The translation should accurately follow the provided guide.",
                "The translated sentences should be coherent and grammatically correct in English.",
                "The translation should cover all sentences provided in the fictional language text."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
