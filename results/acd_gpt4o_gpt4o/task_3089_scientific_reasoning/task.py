class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A new species of plant has been discovered in a remote forest. The plant has a unique characteristic: its leaves change color from green to blue during the day and back to green at night. The scientists have observed that the color change is more pronounced on sunny days compared to cloudy days.", "hypothesis": ""},
            "2": {"scenario": "A group of researchers have observed that a certain type of bacteria can survive in environments with extremely high levels of radiation. Preliminary studies suggest that these bacteria have unique proteins in their cell membranes that may play a role in radiation resistance.", "hypothesis": ""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a plausible hypothesis based on the given scientific scenario and then design an experiment to test that hypothesis. Here is the scenario:\n{t['scenario']}\n\nPlease provide your hypothesis and a detailed experimental design, including the following components:\n1. Hypothesis\n2. Experimental Design\n  - Materials and Methods\n  - Procedure\n  - Expected Results\n\nEnsure that your hypothesis is plausible and that your experiment is designed to effectively test the hypothesis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The hypothesis should be plausible based on the scenario.", "The experimental design should be detailed and logical.", "The experiment should be capable of testing the hypothesis effectively."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
