import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_theories = [
            "Construction Grammar",
            "Cognitive Grammar",
            "Usage-Based Theory of Language Acquisition",
            "Embodied Cognition in Language Processing",
            "Dynamic Systems Theory in Language Development",
            "Conceptual Metaphor Theory",
            "Frame Semantics",
            "Cognitive Semantics"
        ]
        ai_components = [
            "Attention Mechanisms",
            "Recursive Neural Networks",
            "Graph Neural Networks",
            "Memory Networks",
            "Meta-Learning Algorithms",
            "Neuro-symbolic Integration",
            "Hierarchical Reinforcement Learning",
            "Generative Adversarial Networks"
        ]
        return {
            "1": {"theory": random.choice(linguistic_theories), "ai_component": random.choice(ai_components)},
            "2": {"theory": random.choice(linguistic_theories), "ai_component": random.choice(ai_components)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel language model architecture inspired by the cognitive linguistics theory of {t['theory']}, incorporating elements of {t['ai_component']} from artificial intelligence. Your task has the following parts:\n\n1. Theoretical Foundation (150-200 words):\n   Explain the key principles of {t['theory']} and how they relate to human language acquisition and processing. Discuss why this theory is particularly relevant for AI language models.\n\n2. Architecture Design (250-300 words):\n   Describe your proposed language model architecture, including:\n   - How it incorporates principles from {t['theory']}\n   - How it utilizes or modifies {t['ai_component']}\n   - The main components and their interactions\n   - How the model processes and generates language\n   Provide a high-level diagram or pseudocode to illustrate your architecture.\n\n3. Learning and Adaptation (150-200 words):\n   Explain how your model would learn and adapt, addressing:\n   - The training process and data requirements\n   - How the model might simulate aspects of human language acquisition\n   - Potential for continual or lifelong learning\n\n4. Comparative Analysis (200-250 words):\n   Compare your proposed architecture to existing language models (e.g., GPT, BERT, T5):\n   - Potential advantages and novel capabilities\n   - Possible limitations or challenges\n   - How it might perform on various natural language processing tasks\n\n5. Implications and Future Directions (200-250 words):\n   Discuss the broader implications of your model for:\n   - AI and natural language processing\n   - Cognitive science and our understanding of human language\n   - Potential applications in fields like education, therapy, or human-computer interaction\n   Propose at least two directions for future research or development based on your architecture.\n\nEnsure your response demonstrates a deep understanding of both cognitive linguistics and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive linguistics theory and AI component.",
            "The proposed architecture creatively and coherently integrates principles from cognitive linguistics with AI techniques.",
            "The design is innovative yet scientifically plausible, with clear explanations of its components and functioning.",
            "The comparative analysis shows insight into the strengths and limitations of the proposed model relative to existing approaches.",
            "The discussion of implications and future directions is thoughtful and demonstrates an understanding of the broader context of AI and cognitive science.",
            "The overall response is well-structured, logically consistent, and demonstrates high-level interdisciplinary thinking and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
