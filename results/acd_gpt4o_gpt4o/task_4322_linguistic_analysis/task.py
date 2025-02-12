class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"word": "antidisestablishmentarianism"},
            "2": {"word": "pseudopseudohypoparathyroidism"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the etymology and morphology of the given word. Break down the word into its morphemes, identify their origins, and explain how they combine to form the given word. Provide the following details in your analysis:\n\n1. Word: {t['word']}\n2. Morphemes: [List the morphemes] \n3. Origins: [Describe the origins of each morpheme] \n4. Combination: [Explain how the morphemes combine to form the word]\n\nEnsure your analysis is detailed, accurate, and logically structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should correctly identify and list the morphemes.", "The origins of each morpheme should be accurately described.", "The explanation of morpheme combination should be logical and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
