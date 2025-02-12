class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Computing",
                "audience": "High school students with basic understanding of physics"
            },
            "2": {
                "concept": "Blockchain Technology",
                "audience": "Business professionals with limited technical knowledge"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write detailed technical documentation for the following scientific concept or technology:

Concept: {t['concept']}

Audience: {t['audience']}

Your documentation should include:
1. An introduction to the concept or technology.
2. A detailed explanation of how it works.
3. Key applications and use cases.
4. Potential challenges and limitations.
5. Any relevant diagrams or illustrations (described in text, as actual diagrams cannot be provided).

Ensure that your explanation is accurate, comprehensive, and accessible to the specified audience. Format your text clearly and logically to enhance readability. Submit your documentation as a plain text string in the following format:

Technical Documentation: <your documentation>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The documentation should be accurate and comprehensive.",
            "The documentation should be accessible to the specified audience.",
            "The documentation should include an introduction, detailed explanation, applications, challenges, and relevant diagrams (in text).",
            "The text should be formatted clearly and logically."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
