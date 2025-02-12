import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        consciousness_aspects = [
            "self-awareness",
            "qualia",
            "intentionality",
            "metacognition"
        ]
        constraints = [
            "limited coherence time",
            "scalability issues",
            "noise sensitivity",
            "measurement problem"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "consciousness_aspect": random.choice(consciousness_aspects),
                "constraint": random.choice(constraints)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "consciousness_aspect": random.choice(consciousness_aspects),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum neural network model of consciousness that integrates principles from neuroscience, quantum mechanics, and artificial intelligence to explain and simulate conscious experiences. Your model should specifically leverage the quantum principle of {t['quantum_principle']} to address the consciousness aspect of {t['consciousness_aspect']}, while considering the constraint of {t['constraint']}.

Your response should include the following sections:

1. Model Architecture (300-350 words):
   a) Describe the key components of your quantum neural network model.
   b) Explain how it integrates classical neural network principles with quantum computing.
   c) Detail how your model incorporates the specified quantum principle.
   d) Provide a diagram or pseudocode representation of a key component in your system.

2. Consciousness Simulation (250-300 words):
   a) Explain how your model simulates or explains the specified aspect of consciousness.
   b) Discuss the advantages of using a quantum approach for this aspect of consciousness.
   c) Address any challenges or limitations in modeling consciousness with your approach.

3. Quantum-Classical Interface (200-250 words):
   a) Describe how your model interfaces between quantum and classical information processing.
   b) Explain any novel techniques used to maintain quantum effects in a biological context.
   c) Discuss how you address the specified constraint in your model.

4. Theoretical Predictions (200-250 words):
   a) Propose at least two testable predictions that your model makes about consciousness.
   b) Explain how these predictions differ from those of classical neuroscience models.
   c) Suggest potential experiments or observations that could validate your model.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the potential ethical implications of a quantum model of consciousness.
   b) Address how your model might impact our understanding of free will and decision-making.
   c) Consider the philosophical consequences of a quantum basis for consciousness.

6. Future Research Directions (150-200 words):
   a) Propose two potential improvements or expansions to your model.
   b) Discuss how emerging technologies in quantum computing or neuroscience could enhance your model's capabilities.
   c) Suggest a related aspect of cognition that could be explored using a similar quantum neural network approach.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and artificial intelligence. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed design of a quantum neural network model that incorporates {t['quantum_principle']} to address {t['consciousness_aspect']}.",
            f"The model should adequately address the constraint of {t['constraint']}.",
            "The response should demonstrate a deep understanding of quantum mechanics, neuroscience, and artificial intelligence.",
            "The proposed model should be creative and speculative while maintaining scientific plausibility.",
            "The response should include testable predictions and discuss ethical and philosophical implications.",
            "The overall response should showcase interdisciplinary knowledge integration and creative scientific reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
