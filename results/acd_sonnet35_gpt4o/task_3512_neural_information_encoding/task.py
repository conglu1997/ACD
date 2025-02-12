import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_state": "Decision-making under uncertainty",
                "neuroscience_principle": "Predictive coding",
                "information_theory_concept": "Mutual information",
                "ai_application": "Reinforcement learning agent"
            },
            {
                "cognitive_state": "Emotional regulation",
                "neuroscience_principle": "Neuroplasticity",
                "information_theory_concept": "Entropy reduction",
                "ai_application": "Affective computing system"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system that encodes and decodes the complex cognitive state of {t['cognitive_state']} using the neuroscience principle of {t['neuroscience_principle']} and the information theory concept of {t['information_theory_concept']}. Then, apply this system to enhance the performance of an {t['ai_application']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your neural information encoding and decoding system.\n   b) Explain how your system incorporates the specified neuroscience principle and information theory concept.\n   c) Detail how your system encodes and decodes the given cognitive state.\n   d) Include a high-level diagram or flowchart of your system (using ASCII art or clear textual description).\n\n2. Encoding Process (250-300 words):\n   a) Explain the step-by-step process of encoding the specified cognitive state.\n   b) Describe how your system translates neural activity into an information-theoretic representation.\n   c) Discuss any novel algorithms or techniques used in the encoding process.\n\n3. Decoding Process (250-300 words):\n   a) Detail the method for decoding the information-theoretic representation back into a neural or cognitive state.\n   b) Explain how your system ensures accuracy and robustness in the decoding process.\n   c) Discuss how your system handles potential noise or errors in the encoded information.\n\n4. Application to AI (200-250 words):\n   a) Describe how your neural information encoding/decoding system can be integrated with the specified AI application.\n   b) Explain the potential benefits of using your system in this AI context.\n   c) Discuss any challenges in applying your system to the given AI application and how you would address them.\n\n5. Comparative Analysis (150-200 words):\n   a) Compare your system to existing methods of representing cognitive states in AI.\n   b) Discuss potential advantages and limitations of your approach.\n\n6. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues related to encoding and decoding cognitive states.\n   b) Propose guidelines for the responsible development and use of such systems in AI applications.\n\n7. Future Research Directions (100-150 words):\n   a) Suggest two potential extensions or modifications to your system for different cognitive states or AI applications.\n   b) Propose a specific research question that emerges from your design.\n\nEnsure your response demonstrates a deep understanding of neuroscience, information theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1750 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed system that integrates {t['neuroscience_principle']} and {t['information_theory_concept']} to encode and decode {t['cognitive_state']}.",
            f"The encoding and decoding processes are clearly explained and scientifically plausible.",
            f"The application to the {t['ai_application']} is well-reasoned and considers potential benefits and challenges.",
            "The comparative analysis demonstrates a deep understanding of existing methods and the advantages of the proposed system.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "Ethical considerations are thoroughly addressed, and responsible development guidelines are proposed.",
            "The suggested future research directions are novel and relevant to the field."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
