import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {
                "emotion": "nostalgia",
                "brain_region": "hippocampus",
                "musical_element": "harmonic progression"
            },
            {
                "emotion": "excitement",
                "brain_region": "nucleus accumbens",
                "musical_element": "rhythm"
            }
        ]
        return {
            "1": random.choice(emotions),
            "2": random.choice(emotions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that generates music to evoke the emotion of {t['emotion']}, focusing on the brain region {t['brain_region']} and the musical element of {t['musical_element']}. Your response should include the following sections:\n\n1. Cognitive Neuroscience Framework (250-300 words):\n   a) Explain the role of the {t['brain_region']} in processing the emotion of {t['emotion']}.\n   b) Describe how {t['musical_element']} can influence this brain region and emotional state.\n   c) Discuss any relevant theories or studies linking music, emotion, and brain function.\n\n2. AI System Architecture (300-350 words):\n   a) Outline the key components of your AI music generation system.\n   b) Explain how your system incorporates cognitive neuroscience principles.\n   c) Describe how your AI models and manipulates {t['musical_element']} to target the {t['brain_region']}.\n   d) Include a high-level diagram or pseudocode of your system's architecture.\n\n3. Music Theory Integration (200-250 words):\n   a) Explain how your system applies music theory principles to evoke {t['emotion']}.\n   b) Describe specific musical techniques or structures your AI uses to manipulate {t['musical_element']}.\n   c) Discuss how your system balances adherence to music theory with novel, emotion-driven composition.\n\n4. Training and Data (200-250 words):\n   a) Propose a method for training your AI system, including data sources and preprocessing.\n   b) Explain how you would incorporate human emotional responses into the training process.\n   c) Discuss any ethical considerations in data collection and use for this purpose.\n\n5. Evaluation and Validation (150-200 words):\n   a) Propose methods to evaluate the effectiveness of your AI in evoking {t['emotion']}.\n   b) Describe how you would validate the neuroscientific basis of your approach.\n   c) Discuss potential challenges in measuring and quantifying emotional responses to AI-generated music.\n\n6. Potential Applications and Implications (150-200 words):\n   a) Suggest two potential applications of your emotion-evoking AI music system.\n   b) Discuss the broader implications of this technology for music, therapy, and human-AI interaction.\n   c) Address any ethical concerns or potential misuses of emotion-manipulating AI music.\n\n7. Specific Example (100-150 words):\n   Provide a detailed description of a short musical piece your AI might generate to evoke {t['emotion']}. Include specific references to {t['musical_element']} and how it would theoretically activate the {t['brain_region']}.\n\nEnsure your response demonstrates a deep understanding of cognitive neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the role of the {t['brain_region']} in processing the emotion of {t['emotion']}.",
            f"The AI system architecture effectively incorporates cognitive neuroscience principles and manipulates {t['musical_element']} to target the {t['brain_region']}.",
            "The music theory integration is well-explained and balances traditional principles with novel, emotion-driven composition.",
            "The proposed training method and data sources are appropriate and address ethical considerations.",
            "The evaluation and validation methods are well-thought-out and address the challenges of measuring emotional responses.",
            "The potential applications and implications are insightful and address ethical concerns.",
            f"A specific example of an AI-generated musical piece to evoke {t['emotion']} is provided, with clear references to {t['musical_element']} and its effect on the {t['brain_region']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
