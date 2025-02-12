class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Space Exploration",
                "constraints": "The game should be playable by 2-4 players, involve resource management, and have a cooperative goal."
            },
            "2": {
                "theme": "Medieval Kingdoms",
                "constraints": "The game should be a strategy game for 3-6 players, involve territory control, and have elements of both luck and skill."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        constraints = t["constraints"]
        instructions = f"""Your task is to design the rules and basic gameplay mechanics for a new game based on the following theme and constraints:

Theme: {theme}

Constraints: {constraints}

Ensure your game design includes:
1. A clear objective or goal for the players.
2. A list of components or pieces required to play the game.
3. A detailed description of the rules and gameplay mechanics.
4. Any special conditions or events that can occur during the game.
5. Instructions on how to win the game.
6. Examples of gameplay scenarios to illustrate the rules.
7. A brief playtesting scenario to demonstrate the balance and fairness of the game.

Provide your game design in plain text format, structured as follows:

1. Objective
2. Components
3. Rules and Gameplay Mechanics
4. Special Conditions
5. Winning Conditions
6. Gameplay Scenarios
7. Playtesting Scenario"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game design should include all required sections: Objective, Components, Rules and Gameplay Mechanics, Special Conditions, Winning Conditions, Gameplay Scenarios, and Playtesting Scenario.",
            "The game should be playable based on the provided rules.",
            "The design should adhere to the given theme and constraints.",
            "The game should be engaging and interesting for the players.",
            "The game should be balanced and fair based on the playtesting scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
