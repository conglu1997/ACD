import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "global pandemic response strategy",
                "quantum_effect": "superposition",
                "brain_region": "prefrontal cortex"
            },
            {
                "scenario": "high-frequency trading algorithm design",
                "quantum_effect": "entanglement",
                "brain_region": "anterior cingulate cortex"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-biological model of decision-making in the human brain, focusing on the quantum effect of {t['quantum_effect']} in the {t['brain_region']}. Then, apply your model to analyze decision-making processes in the context of {t['scenario']}. Your response should include:

1. Quantum-Biological Model (300-350 words):
   a) Describe the key components of your quantum-biological decision-making model.
   b) Explain how {t['quantum_effect']} is incorporated into neural processes in the {t['brain_region']}.
   c) Discuss how your model differs from classical decision-making theories.
   d) Provide a visual representation (described in words) or mathematical formulation of your model.
   e) Clearly state any assumptions made in your model.

2. Neural Implementation (250-300 words):
   a) Detail how quantum effects could physically manifest in neurons or synapses.
   b) Explain the mechanisms by which {t['quantum_effect']} influences information processing in the {t['brain_region']}.
   c) Discuss any challenges or limitations in implementing quantum effects in biological systems.

3. Decision-Making Process (250-300 words):
   a) Describe step-by-step how a decision would be made using your quantum-biological model.
   b) Compare this process to traditional decision-making models.
   c) Explain how {t['quantum_effect']} might lead to different outcomes compared to classical models.

4. Application to {t['scenario']} (300-350 words):
   a) Apply your model to analyze decision-making processes in the context of {t['scenario']}.
   b) Provide a specific example of how your model could be used in this scenario.
   c) Discuss potential advantages or insights your model might offer in this context.
   d) Address any ethical considerations related to using quantum-biological models in this scenario.

5. Experimental Validation (200-250 words):
   a) Propose an experiment to test your quantum-biological decision-making model.
   b) Describe the methodology, including how you would measure quantum effects in the brain.
   c) Discuss potential outcomes and how they would support or refute your model.

6. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your model for our understanding of consciousness and free will.
   b) Suggest potential applications of quantum-biological decision-making models in fields such as AI, medicine, or public policy.
   c) Propose future research directions to further develop and refine quantum-biological models of cognition.

7. Critical Analysis (100-150 words):
   a) Discuss at least one potential criticism or alternative interpretation of your proposed model.
   b) Briefly address how you would respond to this criticism or why the alternative interpretation might be less plausible.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and decision theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Include at least 5 relevant scientific citations to support your model and claims. Use the format (Author, Year) for in-text citations and provide a references list at the end of your response.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear description of a quantum-biological decision-making model incorporating {t['quantum_effect']} in the {t['brain_region']}.",
            f"The model is applied to analyze decision-making processes in the context of {t['scenario']}.",
            "The explanation demonstrates understanding of quantum mechanics, neuroscience, and decision theory.",
            "The response includes a proposed experiment to test the quantum-biological decision-making model.",
            "The implications and future directions section discusses consciousness, free will, and potential applications.",
            "The response includes at least 5 relevant scientific citations in the specified format.",
            "The response includes a critical analysis section discussing at least one potential criticism or alternative interpretation.",
            "The total word count is between 1550-1900 words."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
