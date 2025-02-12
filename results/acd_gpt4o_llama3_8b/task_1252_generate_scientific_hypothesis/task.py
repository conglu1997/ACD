class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "observations": "1. A certain plant species in a particular region blooms only during the night.\n2. The same plant species in nearby regions blooms during the day.\n3. The nighttime blooming region has a higher population of nocturnal pollinators.\n4. The temperature in the nighttime blooming region drops significantly at night.\n5. The soil composition in both regions is identical."},
            "2": {
                "observations": "1. A certain type of fish is found in abundance only in waters with high levels of a specific type of algae.\n2. The fish have specialized mouthparts that seem adapted for grazing on the algae.\n3. The fish are rarely found in waters where this algae is absent.\n4. The algae produce a toxin that is harmful to other fish species.\n5. The water temperature in regions with high algae levels is slightly higher."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a plausible scientific hypothesis based on the following observations and provide a rationale for your hypothesis:

{t['observations']}

Your hypothesis should explain the observations logically and include a detailed rationale. Submit your hypothesis and rationale as a plain text string in the following format:

Hypothesis: [Your plausible scientific hypothesis]\nRationale: [Your detailed rationale]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The hypothesis should logically explain the observations.",
            "The rationale should be detailed and support the hypothesis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
