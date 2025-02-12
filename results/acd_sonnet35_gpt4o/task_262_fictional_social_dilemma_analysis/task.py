import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'dilemma_type': 'Resource allocation',
                'societal_context': 'Post-scarcity society',
                'behavioral_bias': 'Status quo bias',
                'bias_explanation': 'The tendency to prefer things to stay the same by doing nothing or by sticking with a decision made previously.'
            },
            {
                'dilemma_type': 'Information sharing',
                'societal_context': 'Highly connected digital world',
                'behavioral_bias': 'Hyperbolic discounting',
                'bias_explanation': 'The tendency for people to increasingly choose a smaller-sooner reward over a larger-later reward as the delay occurs sooner rather than later in time.'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a fictional social dilemma based on the following parameters:

Dilemma Type: {t['dilemma_type']}
Societal Context: {t['societal_context']}
Behavioral Bias: {t['behavioral_bias']}
Bias Explanation: {t['bias_explanation']}

Your task:

1. Dilemma Description (150-200 words):
   a) Create a specific scenario that illustrates the given dilemma type in the provided societal context.
   b) Explain how the behavioral bias influences decision-making in this scenario.
   c) Describe the key stakeholders and their primary motivations.

2. Game Theory Analysis (200-250 words):
   a) Model the dilemma as a game, clearly defining players, strategies, and payoffs.
   b) Identify and explain any Nash equilibria in the game.
   c) Discuss how the behavioral bias might lead to deviations from rational game theory predictions.
   d) Provide a specific example of a decision scenario in this game, showing how players might act with and without the influence of the behavioral bias.

3. Societal Impact (150-200 words):
   a) Analyze potential short-term and long-term consequences of this dilemma on society.
   b) Discuss how this dilemma might evolve over time if left unaddressed.
   c) Explain any feedback loops or cascading effects that could amplify the dilemma's impact.

4. Intervention Design (200-250 words):
   a) Propose an intervention to address the dilemma, considering both policy and technological approaches.
   b) Explain how your intervention accounts for or mitigates the influence of the behavioral bias.
   c) Discuss potential unintended consequences of your intervention and how they might be minimized.

5. Ethical Considerations (100-150 words):
   a) Identify and discuss at least two ethical issues raised by either the dilemma itself or your proposed intervention.
   b) Suggest how these ethical concerns might be balanced against the need to address the dilemma.

Ensure your response demonstrates a deep understanding of game theory principles, behavioral economics, and social dynamics. Use clear headings for each section of your response. Adhere to the word limits for each section to maintain conciseness and focus."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dilemma description is creative, coherent, and accurately incorporates the given parameters.",
            "The game theory analysis demonstrates a strong understanding of game theory principles and their application, including a clear example of decision-making.",
            "The societal impact analysis is insightful and considers complex, long-term effects.",
            "The proposed intervention is innovative and addresses the dilemma and behavioral bias effectively.",
            "The ethical consideration shows nuanced understanding of potential conflicts and trade-offs.",
            "The overall response demonstrates interdisciplinary thinking and deep analysis of complex social dynamics.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
