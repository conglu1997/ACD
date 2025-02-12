class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dataset": [
                    {"month": "January", "sales": 150},
                    {"month": "February", "sales": 200},
                    {"month": "March", "sales": 175},
                    {"month": "April", "sales": 225},
                    {"month": "May", "sales": 250},
                    {"month": "June", "sales": 300},
                    {"month": "July", "sales": 275},
                    {"month": "August", "sales": 325},
                    {"month": "September", "sales": 275},
                    {"month": "October", "sales": 250},
                    {"month": "November", "sales": 225},
                    {"month": "December", "sales": 200}
                ],
                "question": "Identify the month with the highest sales and calculate the average sales for the year."
            },
            "2": {
                "dataset": [
                    {"year": 2015, "temperature": 15.2},
                    {"year": 2016, "temperature": 15.5},
                    {"year": 2017, "temperature": 15.8},
                    {"year": 2018, "temperature": 16.0},
                    {"year": 2019, "temperature": 16.3},
                    {"year": 2020, "temperature": 16.5},
                    {"year": 2021, "temperature": 16.7},
                    {"year": 2022, "temperature": 17.0}
                ],
                "question": "Identify the year with the highest temperature and calculate the overall temperature increase from 2015 to 2022."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dataset = t["dataset"]
        question = t["question"]
        instructions = f"""Your task is to analyze the following dataset and extract specific insights based on the given question:

Dataset: {dataset}

Question: {question}

Your response should include the identification of the specific insight requested and the calculation needed. Format your response as:

Insight: [Identified insight]
Calculation: [Calculation steps]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the specific insight requested.",
            "The calculations should be accurate based on the dataset provided.",
            "The response should be clear and formatted as specified in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
