import random
import re

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        base_systems = [
            {"name": "Fibonacci", "sequence": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]},
            {"name": "Prime", "sequence": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]},
            {"name": "Triangular", "sequence": [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]}
        ]
        operations = ["addition", "multiplication"]
        
        tasks = {}
        for i in range(1, 3):
            base_system = random.choice(base_systems)
            operation = random.choice(operations)
            tasks[str(i)] = {
                "base_system": base_system,
                "operation": operation
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_system = t['base_system']
        operation = t['operation']
        
        return f"""Create a novel number system based on the {base_system['name']} sequence: {base_system['sequence']}. Then, use this system to perform {operation} and solve logical problems. Follow these steps:

1. Number System Design (200-250 words):
   a) Describe how your number system represents digits using the given sequence.
   b) Explain the place value system in your number representation.
   c) Define how to represent zero and negative numbers (if applicable).
   d) Provide examples of how to write at least five different numbers in your system.

2. Arithmetic Operations (250-300 words):
   a) Define how to perform {operation} in your number system.
   b) Provide step-by-step examples of at least three {operation} operations.
   c) Explain any unique properties or challenges of {operation} in your system.
   d) Describe how to check if the result of an operation is correct.

3. Problem Solving (200-250 words):
   a) Create a word problem that can be solved using your number system and the {operation} operation.
   b) Provide a step-by-step solution to your problem, showing all work in your number system.
   c) Explain how the problem showcases the unique aspects of your number system.

4. System Analysis (200-250 words):
   a) Discuss the advantages and limitations of your number system compared to the decimal system.
   b) Analyze how your system might affect mathematical or logical thinking if it were widely adopted.
   c) Propose a real-world application where your number system might be particularly useful.

5. Extension and Reflection (150-200 words):
   a) Suggest how your system could be extended to include other arithmetic operations.
   b) Reflect on how creating and using this system has influenced your understanding of number systems and mathematical logic.
   c) Propose a research question or experiment to further explore the implications of your number system.

Ensure your response demonstrates a deep understanding of number systems, mathematical logic, and creative problem-solving. Use clear headings for each section and number your paragraphs within each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a fully-defined number system based on the given sequence",
            f"The {t['operation']} operation is clearly defined and demonstrated with examples",
            "A word problem is created and solved using the invented number system",
            "The analysis of the system's advantages, limitations, and potential applications is insightful",
            "The response demonstrates creativity, logical consistency, and deep understanding of number systems and mathematical logic"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
