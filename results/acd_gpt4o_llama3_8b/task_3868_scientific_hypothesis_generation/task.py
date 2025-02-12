class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A new species of plant has been discovered in a remote jungle. The plant has unusually thick leaves and appears to survive with minimal sunlight. Scientists suspect this plant has a unique method of photosynthesis.",
                "questions": [
                    "What plausible hypothesis can you generate about the plant's method of photosynthesis?",
                    "Explain the reasoning behind your hypothesis."]
            },
            "2": {
                "scenario": "A recently discovered mineral on Mars shows signs of containing water within its structure. This finding has significant implications for the possibility of past life on Mars.",
                "questions": [
                    "What plausible hypothesis can you generate about the presence of water in this mineral?",
                    "Explain the reasoning behind your hypothesis."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to generate a plausible scientific hypothesis based on the given scenario and explain the reasoning behind it.

Scenario: {t['scenario']}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Your responses should demonstrate a clear understanding of scientific principles and logical reasoning. Submit your response as a plain text string in the following format:

1. [Your hypothesis]
2. [Your reasoning]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The hypothesis should be scientifically plausible based on the scenario provided.",
            "The reasoning should demonstrate understanding of relevant scientific principles and logical coherence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
