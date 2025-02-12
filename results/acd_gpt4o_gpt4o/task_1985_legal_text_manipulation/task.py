class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Interpret the following legal clause and describe its implications:", "legal_clause": "The lessee shall not sublet the premises without the prior written consent of the lessor, which consent shall not be unreasonably withheld."},
            "2": {"description": "Draft a legal clause that allows a tenant to make minor alterations to the rental property with the landlord's consent, specifying what constitutes minor alterations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "legal_clause" in t:
            instructions = f"""Your task is to interpret the following legal clause and describe its implications:

{t['legal_clause']}

Provide your answer in plain text format, clearly and concisely explaining the implications of the legal clause."""
        else:
            instructions = f"""Your task is to draft a legal clause based on the following description:

{t['description']}

Ensure your legal clause is clear, precise, and covers all specified criteria. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "legal_clause" in t:
            criteria = ["The response should accurately describe the implications of the legal clause."]
        else:
            criteria = [
                "The legal clause should allow a tenant to make minor alterations to the rental property.",
                "The legal clause should specify what constitutes minor alterations.",
                "The legal clause should require the landlord's consent for alterations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
