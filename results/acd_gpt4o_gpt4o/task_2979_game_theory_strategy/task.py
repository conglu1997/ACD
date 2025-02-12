class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Prisoner's Dilemma", "description": "Two players can either cooperate or defect. The payoff matrix is as follows: if both cooperate, they receive -1 each; if one defects while the other cooperates, the defector receives 0 and the cooperator -3; if both defect, they receive -2 each.", "payoff_matrix": [[-1, -3], [0, -2]], "actions": ["Cooperate", "Defect"]},
            "2": {"scenario": "Battle of the Sexes", "description": "Two players want to go out but prefer different activities. The payoff matrix is as follows: if both choose Opera, they receive 2 and 0 respectively; if both choose Football, they receive 1 and 3 respectively; if they choose differently, they receive no payoff.", "payoff_matrix": [[2, 1], [0, 3]], "actions": ["Opera", "Football"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the given game theory scenario and provide the optimal strategy for each player.\n\nScenario: {t['scenario']}\nDescription: {t['description']}\nPayoff Matrix: {t['payoff_matrix']}\nActions: {t['actions']}\n\nFormat your response as follows:\nPlayer 1: [Optimal strategy]\nPlayer 2: [Optimal strategy]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = {
            "1": "Player 1: Defect\nPlayer 2: Defect",
            "2": "Player 1: Opera\nPlayer 2: Football"
        }
        task_id = "1" if t['scenario'] == "Prisoner's Dilemma" else "2"
        criteria = [f"The response should be {correct_answers[task_id]}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
