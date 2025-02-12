class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Treatment,Control\n10,8\n15,12\n14,13\n18,16\n20,18",
                "hypothesis": "The treatment has a significant positive effect on the outcome compared to the control."
            },
            "2": {
                "data": "Before,After\n5,7\n6,8\n7,9\n5,6\n7,10",
                "hypothesis": "The intervention increases the outcome compared to the baseline."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Formulate a scientific conclusion based on the given data and hypothesis. Your response should include:
1. A brief description of the data.
2. A statistical test to evaluate the hypothesis.
3. The result of the statistical test.
4. A conclusion stating whether the hypothesis is supported or not supported by the data.

Data:
{t['data']}
Hypothesis:
{t['hypothesis']}

Example response format:
- Data Description: The dataset consists of two groups, Treatment and Control, with five observations each.
- Statistical Test: Conduct a t-test to compare the means of the two groups.
- Test Result: The p-value is 0.03.
- Conclusion: The hypothesis is supported as the treatment group has a significantly higher outcome compared to the control group."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The data description should accurately reflect the given dataset.",
            "The statistical test should be appropriate for the hypothesis.",
            "The test result should be correctly calculated based on the data.",
            "The conclusion should logically follow from the test result and hypothesis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
