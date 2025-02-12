class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_response": "The capital of Australia is Sydney."},
            "2": {"initial_response": "The theory of relativity was developed by Isaac Newton."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_response = t["initial_response"]
        return f"""Analyze the following response for potential errors or areas for improvement. Reflect on the accuracy and completeness of the response. After identifying any issues, provide a revised version of the response that corrects the errors and improves the overall quality.

Initial Response: '{initial_response}'

Submit your revised response in the following format:
- Identified Issues: [List any errors or areas for improvement]
- Revised Response: [Your revised and improved response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission must accurately identify any errors or areas for improvement in the initial response.",
            "The revised response must correct the identified errors and improve the overall quality of the response.",
            "The submission must be well-structured and clearly explain the identified issues and the revisions made.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
