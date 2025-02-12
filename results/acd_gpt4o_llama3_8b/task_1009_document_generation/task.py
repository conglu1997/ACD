class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"title": "Research Proposal", "sections": ["Introduction", "Literature Review", "Methodology", "Expected Results", "Conclusion"], "instructions": "Generate a research proposal document including the following sections: Introduction, Literature Review, Methodology, Expected Results, Conclusion. Ensure each section is clearly labeled and follows a logical flow, with original content relevant to a hypothetical research project."},
            "2": {"title": "Business Plan", "sections": ["Executive Summary", "Market Analysis", "Organizational Structure", "Product Line", "Marketing Strategy", "Financial Projections"], "instructions": "Generate a business plan document including the following sections: Executive Summary, Market Analysis, Organizational Structure, Product Line, Marketing Strategy, Financial Projections. Ensure each section is clearly labeled and follows a logical flow, with original content relevant to a hypothetical business venture."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        title = t["title"]
        sections = ", ".join(t["sections"])
        instructions = t["instructions"]
        return f"""Generate a structured document with the title '{title}'. The document should include the following sections: {sections}. {instructions}

Submit your document as a plain text string with each section clearly labeled and formatted as follows:

Title: {title}

Section 1: [Content]

Section 2: [Content]

...

Ensure the content in each section is original, relevant, and coherent. The document should follow a logical flow from one section to the next."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The document should include all specified sections.",
            "Each section should be clearly labeled.",
            "The content in each section should be original, relevant, and coherent.",
            "The document should follow a logical flow." ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
