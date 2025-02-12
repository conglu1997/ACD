class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A study shows that people who drink more than 2 liters of water per day tend to have better skin hydration levels.",
                "field": "Health and Nutrition"
            },
            "2": {
                "data": "Observations indicate that certain plants grow faster when exposed to classical music compared to those that are not.",
                "field": "Botany"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following data, generate a plausible scientific hypothesis and then critique its validity based on scientific principles.

Data: {t['data']}
Field: {t['field']}

Your response should include the following sections:
1. Hypothesis: [Your generated hypothesis based on the data]
2. Critique: [Your critique of the hypothesis, discussing its strengths, weaknesses, and any potential biases or limitations]

Ensure that your hypothesis is logically consistent with the data and your critique is thorough and scientifically sound. Your critique should cover the following aspects:
- Logical consistency with the data
- Potential biases or limitations in the data
- Scientific soundness
- Any assumptions made

Submit your response as a plain text string in the following format:
Hypothesis: [Your hypothesis]
Critique: [Your critique]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be logically consistent with the provided data.",
            "The critique should discuss potential biases or limitations in the data.",
            "The critique should assess the scientific soundness of the hypothesis.",
            "The critique should identify any assumptions made in the hypothesis.",
            "The response should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
