class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "hypothesis": "Plants grow faster in blue light than in red light.",
                "variables": {
                    "independent": "light color",
                    "dependent": "plant growth rate",
                    "controlled": ["soil type", "water amount", "temperature", "plant species"],
                    "confounding": ["light intensity"]
                }
            },
            "2": {
                "hypothesis": "Exercise improves cognitive function in adults.",
                "variables": {
                    "independent": "exercise regimen",
                    "dependent": "cognitive function scores",
                    "controlled": ["age", "diet", "sleep duration", "baseline cognitive function"],
                    "confounding": ["stress levels"]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a scientific experiment to test the following hypothesis: '{t['hypothesis']}'. Ensure your experimental design includes all necessary components and follows the scientific method. Provide a detailed description of your experiment in plain text format.\n\nHypothesis: {t['hypothesis']}\nVariables:\nIndependent Variable: {t['variables']['independent']}\nDependent Variable: {t['variables']['dependent']}\nControlled Variables: {', '.join(t['variables']['controlled'])}\nConfounding Variables: {', '.join(t['variables']['confounding'])}\n\nResponse format:\n1. Introduction: [Introduce the hypothesis and its significance]\n2. Methodology: [Describe the experimental design, including how you will manipulate the independent variable and measure the dependent variable]\n3. Controls: [Explain how you will control the other variables]\n4. Confounding Variables: [Identify potential confounding variables and describe how you will address them]\n5. Control Group: [Explain the use of a control group in your experiment]\n6. Replication and Sample Size: [Describe how you will ensure replication and determine the sample size]\n7. Data Collection: [Describe how you will collect and analyze the data]\n8. Expected Results: [State what results you expect and how they will support or refute the hypothesis]\n\nExample response:\n1. Introduction: The hypothesis states that plants grow faster in blue light than in red light. Understanding the effect of light color on plant growth can help optimize agricultural practices.\n2. Methodology: We will grow two groups of the same plant species, one under blue light and one under red light, in identical conditions. We will measure plant growth rate by recording the height of the plants every week for eight weeks.\n3. Controls: We will use the same soil type, water amount, temperature, and plant species for both groups.\n4. Confounding Variables: We will ensure that the light intensity is the same for both light colors to avoid confounding effects.\n5. Control Group: We will include a control group of plants grown in natural light to compare growth rates.\n6. Replication and Sample Size: Each group will consist of 30 plants to ensure statistical significance. The experiment will be repeated three times to confirm the results.\n7. Data Collection: We will collect weekly measurements of plant height and analyze the data using statistical methods to determine if there is a significant difference in growth rates between the two groups.\n8. Expected Results: We expect the plants under blue light to grow faster than those under red light, supporting the hypothesis that blue light promotes faster plant growth."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The experimental design should be detailed and follow the scientific method.",
            "The response should include all components: Introduction, Methodology, Controls, Confounding Variables, Control Group, Replication and Sample Size, Data Collection, and Expected Results.",
            "The response should be coherent and logically structured.",
            "The described experiment should be feasible and scientifically valid."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
