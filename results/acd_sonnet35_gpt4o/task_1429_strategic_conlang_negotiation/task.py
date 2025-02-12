import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "trade negotiation between alien species",
            "peace talks in a fantasy world",
            "resource allocation on a space station",
            "diplomatic crisis in a cyberpunk setting"
        ]
        game_theory_concepts = [
            "Nash equilibrium",
            "Prisoner's dilemma",
            "Pareto efficiency",
            "Bayesian game"
        ]
        
        tasks = {
            "1": {
                "scenario": random.choice(scenarios),
                "game_theory_concept": random.choice(game_theory_concepts)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "game_theory_concept": random.choice(game_theory_concepts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can engage in strategic negotiations using a constructed language (conlang) based on game theory principles, focusing on the scenario of {t['scenario']} and incorporating the game theory concept of {t['game_theory_concept']}. Your response should include the following sections:

1. Conlang Design (250-300 words):
   a) Describe the key features of your constructed language, including its syntax, semantics, and pragmatics.
   b) Explain how the language incorporates game theory principles, especially {t['game_theory_concept']}.
   c) Provide examples of how the language expresses concepts related to negotiation and strategy.
   d) Discuss how the language's structure influences or constrains strategic thinking.

2. AI System Architecture (250-300 words):
   a) Outline the architecture of your AI system, including key components and their functions.
   b) Explain how the system processes and generates the constructed language.
   c) Describe how the system incorporates game theory principles in its decision-making process.
   d) Discuss any novel algorithms or approaches used in your design.

3. Negotiation Scenario Analysis (200-250 words):
   a) Analyze how your AI system would approach the given scenario: {t['scenario']}.
   b) Provide a sample dialogue or interaction demonstrating the system's use of the conlang in this scenario.
   c) Explain how the system's strategy in this scenario relates to {t['game_theory_concept']}.

4. Performance Evaluation (200-250 words):
   a) Propose metrics to evaluate the AI system's performance in strategic negotiations.
   b) Discuss potential strengths and weaknesses of your system compared to traditional negotiation AI.
   c) Analyze how the use of the constructed language might impact negotiation outcomes.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical considerations of using AI systems with specialized languages for strategic negotiations.
   b) Explore potential societal impacts of widespread adoption of such systems.
   c) Propose guidelines for responsible development and use of strategic conlang AI systems.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how these extensions could enhance its capabilities or address limitations.

Ensure your response demonstrates a deep understanding of linguistics, game theory, and AI principles. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed constructed language that incorporates game theory principles, especially {t['game_theory_concept']}",
            "The AI system architecture is clearly described and incorporates both the conlang and game theory principles",
            f"The negotiation scenario analysis for {t['scenario']} is thorough and demonstrates the system's strategic use of the conlang",
            "The performance evaluation includes relevant metrics and a thoughtful comparison to traditional negotiation AI",
            "Ethical and societal implications are thoroughly addressed",
            "The response demonstrates deep understanding of linguistics, game theory, and AI principles",
            "The proposed system is creative and innovative while remaining scientifically and technologically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
