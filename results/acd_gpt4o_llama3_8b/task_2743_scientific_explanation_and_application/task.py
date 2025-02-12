class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Newton's Third Law of Motion", "scenario": "Explain how Newton's Third Law of Motion applies to the motion of a rocket during launch. Consider the forces involved and how they interact to propel the rocket."},
            "2": {"concept": "Photosynthesis", "scenario": "Explain how photosynthesis could be utilized to sustain human life in a closed environment, such as a space station. Consider the necessary conditions and how they can be maintained."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        scenario = t["scenario"]
        return f"""Explain the following scientific concept and then apply it to the given scenario:\n\nConcept: {concept}\nScenario: {scenario}\n\nEnsure that your explanation is clear, accurate, and demonstrates a deep understanding of the scientific principles involved. Your application should be logically sound and feasible.\n\nSubmit your response in the following format:\n1. Explanation: [Your explanation of the scientific concept]\n2. Application: [Your application of the concept to the scenario]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the scientific concept should be clear and accurate.",
            "The application of the concept to the scenario should be logically sound and feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
