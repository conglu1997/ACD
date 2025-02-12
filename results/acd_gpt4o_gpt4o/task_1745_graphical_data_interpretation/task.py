class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A bar chart shows the number of books read by students in a class over four months. In January, 10 books were read; in February, 15 books were read; in March, 20 books were read; and in April, 25 books were read. Additionally, in May, the number of books read dropped to 5.",
                "question": "What is the average number of books read per month from January to May?"
            },
            "2": {
                "description": "A pie chart represents the market share of different smartphone brands. Brand A has 35%, Brand B has 25%, Brand C has 20%, and Brand D has 20%. Additionally, Brand E enters the market and gains a 10% share, reducing the shares of Brand A and Brand B by 5% each.",
                "question": "If there are 2000 smartphones in the market, how many smartphones does Brand C have after Brand E enters?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        question = t["question"]
        instructions = f"""Your task is to interpret the following textual description of graphical data and answer the related question.

Description: {description}

Question: {question}

Provide your answer in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should correctly interpret the provided graphical data description.",
            "The answer should accurately address the question based on the interpretation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
