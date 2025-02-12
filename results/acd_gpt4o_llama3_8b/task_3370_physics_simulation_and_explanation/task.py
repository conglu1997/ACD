class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Simulate the motion of a projectile launched at a certain angle and speed."
            },
            "2": {
                "prompt": "Simulate the oscillations of a simple pendulum given its length and initial displacement."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"""Simulate the following physical system based on the given parameters: {prompt}.
Your simulation should include:
1. A description of the physical system and the parameters involved.
2. The equations of motion governing the system.
3. A step-by-step explanation of how the simulation is conducted.
4. The final result of the simulation (e.g., trajectory path for projectile, time period for pendulum).

Provide your result in a clear and detailed manner, ensuring that all steps and calculations are logically presented. Submit your response as a plain text string in the following format:

Description: [Your description]
Equations: [Your equations of motion]
Steps: [Your step-by-step explanation]
Result: [The final result of the simulation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately describe the physical system and parameters.",
            "The equations of motion should be correct and relevant.",
            "The step-by-step explanation should be clear and logically structured.",
            "The final result of the simulation should be correct based on the provided parameters."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
