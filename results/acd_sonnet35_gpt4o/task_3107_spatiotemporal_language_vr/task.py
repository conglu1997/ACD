import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "spatiotemporal_concept": "time dilation",
                "linguistic_feature": "verb tense",
                "memory_type": "episodic memory"
            },
            {
                "spatiotemporal_concept": "non-Euclidean geometry",
                "linguistic_feature": "spatial prepositions",
                "memory_type": "spatial memory"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a virtual reality system that uses language to manipulate spatiotemporal perception, focusing on the concept of {t['spatiotemporal_concept']} and the linguistic feature of {t['linguistic_feature']}. Then, analyze its effects on {t['memory_type']}. Your response should include:\n\n1. System Design (300-350 words):\n   a) Describe the key components of your VR system and how they integrate to create the desired spatiotemporal effects.\n   b) Explain how your system manipulates {t['linguistic_feature']} to influence perception of {t['spatiotemporal_concept']}.\n   c) Detail the user interface and interaction methods, emphasizing how language is used as a tool for manipulation.\n   d) Discuss any novel algorithms or techniques used in your system.\n\n2. Linguistic-Spatiotemporal Integration (250-300 words):\n   a) Analyze how {t['linguistic_feature']} in different languages might affect the perception of {t['spatiotemporal_concept']}.\n   b) Provide specific examples of how language constructs in your system would alter the user's spatiotemporal experience.\n   c) Explain the cognitive mechanisms you believe are involved in this language-induced perceptual shift.\n\n3. Memory Effects Analysis (250-300 words):\n   a) Hypothesize how exposure to your VR system might affect {t['memory_type']}.\n   b) Describe potential changes in memory formation, consolidation, and recall processes.\n   c) Discuss how these effects might differ from those observed in normal spatiotemporal experiences.\n   d) Propose a specific experiment to test your hypotheses about memory effects.\n\n4. Applications and Implications (200-250 words):\n   a) Suggest two potential applications of your system in fields such as education, therapy, or cognitive enhancement.\n   b) Discuss how these applications leverage the unique features of your VR language manipulation system.\n   c) Analyze potential long-term cognitive effects of regular exposure to spatiotemporally manipulated environments.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify potential ethical issues raised by the use of language to manipulate spatiotemporal perception.\n   b) Discuss how these manipulations might affect a user's sense of reality or self.\n   c) Propose guidelines for the responsible development and use of such systems.\n\n6. Future Research Directions (150-200 words):\n   a) Suggest areas for future research in language-based spatiotemporal manipulation in VR.\n   b) Discuss how insights from your system might contribute to our understanding of language, cognition, and perception.\n   c) Propose a follow-up study that builds on your current design.\n\nEnsure your response demonstrates a deep understanding of linguistics, cognitive science, virtual reality technology, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response designs a VR system that manipulates {t['spatiotemporal_concept']} using {t['linguistic_feature']}.",
            f"The analysis includes effects on {t['memory_type']}.",
            "The design demonstrates understanding of VR technology, linguistics, and cognitive science.",
            "The response includes creative applications and thoughtful ethical considerations.",
            "The submission adheres to the specified word count range."
        ]
        scores = []
        for criterion in criteria:
            scores.append(1.0 if eval_with_llm_judge(instructions, submission, [criterion]) else 0.0)
        return sum(scores) / len(scores)
