class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Three friends, Alice, Bob, and Charlie, are sitting in a row, each wearing a hat that is either red or blue. Alice can see Bob and Charlie's hats, Bob can see Charlie's hat, but Charlie cannot see anyone's hat. They are all asked to guess the color of their own hat. Alice says, 'I don't know.' Bob then says, 'I don't know.' Finally, Charlie says, 'I know.' What color is Charlie's hat?",
                "task_type": "solve"
            },
            "2": {
                "puzzle_prompt": "Generate a logic puzzle involving three characters with a similar structure to the first task. Ensure that the puzzle has a clear solution and requires logical reasoning to solve it.",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "solve":
            return f"""Solve the following logic puzzle. Provide a detailed explanation of your reasoning and the final solution.

Puzzle:
{t['puzzle']}

Submit your solution as a plain text string in the following format:
'Solution: [Your solution]'
Explanation: [Your explanation]"""
        elif t["task_type"] == "generate":
            return f"""Generate a new logic puzzle involving three characters. Ensure that the puzzle has a clear solution and requires logical reasoning to solve it. Provide the puzzle statement and the solution with an explanation.

Prompt:
{t['puzzle_prompt']}

Submit your response as a plain text string in the following format:
'Puzzle: [Your puzzle]'
Solution: [Your solution]'
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "solve":
            validation_criteria = ["The solution must identify the correct hat color.", "The explanation must demonstrate logical reasoning consistent with the puzzle's information."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated puzzle must have a clear and logical solution.", "The explanation must demonstrate how the solution is derived from the puzzle's information."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
