import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        optimization_problems = [
            {
                "name": "Protein Folding Optimization",
                "description": "Optimize the folding process of a synthetic protein to achieve a desired 3D structure"
            },
            {
                "name": "Metabolic Pathway Engineering",
                "description": "Optimize a synthetic metabolic pathway to maximize the production of a specific biochemical"
            },
            {
                "name": "Gene Regulatory Network Design",
                "description": "Design an optimal gene regulatory network for a synthetic organism with specific behavioral characteristics"
            },
            {
                "name": "Synthetic Genome Optimization",
                "description": "Optimize the design of a synthetic genome to minimize resource usage while maintaining functionality"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(optimization_problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired evolutionary algorithm to solve the following optimization problem in synthetic biology: {t['name']} - {t['description']}

Your response should include the following sections:

1. Problem Formulation (150-200 words):
   a) Clearly define the optimization problem and its constraints.
   b) Explain why this problem is challenging and suitable for a quantum-inspired approach.
   c) Identify the key variables and parameters that need to be optimized.

2. Quantum-Inspired Evolutionary Algorithm Design (250-300 words):
   a) Describe the overall structure of your algorithm, including how it incorporates both quantum and evolutionary principles.
   b) Explain how you represent solutions (e.g., quantum bits, superposition states).
   c) Detail the quantum operators used (e.g., quantum gates, measurements) and their roles in the algorithm.
   d) Describe the evolutionary operators (e.g., selection, crossover, mutation) and how they interact with the quantum components.
   e) Explain how your algorithm maintains a balance between exploration and exploitation.
   
   Note: Your algorithm description should be detailed enough to allow for a theoretical implementation. Include pseudo-code or a step-by-step process where appropriate.

3. Implementation Strategy (200-250 words):
   a) Outline the steps to implement your algorithm, including any necessary preprocessing of biological data.
   b) Describe how you would evaluate the fitness of solutions in the context of the biological problem.
   c) Discuss any potential challenges in implementing this algorithm and propose solutions.

4. Performance Analysis (150-200 words):
   a) Predict the expected performance of your algorithm compared to classical evolutionary algorithms.
   b) Identify potential quantum advantages (e.g., speedup, quality of solutions) for this specific problem.
   c) Discuss any limitations or trade-offs of your approach.

5. Biological Implications (150-200 words):
   a) Explain how solving this optimization problem could advance the field of synthetic biology.
   b) Discuss potential applications or impacts of your optimized solution in real-world biological systems.
   c) Address any ethical considerations related to optimizing biological systems.

6. Future Directions (100-150 words):
   a) Propose two potential improvements or extensions to your algorithm.
   b) Suggest another synthetic biology problem that could benefit from a similar quantum-inspired evolutionary approach.

Ensure your response demonstrates a deep understanding of quantum computing concepts, evolutionary algorithms, and synthetic biology. Be creative in your algorithm design while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1000-1300 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for a quantum-inspired evolutionary algorithm to solve the {t['name']} problem",
            "The problem formulation is clear and well-defined, with appropriate constraints and variables identified",
            "The algorithm design incorporates both quantum and evolutionary principles in a logical and creative manner",
            "The implementation strategy is detailed and addresses the specific challenges of the biological problem",
            "The performance analysis includes a thoughtful comparison to classical algorithms and identifies quantum advantages",
            "The biological implications and potential applications are well-reasoned and demonstrate understanding of synthetic biology",
            "The proposed future directions are innovative and relevant to the field",
            "The overall response demonstrates a deep understanding of quantum computing, evolutionary algorithms, and synthetic biology",
            "The response is well-structured, using clear headings for each section, and adheres to the 1000-1300 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
