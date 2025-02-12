class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A new plant species has been discovered in a remote forest. Observations show that the plant grows faster in shaded areas compared to areas with direct sunlight. Additionally, the soil in shaded areas has higher moisture content, and the temperature is consistently lower.",
                "variables": ["sunlight exposure", "growth rate", "soil moisture", "temperature"]
            },
            "2": {
                "data": "A study on a population of birds shows that those with brighter plumage tend to have higher mating success rates. It has also been observed that these birds are more often found in areas with abundant food resources, and they exhibit more frequent mating calls.",
                "variables": ["plumage brightness", "mating success", "food availability", "mating calls frequency"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the provided data, generate a scientific hypothesis that explains the observed phenomenon. Then, outline an experimental setup to test your hypothesis. Ensure that your experimental design includes the following components:
1. A clear statement of the hypothesis.
2. Identification of the independent and dependent variables.
3. A detailed description of the experimental procedure.
4. Methods for data collection and analysis.
5. Any control measures to ensure the validity of the experiment.
6. Consideration of additional variables provided in the data.

Submit your response as a plain text string in the following format:

Hypothesis: [Your hypothesis]
Independent Variable: [Your independent variable]
Dependent Variable: [Your dependent variable]
Experimental Procedure: [Your experimental procedure]
Data Collection and Analysis: [Your methods for data collection and analysis]
Control Measures: [Your control measures]
Additional Variables: [Consideration of additional variables]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The hypothesis should be clearly stated.",
            "The independent and dependent variables should be correctly identified.",
            "The experimental procedure should be detailed and feasible.",
            "Methods for data collection and analysis should be clearly outlined.",
            "Control measures should be included to ensure the validity of the experiment.",
            "Consideration of additional variables should be addressed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
