class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A 15-year-old high school student, Alex, is experiencing severe anxiety before exams. Alex's parents are concerned and want to help but don't know how. They seek advice on how to support Alex effectively.", "question": "What advice would you give to Alex's parents to help reduce Alex's anxiety before exams?"},
            "2": {"scenario": "Jamie, a 30-year-old professional, is feeling burnt out from work and struggling to maintain a work-life balance. Jamie is considering quitting their job but is unsure if it's the right decision.", "question": "What steps should Jamie take to address the burnout and improve work-life balance?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following scenario and provide psychological insights or solutions:\n\nScenario: {t["scenario"]}\n\nQuestion: {t["question"]}\n\nProvide your advice or solution in plain text format, along with a brief explanation of your reasoning. Format your response as follows:\n\nAdvice: [Your advice or solution]\nExplanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a practical and empathetic solution to the problem.",
            "The response should demonstrate an understanding of psychological principles.",
            "The advice should be logically sound and feasible based on the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
