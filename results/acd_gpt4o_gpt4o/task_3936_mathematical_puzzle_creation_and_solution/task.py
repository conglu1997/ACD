class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "number theory", "example": "Create a puzzle involving prime numbers. For instance, 'Find two prime numbers that add up to 50.'"},
            "2": {"topic": "geometry", "example": "Create a puzzle involving the properties of triangles. For instance, 'Given an isosceles triangle with sides 5, 5, and x, find the possible values of x.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        example = t["example"]
        instructions = f"""Your task is to create an original mathematical puzzle based on the following topic:

Topic: {topic}

For example, you could: {example}

In your puzzle creation, you should:
1. Clearly state the puzzle in a single sentence.
2. Ensure the puzzle is challenging but solvable by someone with a good understanding of {topic}.
3. Provide all necessary details and constraints for solving the puzzle.

Additionally, provide a detailed solution to your puzzle. The solution should include:
1. A step-by-step explanation of how to solve the puzzle.
2. The final answer or result.
3. Justification for each step to show logical progression.

Your response should be detailed, logically structured, and demonstrate a clear understanding of the mathematical concepts involved. Format your response as follows:

Puzzle Creation:
1. Puzzle Statement
2. Details and Constraints

Puzzle Solution:
1. Step-by-Step Solution
2. Final Answer
3. Justification for Each Step
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle should be original and based on the given topic.",
            "The puzzle should be challenging but solvable.",
            "All necessary details and constraints should be provided.",
            "The solution should include a clear step-by-step explanation.",
            "The final answer should be correct and logically derived.",
            "Each step of the solution should be justified."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
