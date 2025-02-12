import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Quantum tunneling",
            "Quantum entanglement",
            "Quantum superposition",
            "Quantum coherence"
        ]
        protein_properties = [
            "Hydrophobic interactions",
            "Hydrogen bonding",
            "Electrostatic interactions",
            "Van der Waals forces"
        ]
        tasks = [
            {
                "quantum_concept": qc,
                "protein_property": pp
            }
            for qc in quantum_concepts
            for pp in protein_properties
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational model for simulating protein folding, incorporating the quantum mechanical concept of {t['quantum_concept']} and focusing on the protein folding property of {t['protein_property']}. Your task has the following components:

1. Conceptual Framework (250-300 words):
   a) Explain how you would integrate {t['quantum_concept']} with {t['protein_property']} in a protein folding simulation model.
   b) Describe the key components and structure of your model.
   c) Explain how this integration might enhance our understanding of protein folding processes.

2. Mathematical Formulation (200-250 words):
   a) Present a mathematical representation of a key aspect of your model.
   b) Explain the variables, operators, or functions in your formulation.
   c) Describe how this mathematical representation captures the integration of quantum and biological principles.

3. Simulation Algorithm (200-250 words):
   a) Outline the steps of your quantum-inspired algorithm for simulating protein folding.
   b) Explain how your algorithm incorporates both the quantum concept and the protein property.
   c) Discuss any novel features or advantages of your approach compared to classical protein folding simulations.

4. Potential Applications (150-200 words):
   a) Describe how your model could be applied to real-world problems in molecular biology or drug discovery.
   b) Propose an experiment to test the effectiveness of your model in predicting protein structures.
   c) Discuss potential implications for our understanding of protein misfolding diseases.

5. Technical Challenges and Solutions (150-200 words):
   a) Identify potential technical challenges in implementing your model.
   b) Propose solutions or workarounds for these challenges.
   c) Discuss any computational resources or novel technologies required for your simulation.

6. Future Directions (100-150 words):
   a) Suggest areas for future research or refinement of your model.
   b) Propose how your approach could be extended to other aspects of molecular biology.
   c) Speculate on potential long-term impacts of quantum-inspired biological simulations.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and computational modeling. Be creative and innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and molecular biology",
            "The proposed model creatively integrates the specified quantum concept with the given protein folding property",
            "The mathematical formulation and simulation algorithm are well-explained and scientifically plausible",
            "The potential applications and future directions are innovative and relevant",
            "The response addresses technical challenges and proposes reasonable solutions"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
