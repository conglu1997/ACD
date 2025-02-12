import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'biological_system': 'human immune system',
                'challenge': 'response to a novel respiratory virus',
                'emergent_property': 'cytokine storm',
                'specific_example': 'T-cell exhaustion during prolonged infection'
            },
            {
                'biological_system': 'gut microbiome',
                'challenge': 'response to a new probiotic strain',
                'emergent_property': 'enhanced nutrient absorption',
                'specific_example': 'cross-feeding interactions between bacterial species'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for modeling complex biological systems and predicting emergent properties, then apply it to model the {t['biological_system']} and its {t['challenge']}. Your response should include the following sections:

1. Quantum-Inspired AI Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI system for modeling complex biological systems.
   b) Explain how quantum computing principles are incorporated into your AI architecture.
   c) Detail how your system models and predicts emergent properties in biological systems.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Biological System Modeling (250-300 words):
   a) Explain how your system would model the {t['biological_system']}.
   b) Describe the key parameters and variables your model would consider.
   c) Discuss how your system incorporates different scales (molecular, cellular, tissue-level) in its modeling approach.

3. Simulation of System Response (250-300 words):
   a) Detail how your AI system would simulate the {t['biological_system']}'s {t['challenge']}.
   b) Explain the step-by-step process your system would follow to predict the system's response.
   c) Describe how your system identifies and predicts emergent properties, such as {t['emergent_property']}.
   d) Provide a specific example of how your system would model and predict the phenomenon of {t['specific_example']}.

4. Quantum Advantage Analysis (200-250 words):
   a) Discuss the potential advantages of your quantum-inspired approach over classical AI methods for this task.
   b) Explain any novel insights or capabilities your system might offer in understanding complex biological systems.
   c) Address potential limitations or challenges in implementing your quantum-inspired approach.

5. Validation and Refinement Strategy (200-250 words):
   a) Propose methods to validate your system's predictions against experimental data.
   b) Describe how you would refine and improve your model based on these validations.
   c) Discuss potential challenges in scaling your approach to other biological systems or emergent properties.

6. Ethical Considerations and Future Implications (150-200 words):
   a) Discuss ethical implications of using quantum-inspired AI for modeling biological systems.
   b) Address potential concerns about the use of such technology in medical research or treatment planning.
   c) Propose guidelines for responsible development and use of quantum-inspired AI in biological modeling.

Ensure your response demonstrates a deep understanding of quantum computing principles, complex biological systems, and AI architectures. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering strictly to the word count ranges provided. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and how they can be applied to AI systems.",
            f"The biological system ({t['biological_system']}) is modeled accurately and comprehensively.",
            f"The simulation of the system's response to the {t['challenge']} is well-explained and plausible.",
            f"The prediction of emergent properties, such as {t['emergent_property']}, is addressed in detail.",
            f"A specific example of modeling {t['specific_example']} is provided and well-explained.",
            "The quantum advantage analysis is thorough and insightful.",
            "The validation and refinement strategy is well-thought-out and practical.",
            "Ethical considerations are adequately addressed.",
            "The response is well-structured, clear, and adheres to the specified word count ranges for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
