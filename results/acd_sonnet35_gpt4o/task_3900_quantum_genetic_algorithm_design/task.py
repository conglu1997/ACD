import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'superposition',
                'genetic_process': 'CRISPR-Cas9 gene editing',
                'medical_application': 'cancer treatment optimization'
            },
            {
                'quantum_principle': 'entanglement',
                'genetic_process': 'epigenetic modification',
                'medical_application': 'neurodegenerative disease prevention'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired genetic algorithm for optimizing gene editing strategies, then analyze its potential applications in personalized medicine and ethical implications. Your algorithm should incorporate the quantum principle of {t['quantum_principle']}, focus on the genetic process of {t['genetic_process']}, and target the medical application of {t['medical_application']}.

        Your response should include the following sections:

        1. Quantum-Genetic Algorithm Design (300-350 words):
           a) Describe the key components of your quantum-inspired genetic algorithm.
           b) Explain how you incorporate {t['quantum_principle']} into the algorithm's design.
           c) Detail how your algorithm optimizes {t['genetic_process']} strategies.
           d) Discuss any novel features that distinguish your approach from classical genetic algorithms.

        2. Quantum-Biological Interface (250-300 words):
           a) Explain how your algorithm models the interaction between quantum processes and genetic information.
           b) Describe how {t['quantum_principle']} enhances the optimization of {t['genetic_process']}.
           c) Discuss potential challenges in implementing this quantum-biological interface and propose solutions.

        3. Optimization Process (200-250 words):
           a) Provide a step-by-step explanation of how your algorithm optimizes gene editing strategies.
           b) Describe the fitness function used to evaluate potential solutions.
           c) Explain how your algorithm handles constraints specific to {t['genetic_process']}.

        4. Medical Application Analysis (250-300 words):
           a) Analyze how your algorithm could be applied to {t['medical_application']}.
           b) Discuss potential benefits and limitations of using your approach in this medical context.
           c) Compare your quantum-inspired approach to current methods used in {t['medical_application']}.

        5. Ethical Implications (200-250 words):
           a) Discuss ethical considerations related to using quantum-inspired algorithms for gene editing optimization.
           b) Address potential concerns about privacy, consent, and equitable access to this technology.
           c) Propose guidelines for the responsible development and use of your algorithm in medical applications.

        6. Future Developments (150-200 words):
           a) Suggest two potential improvements or extensions to your quantum-inspired genetic algorithm.
           b) Discuss how these developments could impact the field of personalized medicine.
           c) Propose a novel research question that arises from the intersection of quantum computing and genetics.

        Ensure your response demonstrates a deep understanding of quantum computing principles, genetic processes, and bioethical considerations. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

        Format your response with clear headings for each section and use subheadings where appropriate. Adhere strictly to the word count guidelines provided for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, genetics, and bioethics, with a clear focus on {t['quantum_principle']}, {t['genetic_process']}, and {t['medical_application']}.",
            "The quantum-inspired genetic algorithm design is innovative, scientifically plausible, and thoroughly explained with clear components and processes.",
            f"The quantum-biological interface and optimization process are well-developed, grounded in current scientific understanding, and effectively incorporate {t['quantum_principle']} for {t['genetic_process']}.",
            f"The medical application analysis provides insightful discussion on the use of the algorithm for {t['medical_application']}, including benefits and limitations.",
            "Ethical implications are thoughtfully addressed, with consideration of privacy, consent, and equitable access concerns.",
            "The response adheres to the specified word count guidelines for each section and overall formatting requirements.",
            "The response demonstrates creativity and interdisciplinary knowledge integration while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
