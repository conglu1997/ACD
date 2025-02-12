import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_framework": "Time-centric language",
                "problem_domain": "Resource management"
            },
            {
                "linguistic_framework": "Non-gendered language",
                "problem_domain": "Social dynamics modeling"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system capable of switching between different linguistic frameworks, focusing on the implications of linguistic relativity (Sapir-Whorf hypothesis) for artificial intelligence. Your task is to create a detailed proposal for this AI system, addressing the following points:

1. System Architecture (200-250 words):
   - Describe the key components of your AI system that enable it to switch between linguistic frameworks.
   - Explain how the system incorporates the principles of the Sapir-Whorf hypothesis.
   - Discuss how the system represents and processes different linguistic structures.

2. Linguistic Framework Implementation (200-250 words):
   - Detail how your system would implement the '{t['linguistic_framework']}' framework.
   - Explain the key features and structures of this linguistic framework.
   - Discuss how this framework might influence the AI's perception and processing of information.

3. Problem-Solving Demonstration (250-300 words):
   - Describe how your AI system would approach a problem in the domain of '{t['problem_domain']}' using the '{t['linguistic_framework']}' framework.
   - Provide a step-by-step explanation of the problem-solving process.
   - Contrast this with how the system might approach the same problem using a different linguistic framework of your choice.

4. Cognitive Implications (200-250 words):
   - Analyze how switching between linguistic frameworks might affect the AI's reasoning and decision-making processes.
   - Discuss potential benefits and limitations of this approach compared to traditional AI systems.
   - Explore how this system might provide insights into human cognition and linguistic relativity.

5. Ethical Considerations (150-200 words):
   - Discuss potential ethical implications of an AI system that can adopt different linguistic frameworks.
   - Address concerns related to bias, fairness, and transparency in such a system.

6. Evaluation and Future Directions (200-250 words):
   - Propose methods to evaluate the effectiveness and impact of your AI system.
   - Suggest potential applications of this technology in various fields.
   - Discuss future research directions to enhance the system's capabilities.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Format your response using clear headings for each section.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system design clearly incorporates the '{t['linguistic_framework']}' framework and demonstrates its application in the '{t['problem_domain']}' domain.",
            "The response shows a deep understanding of linguistic relativity and its potential implications for AI.",
            "The problem-solving demonstration effectively contrasts the approach using different linguistic frameworks.",
            "The analysis of cognitive implications is insightful and well-reasoned.",
            "Ethical considerations are thoroughly addressed.",
            "The proposed evaluation methods and future directions are practical and demonstrate foresight."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
