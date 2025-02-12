import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_families = ['Indo-European', 'Sino-Tibetan', 'Afroasiatic', 'Austronesian', 'Niger-Congo']
        linguistic_features = ['morphological complexity', 'syntactic structure', 'phonological systems', 'semantic networks']
        cognitive_processes = ['working memory', 'attention', 'semantic integration', 'syntactic parsing']
        
        return {
            "1": {
                "language_family": random.choice(language_families),
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "language_family": random.choice(language_families),
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a neurolinguistically-inspired AI system for multilingual language acquisition and processing, focusing on the {t['language_family']} language family, the linguistic feature of {t['linguistic_feature']}, and the cognitive process of {t['cognitive_process']}. Then, analyze its performance on a complex cross-linguistic task. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your AI system and how they interact.\n   b) Explain how your system incorporates neurolinguistic principles, particularly related to {t['cognitive_process']}.\n   c) Detail how your system models the acquisition and processing of {t['linguistic_feature']} in {t['language_family']} languages.\n   d) Include a diagram or flowchart illustrating your system's architecture (describe it textually).\n\n2. Language Acquisition Model (250-300 words):\n   a) Explain how your system acquires and represents knowledge about {t['linguistic_feature']} across multiple languages.\n   b) Describe any novel algorithms or approaches used in your language acquisition model.\n   c) Discuss how your model accounts for the specific characteristics of {t['language_family']} languages.\n\n3. Cross-Linguistic Processing (250-300 words):\n   a) Detail how your system processes and analyzes {t['linguistic_feature']} across different languages within the {t['language_family']}.\n   b) Explain how the system handles language-specific variations in {t['linguistic_feature']}.\n   c) Describe how {t['cognitive_process']} is modeled in your system's cross-linguistic processing.\n\n4. Performance Analysis (200-250 words):\n   a) Propose a complex cross-linguistic task that would challenge your system's capabilities.\n   b) Predict how your system would perform on this task, highlighting its strengths and potential limitations.\n   c) Compare your system's predicted performance to that of existing multilingual AI models.\n\n5. Neurolinguistic Implications (200-250 words):\n   a) Discuss how your AI system's performance might inform our understanding of human language acquisition and processing.\n   b) Explain how the system's handling of {t['linguistic_feature']} and {t['cognitive_process']} relates to current neurolinguistic theories.\n   c) Propose a hypothesis about human language processing based on your system's behavior.\n\n6. Ethical Considerations and Future Directions (150-200 words):\n   a) Address potential ethical concerns related to AI systems that can acquire and process multiple languages.\n   b) Suggest future research directions or potential applications of your system in fields such as language education, translation, or cognitive science.\n   c) Discuss how your system might be extended to incorporate other linguistic features or cognitive processes.\n\nEnsure your response demonstrates a deep understanding of neurolinguistics, artificial intelligence, and the specific characteristics of the {t['language_family']} language family. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            f"The system architecture demonstrates a clear understanding of neurolinguistic principles, particularly related to {t['cognitive_process']}.",
            f"The language acquisition model effectively addresses the {t['linguistic_feature']} in {t['language_family']} languages.",
            "The cross-linguistic processing explanation is thorough and scientifically plausible.",
            "The performance analysis includes a challenging and relevant cross-linguistic task.",
            "The response shows creativity and innovation while maintaining scientific rigor.",
            "The ethical considerations and future directions are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
