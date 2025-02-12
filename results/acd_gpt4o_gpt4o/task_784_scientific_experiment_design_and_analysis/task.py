class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "design", "objective": "Determine the effect of different light colors on plant growth.", "constraints": "Use three different colors of light (red, blue, green) and measure plant height after 4 weeks. Ensure all other conditions are kept constant (e.g., water, soil type, temperature)."},
            "2": {"task": "analyze", "results": {"red": [10, 12, 11], "blue": [15, 14, 16], "green": [8, 9, 7]}, "objective": "Interpret the results of the experiment and provide a conclusion."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "design":
            return f"Your task is to design a scientific experiment to achieve the following objective: '{t['objective']}'. Ensure your experiment includes a clear hypothesis, detailed methodology, and a plan for data collection and analysis. Consider the given constraints: '{t['constraints']}'. Provide your experiment design in plain text format, including the following sections:\n1. Hypothesis\n2. Methodology\n3. Data Collection Plan\n4. Data Analysis Plan"
        elif t["task"] == "analyze":
            return f"Your task is to analyze the results of the following experiment: '{t['results']}'. The objective of the experiment was: '{t['objective']}'. Provide a detailed analysis and conclusion based on the results. Include any observations, trends, or patterns you identify. Provide your analysis in plain text format, including the following sections:\n1. Observations\n2. Analysis\n3. Conclusion"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "design":
            criteria = [
                "The experiment design should include a clear hypothesis.",
                "The methodology should be detailed and feasible.",
                "There should be a plan for data collection and analysis.",
                "The design should consider the given constraints."
            ]
        elif t["task"] == "analyze":
            criteria = [
                "The analysis should be detailed and coherent.",
                "The conclusion should be based on the provided results.",
                "The analysis should identify any observations, trends, or patterns in the data."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
