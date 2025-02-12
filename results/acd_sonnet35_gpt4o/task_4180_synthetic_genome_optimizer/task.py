import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "organism": "bacterial_bioremediation",
                "target_function": "degradation_of_plastic_polymers",
                "constraint": "minimal_genome_size"
            },
            {
                "organism": "photosynthetic_algae",
                "target_function": "enhanced_carbon_fixation",
                "constraint": "stability_in_high_temperatures"
            },
            {
                "organism": "engineered_yeast",
                "target_function": "production_of_complex_pharmaceuticals",
                "constraint": "minimal_metabolic_burden"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and optimize a synthetic genome for a {t['organism']} with the target function of {t['target_function']}, while adhering to the constraint of {t['constraint']}. Your task involves applying principles of genetic engineering, information theory, and evolutionary algorithms to create an efficient and effective artificial genetic system.

Key terms:
- Synthetic genome: An artificially constructed set of genetic instructions
- Information theory: A mathematical framework for analyzing and optimizing information content
- Evolutionary algorithm: A computational method inspired by biological evolution to solve optimization problems

Provide your response in the following sections:

1. Genome Design Strategy (300-350 words):
   a) Outline your approach to designing the synthetic genome for the specified organism and function.
   b) Explain how you incorporate information theory principles in your genome design.
   c) Describe any novel genetic elements or regulatory systems you would include.
   d) Discuss how your design addresses the given constraint.

2. Evolutionary Algorithm for Optimization (300-350 words):
   a) Develop an evolutionary algorithm to optimize your synthetic genome.
   b) Define the fitness function that evaluates genome performance, providing a mathematical formulation.
   c) Explain your selection, crossover, and mutation operators, including their probabilities or rates.
   d) Describe how your algorithm balances exploration and exploitation.
   e) Provide pseudocode for your algorithm.

3. Simulation and Analysis (250-300 words):
   a) Propose a computational simulation to test your synthetic genome and optimization algorithm.
   b) Describe the key parameters and metrics you would measure.
   c) Present a hypothetical set of results from your simulation in a tabular or graphical format.
   d) Analyze these results, discussing the efficiency and effectiveness of your design.

4. Biological Implementation and Challenges (200-250 words):
   a) Outline a strategy for implementing your optimized genome in a living organism.
   b) Discuss potential challenges in moving from in silico design to in vivo implementation.
   c) Propose solutions to these challenges.

5. Ethical and Biosafety Considerations (150-200 words):
   a) Discuss the ethical implications of creating synthetic organisms for the specified function.
   b) Outline biosafety measures to prevent unintended environmental or health consequences.
   c) Propose guidelines for responsible development and use of synthetic genome technologies.

6. Future Directions and Applications (150-200 words):
   a) Suggest two potential improvements or extensions to your synthetic genome system.
   b) Discuss how your approach could be adapted for other organisms or functions.
   c) Propose a related challenge in synthetic biology that could be addressed using a similar methodology.

Ensure your response demonstrates a deep understanding of molecular biology, genetic engineering, information theory, and evolutionary computation. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must focus on designing a synthetic genome for {t['organism']} with the function of {t['target_function']} and the constraint of {t['constraint']}",
            "The genome design strategy should incorporate principles of information theory and address the given constraint",
            "An evolutionary algorithm for genome optimization should be clearly described with appropriate operators, fitness function, and pseudocode",
            "The simulation and analysis section should include a hypothetical set of results presented in a tabular or graphical format, with a thorough interpretation",
            "Biological implementation challenges and potential solutions should be discussed in detail",
            "Ethical and biosafety considerations must be thoughtfully addressed with specific guidelines proposed",
            "The response should be well-organized, scientifically plausible, and demonstrate interdisciplinary knowledge",
            "The total response should be between 1350-1650 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
