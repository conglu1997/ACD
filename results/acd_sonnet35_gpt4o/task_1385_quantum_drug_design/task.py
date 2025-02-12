import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        target_proteins = [
            "EGFR (Epidermal Growth Factor Receptor)",
            "HIV-1 Protease",
            "Beta-lactamase",
            "Acetylcholinesterase"
        ]
        quantum_properties = [
            "electron density",
            "molecular orbitals",
            "vibrational modes",
            "excited states"
        ]
        functional_groups = [
            "carboxyl group",
            "amino group",
            "hydroxyl group",
            "phosphate group"
        ]
        
        tasks = {}
        for i in range(2):
            target = random.choice(target_proteins)
            property = random.choice(quantum_properties)
            group = random.choice(functional_groups)
            tasks[str(i+1)] = {
                "target": target,
                "property": property,
                "functional_group": group
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel drug molecule targeting {t['target']} using quantum chemistry principles, with a focus on the quantum property of {t['property']}. Then, analyze its potential efficacy and propose a quantum computing algorithm for simulating its interactions. Your molecule must incorporate a {t['functional_group']}. Your response should include:

1. Molecule Design (250-300 words):
   a) Describe the structure and key features of your proposed drug molecule, including the incorporation of the {t['functional_group']}.
   b) Explain how quantum chemistry principles informed your design, particularly in relation to {t['property']}.
   c) Discuss how your molecule is expected to interact with {t['target']}.
   d) Include a text-based representation of your molecule's structure (e.g., SMILES notation or ASCII art).
   e) Justify your design choices based on current understanding of drug-target interactions.
   f) Propose a potential real-world application of your designed molecule beyond its primary target.

2. Quantum Property Analysis (200-250 words):
   a) Analyze how the {t['property']} of your molecule contributes to its potential efficacy.
   b) Describe any quantum effects that may play a role in the molecule's behavior.
   c) Explain how understanding this quantum property could lead to improved drug design.

3. Efficacy Prediction (200-250 words):
   a) Predict the potential efficacy of your drug molecule based on its quantum properties.
   b) Discuss any possible side effects or limitations of your design.
   c) Compare your approach to traditional drug design methods, highlighting the advantages of using quantum chemistry principles.

4. Quantum Algorithm Proposal (250-300 words):
   a) Propose a specific type of quantum computing algorithm (e.g., variational quantum algorithm, quantum phase estimation) to simulate the interaction between your drug molecule and {t['target']}.
   b) Explain how your algorithm leverages quantum principles to improve upon classical simulation methods.
   c) Compare your quantum algorithm with a specific classical algorithm (e.g., molecular dynamics, Monte Carlo) for molecular simulation.
   d) Discuss the potential computational advantages of your quantum algorithm.
   e) Provide a high-level pseudocode or flow diagram of your proposed algorithm.

5. Experimental Design (150-200 words):
   a) Propose an experiment to validate your quantum drug design approach.
   b) Describe how you would measure the impact of {t['property']} on the drug's efficacy.
   c) Discuss any ethical considerations in testing your novel drug molecule.

6. Reflection and Limitations (100-150 words):
   a) Critically evaluate the strengths and weaknesses of your approach.
   b) Discuss potential areas for improvement in your design and methodology.
   c) Reflect on the broader implications of using quantum-inspired approaches in drug discovery.

Ensure your response demonstrates a deep understanding of quantum chemistry, drug design principles, and quantum computing. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section, adhering to the specified word limits. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed drug molecule targeting {t['target']} with a clear focus on the quantum property of {t['property']} and incorporation of a {t['functional_group']}",
            "The molecule design is justified based on quantum chemistry principles and current understanding of drug-target interactions, with a proposed real-world application beyond its primary target",
            "The quantum property analysis demonstrates a deep understanding of quantum chemistry and its relevance to drug efficacy",
            "The efficacy prediction is scientifically plausible, well-reasoned, and compares the approach to traditional methods",
            "The proposed quantum algorithm for simulating molecular interactions is specific, innovative, and clearly explained with pseudocode or a flow diagram, including a comparison to a classical algorithm",
            "The experimental design is well-thought-out, addresses the measurement of quantum properties, and considers ethical implications",
            "The reflection section critically evaluates the approach and discusses limitations and broader implications",
            "The overall response shows creativity, interdisciplinary knowledge application, and strong scientific reasoning within the specified word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
