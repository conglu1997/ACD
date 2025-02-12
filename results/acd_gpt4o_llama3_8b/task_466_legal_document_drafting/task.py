class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A company wants to include a non-compete clause in its employment contracts for senior software engineers. Draft a non-compete clause that is enforceable in the state of California."},
            "2": {"scenario": "A tenant has been unlawfully evicted from their apartment without proper notice. Draft a demand letter to the landlord, requesting reinstatement of tenancy and compensation for damages."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Interpret the following legal scenario and draft the appropriate legal document:\n\n{scenario}\n\nEnsure that your document is clear, legally sound, and follows the conventions of legal writing.\n\nYour submission should include the following:\n1. A clear and concise statement of the issue.\n2. Relevant legal principles or statutes that apply.\n3. A logically structured argument or clause.\n4. Appropriate legal language and tone.\n\nSubmit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The document should address the given scenario accurately.",
            "The document should include a clear statement of the issue.",
            "The document should reference relevant legal principles or statutes.",
            "The document should be logically structured and legally sound.",
            "The document should use appropriate legal language and tone."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
