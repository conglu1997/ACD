class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Design a simple experiment to test the hypothesis that plants grow faster under blue light than under red light. Include the following sections: Hypothesis, Independent Variable, Dependent Variable, Control Variables, Procedure."},
            "2": {"prompt": "Analyze the following dataset and draw conclusions. The dataset shows the growth of plants (in cm) under different light conditions over 15 days.", "data": "Day, Blue Light, Red Light\n1, 0.5, 0.4\n2, 1.1, 0.9\n3, 1.8, 1.5\n4, 2.5, 2.0\n5, 3.3, 2.6\n6, 4.1, 3.2\n7, 5.0, 3.8\n8, 5.9, 4.4\n9, 6.8, 5.0\n10, 7.8, 5.6\n11, 8.8, 6.2\n12, 9.9, 6.8\n13, 10.9, 7.4\n14, 12.0, 8.0\n15, 13.1, 8.6"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Design" in t["prompt"]:
            return f"""Design a simple scientific experiment based on the given prompt:

{t["prompt"]}

Include the following sections in your response:
1. Hypothesis: State the hypothesis you are testing.
2. Independent Variable: Identify the variable you will change.
3. Dependent Variable: Identify the variable you will measure.
4. Control Variables: Identify the variables you will keep constant.
5. Procedure: Describe the steps you will take to conduct the experiment.

Submit your response as a plain text string in the following format:

Hypothesis:
[Your hypothesis]

Independent Variable:
[Your independent variable]

Dependent Variable:
[Your dependent variable]

Control Variables:
[Your control variables]

Procedure:
[Your procedure]"""
        else:
            return f"""Analyze the following dataset and draw conclusions based on the given prompt:

{t["prompt"]}

{t["data"]}

Include the following sections in your response:
1. Data Summary: Summarize the growth data for plants under blue light and red light.
2. Analysis: Compare the growth rates under blue light and red light.
3. Conclusion: State your conclusion based on the analysis.

Submit your response as a plain text string in the following format:

Data Summary:
[Your data summary]

Analysis:
[Your analysis]

Conclusion:
[Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "Design" in t["prompt"]:
            criteria = ["The hypothesis should be clear and testable.", "The independent variable should be identified correctly.", "The dependent variable should be identified correctly.", "Control variables should be identified and appropriate.", "The procedure should be logical and detailed enough to replicate the experiment."]
        else:
            criteria = ["The data summary should accurately reflect the dataset.", "The analysis should correctly compare the growth rates under different light conditions.", "The conclusion should logically follow from the analysis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
