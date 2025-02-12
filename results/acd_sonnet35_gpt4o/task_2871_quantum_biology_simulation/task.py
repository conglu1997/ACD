import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_phenomena = [
            {
                "phenomenon": "Photosynthesis",
                "quantum_effect": "Quantum coherence in energy transfer"
            },
            {
                "phenomenon": "Magnetoreception in birds",
                "quantum_effect": "Radical pair mechanism"
            }
        ]
        return {
            "1": random.choice(biological_phenomena),
            "2": random.choice(biological_phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model to simulate quantum effects in biological systems, focusing on the phenomenon of {t['phenomenon']} and the quantum effect of {t['quantum_effect']}. Then, use your model to explore this biological phenomenon and propose a novel hypothesis. Your response should include the following sections:

1. Quantum Biology Framework (250-300 words):
   a) Explain the key principles of quantum mechanics relevant to the given biological phenomenon.
   b) Describe how these quantum effects are thought to influence the biological process.
   c) Discuss the challenges in studying quantum effects in biological systems.

2. Computational Model Design (300-350 words):
   a) Outline the key components of your computational model for simulating quantum effects in the given biological system.
   b) Explain how your model incorporates both quantum mechanical principles and biological processes.
   c) Describe any novel algorithms or approaches you've developed for this simulation.
   d) Discuss how your model addresses the challenges of simulating quantum effects in complex biological environments.

3. Simulation Process and Results (250-300 words):
   a) Describe the step-by-step process of how your model simulates the quantum effects in the given biological phenomenon.
   b) Present the key results from your simulation, including any unexpected findings.
   c) Explain how these results contribute to our understanding of the biological phenomenon.

4. Novel Hypothesis Generation (200-250 words):
   a) Based on your simulation results, propose a novel hypothesis about the role of quantum effects in the given biological phenomenon.
   b) Explain how your hypothesis builds upon or challenges existing theories in the field.
   c) Suggest potential experimental approaches to test your hypothesis.

5. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your findings for the field of quantum biology.
   b) Propose potential applications of your model in other areas of science or technology.
   c) Suggest future improvements or extensions to your computational model.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biology, as well as computational modeling techniques. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific rigor and plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum mechanics and its potential role in {t['phenomenon']}.",
            "The computational model design is innovative, scientifically plausible, and addresses the challenges of simulating quantum effects in biological systems.",
            "The simulation process and results are clearly explained and contribute meaningfully to understanding the biological phenomenon.",
            "The proposed hypothesis is novel, well-reasoned, and based on the simulation results.",
            "The response shows interdisciplinary knowledge integration and creative problem-solving in quantum biology.",
            "The implications and future directions are insightful and demonstrate an understanding of the broader field of quantum biology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
