import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "pronoun usage",
            "verb tense system",
            "word order",
            "case marking",
            "honorifics"
        ]
        historical_periods = [
            "Ancient (before 500 CE)",
            "Medieval (500-1500 CE)",
            "Early Modern (1500-1800 CE)",
            "Modern (1800-present)"
        ]
        communication_problems = [
            "cross-generational misunderstandings",
            "international business negotiations",
            "AI language model biases",
            "social media discourse",
            "political rhetoric interpretation"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "historical_periods": random.sample(historical_periods, 3),
                "communication_problem": random.choice(communication_problems)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "historical_periods": random.sample(historical_periods, 3),
                "communication_problem": random.choice(communication_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the evolution of {t['linguistic_feature']} across the following historical periods: {', '.join(t['historical_periods'])}. Then, apply this knowledge to address the modern communication problem of {t['communication_problem']}. Your response should include:

1. Historical Analysis (300-350 words):
   a) Describe how {t['linguistic_feature']} changed across the specified historical periods.
   b) Explain the social, cultural, or technological factors that influenced these changes.
   c) Provide specific examples of the feature's usage in each period.

2. Linguistic Evolution Patterns (200-250 words):
   a) Identify at least two significant patterns or trends in the evolution of {t['linguistic_feature']}.
   b) Discuss any linguistic theories that explain these patterns.
   c) Predict how this feature might continue to evolve in the future.

3. Modern Problem Application (250-300 words):
   a) Explain how your analysis of {t['linguistic_feature']} evolution relates to {t['communication_problem']}.
   b) Propose an innovative solution to this problem, drawing directly from your historical analysis.
   c) Describe how your solution would be implemented, providing specific examples.
   d) Present a detailed case study or hypothetical scenario demonstrating your solution in action.

4. Comparative Analysis (200-250 words):
   a) Identify at least two existing approaches or solutions to {t['communication_problem']}.
   b) Compare and contrast your proposed solution with these existing approaches.
   c) Discuss the potential advantages and limitations of your solution in this context.

5. Unintended Consequences (150-200 words):
   a) Identify at least two potential unintended consequences of implementing your proposed solution.
   b) Explain how these consequences might arise and their potential impact on language use or society.
   c) Propose strategies to mitigate these unintended consequences.

6. Potential Challenges and Mitigation (150-200 words):
   a) Identify at least two potential challenges in applying historical linguistic knowledge to {t['communication_problem']}.
   b) Propose strategies to overcome these challenges.

7. Broader Implications (150-200 words):
   a) Discuss how this approach of using diachronic linguistic analysis could be applied to other communication problems.
   b) Explore potential impacts on fields such as education, technology, or international relations.

Ensure your response demonstrates a deep understanding of linguistic change, historical context, and creative problem-solving. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining logical consistency and plausibility.

Format your response with clear headings for each section and subsections where appropriate. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a thorough understanding of how {t['linguistic_feature']} evolved across the specified historical periods.",
            f"The solution proposed for {t['communication_problem']} is innovative and clearly draws from the historical linguistic analysis.",
            "The response includes a detailed case study or scenario demonstrating the proposed solution.",
            "The comparative analysis effectively contrasts the proposed solution with existing approaches.",
            "The response identifies and analyzes potential unintended consequences of the proposed solution.",
            "The response shows a deep understanding of linguistic change and its application to modern problems.",
            "The analysis, proposed solution, and consideration of unintended consequences are logically consistent and plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
