import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "insect_species": "Honeybees",
                "optimization_problem": "Resource allocation in smart cities",
                "constraint": "Energy efficiency",
                "scale": "Metropolitan area"
            },
            "2": {
                "insect_species": "Leafcutter ants",
                "optimization_problem": "Supply chain optimization",
                "constraint": "Sustainability",
                "scale": "Global network"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic artificial intelligence system inspired by the collective behavior of {t['insect_species']} to solve the complex optimization problem of {t['optimization_problem']} at the scale of a {t['scale']}, with a focus on the constraint of {t['constraint']}. Your response should include:

1. Biological Inspiration (200-250 words):
   a) Describe the key collective behaviors and decision-making processes of the specified insect species.
   b) Explain how these behaviors contribute to the species' problem-solving abilities in nature.
   c) Discuss any specific adaptations or strategies that make this species particularly suited for the given optimization problem.

2. AI System Architecture (250-300 words):
   a) Propose a detailed architecture for your biomimetic AI system, including its main components and their interactions.
   b) Explain how your system mimics or adapts the biological processes of the insect species.
   c) Describe the data structures and algorithms used in your system, highlighting any novel approaches.
   d) Discuss how your system addresses the specified constraint and scale.

3. Problem-Solving Approach (200-250 words):
   a) Explain how your AI system would approach the given optimization problem.
   b) Provide a step-by-step breakdown of the problem-solving process.
   c) Discuss how your system handles trade-offs and conflicting objectives.

4. Scaling and Adaptation (150-200 words):
   a) Analyze how your system would scale to handle larger or more complex versions of the problem.
   b) Describe how the system could adapt to changing conditions or requirements.
   c) Discuss any potential limitations of your approach and how they might be addressed.

5. Performance Evaluation (150-200 words):
   a) Propose metrics and methods to evaluate the performance of your biomimetic AI system.
   b) Compare your system's expected performance to traditional optimization algorithms.
   c) Suggest an experiment to test your system's effectiveness in a real-world scenario.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns or societal impacts of implementing your system.
   b) Analyze how your biomimetic approach might influence public perception of AI.
   c) Propose guidelines for responsible development and deployment of such systems.

7. Future Research Directions (100-150 words):
   a) Suggest two novel research directions that could emerge from your biomimetic AI approach.
   b) Briefly describe potential applications in other domains or industries.

Ensure your response demonstrates a deep understanding of both the biological principles and the AI/computational aspects involved. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Important: Address all parts of the task thoroughly, ensuring that your response is specific to the given insect species, optimization problem, constraint, and scale.

Format your response with clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['insect_species']}' collective behavior and its relevance to {t['optimization_problem']} at the scale of a {t['scale']}.",
            f"The AI system architecture is well-designed, innovative, and clearly mimics or adapts the biological processes of {t['insect_species']}.",
            f"The problem-solving approach is well-explained and addresses the constraint of {t['constraint']} effectively.",
            "The analysis of scaling, adaptation, and performance evaluation is thorough and scientifically sound.",
            "The discussion of ethical and societal implications is insightful and comprehensive.",
            "The proposed future research directions are novel and promising.",
            "The overall response shows a high level of interdisciplinary knowledge integration and creative problem-solving.",
            "All parts of the task are addressed thoroughly and specifically."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
