class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "board game", "elements": ["game mechanics", "rules", "narrative"], "setting": "medieval fantasy"},
            "2": {"type": "video game", "elements": ["game mechanics", "rules", "narrative"], "setting": "sci-fi space exploration"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        game_type = t["type"]
        elements = ", ".join(t["elements"])
        setting = t["setting"]
        instructions = f"""Your task is to design a new {game_type}. Ensure that you include the following elements: {elements}. The game's setting should be {setting}.\n\nProvide detailed descriptions of the game mechanics and rules. The narrative should be engaging and coherent, fitting well within the specified setting. Format your response as follows:\n\nGame Mechanics:\n[Your detailed game mechanics]\n\nRules:\n[Your detailed rules]\n\nNarrative:\n[Your brief narrative]\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game mechanics should be detailed and logically coherent.",
            "The rules should be clear and easy to follow.",
            "The narrative should be engaging and fit well within the specified setting.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
