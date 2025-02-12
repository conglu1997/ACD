import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "initial_language": "Zorbish",
                "time_period": "500 years",
                "factors": ["isolation", "technological advancement", "climate change"]
            },
            {
                "initial_language": "Nexian",
                "time_period": "1000 years",
                "factors": ["cultural exchange", "political upheaval", "religious shift"]
            },
            {
                "initial_language": "Quasilic",
                "time_period": "750 years",
                "factors": ["space colonization", "artificial intelligence integration", "genetic modification"]
            },
            {
                "initial_language": "Symbospeech",
                "time_period": "1500 years",
                "factors": ["global catastrophe", "resource scarcity", "interspecies communication"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate the evolution of the fictional language '{t['initial_language']}' over a period of {t['time_period']}, considering the following factors: {', '.join(t['factors'])}. Provide your response in the following format:

1. Language Changes:
   a) [First change]: [Explanation and potential cause]
   b) [Second change]: [Explanation and potential cause]
   c) [Third change]: [Explanation and potential cause]

2. New Words:
   a) [Word 1]: [Meaning] - Etymology: [Brief etymology]
   b) [Word 2]: [Meaning] - Etymology: [Brief etymology]
   c) [Word 3]: [Meaning] - Etymology: [Brief etymology]
   d) [Word 4]: [Meaning] - Etymology: [Brief etymology]
   e) [Word 5]: [Meaning] - Etymology: [Brief etymology]

3. Lost or Altered Grammatical Structures:
   a) [First structure]: [Explanation of change and reason]
   b) [Second structure]: [Explanation of change and reason]

Ensure your response is coherent and considers how the given factors might realistically influence language evolution. Be creative and innovative in your language design, but ground your answers in plausible linguistic principles. Consider unexpected consequences and interactions between the given factors."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes exactly three significant and diverse language changes with detailed explanations and plausible potential causes.",
            "Exactly five new words are presented with meanings and etymologies that reflect the given factors and time period.",
            "Two grammatical structures that have been lost or altered are described with comprehensive reasons linked to the scenario.",
            "The language evolution comprehensively considers all the given factors and the specified time period, showing complex interactions between them.",
            "The response demonstrates a deep understanding of linguistic principles and highly creative application of language evolution concepts.",
            "The response follows the exact format specified in the instructions and presents a cohesive narrative of language evolution."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
