class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "case_description": "A company is being sued for breach of contract after failing to deliver goods on time. The company argues that an unforeseen natural disaster prevented the delivery. The plaintiff claims that the company should have accounted for such risks in the contract.",
                "legal_precedents": ["Force Majeure Clause", "Breach of Contract"]
            },
            "2": {
                "case_description": "An individual is suing a social media platform for defamation after false information about them was spread on the platform. The platform argues that it is not responsible for user-generated content under Section 230 of the Communications Decency Act.",
                "legal_precedents": ["Defamation", "Section 230 of the Communications Decency Act"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Construct a legal argument based on the following case description and legal precedents. Your argument should include:

1. A brief summary of the case.
2. Identification of the relevant legal principles and precedents.
3. A logical argument supporting one side of the case, taking into account the given precedents and legal principles.
4. A counterargument addressing potential points raised by the opposing side.

Submit your argument as a plain text string in the following format:

Case Description:
{t['case_description']}

Legal Argument:
[Your argument here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should accurately summarize the case description.",
            "The argument should correctly identify and apply the relevant legal principles and precedents.",
            "The argument should be logical, coherent, and well-structured.",
            "The argument should demonstrate understanding of legal concepts.",
            "The argument should include a counterargument addressing potential points from the opposing side."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0