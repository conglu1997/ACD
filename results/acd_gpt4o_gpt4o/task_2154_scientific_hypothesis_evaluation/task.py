class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A new type of plant is found to grow faster in the presence of a specific mineral in the soil. You have data on plant growth rates with varying mineral concentrations.",
                "data": "Concentration (mg/kg),Growth Rate (cm/day)\n0,1\n10,2\n20,3\n30,4\n40,3\n50,2"
            },
            "2": {
                "scenario": "A certain bacteria is observed to produce more antibiotic compounds when exposed to a particular light wavelength. You have data on antibiotic production with different light wavelengths.",
                "data": "Wavelength (nm),Antibiotic Production (units)\n400,5\n450,10\n500,15\n550,20\n600,15\n650,10"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        data = t["data"]
        instructions = f"""Your task is to generate a scientific hypothesis based on the following scenario and data. Then, evaluate the validity of your hypothesis using the provided data.

Scenario: {scenario}

Data:
{data}

Provide your response in the following format:
1. Hypothesis: [Your hypothesis]
2. Evaluation: [Your evaluation of the hypothesis based on the data]

Ensure that your hypothesis is scientifically plausible and that your evaluation is thorough and based on the data provided."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be scientifically plausible.",
            "The evaluation should be thorough and based on the provided data.",
            "The response should be clear and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
