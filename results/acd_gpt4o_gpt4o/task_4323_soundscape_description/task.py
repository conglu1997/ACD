class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are standing in a bustling city market during the day. The market is crowded with people shopping, vendors shouting, and vehicles passing by."},
            "2": {"scenario": "You are in a dense forest at night. The forest is alive with the sounds of nocturnal animals, rustling leaves, and distant water flowing."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to describe the soundscape of the following scenario. Detail the types of sounds you hear, their sources, and the overall atmosphere. Be as vivid and descriptive as possible.

Scenario: {scenario}

Your response should be structured as follows:
1. Types of Sounds: [List of different sounds]
2. Sources: [Sources of the sounds]
3. Atmosphere: [Description of the overall atmosphere]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a variety of sounds that are contextually appropriate.", "The sources of the sounds should be logical and fit the scenario.", "The description of the atmosphere should be vivid and immersive.", "The response should follow the given structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
