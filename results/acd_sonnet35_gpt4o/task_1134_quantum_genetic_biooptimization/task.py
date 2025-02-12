import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_system': 'Photosynthesis efficiency in plants',
                'quantum_principle': 'Superposition',
                'ethical_concern': 'Ecological impact'
            },
            {
                'biological_system': 'Protein folding in drug design',
                'quantum_principle': 'Entanglement',
                'ethical_concern': 'Access to healthcare'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired genetic algorithm to optimize {t['biological_system']}, incorporating the quantum principle of {t['quantum_principle']}. Your response should address the following points:

1. Algorithm Design (250-300 words):
   a) Describe the key components of your quantum-inspired genetic algorithm.
   b) Explain how you incorporate {t['quantum_principle']} into the algorithm.
   c) Detail how the algorithm interacts with and optimizes {t['biological_system']}.
   d) Discuss any novel approaches or techniques used in your design.

2. Quantum-Classical Integration (200-250 words):
   a) Explain how your algorithm bridges quantum and classical computing paradigms.
   b) Discuss the advantages of this hybrid approach for biological optimization.
   c) Address any challenges in implementing this integration and propose solutions.

3. Biological System Modeling (200-250 words):
   a) Describe how you model {t['biological_system']} for optimization.
   b) Explain the key parameters and variables in your model.
   c) Discuss how your model accounts for the complexity of biological systems.

4. Performance Analysis (150-200 words):
   a) Propose metrics to evaluate the performance of your algorithm.
   b) Compare the expected performance to classical genetic algorithms.
   c) Discuss any potential limitations or areas for improvement.

5. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of optimizing {t['biological_system']}.
   b) Discuss potential consequences related to {t['ethical_concern']}.
   c) Propose guidelines for responsible development and application of your algorithm.

6. Future Applications (150-200 words):
   a) Suggest two potential applications of your algorithm in other areas of biotechnology.
   b) Discuss how these applications might impact scientific research or medical treatments.
   c) Address any additional ethical considerations for these applications.

Ensure your response demonstrates a deep understanding of quantum computing, genetic algorithms, and biological systems. Use appropriate technical terminology and provide clear explanations. Be creative in your approach while maintaining scientific plausibility and addressing real-world challenges.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, genetic algorithms, and biological systems.",
            f"The algorithm design effectively incorporates {t['quantum_principle']} and addresses the optimization of {t['biological_system']}.",
            "The quantum-classical integration is well-explained and justified.",
            "The biological system modeling is comprehensive and accounts for system complexity.",
            "The performance analysis includes relevant metrics and a comparison to classical approaches.",
            f"Ethical considerations related to {t['ethical_concern']} are thoroughly discussed.",
            "Future applications are creative, relevant, and well-reasoned.",
            "The response is well-structured, clear, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
