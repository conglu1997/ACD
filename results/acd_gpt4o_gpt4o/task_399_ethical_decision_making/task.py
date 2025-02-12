class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "dilemma": "You are a doctor with five patients in critical condition. Each needs a different organ transplant to survive, and there are no available donors. A healthy young traveler comes to you for a routine check-up. You realize he is a perfect match for all five patients. Should you sacrifice the traveler to save the five patients?"},
            "2": {"type": "evaluate", "action": "A company decides to lay off a significant portion of its workforce to increase short-term profits, knowing that it will cause severe financial distress to many families. Evaluate the ethics of this decision."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            dilemma = t["dilemma"]
            return f"""Your task is to generate a solution to the following ethical dilemma:

{dilemma}

Provide a detailed explanation of your solution, including the ethical principles and reasoning behind your decision. Ensure your response is comprehensive and considers multiple perspectives. Your response should be structured in a step-by-step format."""
        elif t["type"] == "evaluate":
            action = t["action"]
            return f"""Your task is to evaluate the ethics of the following action:

{action}

Provide a detailed evaluation, considering the ethical implications and possible consequences. Ensure your response is thorough and well-reasoned. Your response should be structured in a step-by-step format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be well-reasoned and consider multiple perspectives.",
            "The response should include a detailed explanation of the ethical principles involved.",
            "The response should be comprehensive and reflect a deep understanding of the ethical dilemma or action.",
            "The response should be structured in a step-by-step format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
