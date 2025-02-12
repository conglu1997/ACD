import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                'domain': 'Environmental conservation',
                'target_behavior': 'Reducing personal carbon footprint',
                'user_demographic': 'Urban millennials'
            },
            {
                'domain': 'Personal finance',
                'target_behavior': 'Increasing savings rate',
                'user_demographic': 'Young professionals'
            }
        ]
        return {str(i+1): task for i, task in enumerate(domains)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an adaptive gamification system that uses principles from game theory and behavioral economics to optimize user engagement and behavior change in the domain of {t['domain']}. Your system should focus on the target behavior of {t['target_behavior']} for the user demographic of {t['user_demographic']}. Your response should include:

1. System Overview (200-250 words):
   a) Describe the key components of your adaptive gamification system.
   b) Explain how your system incorporates principles from game theory and behavioral economics.
   c) Discuss how your system adapts to individual users and changing circumstances.

2. Game Mechanics and Incentives (200-250 words):
   a) Detail the specific game mechanics you would implement (e.g., points, levels, challenges).
   b) Explain how these mechanics align with the target behavior and user demographic.
   c) Describe the reward structure and how it promotes long-term engagement.

3. Behavioral Model (150-200 words):
   a) Outline a model of user behavior that your system uses to make predictions and adaptations.
   b) Explain how this model incorporates insights from behavioral economics.
   c) Discuss how your system handles different user types or personas.

4. Adaptive Algorithms (200-250 words):
   a) Describe the algorithms your system uses to adapt to user behavior and preferences.
   b) Explain how these algorithms optimize for both short-term engagement and long-term behavior change.
   c) Discuss how your system balances exploration (trying new strategies) and exploitation (using known effective strategies).

5. Ethics and Privacy Considerations (150-200 words):
   a) Identify potential ethical concerns related to your gamification system.
   b) Explain how your system addresses issues of privacy and data protection.
   c) Discuss how you would ensure the system promotes genuine behavior change rather than manipulation.

6. Evaluation and Metrics (150-200 words):
   a) Propose a method to evaluate the effectiveness of your gamification system.
   b) Describe key performance indicators (KPIs) you would use to measure success.
   c) Explain how you would conduct A/B testing or other experiments to refine the system.

7. Real-world Application (200-250 words):
   a) Provide a specific example of how your system would work in practice for the given domain and target behavior.
   b) Walk through a user's journey, highlighting key interactions and adaptations.
   c) Discuss potential challenges in implementing your system and how you would address them.

Ensure your response demonstrates a deep understanding of game theory, behavioral economics, and adaptive system design. Be creative in your approach while maintaining scientific and practical plausibility. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of game theory, behavioral economics, and adaptive system design.",
            "The gamification system is creative, well-designed, and appropriate for the given domain and target behavior.",
            "The system effectively incorporates principles from game theory and behavioral economics.",
            "The adaptive algorithms and behavioral model are well-explained and scientifically plausible.",
            "Ethical considerations and privacy concerns are thoroughly addressed.",
            "The evaluation method and metrics are appropriate and well-thought-out.",
            "The real-world application example is detailed and illustrates the system's functionality clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
