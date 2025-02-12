import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_function': 'working memory',
                'emotional_state': 'stress reduction',
                'musical_element': 'rhythm',
                'neuroplasticity_mechanism': 'long-term potentiation'
            },
            {
                'cognitive_function': 'attention',
                'emotional_state': 'mood elevation',
                'musical_element': 'harmony',
                'neuroplasticity_mechanism': 'synaptic pruning'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical system based on neuroplasticity principles, focusing on enhancing {t['cognitive_function']} and promoting {t['emotional_state']}. Your system should particularly emphasize the musical element of {t['musical_element']} and incorporate the neuroplasticity mechanism of {t['neuroplasticity_mechanism']}. Provide your response in the following format:

1. System Overview (150-200 words):
   Describe your neuroplasticity-based musical system, explaining its key components and how it integrates principles from neuroscience and music theory.

2. Neuroplasticity Mechanism (150-200 words):
   Explain how your system incorporates {t['neuroplasticity_mechanism']} and how this mechanism is expected to influence {t['cognitive_function']} and {t['emotional_state']}.

3. Musical Structure and Composition (200-250 words):
   Detail the musical structure of your system, focusing on how {t['musical_element']} is used to drive neuroplastic changes. Provide an example of a musical piece or exercise in your system, using standard musical notation or a clear descriptive format.

4. Cognitive and Emotional Effects (200-250 words):
   Analyze the potential impacts of your system on {t['cognitive_function']} and {t['emotional_state']}. Propose a hypothesis about how regular engagement with your system might affect brain structure and function.

5. Implementation and Practice Regimen (150-200 words):
   Describe how individuals would engage with your musical system, including recommended practice duration, frequency, and progression. Explain how the system adapts to individual progress and needs.

6. Measurement and Evaluation (150-200 words):
   Propose methods to measure the effectiveness of your system in enhancing {t['cognitive_function']} and promoting {t['emotional_state']}. Include both subjective and objective measurement techniques.

7. Ethical Considerations and Limitations (150-200 words):
   Discuss potential ethical concerns related to cognitive enhancement through music. Address possible limitations or contraindications of your system.

8. Future Research Directions (100-150 words):
   Suggest areas for further research to refine and expand your neuroplastic music system.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and cognitive psychology. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively incorporates the neuroplasticity mechanism of {t['neuroplasticity_mechanism']}.",
            f"The musical structure clearly emphasizes the element of {t['musical_element']}.",
            f"The system presents a plausible approach to enhancing {t['cognitive_function']}.",
            f"The system offers a credible method for promoting {t['emotional_state']}.",
            "The response demonstrates a deep understanding of neuroscience, music theory, and cognitive psychology.",
            "The proposed measurement and evaluation methods are scientifically sound.",
            "The ethical considerations are thoughtfully addressed.",
            "The system design is innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
