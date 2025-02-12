import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            {"source": "English", "target": "Mandarin Chinese"},
            {"source": "Spanish", "target": "Japanese"},
            {"source": "Arabic", "target": "Russian"},
            {"source": "Hindi", "target": "Swahili"},
            {"source": "French", "target": "Korean"}
        ]
        idioms = [
            "It's raining cats and dogs",
            "To kill two birds with one stone",
            "To be on cloud nine",
            "To bite off more than you can chew",
            "To be caught between a rock and a hard place"
        ]
        return {
            "1": {"pair": random.choice(language_pairs), "idiom": random.choice(idioms)},
            "2": {"pair": random.choice(language_pairs), "idiom": random.choice(idioms)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that maps semantic relationships across multiple languages and generates culturally-aware translations of idiomatic expressions. Your task is to translate the idiom \"{t['idiom']}\" from {t['pair']['source']} to {t['pair']['target']}. Your response should include the following sections:\n\n1. Semantic Mapping (200-250 words):\n   a) Describe how your AI system analyzes and maps semantic relationships between {t['pair']['source']} and {t['pair']['target']}.\n   b) Explain any novel techniques or algorithms used for cross-lingual semantic analysis.\n   c) Discuss how your system accounts for cultural differences in conceptual understanding.\n\n2. Idiom Analysis (150-200 words):\n   a) Analyze the semantic components and cultural context of the given idiom in {t['pair']['source']}.\n   b) Identify potential challenges in translating this idiom to {t['pair']['target']}.\n   c) Explain how your system determines the core meaning or sentiment of the idiom.\n\n3. Translation Generation (200-250 words):\n   a) Describe the process your AI system uses to generate a culturally-aware translation of the idiom in {t['pair']['target']}.\n   b) Provide the generated translation and explain its semantic and cultural relevance.\n   c) Discuss any alternative translations considered and why the final one was chosen.\n\n4. Cultural Nuance Preservation (150-200 words):\n   a) Explain how your system preserves or adapts cultural nuances in the translation process.\n   b) Discuss any specific cultural elements in {t['pair']['target']} that influenced the translation.\n   c) Analyze potential misunderstandings or misinterpretations that could arise from a direct translation.\n\n5. Evaluation and Refinement (150-200 words):\n   a) Propose a method to evaluate the accuracy and cultural appropriateness of the generated translation.\n   b) Describe how your system could learn and improve from feedback or corrections.\n   c) Discuss potential ethical considerations in cross-cultural AI-driven translation.\n\nEnsure your response demonstrates a deep understanding of linguistics, semantic analysis, and cultural awareness. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and practical plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 850-1100 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes a plausible AI system for cross-lingual semantic mapping between {t['pair']['source']} and {t['pair']['target']}.",
            f"The analysis of the idiom '{t['idiom']}' is thorough and considers its semantic components and cultural context in {t['pair']['source']}.",
            f"A culturally-aware translation of the idiom is provided in {t['pair']['target']}, with a clear explanation of its relevance and any adaptations made.",
            "The response demonstrates a deep understanding of linguistic principles, semantic analysis, and cultural awareness.",
            "The proposed evaluation method and ethical considerations are well-reasoned and relevant to the task.",
            "The response is creative and original while maintaining scientific and practical plausibility.",
            "The answer is well-organized with clear headings for each required section and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
