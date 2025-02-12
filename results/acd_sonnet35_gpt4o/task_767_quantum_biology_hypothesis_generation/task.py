import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            'Photosynthesis',
            'Magnetoreception in birds',
            'Olfaction (sense of smell)',
            'Enzyme catalysis'
        ]
        quantum_effects = [
            'Quantum tunneling',
            'Quantum coherence',
            'Quantum entanglement',
            'Zero-point energy'
        ]
        tasks = [
            {
                'biological_process': random.choice(biological_processes),
                'quantum_effect': random.choice(quantum_effects)
            },
            {
                'biological_process': random.choice(biological_processes),
                'quantum_effect': random.choice(quantum_effects)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As a quantum biologist, your task is to generate and evaluate a hypothesis for how {t['quantum_effect']} might play a role in {t['biological_process']}, then design a theoretical experiment to test your hypothesis. Follow these steps:

1. Hypothesis Generation (200-250 words):
   a) Propose a specific hypothesis for how the given quantum effect could influence the biological process.
   b) Explain the potential mechanisms involved, integrating concepts from quantum physics and molecular biology.
   c) Discuss how this quantum effect might provide an advantage or unique feature to the biological process.

2. Theoretical Background (150-200 words):
   a) Provide a brief overview of the relevant quantum mechanical principles.
   b) Explain the key aspects of the biological process that might be influenced by quantum effects.
   c) Discuss any existing research or theories that support or relate to your hypothesis.

3. Experimental Design (250-300 words):
   a) Propose a detailed experimental setup to test your hypothesis.
   b) Describe the methods and techniques you would use, including any specialized equipment.
   c) Explain how your experiment could distinguish between quantum and classical effects.
   d) Discuss potential controls and how you would account for confounding variables.

4. Predicted Outcomes and Interpretation (150-200 words):
   a) Describe the results you would expect if your hypothesis is correct.
   b) Explain how these results would support the involvement of quantum effects.
   c) Discuss alternative explanations and how you would rule them out.

5. Implications and Future Directions (100-150 words):
   a) Discuss the potential implications of your hypothesis if proven correct.
   b) Suggest future research directions or applications that could stem from this work.

Ensure your response demonstrates a deep understanding of both quantum mechanics and molecular biology. Use appropriate scientific terminology and provide clear explanations of complex concepts. Be creative in your hypothesis and experimental design while maintaining scientific plausibility and rigor.

Your total response should be between 850-1100 words. Strive for a balance between scientific accuracy and creative thinking in your approach.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and molecular biology.",
            "The hypothesis is creative, plausible, and well-explained, integrating concepts from quantum physics and biology.",
            "The experimental design is detailed, feasible, and specifically tailored to test the proposed hypothesis.",
            "The predicted outcomes and their interpretation show a clear understanding of how to distinguish quantum effects from classical ones.",
            "The implications and future directions are insightful and demonstrate an understanding of the broader impact of quantum biology.",
            "The response maintains a balance between scientific accuracy and creative thinking throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
