import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'environmental_issue': 'water conservation',
                'psychological_principle': 'social proof',
                'target_population': 'urban households'
            },
            {
                'environmental_issue': 'energy efficiency',
                'psychological_principle': 'loss aversion',
                'target_population': 'small businesses'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses environmental data and psychological principles to subtly influence human behavior towards more sustainable practices, focusing on {t['environmental_issue']} and utilizing the psychological principle of {t['psychological_principle']}. Your target population is {t['target_population']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system.
   b) Explain how it collects and processes environmental data.
   c) Detail how it incorporates the specified psychological principle.
   d) Discuss how the system interfaces with the target population.

2. Data Analysis and Behavior Prediction (200-250 words):
   a) Explain what types of data your system uses to understand current behaviors.
   b) Describe how it identifies opportunities for behavior modification.
   c) Detail the AI algorithms or models used for behavior prediction.

3. Intervention Design (200-250 words):
   a) Explain how your system designs interventions based on the psychological principle.
   b) Provide examples of specific interventions for the given environmental issue.
   c) Discuss how the system personalizes interventions for individuals or groups.

4. Impact Assessment (200-250 words):
   a) Describe how your system measures the effectiveness of its interventions.
   b) Explain how it adapts its strategies based on observed outcomes.
   c) Estimate the potential environmental impact if widely adopted.

5. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of using AI to influence human behavior.
   b) Address concerns about privacy, autonomy, and manipulation.
   c) Propose guidelines for responsible development and use of such systems.

6. Challenges and Future Directions (150-200 words):
   a) Identify potential technical or social challenges in implementing your system.
   b) Suggest areas for future research or improvement.
   c) Discuss how this technology could evolve to address other environmental issues.

Ensure your response demonstrates a deep understanding of environmental science, artificial intelligence, and social psychology. Be innovative in your approach while maintaining scientific and ethical plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a strong understanding of the specified environmental issue, psychological principle, and target population.",
            "The AI system design is innovative, plausible, and well-explained.",
            "The approach effectively integrates environmental science, AI, and social psychology concepts.",
            "The ethical considerations are thoughtfully explored and addressed.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
