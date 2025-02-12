import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "age_group": "children (ages 5-10)",
                "target_language": "Mandarin Chinese"
            },
            {
                "age_group": "adults (ages 25-40)",
                "target_language": "Arabic"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that models human language acquisition for {t['age_group']} learning {t['target_language']} as a second language. Your task is to:

1. Outline the key components of your AI system (200-250 words), including:
   a) Input processing (how the system receives and processes linguistic data)
   b) Learning mechanisms (how the system acquires and generalizes language patterns)
   c) Output generation (how the system produces language)
   d) Adaptation to the specific age group and target language

2. Explain how your system incorporates the critical period hypothesis and accounts for age-related differences in language acquisition (150-200 words).

3. Describe a specific challenge in second language acquisition for the given age group and target language, and how your AI system addresses it (100-150 words).

4. Propose an experiment to test the effectiveness of your AI system, including:
   a) Hypothesis
   b) Methodology
   c) Expected results and their interpretation (150-200 words)

5. Discuss potential implications of your AI system for:
   a) Understanding human language acquisition
   b) Improving second language teaching methods
   c) Ethical considerations in AI-assisted language learning (200-250 words)

Ensure your response demonstrates a deep understanding of linguistic principles, cognitive science, and AI capabilities. Be creative in your approach while grounding your ideas in established theories and research."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a comprehensive outline of the AI system's key components, tailored to the given age group and target language.",
            "The explanation of how the system incorporates the critical period hypothesis is well-reasoned and scientifically grounded.",
            "The description of a specific challenge and its solution demonstrates a deep understanding of second language acquisition issues.",
            "The proposed experiment is well-designed, with a clear hypothesis, methodology, and expected results.",
            "The discussion of implications is insightful and considers multiple aspects of language acquisition, teaching methods, and ethics.",
            "The overall response shows creativity, interdisciplinary knowledge, and analytical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
