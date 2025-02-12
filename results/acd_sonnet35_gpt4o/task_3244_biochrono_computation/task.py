import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "biological_system": "Circadian rhythm regulation",
                "temporal_scale": "Daily",
                "climate_problem": "Predicting short-term weather patterns",
                "biological_mechanism": "Negative feedback loop involving CLOCK and BMAL1 proteins",
                "climate_parameter": "Diurnal temperature variation"
            },
            "2": {
                "biological_system": "Seasonal adaptation in plants",
                "temporal_scale": "Annual",
                "climate_problem": "Forecasting long-term climate trends",
                "biological_mechanism": "Phytochrome-mediated photoperiodism",
                "climate_parameter": "Interannual variability in precipitation"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel computational paradigm inspired by how living organisms process information across different timescales, then apply it to solve a complex problem in climate prediction. Focus on the biological system of {t['biological_system']} operating on a {t['temporal_scale']} scale, and apply your paradigm to the climate problem of {t['climate_problem']}. Your response should include the following sections:

1. Biochrono-Computational Paradigm (300-350 words):
   a) Describe the key principles of your computational paradigm inspired by {t['biological_system']}.
   b) Explain how your paradigm incorporates temporal dynamics and information processing across the {t['temporal_scale']} scale.
   c) Detail the main components and processes of your computational system, including how it models the {t['biological_mechanism']}.
   d) Discuss how your paradigm differs from traditional computing approaches.

2. Biological-Computational Mapping (200-250 words):
   a) Explain the specific mechanisms in {t['biological_system']} that inspire your computational approach.
   b) Describe how you translate these biological processes into computational elements.
   c) Discuss any novel algorithms or data structures that emerge from this bio-inspired approach.
   d) Provide a concrete example of how your system would process a specific input related to {t['climate_parameter']}.

3. Application to Climate Prediction (250-300 words):
   a) Outline how your biochrono-computational paradigm can be applied to {t['climate_problem']}.
   b) Describe the specific advantages your approach offers for this problem.
   c) Provide a high-level algorithm or process flow for solving the climate prediction problem.
   d) Include a quantitative analysis of how your system might improve prediction accuracy for {t['climate_parameter']}.
   e) Discuss potential challenges in implementing your approach and how they might be overcome.

4. Comparative Analysis (200-250 words):
   a) Compare your biochrono-computational approach to existing methods for {t['climate_problem']}.
   b) Analyze the potential improvements in accuracy, efficiency, or novel insights your method might provide.
   c) Discuss any trade-offs or limitations of your approach.
   d) Provide a hypothetical case study demonstrating the advantages of your method.

5. Broader Implications (150-200 words):
   a) Explore potential applications of your biochrono-computational paradigm beyond climate prediction.
   b) Discuss how this approach might impact our understanding of biological information processing.
   c) Propose a future research direction that could further develop or expand upon your paradigm.

Ensure your response demonstrates a deep understanding of biological systems, temporal dynamics, information processing, and climate science. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_system']} and its temporal dynamics, including the {t['biological_mechanism']}",
            "The computational paradigm is novel and clearly inspired by the specified biological system",
            f"The application to {t['climate_problem']} is well-explained and plausible, with a quantitative analysis for {t['climate_parameter']}",
            "The comparative analysis includes a hypothetical case study demonstrating the advantages of the proposed method",
            "The response explores broader implications and future research directions",
            "The overall response is creative, scientifically plausible, and well-structured, adhering to the specified word counts for each section",
            "Concrete examples and quantitative analyses are provided where appropriate"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
