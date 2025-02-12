class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "table": "| Year | Sales (in millions) | Profit (in millions) |\n|------|-------------------|------------------|\n| 2018 | 50                | 10               |\n| 2019 | 60                | 15               |\n| 2020 | 55                | 12               |\n| 2021 | 70                | 20               |",
                "questions": [
                    "What is the average annual sales over the given period?",
                    "In which year did the company have the highest profit?"
                ]
            },
            "2": {
                "table": "| Month | Temperature (°C) | Rainfall (mm) |\n|-------|-----------------|----------------|\n| Jan   | 5               | 50             |\n| Feb   | 7               | 45             |\n| Mar   | 10              | 60             |\n| Apr   | 15              | 70             |\n| May   | 20              | 80             |\n| Jun   | 25              | 90             |",
                "questions": [
                    "What is the average temperature for the given months?",
                    "Which month had the highest rainfall?"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        table = t["table"]
        questions = t["questions"]
        questions_str = "\n".join(questions)
        return f"""Analyze the following data table and answer the questions below:\n\n{table}\n\nQuestions:\n{questions_str}\n\nSubmit your answers as a plain text string in the format: '1. [Answer to question 1] 2. [Answer to question 2]'. Ensure your answers are concise, directly address the questions asked, and are formatted correctly. For example:\n1. 58.75\n2. 2021"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Ensure that the submission format is correct
        if not submission.startswith('1.') or not '2.' in submission:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
