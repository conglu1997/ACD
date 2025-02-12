class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'problem': 'There are 7 people to be seated in a row for a photograph. How many different ways can they be arranged if two specific people must not sit next to each other?'
            },
            '2': {
                'problem': 'In a standard deck of 52 cards, what is the probability of drawing 2 cards of the same suit consecutively without replacement?'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            'Solve the following combinatorial or probability problem. Provide a detailed explanation of your solution, including all steps and reasoning used to arrive at the final answer. Ensure your response is clear, logical, and includes any necessary mathematical formulas or calculations. Structure your response in the following format:\n\n'
            '1. Problem Restatement: Restate the problem in your own words.\n'
            '2. Solution Steps: Break down the steps taken to solve the problem.\n'
            '3. Calculations: Show all necessary calculations and formulas used.\n'
            '4. Final Answer: Provide the final answer to the problem.\n\n'
            'Problem:\n' + t['problem']
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The solution must be logically coherent and correct.',
            'All steps and reasoning must be clearly explained.',
            'Any necessary mathematical formulas or calculations should be included and correctly applied.',
            'The final answer must be correct based on the problem statement.',
            'The response should be well-structured, following the specified format.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
