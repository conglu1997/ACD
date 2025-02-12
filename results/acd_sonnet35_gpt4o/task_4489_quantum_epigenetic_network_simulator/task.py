import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Quantum superposition",
            "Quantum entanglement",
            "Quantum tunneling",
            "Quantum decoherence"
        ]
        epigenetic_mechanisms = [
            "DNA methylation",
            "Histone modification",
            "Chromatin remodeling",
            "Non-coding RNA regulation"
        ]
        info_theory_principles = [
            "Shannon entropy",
            "Mutual information",
            "Kolmogorov complexity",
            "Channel capacity"
        ]
        
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "epigenetic_mechanism": random.choice(epigenetic_mechanisms),
                "info_theory_principle": random.choice(info_theory_principles)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "epigenetic_mechanism": random.choice(epigenetic_mechanisms),
                "info_theory_principle": random.choice(info_theory_principles)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired model for simulating complex epigenetic regulatory networks, focusing on the quantum concept of {t['quantum_concept']}, the epigenetic mechanism of {t['epigenetic_mechanism']}, and the information theory principle of {t['info_theory_principle']}. Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired epigenetic network model.
   b) Explain how you incorporate the specified quantum concept into your model.
   c) Detail how your model represents and simulates the given epigenetic mechanism.
   d) Discuss how the chosen information theory principle is integrated into your model.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how your model bridges the gap between quantum phenomena and epigenetic processes.
   b) Discuss any novel theoretical frameworks or analogies you've developed to connect these domains.
   c) Address potential criticisms or limitations of applying quantum concepts to biological systems.

3. Simulation Process (250-300 words):
   a) Describe the step-by-step process of how your model simulates epigenetic regulatory networks.
   b) Explain how your model handles the complexity and stochasticity of biological systems.
   c) Discuss how the quantum-inspired approach enhances the simulation compared to classical models.

4. Information Processing and Analysis (200-250 words):
   a) Detail how your model applies the specified information theory principle to analyze epigenetic networks.
   b) Explain any novel insights or predictions your model might generate about epigenetic regulation.
   c) Discuss how your model's information processing capabilities could advance our understanding of epigenetics.

5. Experimental Validation (150-200 words):
   a) Propose a hypothetical experiment to validate your model's predictions or capabilities.
   b) Describe the data you would need and how you would collect it.
   c) Explain how you would interpret the results in the context of your quantum-inspired model.

6. Interdisciplinary Implications (200-250 words):
   a) Discuss the potential impact of your model on the fields of quantum biology, epigenetics, and information theory.
   b) Explore possible applications of your model in personalized medicine or drug discovery.
   c) Consider how your approach might inspire new research directions or technologies.

7. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical implications or concerns related to your model and its applications.
   b) Discuss any limitations or assumptions in your model that could affect its real-world applicability.
   c) Propose guidelines for the responsible development and use of quantum-inspired biological models.

Ensure your response demonstrates a deep understanding of quantum mechanics, epigenetics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing potential limitations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate detail and adheres to the specified word count range.",
            f"The model effectively incorporates the quantum concept of {t['quantum_concept']}, the epigenetic mechanism of {t['epigenetic_mechanism']}, and the information theory principle of {t['info_theory_principle']}.",
            "The quantum-biological interface is well-explained and addresses potential criticisms.",
            "The simulation process is clearly described and demonstrates how the quantum-inspired approach enhances the model.",
            "The application of information theory principles is well-explained and demonstrates novel insights.",
            "The proposed experimental validation is feasible and well-reasoned.",
            "The interdisciplinary implications are thoroughly explored and demonstrate creativity.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response demonstrates a deep understanding of quantum mechanics, epigenetics, and information theory.",
            "The proposed model is innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
