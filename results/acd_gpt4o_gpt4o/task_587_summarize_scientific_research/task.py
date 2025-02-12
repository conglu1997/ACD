class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"abstract": "The study investigates the effects of blue light on plant growth. Using a controlled environment, researchers exposed plants to different wavelengths of light and measured growth rates. Results indicate that blue light significantly enhances plant growth compared to red light. The findings suggest potential agricultural applications for optimizing crop yields."},
            "2": {"abstract": "This research explores the use of machine learning algorithms for predicting stock market trends. By analyzing historical market data, the study develops a predictive model with high accuracy. The model's performance is compared to traditional statistical methods, showing superior results. Implications for financial forecasting and investment strategies are discussed. This study also considers the limitations of the model and suggests areas for future research to further improve predictive capabilities."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'abstract' in t:
            return f"""Your task is to summarize the following abstract of a scientific paper in 2-3 sentences:

Abstract: {t['abstract']}

Ensure your summary is concise, accurate, and captures the main findings of the research. Provide your summary in plain text format."""
        else:
            return f"""Your task is to explain the significance and potential impact of the research described in the following abstract. Your explanation should be 3-4 sentences long:

Abstract: {t['abstract']}

Ensure your explanation is clear, logical, and highlights the broader implications of the research. Provide your explanation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be concise and accurately reflect the content of the abstract.", "The response should capture the significance and potential impact of the research."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
