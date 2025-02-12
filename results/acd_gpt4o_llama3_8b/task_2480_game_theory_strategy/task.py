class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the following game theory scenario and determine the optimal strategies for both players:\nScenario: The Prisoner's Dilemma\nPlayer A and Player B have been arrested for a crime. They are interrogated separately and cannot communicate with each other. Each player has two options: to Cooperate (C) with the other by staying silent or to Defect (D) by betraying the other. The outcomes are as follows:\n- If both players cooperate, they each receive a 2-year sentence.\n- If one player defects and the other cooperates, the defector goes free while the cooperator receives a 5-year sentence.\n- If both players defect, they each receive a 4-year sentence.\nDetermine the optimal strategies for both players and explain your reasoning by including relevant game theory concepts such as Nash equilibrium and dominant strategies. Define each concept clearly and explain how it applies to this scenario."},
            "2": {"prompt": "Analyze the following game theory scenario and determine the optimal strategies for both players:\nScenario: The Battle of the Sexes\nPlayer A and Player B want to go out together, but they have different preferences. Player A prefers to go to the Opera (O), while Player B prefers to go to the Football game (F). They can either choose to go to the Opera or the Football game. The outcomes are as follows:\n- If both players choose the Opera, Player A is very happy (3 points) and Player B is moderately happy (2 points).\n- If both players choose the Football game, Player A is moderately happy (2 points) and Player B is very happy (3 points).\n- If they choose different activities, neither is happy (0 points each).\nDetermine the optimal strategies for both players and explain your reasoning by including relevant game theory concepts such as Nash equilibrium and coordination games. Define each concept clearly and explain how it applies to this scenario."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nYour response should include:\n1. The optimal strategies for both players.\n2. A detailed explanation of your reasoning, including definitions and applications of relevant game theory concepts such as Nash equilibrium, dominant strategies, and coordination games.\n\nSubmit your response as a plain text string in the following format:\n\nOptimal Strategies: [Your strategies here]\nReasoning: [Your detailed explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include the optimal strategies for both players.", "The reasoning should be detailed and include definitions and applications of relevant game theory concepts such as Nash equilibrium, dominant strategies, and coordination games."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
