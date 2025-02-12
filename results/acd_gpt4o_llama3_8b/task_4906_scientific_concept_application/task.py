class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Photosynthesis", "scenario": "Imagine a new planet with a different type of sunlight spectrum that plants must adapt to. Explain how the process of photosynthesis might change on this planet. Consider factors such as the wavelength of the light, the energy requirements of the plants, and any potential changes in the biochemical pathways."},
            "2": {"concept": "Newton's Third Law of Motion", "scenario": "A spacecraft is trying to navigate through a region of space with no gravitational influence. Explain how Newton's Third Law of Motion would apply to the spacecraft's movement and how it can maneuver. Describe the mechanisms the spacecraft might use to move and change direction, and how the law applies to these mechanisms."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Explain the given scientific concept and apply it to the hypothetical scenario:\nConcept: {t['concept']}\nScenario: {t['scenario']}\nYour response should include:\n1. A clear and detailed explanation of the scientific concept.\n2. An application of the concept to the given scenario, demonstrating how the principles apply in the new context.\n\nSubmit your response as a plain text string in the following format:\n\nExplanation: [Your explanation]\nApplication: [Your application]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear, detailed, and accurate.", "The application should logically follow from the explanation and be coherent within the given scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
