class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'data': 'Name, Age, Department, Salary\nAlice, 30, HR, 70000\nBob, 25, Engineering, 80000\nCharlie, 35, Marketing, 60000\nDiana, 28, Engineering, 85000\nEve, 40, Engineering, 90000',
                'instructions': 'Calculate the average salary of employees in the Engineering department.'
            },
            '2': {
                'data': 'Product, Category, Price, Quantity\nLaptop, Electronics, 1000, 50\nPhone, Electronics, 500, 200\nDesk, Furniture, 150, 100\nChair, Furniture, 85, 300\nTable, Furniture, 200, 150',
                'instructions': 'Determine the total revenue generated from the Furniture category.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following tabular data and perform the specified operation:

Data:
{t['data']}

Instructions: {t['instructions']}

Submit your response as a plain text string with the result of the operation in numerical format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The response should correctly perform the specified operation.',
            'The result should be a single numerical value.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
