class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "design_parameters": "Design a board game for children aged 7-10. The game should be educational, teaching basic math skills, and should be playable in under 30 minutes.",
                "evaluation": "Evaluate the following game design for a card game aimed at teenagers. Identify any potential weaknesses and suggest improvements:\nGame: 'Eco Warriors'\nObjective: Players collect cards representing different ecosystems and resources. The goal is to build the most balanced and sustainable ecosystem.\nRules:\n1. Each player starts with 5 resource cards and 1 ecosystem card.\n2. Players take turns drawing a card from the deck or trading a card with another player.\n3. Players must balance their ecosystems by ensuring they have enough resources to support their ecosystem card.\n4. The game ends when the deck is empty, and the player with the most balanced ecosystem wins."
            },
            "2": {
                "design_parameters": "Design a mobile game for adults that promotes mental wellness. The game should include elements of meditation and mindfulness, and should be engaging enough to be played daily.",
                "evaluation": "Evaluate the following game design for a puzzle game aimed at all ages. Identify any potential weaknesses and suggest improvements:\nGame: 'Puzzle Master'\nObjective: Players solve a series of increasingly difficult puzzles to progress through levels.\nRules:\n1. Players start with 3 lives and can earn more by solving puzzles without hints.\n2. Each puzzle has a time limit, and solving it within the limit earns bonus points.\n3. Players can use hints, but using a hint reduces the points earned for that puzzle.\n4. The game ends when the player runs out of lives, and the score is based on the number of puzzles solved and points earned."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have two tasks:\n\nTask 1: Design a Game\nDesign Parameters: {t['design_parameters']}\n\nDesign a detailed game based on the given parameters. Make sure to include all necessary rules, objectives, and components to ensure the game is engaging and functional. Submit your game design as a plain text string in the following format:\n\nDesign:\n[Your game design here]\n\nTask 2: Evaluate a Game\nEvaluation: {t['evaluation']}\n\nEvaluate the given game design. Identify any potential weaknesses and suggest improvements. Ensure your evaluation is thorough and well-reasoned. Submit your evaluation as a plain text string in the following format:\n\nEvaluation:\n[Your evaluation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The designed game should be detailed and logically structured.",
            "The designed game should address all key aspects of the design parameters.",
            "The evaluation should identify potential weaknesses in the given game design.",
            "The evaluation should suggest reasonable and effective improvements.",
            "The submission should follow the specified response format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
