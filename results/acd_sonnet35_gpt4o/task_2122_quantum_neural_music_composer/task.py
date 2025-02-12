import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sorrow', 'anger', 'fear', 'love', 'excitement']
        musical_styles = ['classical', 'jazz', 'electronic', 'folk', 'rock', 'ambient']
        return {
            "1": {"emotion": random.choice(emotions), "style": random.choice(musical_styles)},
            "2": {"emotion": random.choice(emotions), "style": random.choice(musical_styles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Design a quantum-inspired neural network for music composition that mimics human creativity and emotional expression, "
            f"focusing on the emotion of {t['emotion']} in the style of {t['style']} music. Your response should include:\n\n"
            "1. Quantum-Neural Architecture (300-350 words):\n"
            "   a) Describe the overall structure of your quantum-inspired neural network.\n"
            "   b) Explain how quantum principles are incorporated into the neural network design.\n"
            "   c) Discuss how this architecture mimics human creative processes in music composition.\n"
            "   d) Provide a diagram or detailed description of the network's key components and their interactions.\n\n"
            "2. Emotional Encoding (250-300 words):\n"
            f"   a) Explain how your system encodes and processes the emotion of {t['emotion']}.\n"
            "   b) Describe the neuroscientific principles used to model emotional expression in music.\n"
            "   c) Discuss how quantum states are used to represent emotional nuances.\n\n"
            "3. Musical Style Implementation (250-300 words):\n"
            f"   a) Detail how your system incorporates the principles of {t['style']} music.\n"
            "   b) Explain how the quantum-neural network generates music that adheres to this style.\n"
            "   c) Discuss any challenges in balancing emotional expression with stylistic constraints.\n\n"
            "4. Composition Process (200-250 words):\n"
            "   a) Outline the step-by-step process your system uses to compose a piece of music.\n"
            "   b) Explain how quantum operations and neural processing interact during composition.\n"
            "   c) Describe how the system ensures coherence and musical quality in its output.\n\n"
            "5. Training and Learning (200-250 words):\n"
            "   a) Propose a method for training your quantum-neural network.\n"
            "   b) Explain how the system learns to associate quantum states with musical elements and emotions.\n"
            "   c) Discuss any novel approaches to machine learning inspired by quantum principles.\n\n"
            "6. Output Analysis (150-200 words):\n"
            "   a) Describe the expected characteristics of the music produced by your system.\n"
            "   b) Explain how these characteristics reflect both the specified emotion and musical style.\n"
            "   c) Propose methods to evaluate the creativity and emotional expressiveness of the generated music.\n\n"
            "7. Ethical and Philosophical Implications (150-200 words):\n"
            "   a) Discuss the implications of using quantum-inspired AI for creative tasks traditionally done by humans.\n"
            "   b) Explore the philosophical questions raised by a system that mimics human emotional expression in art.\n"
            "   c) Propose guidelines for the responsible development and use of such systems.\n\n"
            "Ensure your response demonstrates a deep understanding of quantum computing, cognitive neuroscience, and music theory. "
            "Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology "
            "and provide clear explanations where necessary.\n\n"
            "Format your response with clear headings for each section. Your total response should be between 1500-1850 words."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and word counts.",
            "The quantum-neural architecture demonstrates a clear understanding of both quantum computing principles and neural network design.",
            f"The system effectively encodes and expresses the emotion of {t['emotion']} while adhering to the style of {t['style']} music.",
            "The composition process and training method are well-explained and scientifically plausible.",
            "The response shows creativity and innovation while maintaining scientific rigor.",
            "The ethical and philosophical implications are thoughtfully considered."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
