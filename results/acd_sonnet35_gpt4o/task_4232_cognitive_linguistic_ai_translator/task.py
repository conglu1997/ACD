import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            {"source": "Mandarin Chinese", "target": "Arabic", "cognitive_focus": "semantic mapping"},
            {"source": "Hindi", "target": "Russian", "cognitive_focus": "phonological processing"},
            {"source": "Swahili", "target": "Japanese", "cognitive_focus": "syntactic restructuring"},
            {"source": "Spanish", "target": "Vietnamese", "cognitive_focus": "pragmatic adaptation"}
        ]
        return {
            "1": random.choice(language_pairs),
            "2": random.choice(language_pairs)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that translates between {t['source']} and {t['target']} by modeling the cognitive processes of bilingual speakers, with a focus on {t['cognitive_focus']}. Then, use this system to create a hybrid language that bridges these two distinct language families. Your response should include the following sections:\n\n1. Cognitive-Linguistic Model (300-350 words):\n   a) Describe the key components of your AI system for modeling bilingual cognitive processes.\n   b) Explain how your model incorporates current theories in cognitive linguistics and bilingualism.\n   c) Detail how your system focuses on {t['cognitive_focus']} in the translation process.\n   d) Provide a high-level diagram or flowchart description of your system architecture.\n\n2. Translation Process Analysis (250-300 words):\n   a) Analyze the unique challenges in translating between {t['source']} and {t['target']}.\n   b) Explain how your AI system addresses these challenges using cognitive modeling.\n   c) Provide an example of a complex phrase or idiom and describe how your system would translate it.\n   d) Discuss how your approach differs from traditional machine translation methods.\n\n3. Hybrid Language Generation (250-300 words):\n   a) Describe the process of creating a hybrid language between {t['source']} and {t['target']}.\n   b) Explain how your system combines elements from both languages in terms of phonology, syntax, and semantics.\n   c) Provide three example sentences in your hybrid language, with translations and explanations.\n   d) Discuss how this hybrid language reflects the cognitive processes modeled in your system.\n\n4. Cognitive Implications (200-250 words):\n   a) Analyze how your model contributes to our understanding of bilingual cognition.\n   b) Discuss potential insights your system provides into language acquisition and processing.\n   c) Explore how your hybrid language might influence thought patterns and cognitive flexibility.\n\n5. Ethical Considerations and Applications (150-200 words):\n   a) Discuss ethical implications of AI-generated hybrid languages and cognitive modeling of bilingualism.\n   b) Consider potential applications in fields such as language education, cross-cultural communication, and cognitive therapy.\n   c) Propose guidelines for responsible development and use of cognitive-linguistic AI systems.\n\n6. Evaluation and Future Directions (150-200 words):\n   a) Propose methods to evaluate the effectiveness and cognitive plausibility of your system.\n   b) Describe an experiment to test how human bilinguals interact with your hybrid language.\n   c) Suggest future research directions or expansions of your cognitive-linguistic AI system.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, and AI. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing the ethical and practical implications of your system.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately integrates concepts from linguistics, cognitive science, and AI to create a plausible system for translating between {t['source']} and {t['target']}.",
            f"The cognitive-linguistic model focuses on {t['cognitive_focus']} and demonstrates a deep understanding of bilingual cognitive processes.",
            "The hybrid language generation process is creative, linguistically sound, and reflects elements from both source languages.",
            "The analysis of cognitive implications and ethical considerations is thorough and insightful.",
            "The proposed evaluation methods and future directions are well-reasoned and scientifically plausible.",
            "The response shows creativity, interdisciplinary knowledge integration, and critical thinking throughout, while maintaining scientific accuracy.",
            "The proposed system and hybrid language demonstrate innovation while considering practical applications and limitations.",
            "The response addresses all required elements in the specified word count range and format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
