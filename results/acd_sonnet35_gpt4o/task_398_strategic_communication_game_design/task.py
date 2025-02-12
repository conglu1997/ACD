import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "Political Debate",
                "communication_goal": "Persuade undecided voters",
                "constraint": "Limited time for responses"
            },
            {
                "context": "Corporate Negotiation",
                "communication_goal": "Secure a favorable deal",
                "constraint": "Incomplete information about the other party"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical communication game set in the context of a {t['context']}. The primary communication goal is to {t['communication_goal']}, with the constraint of {t['constraint']}. Your task has the following parts:

1. Game Design (250-300 words):
   a) Describe the basic structure and rules of your communication game.
   b) Explain how the game incorporates elements of game theory, social psychology, and linguistics.
   c) Detail how the game reflects the given context, communication goal, and constraint.
   d) Describe the winning condition(s) and how players' success is measured.

2. Strategic Analysis (200-250 words):
   a) Identify at least three key strategies that players might employ in your game.
   b) Analyze the potential effectiveness of each strategy, considering the game's context and constraints.
   c) Discuss how these strategies relate to real-world communication tactics in the given context.

3. Linguistic Components (200-250 words):
   a) Explain how language and communication are specifically utilized in your game.
   b) Describe any unique linguistic features or mechanics in your game (e.g., restricted vocabulary, time limits, turn-taking rules).
   c) Discuss how these linguistic elements interact with the strategic aspects of the game.

4. Psychological Factors (150-200 words):
   a) Identify at least two psychological principles or cognitive biases that players might exploit in your game.
   b) Explain how these psychological factors might influence player behavior and game outcomes.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of your game, particularly in relation to real-world applications.
   b) Propose one modification to your game that could address an ethical concern while maintaining its core mechanics.

6. Learning Outcomes (100-150 words):
   a) Describe what players might learn about effective communication from playing your game.
   b) Explain how insights from your game could be applied to improve communication in the real-world context it simulates.

Ensure your response demonstrates a deep understanding of game theory, social psychology, linguistics, and their intersections. Be creative in your game design while maintaining logical consistency and relevance to the given context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of game theory, social psychology, and linguistics.",
            "The game design is creative, coherent, and effectively incorporates the given context, goal, and constraint.",
            "The strategic analysis is insightful and relates well to real-world communication tactics.",
            "The linguistic components of the game are well-thought-out and integrated with the strategic elements.",
            "The discussion of psychological factors and ethical considerations shows depth of understanding.",
            "The proposed learning outcomes are meaningful and applicable to real-world communication scenarios."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
