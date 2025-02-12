import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "superposition",
            "entanglement",
            "quantum tunneling"
        ]
        linguistic_aspects = [
            "semantic ambiguity",
            "contextual interpretation",
            "metaphorical reasoning"
        ]
        ethical_concerns = [
            "truth manipulation",
            "information privacy",
            "cognitive bias amplification"
        ]
        return {
            "1": {
                "quantum_property": random.choice(quantum_properties),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "ethical_concern": random.choice(ethical_concerns)
            },
            "2": {
                "quantum_property": random.choice(quantum_properties),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "ethical_concern": random.choice(ethical_concerns)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-enhanced language model that incorporates the quantum property of {t['quantum_property']} into the linguistic aspect of {t['linguistic_aspect']}, focusing on its ethical implications related to {t['ethical_concern']}. Your response should include:

1. Quantum-Linguistic Model (250-300 words):
   a) Describe how your model integrates the quantum property into the specified linguistic aspect.
   b) Explain the potential advantages of this integration for language processing.
   c) Discuss any novel linguistic capabilities enabled by your quantum-enhanced model.

2. Ethical Analysis (200-250 words):
   a) Analyze how your model might impact the specified ethical concern.
   b) Discuss potential positive and negative consequences for society.
   c) Propose safeguards or guidelines to mitigate ethical risks.

3. Technical Implementation (200-250 words):
   a) Outline the key components and architecture of your quantum-enhanced language model.
   b) Explain how quantum computations are integrated with classical NLP techniques.
   c) Discuss any technical challenges and proposed solutions.

4. Societal Impact Scenario (150-200 words):
   a) Describe a specific scenario where your model could significantly impact society.
   b) Analyze both the benefits and risks in this scenario.
   c) Propose a framework for responsible deployment and monitoring.

5. Future Research Directions (100-150 words):
   a) Suggest two potential research projects to further explore the ethical implications of your model.
   b) Briefly describe the methodology and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and ethics. Use appropriate technical terminology and provide clear explanations. Be innovative while maintaining scientific and ethical plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately integrates the quantum property of {t['quantum_property']} with the linguistic aspect of {t['linguistic_aspect']}.",
            f"The ethical implications related to {t['ethical_concern']} are thoroughly analyzed.",
            "The proposed model demonstrates innovation in quantum-enhanced language processing.",
            "The technical implementation is plausible and well-explained.",
            "The societal impact scenario is realistic and thoughtfully analyzed.",
            "The future research directions are relevant and well-justified."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
