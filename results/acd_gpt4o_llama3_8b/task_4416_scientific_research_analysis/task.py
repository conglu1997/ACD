class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"abstract": "Recent advances in quantum computing have demonstrated the potential of quantum processors to solve complex problems more efficiently than classical computers. However, significant challenges remain in terms of error correction and scalability. This study explores new error correction techniques that could enhance the stability and scalability of quantum processors."},
            "2": {"abstract": "Climate change is having a profound impact on global biodiversity. This research examines the effects of rising temperatures on marine life, particularly focusing on coral reefs. The findings suggest that increased water temperatures are leading to widespread coral bleaching and mortality, which has cascading effects on marine ecosystems."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        abstract = t["abstract"]
        return f"""Read the following scientific research abstract and complete the following tasks:\n\n1. Summarize the key findings of the research.\n2. Identify any potential limitations or areas for further study mentioned in the abstract.\n\nDo not include any direct hints or answers in your response. Your summary and analysis should be in your own words.\n\nScientific Abstract:\n{abstract}\n\nSubmit your response as a plain text string in the following format:\n\nSummary: [Your summary]\nLimitations/Areas for Further Study: [Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The summary should accurately capture the key findings of the research.", "The analysis should identify potential limitations or areas for further study mentioned in the abstract.", "The response should be in the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
