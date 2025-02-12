import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        enzymes = [
            {
                "name": "Alcohol dehydrogenase",
                "reaction": "Ethanol to acetaldehyde"
            },
            {
                "name": "Carbonic anhydrase",
                "reaction": "Carbon dioxide hydration"
            },
            {
                "name": "Cytochrome c oxidase",
                "reaction": "Electron transfer in respiration"
            },
            {
                "name": "Lysozyme",
                "reaction": "Peptidoglycan hydrolysis"
            }
        ]
        return {str(i+1): enzyme for i, enzyme in enumerate(random.sample(enzymes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that incorporates quantum tunneling effects in the catalytic mechanism of {t['name']} for the reaction: {t['reaction']}. Your task is to:

1. Model Design (300-350 words):
   a) Describe the key components of your computational model, including how it represents the enzyme's active site, substrate, and quantum effects.
   b) Explain how your model incorporates quantum tunneling into the catalytic mechanism.
   c) Outline the mathematical or computational techniques you would use to simulate the quantum effects.

2. Quantum-Classical Interface (200-250 words):
   a) Discuss how your model bridges the quantum and classical regimes in enzyme catalysis.
   b) Explain how your model accounts for decoherence effects in the biological environment.
   c) Describe any novel emergent properties that arise from the quantum-classical interface in your model.

3. Predictions and Insights (200-250 words):
   a) Describe two specific predictions your model makes about the catalytic mechanism of {t['name']}.
   b) Explain how these predictions differ from classical enzyme kinetics models.
   c) Discuss the potential implications of these predictions for our understanding of enzyme function and evolution.

4. Experimental Validation (250-300 words):
   a) Propose two experiments that could test the predictions of your quantum enzyme model.
   b) For each experiment, describe the methodology, expected results, and how they would support or refute your model.
   c) Discuss any technical challenges in performing these experiments and how they might be overcome.

5. Broader Implications (150-200 words):
   a) Speculate on how quantum effects in enzyme catalysis might influence other areas of biology or biochemistry.
   b) Discuss potential applications of your model in fields such as drug design or synthetic biology.
   c) Address any ethical considerations related to the development and use of quantum biology models.

Ensure your response demonstrates a deep understanding of quantum mechanics, enzyme kinetics, and computational modeling. Be creative in your approach while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience.

Format your response using clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific enzyme {t['name']} and its reaction {t['reaction']}",
            "The model design should clearly incorporate quantum tunneling effects in enzyme catalysis",
            "The response should include all required sections: Model Design, Quantum-Classical Interface, Predictions and Insights, Experimental Validation, and Broader Implications",
            "The proposed experiments should be logically connected to the model's predictions and be scientifically plausible",
            "The response should demonstrate a deep understanding of quantum mechanics, enzyme kinetics, and computational modeling",
            "The discussion should be creative while maintaining scientific rigor and plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
