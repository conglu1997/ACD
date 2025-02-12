import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'quantum tunneling']
        evolutionary_mechanisms = ['natural selection', 'genetic drift', 'gene flow']
        information_theory_concepts = ['entropy', 'mutual information', 'channel capacity']
        
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms),
                "information_theory_concept": random.choice(information_theory_concepts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms),
                "information_theory_concept": random.choice(information_theory_concepts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired simulation model for genetic evolution that incorporates the quantum principle of {t['quantum_principle']}, the evolutionary mechanism of {t['evolutionary_mechanism']}, and the information theory concept of {t['information_theory_concept']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how the specified quantum principle can be analogously applied to genetic evolution.
   b) Describe how this quantum-inspired approach interacts with the given evolutionary mechanism.
   c) Discuss how the information theory concept is incorporated into your model.
   d) Propose a novel hypothesis about genetic evolution that emerges from this integration.

2. Model Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired genetic evolution simulation model.
   b) Explain how genetic information is represented and processed in your model.
   c) Detail how your model accounts for the specified evolutionary mechanism and information theory concept.
   d) Discuss any novel computational or representational elements in your design.

3. Simulation Experiment (200-250 words):
   a) Propose an experiment to test your model's predictions about genetic evolution.
   b) Describe the experimental setup, including initial conditions and measurement techniques.
   c) Explain how the results would support or refute your model.
   d) Discuss potential challenges in implementing this simulation and how they might be addressed.

4. Biological Implications (200-250 words):
   a) Suggest how your model might relate to current understanding of genetic evolution.
   b) Propose a real-world study that could provide evidence for your model's predictions.
   c) Discuss potential implications of your model for theories of adaptation or speciation.

5. Computational Implementation (150-200 words):
   a) Outline an approach for implementing a simplified version of your model in a classical computing environment.
   b) Discuss the limitations of this implementation and how true quantum computing might overcome them.
   c) Propose a novel quantum algorithm or data structure inspired by your model.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of your model, if it were to accurately represent genetic evolution.
   b) Propose two future research directions that could further develop or test your model.
   c) Speculate on how your model might influence the development of genetic engineering or synthetic biology.

Ensure your response demonstrates a deep understanding of quantum mechanics, evolutionary biology, information theory, and genetics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, evolutionary biology, information theory, and genetics.",
            "The theoretical framework effectively integrates the specified quantum principle, evolutionary mechanism, and information theory concept.",
            "The model architecture is well-described and incorporates novel computational or representational elements.",
            "The proposed simulation experiment is well-designed and addresses potential challenges.",
            "The biological implications and real-world applications are thoughtfully considered.",
            "The computational implementation discussion includes a novel quantum algorithm or data structure.",
            "Ethical considerations and future research directions are thoroughly addressed.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
