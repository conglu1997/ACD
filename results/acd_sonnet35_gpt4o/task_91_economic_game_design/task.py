import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "climate change mitigation",
            "wealth inequality",
            "healthcare resource allocation",
            "education funding",
            "urban transportation",
            "renewable energy adoption",
            "water scarcity management",
            "cybersecurity investment"
        ]
        return {
            "1": {"scenario": random.choice(scenarios)},
            "2": {"scenario": random.choice(scenarios)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel economic game that models the real-world scenario of {t['scenario']}. Your task is to:

1. Create a game with at least three players or groups, each with distinct roles and objectives. Describe the players and their goals (2-3 sentences).

2. Define the rules of the game, including:
   a) The actions available to each player
   b) The payoff structure or scoring system
   c) Any constraints or limitations on player actions
   Explain these rules clearly and concisely (4-5 sentences).

3. Provide a specific example of how one round or interaction in the game would play out, illustrating the dynamics between players (2-3 sentences).

4. Analyze the game's equilibrium or likely outcome if all players act rationally. Discuss any potential inefficiencies or suboptimal outcomes (3-4 sentences). Briefly explain any game theory concepts you use in your analysis (1-2 sentences).

5. Propose two policy interventions that could improve the outcome of the game. For each intervention:
   a) Describe the intervention (1-2 sentences)
   b) Explain how it would change the game dynamics (1-2 sentences)
   c) Predict its impact on the equilibrium or outcome (1-2 sentences)
   d) Discuss potential unintended consequences (1-2 sentences)

6. Discuss how your game and proposed interventions relate to real-world approaches to {t['scenario']} (3-4 sentences).

7. Identify one potential limitation or criticism of your game design and suggest how it might be addressed in future iterations (2-3 sentences).

Ensure your game is original, well-defined, and clearly relates to the given scenario. Use economic and game theory concepts accurately, but explain them in a way that a non-expert could understand. Organize your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The game must model the scenario of {t['scenario']}.",
            "The game must involve at least three players or groups with distinct roles and objectives.",
            "The rules of the game, including actions and payoffs, must be clearly defined.",
            "A specific example of game play must be provided.",
            "The response must include an analysis of the game's equilibrium or likely outcome, with brief explanations of any game theory concepts used.",
            "Two policy interventions must be proposed and analyzed, including potential unintended consequences.",
            "The response must discuss how the game relates to real-world approaches to the scenario.",
            "A potential limitation of the game design must be identified and addressed.",
            "The response must be organized with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
