import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'neuroscience_concept': 'Neural oscillations',
                'information_theory_aspect': 'Entropy'
            },
            {
                'quantum_principle': 'Entanglement',
                'neuroscience_concept': 'Synaptic plasticity',
                'information_theory_aspect': 'Mutual information'
            },
            {
                'quantum_principle': 'Quantum tunneling',
                'neuroscience_concept': 'Neuroplasticity',
                'information_theory_aspect': 'Channel capacity'
            },
            {
                'quantum_principle': 'Wave function collapse',
                'neuroscience_concept': 'Default mode network',
                'information_theory_aspect': 'Kolmogorov complexity'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model that integrates quantum mechanics, neuroscience, and information theory to explain consciousness, then use it to make testable predictions about brain function and subjective experience. Focus on the quantum principle of {t['quantum_principle']}, the neuroscience concept of {t['neuroscience_concept']}, and the information theory aspect of {t['information_theory_aspect']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how the specified quantum principle could be applied to neural processes.
   b) Describe how the neuroscience concept interacts with quantum effects in your model.
   c) Discuss how the information theory aspect relates to consciousness in your framework.
   d) Propose a novel hypothesis about consciousness emerging from these interactions.

2. Model Architecture (250-300 words):
   a) Describe the key components of your quantum neural consciousness model.
   b) Explain how information is processed and transformed in your model.
   c) Detail how your model accounts for subjective experience and qualia.
   d) Discuss any novel computational or representational elements in your design.

3. Consciousness Mechanisms (200-250 words):
   a) Propose a specific mechanism by which consciousness arises in your model.
   b) Explain how this mechanism integrates quantum, neural, and informational processes.
   c) Discuss how your model addresses the 'hard problem' of consciousness.

4. Testable Predictions (250-300 words):
   a) Derive at least three testable predictions from your model about brain function or subjective experience.
   b) Explain the reasoning behind each prediction and how it follows from your model.
   c) Propose experiments or observations that could validate or refute these predictions.

5. Implications and Limitations (200-250 words):
   a) Discuss the potential implications of your model for our understanding of consciousness, free will, and the nature of reality.
   b) Address the limitations and potential criticisms of your approach.
   c) Suggest future research directions that could further develop or test your model.

6. Ethical Considerations (150-200 words):
   a) Explore the ethical implications of your model, if it were to accurately represent consciousness.
   b) Discuss potential concerns about altering or manipulating consciousness based on your model.
   c) Propose guidelines for the responsible application of your theory in research and technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, information theory, and philosophical aspects of consciousness. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section, numbered as above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately integrates the quantum principle of {t['quantum_principle']}, the neuroscience concept of {t['neuroscience_concept']}, and the information theory aspect of {t['information_theory_aspect']}.",
            "The proposed model presents a novel and logically consistent approach to explaining consciousness.",
            "The consciousness mechanism clearly addresses the 'hard problem' of consciousness.",
            "At least three specific, well-reasoned testable predictions are derived from the proposed model.",
            "The response critically addresses the implications, limitations, and ethical considerations of the proposed model.",
            "The writing is clear, well-structured, and uses appropriate technical terminology throughout.",
            "The response adheres to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
