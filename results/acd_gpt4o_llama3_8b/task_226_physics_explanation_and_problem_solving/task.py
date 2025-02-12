class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Explain the phenomenon of electromagnetic induction and solve the following problem: A coil with 50 turns and a cross-sectional area of 0.1 square meters is placed in a magnetic field that changes uniformly from 0.2 Tesla to 0 Tesla in 0.5 seconds. Calculate the induced EMF in the coil."
            },
            "2": {
                "prompt": "Explain the concept of wave-particle duality and solve the following problem: Calculate the de Broglie wavelength of an electron traveling at a speed of 2 x 10^6 meters per second."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide a detailed explanation of the following physical phenomenon and solve the related problem:

{t['prompt']}

Ensure that your explanation is clear, accurate, and demonstrates a deep understanding of the physical principles involved. For the problem-solving part, show all steps and calculations clearly. Submit your response as a plain text string with the following format:

1. Explanation: [Your detailed explanation here]
2. Problem Solution: [Your step-by-step solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be clear and accurate.",
            "The explanation should demonstrate a deep understanding of the physical principles involved.",
            "The problem-solving part should include all steps and calculations.",
            "The final answer to the problem should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
