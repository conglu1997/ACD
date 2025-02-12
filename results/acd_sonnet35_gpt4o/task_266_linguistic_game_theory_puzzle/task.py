import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "game_type": "Morphological Prisoner's Dilemma",
                "linguistic_feature": "verb conjugation",
                "payoff_structure": "cooperate: +3, defect: +5/-1"
            },
            {
                "game_type": "Syntactic Auction",
                "linguistic_feature": "word order",
                "payoff_structure": "highest unique bid wins"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language-based game called '{t['game_type']}' that incorporates elements of game theory and computational linguistics. Your task has the following parts:

1. Game Design (200-250 words):
   a) Describe the rules of the game, focusing on how it incorporates the linguistic feature of {t['linguistic_feature']}.
   b) Explain how the game relates to the game theory concept implied by its name.
   c) Detail the payoff structure: {t['payoff_structure']}.
   d) Describe how players make moves or decisions in the game.

2. Linguistic Analysis (150-200 words):
   a) Explain how the game highlights or manipulates the chosen linguistic feature.
   b) Discuss how this game might reveal insights about language structure or use.

3. Strategy Analysis (150-200 words):
   a) Describe an optimal strategy for playing this game.
   b) Explain how this strategy balances linguistic and game-theoretic considerations.

4. AI Implications (100-150 words):
   a) Discuss how an AI might approach playing this game.
   b) Identify potential challenges an AI might face in mastering this game.

5. Sample Game (100-150 words):
   Provide a brief example of how a round of this game might play out between two players.

Ensure your game design is creative, linguistically sound, and incorporates game theory principles effectively. Demonstrate a deep understanding of both linguistic structures and strategic thinking throughout your answer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game design effectively incorporates the specified linguistic feature and game theory concept.",
            "The linguistic analysis demonstrates a deep understanding of the chosen feature and its role in the game.",
            "The strategy analysis shows a clear grasp of both linguistic and game-theoretic considerations.",
            "The discussion of AI implications is insightful and identifies relevant challenges.",
            "The sample game round is coherent and illustrates the game mechanics clearly.",
            "The overall response is creative, well-structured, and demonstrates strong interdisciplinary reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
