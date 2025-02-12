import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = ['superposition', 'entanglement', 'decoherence']
        linguistic_phenomena = ['semantic shift', 'syntactic change', 'phonological evolution']
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired model of language processing that incorporates the quantum concept of {t['quantum_concept']} to explain the linguistic phenomenon of {t['linguistic_phenomenon']}. Your response should include:\n\n1. Theoretical Framework (300-350 words):\n   a) Explain how the specified quantum concept can be analogously applied to language processing.\n   b) Describe how this quantum-inspired approach interacts with the given linguistic phenomenon.\n   c) Discuss how information theory principles are incorporated into your model.\n   d) Propose a novel hypothesis about language change or variation that emerges from this integration.\n\n2. Model Architecture (250-300 words):\n   a) Describe the key components of your quantum-inspired language processing model.\n   b) Explain how temporal dynamics are represented and processed in your model.\n   c) Detail how your model accounts for both diachronic change and synchronic variation.\n   d) Discuss any novel computational or representational elements in your design.\n\n3. Simulated Experiment (200-250 words):\n   a) Propose an experiment to test your model's predictions about language change or variation.\n   b) Describe the experimental setup, including data sources and measurement techniques.\n   c) Explain how the results would support or refute your model.\n   d) Discuss potential challenges in implementing this experiment and how they might be addressed.\n\n4. Linguistic Implications (200-250 words):\n   a) Discuss how your model might influence current theories of language change and variation.\n   b) Propose a corpus study that could provide evidence for your model.\n   c) Explain potential implications for understanding the relationship between language and cognition.\n\n5. Computational Implementation (150-200 words):\n   a) Outline an approach for implementing a simplified version of your model.\n   b) Discuss the limitations of this implementation and how quantum computing might overcome them.\n   c) Propose a novel algorithm or data structure inspired by your model.\n\n6. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss potential ethical implications of your model, particularly regarding language preservation and evolution.\n   b) Propose two future research directions that could further develop or test your model.\n   c) Speculate on how your model might influence the development of AI language processing systems.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, linguistics, information theory, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified quantum concept and linguistic phenomenon",
            "The proposed model integrates quantum principles, linguistics, and information theory in a novel and coherent manner",
            "The simulated experiment is well-designed and directly tests the model's predictions",
            "The response shows originality in approach and generates novel insights or hypotheses about language processing",
            "The computational implementation and future directions are feasible and scientifically grounded",
            "The ethical considerations are thoughtful and relevant to the proposed model"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
