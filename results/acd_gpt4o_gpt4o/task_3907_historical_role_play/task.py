class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are Alexander the Great, and you are discussing military strategy with your generals before the Battle of Gaugamela. Your goal is to motivate your generals and outline a plan for defeating Darius III of Persia.",
                "character": "Alexander the Great"
            },
            "2": {
                "scenario": "You are Marie Curie, and you are explaining the significance of your discovery of radium to a group of skeptical scientists at a conference. Your goal is to convince them of the importance and potential applications of your discovery.",
                "character": "Marie Curie"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        character = t["character"]
        instructions = f"""Your task is to simulate a dialogue where you play the character {character} in the following historical scenario:

Scenario: {scenario}

Ensure that your dialogue is historically accurate, creatively engaging, and maintains consistency with the character's known personality and context. Your response should include interactions with other characters in the scenario and should be detailed and coherent.

Response format:
1. Dialogue: [Your simulated dialogue]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be historically accurate.",
            "The dialogue should be creatively engaging.",
            "The character portrayal should be consistent with the known personality and context.",
            "The interactions with other characters should be detailed and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
