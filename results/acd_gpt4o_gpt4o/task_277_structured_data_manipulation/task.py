class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "table": "| Name  | Age | City     |\n|-------|-----|----------|\n| Alice | 30  | New York |\n| Bob   | 25  | Boston   |\n| Carol | 27  | Chicago  |", "question": "Who is the oldest person and which city do they live in?"},
            "2": {"task_type": "generate", "description": "Generate a table listing 3 students with their names, grades, and favorite subjects.", "criteria": "The table should have columns for Name, Grade, and Favorite Subject."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            instructions = f"""Your task is to interpret the following table and answer the question based on the data provided:

{t['table']}

Question: {t['question']}"""
        else:
            instructions = f"""Your task is to generate a table based on the following description:

{t['description']}

Ensure the table is formatted in plain text using pipes (|) to separate columns and hyphens (-) to separate the header row. For example:

| Name  | Grade | Favorite Subject |
|-------|-------|------------------|
| Alice | A     | Math             |
| Bob   | B     | Science          |
| Carol | A     | History          |"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            criteria = ["The response should correctly identify the oldest person and their city."]
        else:
            criteria = ["The generated table should have columns for Name, Grade, and Favorite Subject.", "The table should list 3 students.", "The table should be formatted correctly with pipes (|) and hyphens (-)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
