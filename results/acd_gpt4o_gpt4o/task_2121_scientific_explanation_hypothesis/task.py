class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "explain", "phenomenon": "Photosynthesis", "context": "Explain the process of photosynthesis in plants, including the role of chlorophyll, sunlight, water, and carbon dioxide. Discuss the light-dependent and light-independent (Calvin cycle) reactions."},
            "2": {"task_type": "generate", "data": "Mysterious increase in algae population in a freshwater lake. Recent data shows a significant increase in nutrient levels, particularly nitrogen and phosphorus, in the lake. There has also been an unusual rise in water temperature over the past month. Additionally, there is evidence of increased agricultural runoff and reduced water flow into the lake.", "context": "Generate a plausible hypothesis for the observed increase in algae population."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'explain':
            return f"""Your task is to explain the following scientific phenomenon in detail:\n\nPhenomenon: {t['phenomenon']}\n\nContext: {t['context']}\n\nEnsure that your explanation is clear, accurate, and covers the key aspects of the phenomenon. Provide your response in the following format:\n\nExplanation: [Your detailed explanation]\n"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a plausible hypothesis based on the following data:\n\nData: {t['data']}\n\nContext: {t['context']}\n\nEnsure that your hypothesis is logically sound, scientifically plausible, and addresses the observed data. Provide your response in the following format:\n\nHypothesis: [Your hypothesis]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'explain':
            criteria = ["The response should be formatted as 'Explanation: [Your detailed explanation]'.", "The explanation must be clear and accurate.", "The explanation must cover the key aspects of the phenomenon, including the light-dependent and light-independent reactions."]
        elif t['task_type'] == 'generate':
            criteria = ["The response should be formatted as 'Hypothesis: [Your hypothesis]'.", "The hypothesis must be logically sound.", "The hypothesis must be scientifically plausible.", "The hypothesis must address the observed data, including nutrient levels, water temperature, agricultural runoff, and water flow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
