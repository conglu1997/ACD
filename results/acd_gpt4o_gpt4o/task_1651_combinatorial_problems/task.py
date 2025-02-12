class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "How many distinct ways can you arrange the letters of the word 'COMBINATORICS' if no letter can be repeated?", "additional_criteria": ["Provide a step-by-step explanation of your solution, including any intermediate steps and calculations.", "The response should include the final numerical answer."]},
            "2": {"problem": "In a group of 10 people, how many ways can you select a committee of 4 people ensuring that a specific pair of people is always included in the committee?", "additional_criteria": ["Provide a detailed explanation of your solution, including any formulas and intermediate steps used.", "The response should include the final numerical answer."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following combinatorial problem:

{t['problem']}

Ensure your solution meets the following criteria:
{', '.join(t['additional_criteria'])}

Provide a detailed explanation of your solution, including any relevant formulas, intermediate steps, and step-by-step calculations. Include the final numerical answer in your response.

Response format:
1. Solution: [Your detailed solution here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('additional_criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
