class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Plant growth rates under different light conditions: \nFull Sun: 10 cm/week\nPartial Sun: 6 cm/week\nShade: 3 cm/week", "experiment_design": "Design an experiment to test the effect of water quantity on plant growth under full sun conditions."},
            "2": {"data": "Reaction times to different stimuli: \nVisual: 0.25 seconds\nAuditory: 0.17 seconds\nTactile: 0.15 seconds", "experiment_design": "Design an experiment to test the effect of sleep deprivation on reaction times to auditory stimuli."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to formulate a scientific hypothesis based on the given data, design an experiment to test it, and draw conclusions from experimental results.

Data: {t['data']}

Experiment Design: {t['experiment_design']}

Provide your hypothesis, experiment design, and expected conclusions in the following format:

1. Hypothesis: [Your hypothesis]
2. Experiment Design: [Your detailed experiment design]
3. Expected Conclusions: [Your expected conclusions based on the hypothesis and experiment design]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should clearly state a hypothesis, a detailed experiment design, and expected conclusions.", 
                    "The experiment design should be logical and feasible.", 
                    "The expected conclusions should logically follow from the hypothesis and experiment design."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
