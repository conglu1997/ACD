class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create a new language for a fictional alien species. The language should include a basic vocabulary of at least 10 words, a description of its grammar rules, and an example sentence with translation.",
                "explanation_task": "Provide a detailed explanation of the language's structure, including phonetics, syntax, and any unique linguistic features."
            },
            "2": {
                "criteria": "Create a new dialect of English that could have evolved in an isolated community. The dialect should include at least 10 unique words or phrases, a description of its grammatical differences from standard English, and an example sentence with translation.",
                "explanation_task": "Provide a detailed explanation of the dialect's structure, including phonetic changes, syntactic differences, and any cultural influences on the language."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        criteria = t["criteria"]
        explanation_task = t["explanation_task"]
        instructions = f"""Your task is to create a new language or dialect based on the given criteria and provide a detailed explanation of its structure and rules:

Criteria: {criteria}

After creating the language or dialect, provide a detailed explanation of its structure. Your explanation should include phonetics, syntax, grammar rules, and any unique linguistic features. Ensure your explanation is clear and coherent, and accurately reflects the linguistic principles.

Response format:
1. Language/Dialect Creation: [Your creation]
2. Explanation of Structure: [Your detailed explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should include a coherent language or dialect based on the given criteria.", "The explanation should accurately reflect the linguistic structure and be clearly described."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
