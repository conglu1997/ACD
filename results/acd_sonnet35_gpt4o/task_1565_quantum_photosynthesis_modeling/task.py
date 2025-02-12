import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                "effect": "quantum coherence",
                "biological_process": "light harvesting",
                "timescale": "femtoseconds"
            },
            {
                "effect": "quantum entanglement",
                "biological_process": "electron transfer",
                "timescale": "picoseconds"
            }
        ]
        return {
            "1": random.choice(quantum_effects),
            "2": random.choice(quantum_effects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational model to simulate and analyze the process of photosynthesis, focusing on the quantum effect of {t['effect']} in the biological process of {t['biological_process']}, which occurs on a {t['timescale']} timescale. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the quantum effect and its potential role in photosynthesis.
   b) Describe how this quantum effect might enhance or influence the specified biological process.
   c) Discuss the challenges of observing and modeling quantum effects at biological scales.
   d) Briefly explain the concept of quantum annealing and its relevance to your model.

2. Model Design (300-350 words):
   a) Outline the key components of your quantum-inspired computational model.
   b) Explain how your model incorporates the specified quantum effect.
   c) Describe how your model simulates the relevant biological processes.
   d) Provide a high-level mathematical or algorithmic representation of your model.

3. Simulation Approach (200-250 words):
   a) Describe the simulation techniques you would use to implement your model.
   b) Explain how you would handle the challenge of simulating quantum effects on the specified timescale.
   c) Discuss any novel computational methods or algorithms your approach might require.

4. Predictions and Testable Hypotheses (150-200 words):
   a) Describe two specific predictions your model makes about photosynthesis.
   b) Propose an experiment that could test one of these predictions.
   c) Explain how your model's predictions differ from classical (non-quantum) models of photosynthesis.

5. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired model with a classical model of photosynthesis.
   b) Discuss the advantages and limitations of each approach.
   c) Explain how your model addresses specific shortcomings of classical models.

6. Interdisciplinary Implications (200-250 words):
   a) Discuss how your model could inform or be applied in fields outside of quantum biology.
   b) Explain potential implications for our understanding of quantum effects in other biological systems.
   c) Speculate on how this research might influence the development of quantum technologies.

7. Limitations and Future Directions (150-200 words):
   a) Address potential limitations or criticisms of your quantum-inspired approach.
   b) Suggest two future research directions based on your model.
   c) Discuss ethical considerations related to this line of research.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and computational modeling. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and photosynthesis.",
            "The proposed model effectively incorporates the specified quantum effect into the simulation of photosynthesis.",
            "The simulation approach is well-thought-out and addresses the challenges of modeling quantum effects at biological scales.",
            "The predictions and proposed experiment are scientifically sound and clearly differentiated from classical models.",
            "The comparative analysis between the quantum-inspired and classical models is thorough and insightful.",
            "The discussion of interdisciplinary implications shows a broad understanding of the potential impact of this research.",
            "The response addresses limitations and future directions in a thoughtful and scientifically rigorous manner.",
            "The response draws meaningful connections between quantum effects in photosynthesis and potential applications in quantum computing or other technologies."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
