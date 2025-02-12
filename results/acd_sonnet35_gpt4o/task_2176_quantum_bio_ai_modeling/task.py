import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = ['Protein folding', 'Gene regulation', 'Metabolic pathways']
        quantum_concepts = ['Superposition', 'Entanglement', 'Quantum annealing']
        return {
            "1": {"biological_system": random.choice(biological_systems),
                   "quantum_concept": random.choice(quantum_concepts)},
            "2": {"biological_system": random.choice(biological_systems),
                   "quantum_concept": random.choice(quantum_concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        biological_system_explanations = {
            'Protein folding': 'the process by which a protein structure assumes its functional shape',
            'Gene regulation': 'the process of controlling the rate and manner of gene expression',
            'Metabolic pathways': 'series of chemical reactions occurring within a cell'
        }
        quantum_concept_explanations = {
            'Superposition': 'the ability of a quantum system to be in multiple states at once',
            'Entanglement': 'a quantum phenomenon where particles become interconnected and share properties',
            'Quantum annealing': 'a quantum-mechanical method for finding the global minimum of a given objective function'
        }
        return f"""Design a quantum-inspired AI system for modeling the complex biological system of {t['biological_system']} ({biological_system_explanations[t['biological_system']]}), with a particular focus on incorporating the quantum concept of {t['quantum_concept']} ({quantum_concept_explanations[t['quantum_concept']]}). Then, analyze its potential impact on drug discovery and personalized medicine. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired AI system.
   b) Explain how it integrates classical AI techniques with quantum computing concepts.
   c) Detail how the system specifically addresses {t['biological_system']} modeling.
   d) Explain how {t['quantum_concept']} is incorporated into the system design.
   e) Provide a simple diagram or schematic representation of your system architecture (describe it textually).

2. Quantum-Biological Interface (200-250 words):
   a) Describe how your system translates biological data into a format suitable for quantum processing.
   b) Explain how quantum computations are mapped back to biologically meaningful results.
   c) Discuss any novel algorithms or approaches used in this interface.

3. Performance Analysis (200-250 words):
   a) Compare the theoretical performance of your system to classical approaches for {t['biological_system']} modeling.
   b) Discuss potential advantages and limitations of your quantum-inspired approach.
   c) Propose benchmarks or experiments to validate your system's performance.

4. Drug Discovery Applications (150-200 words):
   a) Explain how your system could be applied to accelerate drug discovery processes.
   b) Provide a specific example of how it might improve current methods.
   c) Discuss any challenges in integrating your system into existing pharmaceutical research pipelines.

5. Personalized Medicine Implications (150-200 words):
   a) Analyze how your system could contribute to advancing personalized medicine.
   b) Discuss potential ethical considerations in applying quantum-inspired AI to individual patient data.
   c) Propose guidelines for responsible development and use of such systems in healthcare.

6. Future Developments (100-150 words):
   a) Suggest potential improvements or extensions to your system.
   b) Speculate on how advances in quantum computing might further enhance biological modeling and AI in the next decade.

Ensure your response demonstrates a deep understanding of quantum computing principles, biological systems, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, biological systems, and artificial intelligence.",
            "The proposed system creatively and plausibly integrates quantum concepts with AI for biological modeling.",
            f"The system design specifically addresses {t['biological_system']} and incorporates {t['quantum_concept']}.",
            "The answer covers all required sections with appropriate detail and word count.",
            "The response shows clear interdisciplinary thinking and novel approaches to complex scientific challenges.",
            "The proposed system strikes a balance between creativity and scientific plausibility.",
            "The response includes a clear and relevant diagram or schematic representation of the system architecture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
