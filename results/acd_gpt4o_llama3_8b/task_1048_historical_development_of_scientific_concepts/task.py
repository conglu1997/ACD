class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Theory of Evolution"},
            "2": {"concept": "General Relativity"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        return f"""Explain the historical development of the scientific concept: {concept}. Your explanation should include:
1. An overview of the concept.
2. Key figures who contributed to its development, including their specific contributions.
3. The historical context, including the time period and prevailing scientific beliefs.
4. The impact the concept had on society, scientific progress, and subsequent research.

Ensure that your explanation is detailed, historically accurate, and clearly articulated. Avoid using overly technical jargon and make sure the narrative is coherent and engaging. Submit your response as a plain text string in the following format:

Overview: [Your overview of the concept]
Key Figures: [Detailed description of key figures and their contributions]
Historical Context: [Description of the historical context]
Impact: [Impact of the concept on society and science]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The overview of the concept should be accurate and clear.",
            "The key figures and their contributions should be detailed and historically accurate.",
            "The historical context should be well-explained and include the time period and prevailing scientific beliefs.",
            "The impact of the concept on society, scientific progress, and subsequent research should be thoughtfully discussed.",
            "The explanation should be coherent, engaging, and well-articulated.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
