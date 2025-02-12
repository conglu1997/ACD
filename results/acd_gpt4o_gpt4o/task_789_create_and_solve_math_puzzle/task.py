class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "algebra", "difficulty": "medium"},
            "2": {"topic": "geometry", "difficulty": "hard"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        difficulty = t["difficulty"]
        instructions = f"""Your task is to create an original mathematical puzzle in the topic of {topic} with {difficulty} difficulty level. The puzzle should be non-trivial and challenging, yet solvable within the given topic and difficulty. In addition to creating the puzzle, you must also provide a clear and detailed solution. Ensure that your solution is correct and explains the steps taken to arrive at the answer.

Guidelines:
- The puzzle should be unique and not a common or well-known problem.
- The difficulty should correspond to the level specified (medium or hard).
- The solution should include all necessary steps and justifications.
- Avoid overly simple problems and ensure the puzzle requires thoughtful problem-solving.

Please provide your response in the following format:

Puzzle:
[Your puzzle here]

Solution:
[Your solution here]

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle should be original, challenging, and within the specified topic and difficulty.",
            "The solution should be correct and clearly explain the steps taken to solve the puzzle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
