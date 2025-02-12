import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling",
            "quantum superposition"
        ]
        biological_structures = [
            "microtubules",
            "ion channels",
            "neural networks",
            "DNA"
        ]
        philosophical_questions = [
            "What is the nature of qualia?",
            "How does consciousness emerge from physical processes?",
            "Is free will compatible with determinism?",
            "What is the relationship between consciousness and time?"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_structure": random.choice(biological_structures),
                "philosophical_question": random.choice(philosophical_questions)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_structure": random.choice(biological_structures),
                "philosophical_question": random.choice(philosophical_questions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological model of consciousness that incorporates {t['quantum_effect']} in {t['biological_structure']}, implement it as a computational simulation, and use it to explore the philosophical question: {t['philosophical_question']}

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Describe your quantum-biological model of consciousness, explaining how it integrates {t['quantum_effect']} with {t['biological_structure']}.
   b) Discuss the key principles and mechanisms of your model.
   c) Explain how your model addresses current challenges in consciousness theories.

2. Computational Implementation (250-300 words):
   a) Outline the architecture of your computational simulation.
   b) Describe the key algorithms or mathematical formulations used.
   c) Explain how your simulation captures the quantum and biological aspects of your model.
   d) Include a short pseudocode snippet (5-10 lines) illustrating a core function of your simulation.

3. Simulation Scenario (200-250 words):
   a) Describe a specific scenario you would run in your simulation to explore {t['philosophical_question']}.
   b) Explain the parameters, initial conditions, and expected outcomes of this scenario.
   c) Discuss how this scenario might provide insights into the nature of consciousness.

4. Philosophical Analysis (250-300 words):
   a) Analyze how your model and simulation results address {t['philosophical_question']}.
   b) Discuss the implications of your findings for our understanding of consciousness and subjective experience.
   c) Compare your approach to traditional philosophical arguments or thought experiments related to this question.

5. Empirical Predictions (150-200 words):
   a) Propose two testable predictions derived from your quantum-biological model of consciousness.
   b) Describe potential experiments or observations that could validate or refute these predictions.

6. Limitations and Future Directions (150-200 words):
   a) Discuss the main limitations of your model and simulation approach.
   b) Suggest areas for future research or improvements in quantum-biological models of consciousness.
   c) Propose one potential application of your model outside the field of consciousness studies.

Ensure your response demonstrates a deep understanding of quantum physics, neurobiology, and philosophy of mind. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and its potential role in consciousness.",
            f"The model effectively integrates {t['quantum_effect']} with {t['biological_structure']} in a plausible manner.",
            f"The computational implementation is well-described and includes a relevant pseudocode snippet.",
            f"The philosophical analysis provides insightful exploration of the question: {t['philosophical_question']}",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The limitations and future directions demonstrate critical thinking about the model's implications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
