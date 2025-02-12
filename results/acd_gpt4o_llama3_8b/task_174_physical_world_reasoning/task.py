class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A ball is dropped from a height of 5 meters. Describe the motion of the ball considering gravity, air resistance, and the impact with the ground. Provide a detailed explanation covering the different stages of the ball's motion."
            },
            "2": {
                "scenario": "A car is driving around a circular track at a constant speed. Explain the forces acting on the car, including friction, centripetal force, and any other relevant forces. Describe how these forces affect the car's motion and provide a detailed explanation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the physical interactions and spatial relationships in the following scenario. Ensure your explanation covers the relevant physical laws, forces, and any resulting motion. Your explanation should be detailed and logically structured. Submit your explanation as a plain text string.\n\nScenario: {t['scenario']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should accurately describe the physical interactions and spatial relationships.",
            "The explanation should cover relevant physical laws and forces.",
            "The explanation should be detailed and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
