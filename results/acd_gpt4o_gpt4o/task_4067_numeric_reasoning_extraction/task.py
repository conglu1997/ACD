class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "In a class of 30 students, there are twice as many boys as girls. If 5 boys and 3 girls are absent, how many boys and how many girls are present in the class? Provide your answer in the format: 'Boys: [number], Girls: [number]'."},
            "2": {"scenario": "A farmer has 100 acres of land. He decides to plant corn on 40% of the land and wheat on the remaining. If the yield per acre for corn is 50 bushels and for wheat is 30 bushels, what is the total yield of corn and wheat combined? Provide your answer in the format: 'Total Yield: [number] bushels'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Read the following scenario and extract the relevant numeric information to answer the question. Provide your answer in the specified format. Here is the scenario: '" + t["scenario"] + "'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_id = None
        for key, value in TaskFamily.get_tasks().items():
            if value["scenario"] == t["scenario"]:
                task_id = key
                break
        correct_answers = {"1": "Boys: 10, Girls: 5", "2": "Total Yield: 3400 bushels"}
        criteria = [f"The response should correctly extract and reason about the numeric information, providing the correct answer: {correct_answers[task_id]}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
