class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "In the case of Smith v. Jones, the court held that the defendant was liable for negligence. The plaintiff, Smith, argued that Jones had a duty of care to ensure the safety of visitors on his property. The court found that Jones breached this duty by failing to repair a broken stairway, which resulted in Smith’s injury. The court awarded damages to Smith for medical expenses and pain and suffering."},
            "2": {"text": "The United States Constitution guarantees certain fundamental rights to its citizens. The First Amendment protects the freedom of speech, religion, and the press. The Fourth Amendment protects against unreasonable searches and seizures, requiring a warrant supported by probable cause. The Fourteenth Amendment ensures equal protection under the law and due process for all citizens."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to summarize the following legal text and identify the key legal principles or clauses within it.

Text: {t['text']}

Your response should include:
1. A concise summary of the text.
2. Identification of the key legal principles or clauses.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should be concise and accurately reflect the main points of the text.",
            "The key legal principles or clauses should be correctly identified.",
            "The response should be logically structured.",
            "The response should be in plain text format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
