class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"custom": "Tea ceremony in Japan", "context": "The Japanese tea ceremony is a traditional ritual influenced by Zen Buddhism, where powdered green tea (matcha) is ceremonially prepared by a skilled practitioner and served to a small group of guests in a tranquil setting. The ceremony emphasizes aesthetics, respect, and mindfulness."},
            "2": {"custom": "Diwali festival in India", "context": "Diwali, also known as the Festival of Lights, is a major Hindu festival celebrated with the lighting of oil lamps, fireworks, and sharing of sweets. It signifies the victory of light over darkness and good over evil. The festival also includes prayers, family gatherings, and festive meals."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        custom = t["custom"]
        context = t["context"]
        instructions = f"""Your task is to explain the following cultural custom or practice, including its significance and context:

Custom: {custom}

Context: {context}

Your explanation should be clear, accurate, and respectful. Provide details about the custom's history, how it is practiced, and its cultural significance. Ensure that your explanation is informative and easy to understand. Provide your explanation in plain text format. Your response should be structured as follows:

Explanation: [Your detailed explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and accurate.",
            "The explanation should include details about the custom's history, practice, and cultural significance.",
            "The explanation should be respectful and informative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
