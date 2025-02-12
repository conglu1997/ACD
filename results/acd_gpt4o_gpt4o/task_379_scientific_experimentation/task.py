class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"hypothesis": "Plants grow faster when exposed to classical music.", "variables": "independent: type of music (classical, rock, no music), dependent: plant growth rate (height in cm per week), control: plants with no music, constants: type of plant, soil, water, light"},
            "2": {"experiment": "A study was conducted to test the effect of different light colors on plant growth. Three groups of plants were exposed to red, blue, and green light respectively. The average height of plants after 4 weeks was recorded: Red light: 15 cm, Blue light: 20 cm, Green light: 10 cm.", "question": "What can you conclude from the experiment? How might you improve the experimental design? Consider factors such as sample size, control groups, and potential confounding variables."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "hypothesis" in t:
            return f"""Your task is to design a scientific experiment to test the given hypothesis.

Hypothesis: {t['hypothesis']}

Your response should include:
1. A clear description of the experimental setup.
2. Identification of the independent, dependent, and control variables.
3. The procedure you would follow to conduct the experiment.
4. The type of data you would collect and how you would analyze it.

Provide your response in plain text format."""
        elif "experiment" in t:
            return f"""Your task is to interpret the results of the given experiment and suggest improvements.

Experiment: {t['experiment']}

Your response should include:
1. A clear interpretation of the results.
2. Any conclusions that can be drawn from the data.
3. Suggestions for improving the experimental design.

Provide your response in plain text format."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "hypothesis" in t:
            criteria = [
                "The experimental setup should be clear and feasible.",
                "The independent, dependent, and control variables should be correctly identified.",
                "The procedure should be detailed and logical.",
                "The type of data to be collected and analysis method should be appropriate for testing the hypothesis."
            ]
        elif "experiment" in t:
            criteria = [
                "The interpretation of the results should be accurate and logical.",
                "The conclusions should be supported by the data.",
                "The suggestions for improving the experimental design should be reasonable and relevant."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
