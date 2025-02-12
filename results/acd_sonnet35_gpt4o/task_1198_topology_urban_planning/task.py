import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'topological_concept': 'homotopy',
                'urban_challenge': 'traffic flow optimization'
            },
            {
                'topological_concept': 'manifold',
                'urban_challenge': 'public transportation network design'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply the topological concept of {t['topological_concept']} to address the urban planning challenge of {t['urban_challenge']}. Your response should include:

1. Concept Explanation (100-150 words):
   Explain the topological concept of {t['topological_concept']} in simple terms, including its key properties and how it's typically used in mathematics.

2. Urban Challenge Analysis (100-150 words):
   Analyze the urban planning challenge of {t['urban_challenge']}, discussing its key aspects and why it's a significant issue in modern cities.

3. Topological Application (200-250 words):
   Describe how the topological concept can be applied to address the urban planning challenge. Be specific about how properties of the topological concept map onto aspects of the urban problem.

4. Solution Proposal (200-250 words):
   Propose a detailed solution to the urban planning challenge using your topological approach. Include a step-by-step explanation of how your solution would be implemented.

5. Advantages and Limitations (150-200 words):
   Discuss the potential advantages of your topological approach compared to traditional urban planning methods. Also, address any limitations or potential issues with your proposed solution.

6. Visualization (Describe in 100-150 words):
   Describe a visual representation or diagram that would illustrate your topological solution to the urban planning challenge. Explain what elements would be included and how it would help stakeholders understand your approach.

Ensure your response demonstrates a deep understanding of both the mathematical concept and the urban planning challenge. Use appropriate terminology from both fields and provide clear explanations for complex ideas. Be creative in your approach while maintaining scientific and practical plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the topological concept is accurate and clear.",
            "The urban planning challenge is well-analyzed and its significance is explained.",
            "The application of the topological concept to the urban challenge is creative and logical.",
            "The proposed solution is detailed, feasible, and demonstrates a clear understanding of both topology and urban planning.",
            "The advantages and limitations of the approach are thoughtfully discussed.",
            "The described visualization effectively illustrates the topological solution to the urban planning challenge.",
            "The overall response demonstrates a high level of interdisciplinary thinking and problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
