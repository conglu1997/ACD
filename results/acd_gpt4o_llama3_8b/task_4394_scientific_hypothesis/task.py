class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "observations": "Several plants in a garden are observed to grow more rapidly when exposed to classical music compared to those exposed to no music.",
                "additional_data": "Further experiments show that plants exposed to classical music have higher chlorophyll content and increased photosynthetic activity."
            },
            "2": {
                "observations": "A group of lab mice on a high-fat diet show an increase in weight, while another group on the same diet but given a particular supplement do not show significant weight gain.",
                "additional_data": "Further tests reveal that the supplement affects the expression of genes related to fat metabolism in the mice."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a scientific hypothesis based on the following observations. Then, evaluate the validity of your hypothesis based on the additional data provided. Your response should include:

1. The hypothesis generated from the initial observations.
2. An evaluation discussing how the additional data supports or contradicts your hypothesis.

Observations: {t['observations']}

Additional Data: {t['additional_data']}

Submit your response as a plain text string in the following format:

Hypothesis: [Your hypothesis]
Evaluation: [Your evaluation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The hypothesis should be logically derived from the given observations.",
            "The evaluation should accurately relate the additional data to the hypothesis, discussing whether it supports or contradicts the hypothesis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
