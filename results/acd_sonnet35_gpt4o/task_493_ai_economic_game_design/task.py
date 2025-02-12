import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        economic_concepts = [
            {
                "concept": "tragedy of the commons",
                "description": "A situation where individual users, acting independently according to their own self-interest, behave contrary to the common good of all users by depleting or spoiling a shared resource."
            },
            {
                "concept": "prisoner's dilemma",
                "description": "A paradox in decision analysis where two individuals acting in their own self-interests do not produce the optimal outcome."
            },
            {
                "concept": "network effects",
                "description": "The phenomenon where the value of a product or service increases as the number of users or participants grows."
            },
            {
                "concept": "moral hazard",
                "description": "A situation where an individual has an incentive to increase their exposure to risk because they do not bear the full costs of that risk."
            }
        ]
        return {
            "1": random.choice(economic_concepts),
            "2": random.choice(economic_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered economic game that models complex societal interactions based on the concept of {t['concept']}. Your task is to create a game that incorporates AI agents and human players to explore this economic principle in a novel way.

Brief explanation of the economic concept: {t['description']}

Your response should include:

1. Game Design (250-300 words):
   a) Describe the basic structure and rules of your game.
   b) Explain how the game incorporates the given economic concept.
   c) Detail the roles and interactions between AI agents and human players.
   d) Discuss how the game simulates real-world economic behaviors and decisions.

2. AI Implementation (200-250 words):
   a) Outline the AI system powering the game (e.g., machine learning algorithms, decision-making processes).
   b) Explain how the AI adapts to player behavior and game dynamics.
   c) Discuss any ethical considerations in the AI's design and implementation.

3. Economic Analysis (200-250 words):
   a) Analyze how your game might predict or model real-world economic phenomena.
   b) Discuss potential insights that could be gained from large-scale play of your game.
   c) Explain how the game could be used as a tool for economic research or policy-making.

4. Societal Impact (150-200 words):
   a) Discuss potential positive and negative impacts of widespread adoption of your game.
   b) Analyze how the game might influence people's understanding of economics and decision-making.
   c) Propose safeguards to prevent misuse or unintended consequences of the game.

5. Future Developments (100-150 words):
   a) Suggest two potential expansions or modifications to your game.
   b) Briefly describe how these changes would enhance its educational or predictive value.

Ensure your response demonstrates a deep understanding of game theory, behavioral economics, and artificial intelligence. Be creative in your game design while maintaining scientific and economic plausibility. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed game that clearly incorporates the given economic concept.",
            "The game design effectively integrates AI agents and human players in a novel and interesting way.",
            "The AI implementation is described in sufficient detail and addresses ethical considerations.",
            "The economic analysis demonstrates a strong understanding of how the game relates to real-world phenomena.",
            "The discussion of societal impact is thoughtful and considers both positive and negative consequences.",
            "The proposed future developments are creative and would enhance the game's value.",
            "The response demonstrates a deep understanding of game theory, behavioral economics, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
