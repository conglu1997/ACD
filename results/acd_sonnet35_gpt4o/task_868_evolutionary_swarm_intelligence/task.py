import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        evolutionary_mechanisms = [
            {
                'mechanism': 'Natural Selection',
                'description': 'The process by which individuals with advantageous traits are more likely to survive and reproduce'
            },
            {
                'mechanism': 'Genetic Drift',
                'description': 'Random changes in the frequency of traits in a population due to chance events'
            }
        ]
        optimization_problems = [
            {
                'problem': 'Resource Allocation',
                'description': 'Optimizing the distribution of limited resources across various tasks or entities'
            },
            {
                'problem': 'Network Routing',
                'description': 'Finding the most efficient paths for data transmission in complex networks'
            }
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'evolutionary_mechanism': random.choice(evolutionary_mechanisms),
                'optimization_problem': random.choice(optimization_problems)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired swarm intelligence system that models the evolutionary mechanism of {t['evolutionary_mechanism']['mechanism']} to solve the optimization problem of {t['optimization_problem']['problem']}. Your task has the following parts:

1. System Design (250-300 words):
   a) Describe the key components and structure of your swarm intelligence system.
   b) Explain how your system incorporates {t['evolutionary_mechanism']['mechanism']} ({t['evolutionary_mechanism']['description']}).
   c) Detail how your system approaches {t['optimization_problem']['problem']} ({t['optimization_problem']['description']}).
   d) Provide a high-level pseudocode or flowchart of your system's main algorithm.

2. Biological Inspiration (200-250 words):
   a) Discuss the biological systems or phenomena that inspired your design.
   b) Explain how your system mimics or diverges from these natural processes.
   c) Analyze potential advantages of your bio-inspired approach over traditional optimization methods.

3. Mathematical Formulation (200-250 words):
   a) Present a mathematical representation of a key aspect of your system.
   b) Explain the variables, functions, or equations in your formulation.
   c) Describe how this mathematical model captures the integration of swarm behavior and evolutionary processes.

4. Simulation and Analysis (250-300 words):
   a) Propose a detailed simulation scenario to test your system's performance.
   b) Describe the metrics you would use to evaluate your system's effectiveness.
   c) Predict potential emergent behaviors or unexpected outcomes in your simulation.
   d) Discuss how you would validate your system's results against real-world data or alternative models.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical concerns or unintended consequences of implementing your system.
   b) Discuss the broader societal implications of using bio-inspired AI for complex problem-solving.
   c) Propose guidelines for the responsible development and application of such systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your system for solving different types of problems.
   b) Propose a specific research question or hypothesis that emerges from your design.
   c) Discuss how insights from your system might contribute to our understanding of biological evolution or complex systems.

Ensure your response demonstrates a deep understanding of evolutionary biology, complex systems theory, and computational modeling. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Your total response should be between 1200-1500 words.

Format your response with clear headings for each section, as follows:

1. System Design:
   [Your content here]

2. Biological Inspiration:
   [Your content here]

3. Mathematical Formulation:
   [Your content here]

4. Simulation and Analysis:
   [Your content here]

5. Ethical Considerations and Societal Impact:
   [Your content here]

6. Future Research Directions:
   [Your content here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The System Design effectively incorporates {t['evolutionary_mechanism']['mechanism']} to address {t['optimization_problem']['problem']}.",
            "The Biological Inspiration section demonstrates a deep understanding of relevant natural systems and processes.",
            "The Mathematical Formulation is clear, relevant, and accurately represents key aspects of the system.",
            "The Simulation and Analysis proposal is well-constructed and includes appropriate evaluation metrics.",
            "Ethical Considerations and Societal Impact are thoughtfully addressed with relevant guidelines proposed.",
            "Future Research Directions are innovative and well-justified based on the proposed system.",
            "The response demonstrates a deep understanding of evolutionary biology, complex systems theory, and computational modeling.",
            "The ideas presented are creative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
