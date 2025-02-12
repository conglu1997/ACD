import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                'concept': 'superposition',
                'cognitive_process': 'decision-making',
                'measurement_technique': 'fMRI'
            },
            {
                'concept': 'entanglement',
                'cognitive_process': 'memory formation',
                'measurement_technique': 'EEG'
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(quantum_concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical experiment to investigate the potential influence of quantum phenomena on human cognition. Your task is to explore how the quantum concept of {t['concept']} might affect the cognitive process of {t['cognitive_process']}, using {t['measurement_technique']} as your primary measurement technique. Your response should include:

1. Hypothesis (100-150 words):
   Formulate a specific, testable hypothesis about how {t['concept']} might influence {t['cognitive_process']}. Explain the rationale behind your hypothesis, drawing on current understanding of both quantum mechanics and cognitive science.

2. Experimental Design (200-250 words):
   a) Describe the overall setup of your experiment.
   b) Explain how you will manipulate or observe the quantum phenomenon.
   c) Detail how you will measure the cognitive process using {t['measurement_technique']}.
   d) Discuss any control conditions or variables you will include.
   e) Describe your proposed data analysis methods.

3. Predicted Results (100-150 words):
   Speculate on the possible outcomes of your experiment. Discuss what different results might imply about the relationship between quantum phenomena and cognition.

4. Challenges and Limitations (100-150 words):
   Identify potential obstacles in implementing your experiment and limitations in interpreting the results. Suggest possible solutions or alternative approaches.

5. Broader Implications (150-200 words):
   Discuss the potential impact of your experiment's findings on our understanding of consciousness, free will, or decision-making processes. Consider how these results might influence fields such as psychology, neuroscience, or philosophy of mind.

6. Future Directions (100-150 words):
   Propose two follow-up studies that could build on your experiment, regardless of its outcome. Explain how these studies would further our understanding of quantum effects in cognition.

Ensure your response is well-structured, scientifically grounded, and creative in its approach to this speculative topic. Use appropriate scientific terminology and provide clear explanations for a knowledgeable audience.

Your total response should be between 750-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['concept']} in quantum mechanics and {t['cognitive_process']} in cognitive science.",
            "The experimental design is logically structured and scientifically plausible, even if highly speculative.",
            f"The proposed use of {t['measurement_technique']} is explained in detail and is appropriate for the study.",
            "The discussion of challenges, limitations, and broader implications shows critical thinking and awareness of the speculative nature of the topic.",
            "The response is creative and original in its approach to combining quantum mechanics and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
