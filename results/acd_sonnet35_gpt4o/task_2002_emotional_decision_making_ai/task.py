import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "dilemma": "Autonomous vehicle accident",
                "context": "An autonomous vehicle must choose between saving its passengers or pedestrians in an unavoidable accident.",
                "emotions": ["fear", "guilt", "responsibility"]
            },
            {
                "dilemma": "Medical resource allocation",
                "context": "A hospital AI must decide how to allocate limited life-saving resources among patients with varying survival probabilities.",
                "emotions": ["compassion", "anxiety", "fairness"]
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human-like emotional processes in decision-making, then apply it to the following ethical dilemma:

Scenario: {t['dilemma']}
Context: {t['context']}
Key emotions to consider: {', '.join(t['emotions'])}

Your response should include the following sections:

1. Emotional-Cognitive Architecture (300-350 words):
   a) Describe the key components of your AI system that enable emotional processing in decision-making.
   b) Explain how your system models and integrates the specified emotions.
   c) Detail the mechanisms that allow for interaction between emotional and rational decision-making processes.
   d) Discuss how your system's emotional processing differs from and/or mimics human emotional decision-making.

2. Ethical Framework Integration (200-250 words):
   a) Explain how your system incorporates ethical principles into its decision-making process.
   b) Describe how emotional factors influence the ethical reasoning of your AI.
   c) Discuss any potential biases or limitations in your system's ethical framework.

3. Scenario Analysis and Decision Process (250-300 words):
   a) Apply your emotional decision-making AI to the given ethical dilemma.
   b) Describe step-by-step how your system would approach and resolve this dilemma.
   c) Explain how the emotional processes contribute to the final decision.
   d) Provide a clear statement of the AI's final decision and its justification.

4. Comparative Analysis (200-250 words):
   a) Compare your AI's decision-making process to a hypothetical purely rational AI approach.
   b) Discuss the potential advantages and disadvantages of incorporating emotional processes in AI decision-making for ethical dilemmas.
   c) Analyze how your AI's decision might differ from typical human decisions in similar scenarios.

5. Ethical Implications and Safeguards (150-200 words):
   a) Discuss the ethical implications of using emotionally-influenced AI for critical decision-making.
   b) Propose safeguards or oversight mechanisms to ensure responsible use of such AI systems.
   c) Consider potential unintended consequences of emotional AI in decision-making roles.

6. Future Research Directions (100-150 words):
   a) Suggest two potential improvements or expansions to your emotional decision-making AI system.
   b) Propose an experiment to further validate or refine your AI's emotional decision-making capabilities.

Ensure your response demonstrates a deep understanding of emotional processes, ethical reasoning, and artificial intelligence. Be creative and innovative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must demonstrate a clear and innovative design for an AI system that integrates emotional processes into decision-making.",
            f"The AI system must appropriately consider and model the specified emotions: {', '.join(t['emotions'])}.",
            f"The scenario analysis must directly address the given ethical dilemma: {t['dilemma']}.",
            "The comparative analysis should provide insightful comparisons between the emotional AI, rational AI, and human decision-making.",
            "The response must thoughtfully address ethical implications and propose relevant safeguards for the use of emotional AI in decision-making."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
