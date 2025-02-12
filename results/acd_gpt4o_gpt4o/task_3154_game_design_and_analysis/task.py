class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": "Design a simple board game for 2-4 players that can be played within 30 minutes. The game should include elements of strategy and chance. Provide the rules, objectives, and a brief description of the game components."},
            "2": {"game": "Tic-Tac-Toe", "question": "Analyze the game 'Tic-Tac-Toe' and identify its core mechanics, player experience, and design choices. Provide your analysis in plain text format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "parameters" in t:
            instructions = f"""Your task is to design a simple game based on the following parameters:

Parameters: {t['parameters']}

Ensure that the game design includes clear rules, objectives, and a brief description of the game components. The game should be engaging and balanced for 2-4 players and should be playable within 30 minutes. Provide your response in plain text format with the following structure:

1. Game Title
2. Objective
3. Rules
4. Components
5. Brief Description of Gameplay"""
        else:
            instructions = f"""Your task is to analyze the following game and identify its core mechanics, player experience, and design choices:

Game: {t['game']}

Question: {t['question']}

Your analysis should be clear, detailed, and cover aspects such as core mechanics, player experience, and design choices. Provide your analysis in plain text format with the following structure:

1. Core Mechanics
2. Player Experience
3. Design Choices"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "parameters" in t:
            criteria = [
                "The game design should include clear rules, objectives, and a description of the game components.",
                "The game should be engaging and balanced for 2-4 players.",
                "The game should be playable within 30 minutes.",
                "The response should follow the specified structure."]
        else:
            criteria = [
                "The analysis should cover core mechanics, player experience, and design choices.",
                "The analysis should be clear, detailed, and accurate.",
                "The response should follow the specified structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
