class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "A recent study has shown that a specific plant species grows faster when exposed to blue light compared to red light. However, the study also noted that plants exposed to blue light had a higher incidence of leaf discoloration.",
                "data": "Blue light exposure: 20% increase in growth rate, 30% incidence of leaf discoloration; Red light exposure: 5% increase in growth rate, 5% incidence of leaf discoloration",
                "task": "Generate two plausible scientific hypotheses based on the given context and data. Then, evaluate the strengths and weaknesses of each hypothesis."
            },
            "2": {
                "context": "Observations indicate that urban areas have higher temperatures compared to rural areas due to the 'urban heat island' effect. Additionally, it was found that urban areas with more green spaces had slightly lower temperatures than those with fewer green spaces.",
                "data": "Urban temperature: 5°C higher on average, Green space urban areas: 2°C lower on average; Rural temperature: baseline",
                "task": "Generate two plausible scientific hypotheses based on the given context and data. Then, evaluate the strengths and weaknesses of each hypothesis."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the given context and data, generate two plausible scientific hypotheses. Then, evaluate the strengths and weaknesses of each hypothesis.

Context: {t['context']}
Data: {t['data']}

Task:
1. Generate two scientific hypotheses based on the context and data.
2. Evaluate the strengths and weaknesses of each hypothesis.

Submit your response as a plain text string in the following format:

Hypothesis 1: [Your first hypothesis]
Strengths: [Strengths of the first hypothesis]
Weaknesses: [Weaknesses of the first hypothesis]

Hypothesis 2: [Your second hypothesis]
Strengths: [Strengths of the second hypothesis]
Weaknesses: [Weaknesses of the second hypothesis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should include two plausible scientific hypotheses.", "The evaluation should include strengths and weaknesses for each hypothesis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
