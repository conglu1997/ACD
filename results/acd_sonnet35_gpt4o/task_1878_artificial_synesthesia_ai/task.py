import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "input_type": "music",
                "output_type": "visual",
                "synesthesia_type": "chromesthesia"
            },
            {
                "input_type": "visual",
                "output_type": "music",
                "synesthesia_type": "visual-auditory"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of artificial {t['synesthesia_type']} synesthesia, then use it to translate a piece of {t['input_type']} into a {t['output_type']} representation. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the main components of your AI system and their functions.\n   b) Explain how your system mimics the cognitive processes involved in {t['synesthesia_type']}.\n   c) Discuss any novel features that make your system particularly suited for {t['input_type']}-to-{t['output_type']} translation.\n\n2. Sensory Processing Mechanism (200-250 words):\n   a) Explain the step-by-step process your AI system uses to analyze the input {t['input_type']}.\n   b) Describe how your system generates the corresponding {t['output_type']} output.\n   c) Discuss any constraints or guidelines your system follows to maintain perceptual consistency.\n\n3. Neuroscientific Basis (150-200 words):\n   a) Discuss the neuroscientific theories or models of synesthesia that inform your AI system's design.\n   b) Explain how your system accounts for individual differences in synesthetic experiences.\n\n4. Example Translation (200-250 words):\n   a) Provide a detailed example of how your system would translate a specific {t['input_type']} input to a {t['output_type']} output.\n   b) Explain the rationale behind the translation choices made by your AI system.\n\n5. Evaluation and Validation (150-200 words):\n   a) Propose a method to evaluate the accuracy and consistency of your AI system's synesthetic translations.\n   b) Discuss how you would validate your system's output against human synesthetic experiences.\n\n6. Potential Applications and Ethical Considerations (150-200 words):\n   a) Explore potential applications of your artificial synesthesia AI system in fields such as art, therapy, or human-computer interaction.\n   b) Discuss ethical implications of creating AI systems that simulate human perceptual experiences.\n\nEnsure your response demonstrates a deep understanding of cognitive science, neuroscience, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.\n\nFormat your response with clear headings for each section and subsections where appropriate. Your total response should be between 1100-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synesthesia and its neural basis",
            "The AI system design is innovative and scientifically plausible",
            "The sensory processing mechanism is clearly explained and logical",
            "The example translation is detailed and consistent with the proposed system",
            "The evaluation and validation methods are well-thought-out and feasible",
            "Potential applications and ethical considerations are thoroughly discussed",
            "The response uses appropriate terminology from cognitive science, neuroscience, and AI",
            "The overall response shows interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
