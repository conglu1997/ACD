import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = ['quantum tunneling', 'quantum coherence', 'quantum entanglement']
        enzyme_types = ['oxidoreductases', 'transferases', 'hydrolases', 'lyases', 'isomerases', 'ligases']
        applications = ['drug design', 'biocatalysis optimization', 'personalized enzyme therapeutics']
        
        tasks = {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "enzyme_type": random.choice(enzyme_types),
                "application": random.choice(applications),
                "kinetic_data": {
                    "Km": round(random.uniform(0.1, 10.0), 2),  # Michaelis constant (mM)
                    "kcat": round(random.uniform(1, 1000), 2),  # Turnover number (s^-1)
                    "temperature": round(random.uniform(20, 40), 1)  # Temperature (°C)
                }
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "enzyme_type": random.choice(enzyme_types),
                "application": random.choice(applications),
                "kinetic_data": {
                    "Km": round(random.uniform(0.1, 10.0), 2),
                    "kcat": round(random.uniform(1, 1000), 2),
                    "temperature": round(random.uniform(20, 40), 1)
                }
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational model to simulate and optimize enzyme catalysis for {t['enzyme_type']}, focusing on the quantum effect of {t['quantum_effect']} and exploring applications in {t['application']}. Use the provided enzyme kinetic data: Km = {t['kinetic_data']['Km']} mM, kcat = {t['kinetic_data']['kcat']} s^-1, at {t['kinetic_data']['temperature']}°C. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the role of {t['quantum_effect']} in enzyme catalysis.
   b) Describe how this quantum effect contributes to the efficiency of {t['enzyme_type']}.
   c) Discuss the potential for optimizing enzyme function through quantum-inspired approaches.
   d) Relate the provided kinetic data to the quantum effect and enzyme efficiency.

2. Computational Model Design (300-350 words):
   a) Outline the architecture of your quantum-inspired computational model.
   b) Explain how your model simulates enzyme catalysis and incorporates {t['quantum_effect']}.
   c) Describe the key algorithms or techniques used in your simulation.
   d) Provide a high-level pseudocode (10-15 lines) illustrating a critical component of your model.

3. Optimization Strategy (200-250 words):
   a) Propose a method for optimizing enzyme catalysis using your computational model.
   b) Explain how your optimization strategy leverages quantum principles.
   c) Discuss potential trade-offs or limitations in your approach.
   d) Describe how your strategy would improve the given kinetic parameters.

4. Application to {t['application']} (200-250 words):
   a) Describe how your model could be applied to {t['application']}.
   b) Discuss the potential benefits and challenges of using your approach in this field.
   c) Propose a specific example or use case demonstrating the potential impact of your model.
   d) Explain how the optimized enzyme parameters would benefit the chosen application.

5. Validation and Experimental Design (200-250 words):
   a) Describe how you would validate your model's accuracy in simulating enzyme catalysis.
   b) Propose an experimental setup to test predictions made by your model.
   c) Discuss how you would compare your model's performance to classical simulation methods.
   d) Explain how you would measure the impact of the quantum effect on enzyme catalysis.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical implications or risks associated with your proposed model and its applications.
   b) Suggest guidelines for responsible development and use of quantum-inspired enzyme catalysis models.
   c) Propose two future research directions to further advance this field.

Ensure your response demonstrates a deep understanding of quantum mechanics, biochemistry, and computational modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate word counts: Theoretical Framework, Computational Model Design, Optimization Strategy, Application, Validation and Experimental Design, and Ethical Considerations and Future Directions.",
            f"The design effectively incorporates the quantum effect of {t['quantum_effect']} in modeling enzyme catalysis for {t['enzyme_type']}.",
            f"The proposed model demonstrates a clear strategy for application in {t['application']} and uses the provided kinetic data.",
            "The response shows a deep understanding of quantum mechanics, biochemistry, and computational modeling.",
            "The proposed model and optimization strategy are innovative while maintaining scientific plausibility.",
            "The computational model design includes a 10-15 line pseudocode for a critical component.",
            "The validation and experimental design methods are well-thought-out and appropriate for the proposed model.",
            "The ethical considerations and future directions are relevant and demonstrate an understanding of broader implications.",
            "The response uses appropriate terminology and provides clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
