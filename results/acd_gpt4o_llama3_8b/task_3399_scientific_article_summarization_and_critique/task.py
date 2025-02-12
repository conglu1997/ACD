class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "article": "In this study, we investigated the effects of a new drug on reducing blood pressure in patients with hypertension. The study was a double-blind, placebo-controlled trial involving 200 participants over a period of 12 weeks. The results showed a significant reduction in blood pressure in the treatment group compared to the placebo group. However, some adverse effects were reported, including dizziness and headaches. The authors conclude that the new drug is effective but recommend further research to evaluate its long-term safety.",
                "field": "medical"
            },
            "2": {
                "article": "This research explores the impact of climate change on marine biodiversity in the Pacific Ocean. Using satellite imagery and underwater sensors, the study tracked changes in water temperature, acidity, and marine life over ten years. The findings indicate a notable decline in species diversity, particularly among coral reefs and fish populations. The researchers argue that immediate action is needed to mitigate the adverse effects of climate change on marine ecosystems.",
                "field": "environmental science"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the provided scientific article from the field of {t['field']}. Your task is to: 
1. Summarize the article in a concise manner, capturing the main points and findings.
2. Provide a critical analysis of the article's methodology, results, and conclusions.

Ensure that your summary is comprehensive and your critique is well-reasoned and evidence-based. Submit your response in the following format:

Summary: [Your summary]
Critique: [Your critique]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The summary should accurately capture the main points and findings of the article.",
            "The critique should be well-reasoned, addressing the methodology, results, and conclusions of the article with appropriate evidence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
