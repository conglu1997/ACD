class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"setting": "A spaceship on a mission to Mars.", "characters": ["Captain Jones", "Engineer Smith"], "scenario": "Engineer Smith discovers a critical issue with the spaceship's navigation system that could jeopardize the mission."},
            "2": {"setting": "A medieval village during a festival.", "characters": ["Blacksmith Henry", "Traveler Aria"], "scenario": "Traveler Aria arrives at Blacksmith Henry's forge, seeking help with a broken sword she needs for a tournament."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        setting = t["setting"]
        characters = t["characters"]
        scenario = t["scenario"]
        return f"""Generate a coherent and engaging fictional dialogue based on the following prompt. Ensure the dialogue is creative, logically consistent, and captures the personalities of the characters involved.

Setting: {setting}
Characters: {', '.join(characters)}
Scenario: {scenario}

Submit your dialogue as a plain text string in the following format:

Dialogue:
[Your dialogue here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue must be coherent and logically consistent.",
            "The characters' personalities must be distinct and well-developed.",
            "The dialogue must be creative and engaging.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
