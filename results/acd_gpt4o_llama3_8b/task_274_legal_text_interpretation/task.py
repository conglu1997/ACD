class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "According to Section 2 of the Employment Law, an employee is entitled to a minimum of 21 days of paid leave per year. Additionally, employees who have completed 5 years of service are entitled to an additional 5 days of paid leave."},
            "2": {"text": "Under Section 4 of the Property Law, any lease agreement for a term exceeding 3 years must be in writing and registered with the local land registry office. Failure to comply with these requirements renders the lease agreement void."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following legal text and answer the questions below:

{t["text"]}

Questions:
1. What are the minimum paid leave entitlements for an employee who has worked for 6 years according to the Employment Law?
2. What is the legal status of an oral lease agreement for 4 years under the Property Law?

Provide your answers in a clear and concise manner as a plain text string in the following format:

Answer 1: [Your answer]
Answer 2: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answers should be accurate based on the provided legal text.", "The answers should be clear and concise."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
