import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                "process": "photosynthesis",
                "primary_effect": "quantum coherence",
                "secondary_effect": "quantum entanglement"
            },
            {
                "process": "enzyme catalysis",
                "primary_effect": "quantum tunneling",
                "secondary_effect": "zero-point energy"
            },
            {
                "process": "avian magnetoreception",
                "primary_effect": "radical pair mechanism",
                "secondary_effect": "quantum coherence"
            },
            {
                "process": "olfaction",
                "primary_effect": "vibrational theory of olfaction",
                "secondary_effect": "quantum tunneling"
            }
        ]
        return {
            "1": random.choice(biological_processes),
            "2": random.choice(biological_processes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model simulating multiple quantum effects in a biological system, focusing primarily on {t['primary_effect']} and secondarily on {t['secondary_effect']} in {t['process']}. Then, use your model to analyze and predict the behavior of this biological process. Your response should include:

1. Quantum Biology Framework (250-300 words):
   a) Explain the key principles of quantum biology relevant to {t['process']}.
   b) Describe how {t['primary_effect']} and {t['secondary_effect']} contribute to the efficiency or functionality of {t['process']}.
   c) Compare and contrast the roles of {t['primary_effect']} and {t['secondary_effect']} in {t['process']}.
   d) Discuss the challenges in studying and modeling multiple quantum effects in biological systems.

2. Computational Model Design (300-350 words):
   a) Outline the architecture of your computational model for simulating both {t['primary_effect']} and {t['secondary_effect']} in {t['process']}.
   b) Explain how your model integrates multiple quantum mechanical principles with biological processes.
   c) Describe any novel algorithms or techniques used in your model to handle multiple quantum effects.
   d) Provide a high-level pseudocode (15-20 lines, not counted in the word limit) of your simulation algorithm. Use clear variable names and comments to explain each step.

3. Simulation and Analysis (250-300 words):
   a) Describe a specific scenario you would simulate using your model that involves both quantum effects.
   b) Explain the step-by-step process of how your model simulates this scenario.
   c) Analyze the results of your simulation, focusing on how the interplay between {t['primary_effect']} and {t['secondary_effect']} influences the biological process.
   d) Discuss any surprising or counterintuitive findings from your simulation, particularly regarding the interaction of the two quantum effects.

4. Predictions and Testable Hypotheses (200-250 words):
   a) Based on your model and simulation results, make at least two specific predictions about {t['process']} that involve both {t['primary_effect']} and {t['secondary_effect']}.
   b) Propose experiments or observations that could test these predictions.
   c) Discuss the potential implications of your predictions for our understanding of {t['process']} and quantum biology in general.

5. Model Evaluation and Limitations (200-250 words):
   a) Propose methods for validating your computational model against experimental data, considering the challenges of measuring multiple quantum effects simultaneously.
   b) Discuss the limitations of your model and potential sources of error or uncertainty, particularly in relation to modeling multiple quantum effects.
   c) Suggest improvements or extensions to your model for future research.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how your multi-effect quantum biology model and findings might impact other fields of study (e.g., quantum computing, medicine, or artificial photosynthesis).
   b) Discuss the philosophical implications of multiple interacting quantum effects in biological systems for our understanding of life and consciousness.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and computational modeling. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words, not including the pseudocode."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum biology, particularly the interplay between {t['primary_effect']} and {t['secondary_effect']} in {t['process']}.",
            "The computational model design is innovative, scientifically plausible, and well-explained, incorporating multiple quantum effects.",
            "The simulation and analysis show a clear connection between multiple quantum effects and biological processes.",
            "The predictions and proposed experiments are logical, grounded in the model's results, and address both quantum effects.",
            "The response addresses model limitations and suggests valid improvements, considering the challenges of modeling multiple quantum effects.",
            "The interdisciplinary implications are thoughtfully explored and scientifically sound, reflecting the complexity of multi-effect quantum biology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
