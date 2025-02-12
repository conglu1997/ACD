class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "In a study of plant growth under different light conditions, it was observed that plants exposed to blue light grew 20% taller than those exposed to red light."},
            "2": {"data": "A population of birds has shown a significant increase in beak length over the past 10 years, coinciding with a change in the availability of their primary food source."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        data = t["data"]
        instructions = f"""Your task is to generate a plausible scientific hypothesis based on the following data and observations:

{data}

Then, evaluate the plausibility of your hypothesis by considering alternative explanations and potential experiments that could test it. Provide your response in the following format:

Hypothesis: [Your hypothesis]
Evaluation: [Your evaluation of the hypothesis, including alternative explanations and potential experiments]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a plausible scientific hypothesis.",
            "The evaluation should consider alternative explanations.",
            "The evaluation should propose potential experiments to test the hypothesis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
