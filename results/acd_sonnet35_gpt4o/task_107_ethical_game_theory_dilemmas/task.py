import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'title': 'The Ethical Prisoner\'s Dilemma',
                'context': 'Two suspects are being interrogated separately. If both remain silent, they each serve 1 year. If one betrays the other, the betrayer goes free and the silent one serves 3 years. If both betray, each serves 2 years. However, the crime they\'re accused of was committed to save a life.',
                'payoff_matrix': {
                    'Silent': {'Silent': (-1, -1), 'Betray': (-3, 0)},
                    'Betray': {'Silent': (0, -3), 'Betray': (-2, -2)}
                },
                'ethical_factor': 'The crime was committed for a noble cause.'
            },
            {
                'title': 'The Corporate Social Responsibility Game',
                'context': 'Two competing companies must decide whether to invest in expensive eco-friendly practices. If both invest, they each gain moderate profit and positive public image. If one invests and the other doesn\'t, the investor loses money while the other gains high profit but risks public backlash. If neither invests, both maintain current profits but risk future regulations.',
                'payoff_matrix': {
                    'Invest': {'Invest': (2, 2), 'Not Invest': (-1, 3)},
                    'Not Invest': {'Invest': (3, -1), 'Not Invest': (1, 1)}
                },
                'ethical_factor': 'Environmental impact and long-term sustainability.'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following game theory scenario with ethical implications:

Title: {t['title']}

Context: {t['context']}

Payoff Matrix:
{t['payoff_matrix']}

Ethical Factor: {t['ethical_factor']}

Your task:

1. Game Theory Analysis (100-150 words):
   Analyze the scenario using game theory principles. Identify the Nash equilibrium (if any) and explain the strategic considerations for each player.

2. Ethical Considerations (100-150 words):
   Discuss the ethical implications of the scenario. How does the ethical factor complicate the decision-making process?

3. Proposed Strategy (100-150 words):
   Propose and justify an optimal strategy that balances game-theoretic and ethical considerations. Explain why this strategy is superior to alternatives.

4. Real-world Application (50-100 words):
   Briefly describe a real-world situation that mirrors this game theory scenario. How might your analysis and proposed strategy apply in practice?

5. Potential Criticisms (50-100 words):
   Identify potential criticisms or limitations of your proposed strategy. How might different ethical frameworks or cultural perspectives challenge your approach?

Ensure your response demonstrates a deep understanding of both game theory and ethical reasoning. Use clear, concise language and provide well-structured arguments for your analysis and recommendations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately applies game theory principles to analyze the scenario.",
            "The ethical implications are thoroughly discussed and well-integrated into the analysis.",
            "The proposed strategy effectively balances game-theoretic and ethical considerations.",
            "The real-world application is relevant and insightful.",
            "Potential criticisms are thoughtfully identified and addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
