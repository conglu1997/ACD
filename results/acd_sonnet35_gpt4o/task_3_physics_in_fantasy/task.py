import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "setting": "a planet with half of Earth's gravity",
                "problem": "design a sport that takes advantage of the lower gravity"
            },
            {
                "setting": "a world where the speed of light is only 100 km/h",
                "problem": "describe how communication and transportation would work"
            },
            {
                "setting": "a universe where objects become larger as they move faster",
                "problem": "explain how this would affect space travel"
            },
            {
                "setting": "a dimension where time flows backwards",
                "problem": "describe how cause and effect would operate"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Imagine {t['setting']}. Your task is to {t['problem']}. In your response, clearly explain the relevant physics principles and how they would apply in this scenario. Be creative in your solution, but ensure it remains consistent with the laws of physics (as modified in the scenario). Provide a detailed explanation in 3-5 sentences."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate a clear understanding of relevant physics principles.",
            "The solution should be creative and original, while remaining consistent with the modified laws of physics in the scenario.",
            "The explanation should be detailed and logical, connecting the physics principles to the proposed solution.",
            "The response should be 3-5 sentences long and address all aspects of the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
