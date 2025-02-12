class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirement": "A confidentiality clause for a non-disclosure agreement between two companies.", "legal_text": "This contract shall be governed by the laws of [state]. The parties agree to resolve any disputes through mediation before pursuing litigation."},
            "2": {"requirement": "An indemnity clause for a service agreement between a service provider and a client.", "legal_text": "The service provider shall not be liable for any indirect, incidental, or consequential damages arising out of or in connection with this agreement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        requirement = t['requirement']
        legal_text = t['legal_text']
        return f"""Task 1: Generate a legal clause based on the following requirement:

Requirement: {requirement}

The clause should be precise, legally sound, and adhere to formal legal language and structure. Submit your clause as a plain text string.

Task 2: Identify any issues in the following legal text and provide suggestions for improvement:

Legal Text: {legal_text}

Your response should clearly identify any ambiguities, inconsistencies, or potential legal risks in the text and suggest how to improve it. Submit your response in the following format:

Issues:
[Your identified issues]

Suggestions:
[Your suggestions for improvement]

Criteria for evaluation:
1. Precision: The clause should be legally precise and avoid ambiguity.
2. Adherence to Legal Standards: The clause should follow formal legal language and structure.
3. Issue Identification: The response should accurately identify issues in the provided legal text.
4. Suggestions for Improvement: The response should provide clear and legally sound suggestions for improvement."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The clause should be legally precise and avoid ambiguity.",
            "The clause should follow formal legal language and structure.",
            "The response should accurately identify issues in the provided legal text.",
            "The response should provide clear and legally sound suggestions for improvement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
