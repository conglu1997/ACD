import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("English", "Mandarin"),
            ("Spanish", "Arabic"),
            ("French", "Japanese"),
            ("German", "Russian"),
            ("Hindi", "Swahili")
        ]
        linguistic_features = [
            "phonology",
            "syntax",
            "semantics",
            "pragmatics",
            "morphology"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "language_pair": random.choice(language_pairs),
                "linguistic_feature": random.choice(linguistic_features)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that models the neurological processes involved in language acquisition and processing, focusing on multilingualism. Your system should specifically address the language pair {t['language_pair'][0]} and {t['language_pair'][1]}, with emphasis on the linguistic feature of {t['linguistic_feature']}. Then, analyze its performance in simulating language learning and code-switching. Your response should include:\n\n1. Neural Architecture (300-350 words):\n   a) Describe the key components of your AI system that model different brain regions involved in language processing.\n   b) Explain how these components interact to simulate language acquisition and bilingual processing.\n   c) Detail how your model incorporates current neuroscientific understanding of multilingualism.\n\n2. Language Acquisition Simulation (250-300 words):\n   a) Explain how your system models the acquisition of {t['language_pair'][0]} and {t['language_pair'][1]}.\n   b) Describe how the model accounts for differences in {t['linguistic_feature']} between these languages.\n   c) Discuss how your system simulates the development of bilingual competence over time.\n\n3. Code-switching Mechanism (200-250 words):\n   a) Detail how your AI system models code-switching between {t['language_pair'][0]} and {t['language_pair'][1]}.\n   b) Explain how the model accounts for the cognitive processes involved in switching between languages.\n   c) Describe how your system handles the specific challenges related to {t['linguistic_feature']} in code-switching.\n\n4. Performance Analysis (250-300 words):\n   a) Propose methods to evaluate your system's performance in language acquisition and code-switching.\n   b) Analyze potential strengths and weaknesses of your model compared to human bilingual performance.\n   c) Discuss how well your system captures the neurocognitive aspects of bilingualism.\n\n5. Practical Applications (150-200 words):\n   a) Suggest two potential applications of your AI system in language education or cognitive research.\n   b) Explain how these applications could benefit from the neurolinguistic approach of your model.\n\n6. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss ethical implications of using AI to model human language acquisition and processing.\n   b) Identify limitations of your approach and potential areas for future improvement.\n\nEnsure your response demonstrates a deep understanding of neuroscience, linguistics, and AI principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, linguistics, and AI principles in the context of multilingual language acquisition and processing",
            f"The proposed AI system presents a plausible and creative approach to modeling neurological processes involved in acquiring and processing {t['language_pair'][0]} and {t['language_pair'][1]}",
            f"The explanation of how the system handles {t['linguistic_feature']} in the context of these languages is thorough and insightful",
            "The code-switching mechanism is well-explained and grounded in current understanding of bilingual cognition",
            "The performance analysis and practical applications are thoughtfully considered and demonstrate strong interdisciplinary knowledge integration"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
