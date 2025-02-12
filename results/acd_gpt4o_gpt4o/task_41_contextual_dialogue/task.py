class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are at a job interview for a software engineering position. The interviewer asks you about your previous project experience and how you handle tight deadlines. Generate a dialogue that includes at least 5 exchanges."},
            "2": {"scenario": "You are at a networking event, and you meet someone who works in the same industry but at a different company. The conversation begins with an introduction and moves on to discussing recent industry trends. Generate a dialogue that includes at least 5 exchanges."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a coherent and contextually appropriate dialogue based on the following scenario. Ensure that the dialogue is natural, relevant, and maintains the flow of conversation throughout the exchanges. Use quotation marks for each turn in the dialogue. Here is the scenario:

{t['scenario']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be coherent and contextually appropriate.", "The dialogue should include at least 5 exchanges."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
