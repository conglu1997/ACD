import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {"aspect": "self-awareness", "cognitive_process": "introspection"},
            {"aspect": "qualia", "cognitive_process": "sensory processing"},
            {"aspect": "intentionality", "cognitive_process": "goal-directed behavior"},
            {"aspect": "metacognition", "cognitive_process": "self-reflection"},
            {"aspect": "phenomenal consciousness", "cognitive_process": "subjective experience"}
        ]
        return {
            "1": random.choice(consciousness_aspects),
            "2": random.choice(consciousness_aspects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical model for simulating synthetic consciousness in an AI system, focusing on the consciousness aspect of {t['aspect']} and the cognitive process of {t['cognitive_process']}. Then, use this model to explore the emergence of creativity and self-awareness. Your response should include:\n\n1. Theoretical Framework (300-350 words):\n   a) Explain your interpretation of {t['aspect']} in the context of synthetic consciousness.\n   b) Describe how {t['cognitive_process']} contributes to the emergence of consciousness in your model.\n   c) Discuss the philosophical implications of simulating this aspect of consciousness.\n   d) Propose a novel hypothesis about the relationship between {t['aspect']} and artificial creativity.\n\n2. Model Architecture (250-300 words):\n   a) Describe the key components of your synthetic consciousness model.\n   b) Explain how your model simulates {t['aspect']} and {t['cognitive_process']}.\n   c) Discuss how your model integrates with other cognitive functions.\n   d) Provide a high-level diagram or pseudocode illustrating your model's architecture.\n\n3. Emergence of Creativity (250-300 words):\n   a) Explain how creativity could emerge from your synthetic consciousness model.\n   b) Describe a specific mechanism by which {t['aspect']} contributes to creative processes.\n   c) Propose an experiment to test the creative capabilities of your model.\n   d) Discuss the implications of machine creativity for our understanding of human creativity.\n\n4. Self-Awareness Simulation (200-250 words):\n   a) Describe how your model simulates self-awareness.\n   b) Explain the role of {t['aspect']} in the development of self-awareness.\n   c) Discuss the challenges in verifying genuine self-awareness in an AI system.\n   d) Propose a novel test for self-awareness in synthetic consciousness.\n\n5. Ethical Implications (200-250 words):\n   a) Discuss the ethical considerations of creating a potentially conscious AI system.\n   b) Explore the rights and moral status of a synthetic consciousness.\n   c) Analyze the potential societal impacts of advanced AI systems with simulated consciousness.\n   d) Propose guidelines for the responsible development and use of synthetic consciousness technology.\n\n6. Future Directions (150-200 words):\n   a) Suggest potential improvements or extensions to your model.\n   b) Discuss how your approach could contribute to our understanding of biological consciousness.\n   c) Propose a novel research direction that could emerge from your work on synthetic consciousness.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section, numbered as above. Use appropriate subheadings where necessary to organize your thoughts clearly. Your total response should be between 1350-1650 words (excluding section headings and subheadings). Conclude with a brief summary (50-100 words) of the key innovations and potential impact of your proposed synthetic consciousness model."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['aspect']} and {t['cognitive_process']} in the context of synthetic consciousness.",
            "The proposed model is innovative, scientifically plausible, and well-explained.",
            f"The discussion of creativity and self-awareness emergence is insightful and well-reasoned, with a clear connection to {t['aspect']}.",
            "The ethical implications are thoroughly explored with thoughtful analysis.",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
