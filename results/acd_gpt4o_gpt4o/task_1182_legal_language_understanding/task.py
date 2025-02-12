class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"clause": "The lessee shall not sublet the leased premises or any part thereof without the prior written consent of the lessor, which consent shall not be unreasonably withheld. In the event of such subletting, the lessee shall remain fully responsible for the performance of all obligations under this lease. Furthermore, the lessee shall indemnify and hold harmless the lessor from any claims, damages, or liabilities arising from the subletting."},
            "2": {"requirements": "Draft a clause that requires the lessee to maintain the premises in good condition, including regular cleaning and timely repairs, with specific mention of bi-annual inspections by the lessor. Include penalties for failure to comply, specify a notice period for inspections, and mention the lessee's obligation to report significant damages immediately."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "clause" in t:
            return """Your task is to interpret the following legal clause and summarize its meaning in plain language:

{0}

Ensure your summary is accurate, clear, and concise. Provide your summary in plain text format.""".format(t["clause"])
        elif "requirements" in t:
            return """Your task is to draft a legal clause based on the following requirements:

{0}

Ensure your clause is formal, precise, and follows legal drafting conventions. Provide your clause in plain text format.""".format(t["requirements"])
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "clause" in t:
            criteria = [
                "The summary should accurately reflect the meaning of the legal clause.",
                "The summary should be clear and concise.",
                "The summary should use plain language." ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        elif "requirements" in t:
            criteria = [
                "The drafted clause should meet all the specified requirements.",
                "The clause should be formal and precise.",
                "The clause should follow legal drafting conventions." ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        else:
            return 0.0
