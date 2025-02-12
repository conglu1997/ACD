class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"observations": "Plants in a shaded area grow slower than plants in full sunlight. Additionally, the leaves of shaded plants appear to be larger and darker green. Plants in partial sunlight have an intermediate growth rate and leaf size.", "domain": "botany"},
            "2": {"observations": "A metal object left outside in the rain develops rust, while a similar object kept indoors does not. Furthermore, objects exposed to salty air near the ocean rust faster than those in a dry climate. Objects in humid environments also tend to rust faster.", "domain": "chemistry"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        observations = t["observations"]
        domain = t["domain"]
        instructions = f"""Your task involves two parts:\n\n1. Hypothesis Generation: Based on the following observations, generate a scientific hypothesis.\n\nObservations: {observations}\n\n2. Experimental Design: Design an experiment to test the hypothesis you generated. Your experimental design should include the following:\n- A clear statement of the hypothesis\n- The independent and dependent variables\n- A detailed procedure for conducting the experiment, including materials and methods\n- The control setup\n- Methods for data collection and analysis\n- Safety considerations (if applicable)\n\nEnsure that your hypothesis is logical and based on the given observations. Avoid overly simple or obvious hypotheses. Your experimental design should be thorough and scientifically sound, demonstrating an understanding of the principles of experimental design.\n\nResponse Format:\nHypothesis: <Your hypothesis>\nExperimental Design: <Your experimental design>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be logical and based on the given observations.",
            "The experimental design should include the independent and dependent variables.",
            "The experimental design should include a detailed procedure for conducting the experiment, including materials and methods.",
            "The experimental design should include a control setup.",
            "The experimental design should include methods for data collection and analysis.",
            "The experimental design should include safety considerations (if applicable)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
