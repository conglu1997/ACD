import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Predictive Processing Theory",
            "Orchestrated Objective Reduction Theory"
        ]
        cognitive_phenomena = [
            "Subjective experience of color",
            "The sense of self",
            "Decision-making under uncertainty",
            "The experience of time",
            "Emergence of creative insights"
        ]
        return {
            "1": {
                "theory": random.choice(consciousness_theories),
                "phenomenon": random.choice(cognitive_phenomena)
            },
            "2": {
                "theory": random.choice(consciousness_theories),
                "phenomenon": random.choice(cognitive_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model of consciousness based on {t['theory']}, and use it to analyze the cognitive phenomenon of {t['phenomenon']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of {t['theory']} and how they relate to consciousness.
   b) Describe how you will translate these principles into a computational model.
   c) Discuss any assumptions or simplifications you need to make in your model.

2. Computational Model Design (300-350 words):
   a) Outline the architecture of your computational model, including its main components and their interactions.
   b) Explain how your model implements the key aspects of {t['theory']}.
   c) Describe the data structures and algorithms you would use to represent and process information in your model.
   d) Discuss how your model accounts for the emergence of conscious experience.

3. Analysis of {t['phenomenon']} (250-300 words):
   a) Explain how your computational model would simulate or represent {t['phenomenon']}.
   b) Describe the specific processes or mechanisms in your model that give rise to this phenomenon.
   c) Discuss any predictions or insights your model provides about {t['phenomenon']}.

4. Empirical Predictions and Testability (200-250 words):
   a) Propose two empirically testable predictions that your model makes about conscious experience or {t['phenomenon']}.
   b) Describe an experimental setup that could potentially validate or falsify these predictions.
   c) Discuss the challenges in designing experiments to test computational models of consciousness.

5. Philosophical Implications (200-250 words):
   a) Analyze the philosophical implications of your computational model of consciousness.
   b) Discuss how your model addresses the hard problem of consciousness or other related philosophical questions.
   c) Consider potential objections to your approach from alternative philosophical perspectives.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss the ethical implications of developing computational models of consciousness.
   b) Propose guidelines for responsible research in this field.
   c) Suggest future directions for improving or expanding your model.

Ensure your response demonstrates a deep understanding of consciousness theories, computational modeling, and philosophical concepts related to mind and cognition. Be innovative in your approach while maintaining scientific and philosophical rigor. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and applies the principles of {t['theory']}.",
            "The computational model design is clearly described and logically consistent.",
            f"The analysis of {t['phenomenon']} is thorough and demonstrates how the model applies to this specific cognitive phenomenon.",
            "The response includes testable empirical predictions and a feasible experimental setup.",
            "The philosophical implications of the model are thoughtfully discussed.",
            "Ethical considerations are addressed, and future research directions are proposed.",
            "The response demonstrates a deep understanding of consciousness theories, computational modeling, and philosophy of mind.",
            "The approach is innovative while maintaining scientific and philosophical rigor.",
            "The response is well-structured with clear headings for each required section.",
            "The total response is between 1350-1650 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
