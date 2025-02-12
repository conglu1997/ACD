import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "negotiation_context": "International climate change treaty",
                "number_of_parties": 3,
                "linguistic_constraint": "Use of diplomatic language and euphemisms",
                "game_theory_concept": "Nash equilibrium"
            },
            {
                "negotiation_context": "Corporate merger",
                "number_of_parties": 2,
                "linguistic_constraint": "Technical financial jargon",
                "game_theory_concept": "Prisoner's dilemma"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of engaging in complex linguistic negotiations while applying game theory principles. Then, analyze its performance in a specific negotiation scenario. Your task involves:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI negotiation system.
   b) Explain how your system integrates natural language processing with game theory principles.
   c) Detail how your system models and reasons about multiple negotiating parties.
   d) Discuss any novel algorithms or techniques used in your design.

2. Linguistic-Strategic Integration (200-250 words):
   a) Explain how your system analyzes and generates language appropriate for the {t['negotiation_context']} scenario.
   b) Describe how it incorporates the linguistic constraint: {t['linguistic_constraint']}.
   c) Detail how your system translates linguistic inputs into game-theoretic models and vice versa.

3. Game Theory Implementation (200-250 words):
   a) Explain how your system applies the game theory concept of {t['game_theory_concept']} in the negotiation process.
   b) Describe how it models and predicts the strategies of {t['number_of_parties']} negotiating parties.
   c) Discuss how your system balances short-term gains with long-term strategic considerations.

4. Negotiation Simulation (250-300 words):
   a) Provide a step-by-step walkthrough of how your AI system would handle a specific round of negotiation in the given scenario.
   b) Include example dialogues or decisions made by the AI, demonstrating its linguistic and strategic capabilities.
   c) Explain how the system's actions reflect both its linguistic constraints and game-theoretic reasoning.

5. Performance Analysis (200-250 words):
   a) Analyze the strengths and weaknesses of your AI system's performance in the negotiation scenario.
   b) Discuss how well it balances linguistic appropriateness with strategic optimization.
   c) Compare its expected performance to that of human negotiators or traditional non-AI negotiation systems.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues arising from the use of AI in high-stakes negotiations.
   b) Address any limitations or potential biases in your system's approach.
   c) Propose guidelines for responsible development and use of game-theoretic linguistic AI negotiators.

Ensure your response demonstrates a deep understanding of linguistics, game theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, game theory, and artificial intelligence",
            "The system architecture effectively integrates natural language processing with game theory principles",
            f"The design incorporates the specified linguistic constraint: {t['linguistic_constraint']}",
            f"The system correctly applies the game theory concept of {t['game_theory_concept']}",
            f"The negotiation simulation effectively demonstrates the system's capabilities in the {t['negotiation_context']} scenario",
            "The performance analysis critically evaluates the system's strengths and weaknesses",
            "Ethical considerations and limitations are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
