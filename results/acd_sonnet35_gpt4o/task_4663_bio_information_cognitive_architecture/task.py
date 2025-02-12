import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "biological_process": "DNA replication",
                "information_theory_concept": "Shannon entropy",
                "cognitive_function": "Memory consolidation"
            },
            {
                "biological_process": "Protein folding",
                "information_theory_concept": "Kolmogorov complexity",
                "cognitive_function": "Decision making under uncertainty"
            },
            {
                "biological_process": "Neural signaling",
                "information_theory_concept": "Mutual information",
                "cognitive_function": "Pattern recognition"
            },
            {
                "biological_process": "Gene expression",
                "information_theory_concept": "Compression ratio",
                "cognitive_function": "Learning and adaptation"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical bio-inspired cognitive architecture that uses principles from molecular biology and information theory to model complex information processing and decision-making in living systems. Focus on the following scenario:\n\nBiological process: {t['biological_process']}\nInformation theory concept: {t['information_theory_concept']}\nCognitive function: {t['cognitive_function']}\n\nYour response should include the following sections:\n\n1. Theoretical Framework (300-350 words):\n   a) Explain how the specified biological process can be used as a model for information processing.\n   b) Describe how the given information theory concept applies to this biological process.\n   c) Discuss how these principles could be used to model the specified cognitive function.\n   d) Propose a novel hypothesis that integrates these three elements.\n\n2. Architecture Design (250-300 words):\n   a) Describe the key components of your bio-inspired cognitive architecture.\n   b) Explain how your architecture implements the biological process and information theory concept.\n   c) Discuss how your architecture models the specified cognitive function.\n   d) Include a simple diagram or flowchart illustrating your architecture. (Describe this textually, e.g., 'Component A connects to Component B, which processes information and sends output to Component C')\n\n3. Information Processing Mechanism (200-250 words):\n   a) Detail how information is encoded, processed, and transmitted in your architecture.\n   b) Explain how your system handles noise, errors, or uncertainty.\n   c) Compare the efficiency and capacity of your bio-inspired system to traditional computing architectures.\n\n4. Cognitive Function Simulation (200-250 words):\n   a) Provide a specific example of how your architecture would simulate the given cognitive function.\n   b) Describe the inputs, processing steps, and outputs of this simulation.\n   c) Discuss any emergent properties or behaviors that might arise from your architecture.\n\n5. Potential Applications and Implications (150-200 words):\n   a) Propose two potential applications of your bio-inspired cognitive architecture.\n   b) Discuss how your architecture might inform our understanding of biological cognition.\n   c) Consider the implications of your model for the development of new AI systems.\n\n6. Experimental Validation and Future Work (150-200 words):\n   a) Suggest an experiment to validate a key aspect of your architecture.\n   b) Discuss potential challenges in implementing or testing your model.\n   c) Propose two directions for future research based on your architecture.\n\nEnsure your response demonstrates a deep understanding of molecular biology, information theory, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words. Use numbered paragraphs within each section for clarity."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_process']}, {t['information_theory_concept']}, and {t['cognitive_function']}.",
            "The proposed architecture effectively integrates the specified biological process, information theory concept, and cognitive function.",
            "The information processing mechanism is well-explained and plausible, including how it handles noise, errors, or uncertainty.",
            f"The cognitive function simulation for {t['cognitive_function']} is detailed and coherent, with clear inputs, processing steps, and outputs.",
            "The potential applications and implications are thoughtfully considered and relevant to the proposed architecture.",
            "The experimental validation proposal and future work suggestions are specific, relevant, and well-reasoned.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response is well-structured, clear, and within the specified word count range (1250-1550 words).",
            "The response includes a textual description of a diagram or flowchart for the architecture design."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
