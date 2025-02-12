import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {
                'system': 'Protein folding',
                'quantum_concept': 'Superposition',
                'information_metric': 'Entropy'
            },
            {
                'system': 'Gene regulatory networks',
                'quantum_concept': 'Entanglement',
                'information_metric': 'Mutual Information'
            }
        ]
        
        return {str(i+1): system for i, system in enumerate(random.sample(biological_systems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired evolutionary algorithm to optimize the biological system of {t['system']}, incorporating the quantum concept of {t['quantum_concept']} and the information theory metric of {t['information_metric']}. Your response should include the following sections:

1. Algorithm Design (300-350 words):
   a) Describe the key components of your quantum-inspired evolutionary algorithm.
   b) Explain how you incorporate {t['quantum_concept']} into the algorithm's design.
   c) Detail how your algorithm models and optimizes the {t['system']} system.
   d) Explain how {t['information_metric']} is used in the optimization process.

2. Quantum-Biological Interface (250-300 words):
   a) Analyze how quantum principles can be meaningfully applied to the biological problem of {t['system']}.
   b) Discuss any challenges in bridging quantum computing concepts with biological systems.
   c) Propose a novel approach to represent biological information in a quantum-inspired framework.

3. Optimization Process (250-300 words):
   a) Describe the step-by-step process of how your algorithm would optimize the {t['system']} system.
   b) Explain how evolutionary principles are integrated with quantum-inspired operations.
   c) Discuss how your algorithm handles constraints specific to the biological system.

4. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate the performance of your quantum-inspired algorithm.
   b) Compare your approach to traditional evolutionary algorithms and quantum algorithms.
   c) Discuss potential advantages and limitations of your method.

5. Practical Implementation (200-250 words):
   a) Describe how your algorithm could be implemented using current or near-future technologies.
   b) Discuss any technological barriers and propose potential solutions.
   c) Suggest a specific application or experiment to test your algorithm's effectiveness.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical considerations in optimizing biological systems using quantum-inspired methods.
   b) Analyze possible societal impacts of successfully implementing your algorithm.
   c) Propose guidelines for responsible development and use of such technologies.

Ensure your response demonstrates a deep understanding of quantum computing principles, evolutionary biology, and information theory. Use appropriate technical terminology and provide clear explanations of complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Algorithm Design', '2. Quantum-Biological Interface', etc.). Your total response should be between 1350-1650 words. Provide a word count at the end of each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithm design clearly incorporates {t['quantum_concept']} and uses {t['information_metric']} in the optimization process for {t['system']}.",
            "The response demonstrates a deep understanding of quantum principles, evolutionary biology, and information theory.",
            "The optimization process is well-explained, integrating evolutionary principles with quantum-inspired operations.",
            "The performance analysis includes specific metrics and a thorough comparison with traditional methods.",
            "The response addresses practical implementation challenges and proposes feasible solutions.",
            "Ethical and societal implications are thoughtfully considered, with specific guidelines proposed.",
            "The response is well-structured with clear headings and adheres to the specified word count ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
