class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Name,Age,Salary\nAlice,30,70000\nBob,25,65000\nCharlie,35,80000\nDiana,28,72000\nEthan,32,75000\n", 
                "task": "Calculate the average salary of all employees and identify the employee with the highest salary."
            },
            "2": {
                "data": "Product,Price,Quantity\nApples,2,50\nBananas,1,100\nCherries,3,75\nDates,5,60\nElderberries,4,80\n", 
                "task": "Calculate the total revenue for each product and identify which product has the highest total revenue."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task = t["task"]
        data = t["data"]
        instructions = f"""Your task is to perform the following analysis on the given tabular data:\n\n{task}\n\nData:\n{data}\n\nSteps to follow:\n1. Read and understand the tabular data provided above.\n2. Perform the necessary calculations as required by the task.\n3. Provide your result in the format specified below.\n4. Explain the steps you took to arrive at your result.\n\nProvide your response in the following format:\n\nResult: [Your result]\nExplanation: [Your detailed explanation]\n\nExample Response:\nResult: The average salary is 72400 and the highest salary is 80000 (Charlie).\nExplanation: To calculate the average salary, I summed all the salaries and divided by the number of employees. For the highest salary, I compared each salary and found that Charlie has the highest salary."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["task"].startswith("Calculate the average salary"):
            criteria = [
                "The average salary must be correctly calculated.",
                "The highest salary must be correctly identified.",
                "The explanation must show the correct steps taken to arrive at the results."
            ]
        elif t["task"].startswith("Calculate the total revenue"):
            criteria = [
                "The total revenue for each product must be correctly calculated.",
                "The product with the highest total revenue must be correctly identified.",
                "The explanation must show the correct steps taken to arrive at the results."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
