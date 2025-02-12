class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Entanglement", "experiment": "Design a simple experiment to demonstrate the concept of quantum entanglement to a high school student. Ensure the experiment includes at least 3 steps and uses common lab materials."},
            "2": {"concept": "Photosynthesis", "experiment": "Design a simple experiment to demonstrate the process of photosynthesis to a middle school student. Ensure the experiment includes at least 3 steps and uses common household or school lab materials."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        experiment = t["experiment"]
        instructions = f"""Your task is to explain the following scientific concept in simple terms and design a simple experiment to demonstrate it:

Scientific Concept: {concept}

1. Provide a clear and simple explanation of the concept. Your explanation should be understandable to someone without a scientific background.
2. Design a simple experiment that can be conducted to demonstrate the concept. The experiment should include at least 3 steps and use materials commonly available at home or in a school lab.

Ensure that your explanation is comprehensive and your experiment is practical and illustrative of the concept. Provide your response in the following format:

Explanation: [Your explanation]
Experiment: [Your experiment design]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately and clearly explain the scientific concept in simple terms.",
            "The explanation should be understandable to someone without a scientific background.",
            "The experiment should be practical, easy to understand, and effectively demonstrate the concept.",
            "The experiment should include at least 3 steps and use common materials." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
