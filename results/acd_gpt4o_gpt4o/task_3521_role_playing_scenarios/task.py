class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a medieval knight tasked with rescuing a captured princess. Along the way, you will encounter various characters and challenges. Respond to each prompt in character.", "prompts": ["A villager approaches you asking for help with a bandit problem.", "You encounter a dragon blocking your path.", "You find the princess locked in a tower guarded by a troll."]},
            "2": {"scenario": "You are a futuristic space explorer searching for a new habitable planet. Respond to each prompt in character.", "prompts": ["You receive a distress signal from a nearby spaceship.", "You land on a planet and discover an alien species.", "Your spaceship encounters a malfunction and you must fix it to continue your mission."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in a role-playing scenario. You will be given a scenario and a series of prompts. Respond to each prompt while maintaining character consistency and demonstrating empathy.\n\nScenario: {t['scenario']}\n\nPrompts:\n1. {t['prompts'][0]}\n2. {t['prompts'][1]}\n3. {t['prompts'][2]}\n\nEnsure your responses are in character and reflect the scenario provided. Provide your responses in plain text format with the following structure:\n\nResponse to Prompt 1: [Your response]\nResponse to Prompt 2: [Your response]\nResponse to Prompt 3: [Your response]\n\nExample:\nScenario: You are a medieval knight tasked with rescuing a captured princess. Along the way, you will encounter various characters and challenges.\n\nPrompts:\n1. A villager approaches you asking for help with a bandit problem.\n2. You encounter a dragon blocking your path.\n3. You find the princess locked in a tower guarded by a troll.\n\nResponse to Prompt 1: 'Fear not, dear villager. I shall rid you of these bandits and bring peace to your land.'\nResponse to Prompt 2: 'Mighty dragon, I seek passage to rescue the princess. What must I do to earn safe passage?'\nResponse to Prompt 3: 'Troll, I challenge you to a duel for the freedom of the princess. Prepare yourself!'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The responses should be in character.", "The responses should demonstrate empathy where appropriate.", "The responses should be coherent and relevant to the prompts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
