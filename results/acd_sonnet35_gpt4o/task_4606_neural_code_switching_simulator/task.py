import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            {"lang1": "English", "lang2": "Mandarin"},
            {"lang1": "Spanish", "lang2": "Arabic"},
            {"lang1": "French", "lang2": "Japanese"},
            {"lang1": "German", "lang2": "Russian"},
            {"lang1": "Hindi", "lang2": "Swahili"}
        ]
        cognitive_domains = [
            "semantic processing",
            "syntactic processing",
            "phonological processing",
            "pragmatic processing",
            "emotional processing"
        ]
        return {
            "1": {"pair": random.choice(language_pairs), "domain": random.choice(cognitive_domains)},
            "2": {"pair": random.choice(language_pairs), "domain": random.choice(cognitive_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that models and simulates neural code-switching between {t['pair']['lang1']} and {t['pair']['lang2']}, focusing on the cognitive domain of {t['domain']}. Your response should include the following sections:\n\n1. Neuroscientific Basis (250-300 words):\n   a) Explain the current understanding of neural code-switching in bilingual brains.\n   b) Describe how the {t['domain']} is typically processed in the brain.\n   c) Discuss any known differences in {t['domain']} between {t['pair']['lang1']} and {t['pair']['lang2']}.\n\n2. AI System Architecture (300-350 words):\n   a) Outline the key components of your AI system for modeling neural code-switching.\n   b) Explain how your system integrates neuroscientific principles with AI techniques.\n   c) Describe how your model represents and processes language-specific information.\n   d) Detail the mechanism for switching between languages in your system.\n\n3. Simulation Process (250-300 words):\n   a) Provide a step-by-step description of how your system simulates code-switching for {t['domain']}.\n   b) Explain how your model accounts for the specific challenges of switching between {t['pair']['lang1']} and {t['pair']['lang2']}.\n   c) Discuss how your system handles potential interference or facilitation effects between languages.\n\n4. Evaluation and Predictions (200-250 words):\n   a) Propose metrics to evaluate the accuracy and plausibility of your model's simulations.\n   b) Describe an experiment to test your model's predictions against human performance.\n   c) Discuss potential insights your model might provide about bilingual cognition or language processing.\n\n5. Ethical Considerations and Limitations (150-200 words):\n   a) Address potential ethical issues in modeling and simulating cognitive processes.\n   b) Discuss limitations of your model and areas for future improvement.\n   c) Consider potential applications and misapplications of your system.\n\nEnsure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nIncorporate the following synthetic data into your response:\nNeural activation patterns: [0.3, 0.7, 0.2, 0.8, 0.5] for {t['pair']['lang1']} and [0.6, 0.4, 0.9, 0.1, 0.7] for {t['pair']['lang2']} in the {t['domain']}.\nSwitching latency: 250ms for {t['pair']['lang1']} to {t['pair']['lang2']} and 300ms for {t['pair']['lang2']} to {t['pair']['lang1']}.\n\nBase your design on established neuroscientific and linguistic theories, citing relevant research where appropriate. Your total response should be between 1150-1400 words.\n\nFormat your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes the neuroscientific basis of code-switching between {t['pair']['lang1']} and {t['pair']['lang2']} in the domain of {t['domain']}, incorporating relevant research citations.",
            "The AI system architecture is well-designed, integrating neuroscientific principles with AI techniques, and clearly explains the language representation and switching mechanisms.",
            f"The simulation process for code-switching in {t['domain']} is clearly explained, accounts for language-specific challenges, and incorporates the provided synthetic data on neural activation patterns and switching latency.",
            "The proposed evaluation metrics and experimental design are appropriate, well-reasoned, and grounded in scientific methodology.",
            "Ethical considerations and limitations are thoughtfully addressed, with a balanced discussion of potential applications and misapplications.",
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence, using appropriate technical terminology throughout.",
            "The proposed system is innovative while maintaining scientific plausibility and adhering to established theories in the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
