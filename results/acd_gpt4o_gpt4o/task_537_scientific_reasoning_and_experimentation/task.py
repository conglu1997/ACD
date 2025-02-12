class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "Explain how photosynthesis works in plants and describe an experiment to measure the effect of different light intensities on the rate of photosynthesis."},
            "2": {"phenomenon": "Explain the greenhouse effect and propose an experiment to determine the impact of increased CO2 levels on temperature in a controlled environment."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following scientific phenomenon and design an experiment to test a related hypothesis. Ensure that your explanation is clear, accurate, and based on scientific principles. The experiment should be practical, well-structured, and include necessary controls. Here is the phenomenon:\n\n{t['phenomenon']}\n\nSubmit your response in the following format:\nExplanation: [Your explanation]\nExperiment: [Your experimental design]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear, accurate, and scientifically sound.", "The experimental design should be practical, well-structured, and include necessary controls."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
