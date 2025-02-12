class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dataset": "Name,Age,Salary,Department\nAlice,30,70000,HR\nBob,25,48000,Engineering\nCharlie,35,80000,Marketing\nDiana,28,56000,HR\nEve,22,45000,Engineering\nFrank,40,60000,Marketing\nGrace,30,75000,HR\n",
                "instructions": "1. Filter out individuals with Salary less than 50000.\n2. Group the remaining individuals by Department and calculate the average Salary for each department.\n3. Return the modified dataset and the average Salary per Department."
            },
            "2": {
                "dataset": "Product,Category,Price,Stock,Rating\nLaptop,Electronics,1000,50,4.5\nHeadphones,Electronics,200,150,4.0\nT-Shirt,Clothing,25,300,3.8\nBook,Stationery,15,500,4.9\nSmartphone,Electronics,800,30,4.3\nNotebook,Stationery,5,700,4.1\nBackpack,Clothing,50,200,4.7\n",
                "instructions": "1. Filter out products in the 'Electronics' category.\n2. Calculate the total Stock and the average Rating of the remaining products.\n3. Return the modified dataset, the total Stock, and the average Rating."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the following transformations and analyses on the given dataset:\n{t['instructions']}\n\nDataset:\n{t['dataset']}\n\nSubmit your response as a plain text string with the modified dataset and the results of the analyses clearly labeled.\nResponse format:\nModified Dataset:\n[Modified dataset]\nResults:\n[Results]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        response_format_criteria = [
            "The response should start with 'Modified Dataset:' followed by the modified dataset.",
            "The response should include 'Results:' followed by the results of the analyses.",
            "The modified dataset should be consistent with the described transformations.",
            "The results should accurately reflect the analyses performed on the modified dataset."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, response_format_criteria) else 0.0
