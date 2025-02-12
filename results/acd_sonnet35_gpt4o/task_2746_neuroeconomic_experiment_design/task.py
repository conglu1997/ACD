import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        decision_contexts = [
            {
                "context": "Intertemporal choice",
                "description": "Decisions involving tradeoffs between immediate and delayed rewards"
            },
            {
                "context": "Social decision-making",
                "description": "Decisions affecting both self and others, involving concepts like fairness and reciprocity"
            }
        ]
        neural_techniques = [
            {
                "technique": "fMRI",
                "description": "Functional Magnetic Resonance Imaging to measure brain activity"
            },
            {
                "technique": "EEG",
                "description": "Electroencephalography to measure electrical activity in the brain"
            }
        ]
        additional_constraints = [
            "The experiment must include a cross-cultural comparison",
            "The experiment must incorporate a stress manipulation"
        ]
        return {
            "1": {
                "decision_context": random.choice(decision_contexts),
                "neural_technique": random.choice(neural_techniques),
                "additional_constraint": random.choice(additional_constraints)
            },
            "2": {
                "decision_context": random.choice(decision_contexts),
                "neural_technique": random.choice(neural_techniques),
                "additional_constraint": random.choice(additional_constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Neuroeconomics is an interdisciplinary field that combines neuroscience, economics, and psychology to study how the brain makes decisions. Your task is to design a hypothetical neuroeconomic experiment that investigates the neural basis of economic decision-making in the context of {t['decision_context']['context']} using {t['neural_technique']['technique']}. Create an innovative and scientifically plausible experimental design that integrates economic theory, psychological insights, and neuroscientific methods. Additionally, your experiment must address the following constraint: {t['additional_constraint']}.

Your response should include:

1. Experimental Design (300-400 words):
   a) Describe the overall structure of your experiment, including the task participants will perform.
   b) Explain how your design specifically addresses {t['decision_context']['description']}.
   c) Detail how you will use {t['neural_technique']['technique']} to measure neural activity during the task.
   d) Discuss any control conditions or comparison groups you will include.
   e) Explain how you will incorporate the additional constraint: {t['additional_constraint']}.
   f) Specify the minimum number of participants (at least 50) and justify your choice.
   g) If applicable, describe the game-theoretic approach you will use.
   h) Propose a novel neuroeconomic measure or paradigm that your experiment will introduce.

2. Hypotheses and Predictions (200-300 words):
   a) State at least two specific hypotheses your experiment will test.
   b) For each hypothesis, predict the behavioral outcomes you expect to observe.
   c) Describe the neural activity patterns you anticipate seeing, and how they relate to your hypotheses.
   d) Explain how the additional constraint might affect your hypotheses and predictions.

3. Data Analysis Plan (200-300 words):
   a) Explain the key measures and variables you will analyze from both behavioral and neural data.
   b) Describe the statistical methods you will use to test your hypotheses.
   c) Discuss how you will integrate the behavioral and neural data in your analysis.
   d) Address how you will control for potential confounding variables.

4. Potential Implications (150-250 words):
   a) Discuss how the results of your experiment could inform economic theory or models of decision-making.
   b) Explain potential real-world applications of your findings (e.g., policy, marketing, or clinical interventions).
   c) Describe how your experiment might contribute to our understanding of the neural basis of economic behavior.

5. Ethical Considerations (150-250 words):
   a) Identify potential ethical issues related to your experimental design.
   b) Discuss how you would address these ethical concerns.
   c) Consider any broader societal implications of using neuroscientific methods to study economic decision-making.

6. Limitations and Future Directions (150-250 words):
   a) Acknowledge potential limitations of your experimental design.
   b) Suggest how these limitations might be addressed in future studies.
   c) Propose a follow-up experiment that could build on your findings.

Ensure your response demonstrates a deep understanding of economics, psychology, and neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

IMPORTANT: Do not include any actual data or results in your response, as this is a hypothetical experiment design. Your design should be novel and scientifically plausible, pushing the boundaries of current neuroeconomic research without venturing into science fiction.

Format your response using clear headings for each section. Your total response should be between 1150-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of neuroeconomics, integrating concepts from economics, psychology, and neuroscience.",
            "The experimental design is innovative, detailed, and scientifically plausible, with clear explanations of how it addresses the specified decision-making context and additional constraint.",
            "The use of the specified neural measurement technique is well-explained and appropriate for the experimental design.",
            "The response includes a novel neuroeconomic measure or paradigm that is both creative and scientifically grounded.",
            "The hypotheses and predictions are clearly stated and logically connected to the experimental design, including considerations for the additional constraint.",
            "The data analysis plan is comprehensive, appropriate for testing the stated hypotheses, and includes methods for controlling confounding variables.",
            "The potential implications of the experiment are thoughtfully discussed, with clear connections to economic theory and real-world applications.",
            "Ethical considerations are thoroughly addressed, demonstrating awareness of the sensitive nature of neuroscientific research.",
            "Limitations of the study are acknowledged, and future directions are proposed that logically build on the current design.",
            "The response shows strong interdisciplinary reasoning, effectively combining insights from economics, psychology, and neuroscience.",
            "The writing is clear, well-structured, and adheres to the specified word limits for each section.",
            "The response does not include any actual data or results, maintaining the hypothetical nature of the experiment design.",
            "The proposed experiment is novel and pushes the boundaries of current neuroeconomic research while remaining scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
