class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "You are on a game show and there are three doors. Behind one of the doors is a car; behind the other two, goats. You pick a door, say Door A. The host, who knows what's behind the doors, opens another door, say Door B, which has a goat. You are then given the choice to either stick with your original pick or switch to the remaining unopened door. What should you do to maximize your chances of winning the car? Explain your reasoning.",
                "solution": "You should switch to the remaining unopened door. Initially, the probability of picking the car is 1/3, and the probability of picking a goat is 2/3. When the host opens a door with a goat, the probability of the car being behind the other unopened door is 2/3, while the probability of the car being behind your initially chosen door remains 1/3. Hence, switching increases your chance of winning to 2/3."
            },
            "2": {
                "problem": "You have two envelopes, one containing twice the amount of money as the other. You pick one envelope at random and see $100 inside. You are then given the option to switch envelopes. Should you switch or stick with your initial choice? Explain your reasoning.",
                "solution": "You should switch. Initially, there is an equal probability that the envelope contains $100 or $200. If you switch, your expected value is calculated as follows: there's a 50% chance the other envelope contains $200 (double) and a 50% chance it contains $50 (half). Thus, the expected value of switching is (0.5 * $200) + (0.5 * $50) = $125, which is greater than the $100 you have. Hence, switching increases your expected value."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following logical puzzle and explain your reasoning:\n\nProblem: {t['problem']}\n\nYour response should include:\n1. Your solution (whether you should stick or switch).\n2. A detailed explanation of your reasoning, including relevant probabilities or expected values.\n\nProvide your response in the following format:\nSolution: [Your solution]\nExplanation: [Your explanation]\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly identify whether to stick or switch.",
            "The explanation should clearly and logically justify the decision using probabilistic reasoning.",
            "The explanation should mention relevant probabilities or expected values."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
