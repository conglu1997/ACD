import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "decision_context": "financial investment",
                "uncertainty_factor": "market volatility",
                "psychological_bias": "loss aversion"
            },
            {
                "decision_context": "medical treatment",
                "uncertainty_factor": "treatment efficacy",
                "psychological_bias": "optimism bias"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a neuroeconomic model of decision-making under uncertainty for the following scenario:

Decision Context: {t['decision_context']}
Uncertainty Factor: {t['uncertainty_factor']}
Psychological Bias: {t['psychological_bias']}

Your response should include the following sections:

1. Model Framework (300-350 words):
   a) Describe the key components of your neuroeconomic model.
   b) Explain how your model integrates neural, economic, and psychological factors.
   c) Discuss how your model accounts for the specified uncertainty factor and psychological bias.
   d) Provide a visual representation (described in words) of your model's structure.

2. Neural Mechanisms (250-300 words):
   a) Identify the key brain regions involved in your model.
   b) Explain the role of each region in the decision-making process.
   c) Describe how these regions interact during decision-making under uncertainty.
   d) Discuss how the specified psychological bias is represented at the neural level.

3. Economic Principles (200-250 words):
   a) Explain how your model incorporates economic concepts related to decision-making under uncertainty.
   b) Discuss how your model handles risk assessment and utility maximization.
   c) Describe how the model accounts for the temporal aspects of decision-making (e.g., immediate vs. delayed rewards).

4. Model Predictions (200-250 words):
   a) Provide at least three specific, testable predictions derived from your model.
   b) Explain the reasoning behind each prediction.
   c) Describe how these predictions differ from those of traditional economic or psychological models.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test a key aspect of your neuroeconomic model.
   b) Describe the methodology, including any required technologies (e.g., fMRI, EEG).
   c) Explain what results would support or refute your model.

6. Model Limitations and Future Directions (150-200 words):
   a) Discuss potential limitations of your neuroeconomic model.
   b) Suggest two ways to improve or extend your model in future research.
   c) Propose a potential application of your model in a real-world context.

Ensure your response demonstrates a deep understanding of neuroscience, economics, and psychology. Use appropriate technical terminology and provide clear explanations of complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, economics, and psychology in the context of {t['decision_context']}.",
            f"The model effectively integrates neural, economic, and psychological factors, accounting for {t['uncertainty_factor']} and {t['psychological_bias']}.",
            "The neural mechanisms are accurately described and relevant to the decision-making process.",
            "The economic principles are correctly applied and integrated into the model.",
            "The model predictions are specific, testable, and logically derived from the proposed framework.",
            "The experimental design is well-thought-out and appropriate for testing the model.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
