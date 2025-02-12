class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster under blue light compared to red light."},
            "2": {"hypothesis": "Consuming Vitamin C can reduce the duration of the common cold."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        hypothesis = t["hypothesis"]
        instructions = f"""Your task is to design a scientific experiment to test the following hypothesis:

Hypothesis: {hypothesis}

In your experiment design, you should:
1. Clearly state the hypothesis.
2. Describe the materials and methods you would use to test the hypothesis.
3. Outline the experimental procedure step-by-step.
4. Identify the control and experimental groups.
5. Specify the variables to be measured and how they will be measured.
6. Explain how you would analyze the data to determine whether the hypothesis is supported or refuted.
7. Discuss any potential limitations or sources of error in your experiment.

Additionally, provide a set of hypothetical results that could be expected from the experiment design and analyze these results. Include a discussion on whether the results support or refute the hypothesis and why.

Your response should be detailed, well-structured, and demonstrate a clear understanding of scientific methodology. Format your response as follows:

Experiment Design:
1. Hypothesis
2. Materials and Methods
3. Experimental Procedure
4. Control and Experimental Groups
5. Variables Measured
6. Data Analysis
7. Potential Limitations

Hypothetical Results and Analysis:
1. Hypothetical Results
2. Analysis and Conclusion
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The experiment design should be logically sound and well-structured.",
            "The materials and methods should be clearly described and appropriate for testing the hypothesis.",
            "The experimental procedure should be detailed and step-by-step.",
            "The control and experimental groups should be correctly identified.",
            "The variables to be measured should be clearly specified and measurable.",
            "The data analysis method should be appropriate for determining whether the hypothesis is supported or refuted.",
            "The discussion of potential limitations or sources of error should be thorough.",
            "The hypothetical results should be realistic and relevant to the experiment design.",
            "The analysis of the hypothetical results should be logical, well-reasoned, and clearly indicate whether the hypothesis is supported or refuted."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
