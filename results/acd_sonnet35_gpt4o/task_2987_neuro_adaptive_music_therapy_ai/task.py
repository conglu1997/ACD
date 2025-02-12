import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_state": "anxiety",
                "brain_region": "amygdala",
                "musical_element": "rhythm",
                "neural_data": "Increased amygdala activation (30% above baseline), elevated heart rate (100 bpm), and increased skin conductance (5 μS)"
            },
            {
                "cognitive_state": "memory recall",
                "brain_region": "hippocampus",
                "musical_element": "melody",
                "neural_data": "Increased hippocampal activation (25% above baseline), elevated theta wave activity (6 Hz), and increased functional connectivity with prefrontal cortex"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates personalized music therapy interventions based on real-time neurological data to address the cognitive state of {t['cognitive_state']}, focusing on activity in the {t['brain_region']} and primarily utilizing the musical element of {t['musical_element']}. The system should interpret and respond to the following neural data: {t['neural_data']}.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neuro-adaptive music therapy.
   b) Explain how the system processes real-time neurological data.
   c) Detail how the system generates and adapts musical interventions.
   d) Provide a high-level diagram or flowchart of your system's architecture (use ASCII art or a text-based representation).

2. Neurofeedback Mechanism (250-300 words):
   a) Explain how your system interprets the given neural activity data.
   b) Describe how this data is used to modulate the musical output.
   c) Discuss any novel algorithms or techniques used in this process.
   d) Provide a specific example of how the system would respond to a change in the given neural data.

3. Musical Composition Engine (250-300 words):
   a) Detail how your AI generates music based on the specified musical element.
   b) Explain how the system ensures the music is therapeutically appropriate for the given cognitive state.
   c) Describe how the engine adapts to changes in neural activity in real-time.
   d) Provide a brief example of the musical output for the given scenario.

4. Therapeutic Approach (200-250 words):
   a) Explain how your system's output addresses the specified cognitive state.
   b) Discuss the theoretical basis for your therapeutic approach, citing relevant research.
   c) Describe how you would measure the effectiveness of the intervention.
   d) Propose a specific hypothesis about the expected therapeutic outcome.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI-generated music for therapy.
   b) Address issues such as data privacy, informed consent, and potential side effects.
   c) Propose guidelines for the responsible development and use of such systems.

6. Future Developments (200-250 words):
   a) Suggest two potential advancements or extensions of this technology.
   b) Discuss how this system could be applied to other areas of mental health or cognitive enhancement.
   c) Speculate on the long-term implications for the fields of music therapy and neuroscience.
   d) Propose a novel research question that arises from your system design.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1350-1650 words, not including the diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence.",
            "The system design is creative, innovative, and scientifically plausible.",
            "The approach effectively addresses the specified cognitive state using the given brain region, musical element, and neural data.",
            "The neurofeedback mechanism and musical composition engine are well-explained and appropriate for the task.",
            "The therapeutic approach is well-grounded in theory and includes a clear hypothesis and measurement strategy.",
            "Ethical considerations are comprehensively addressed with specific guidelines proposed.",
            "Future developments and implications are thoughtfully explored with a novel research question proposed.",
            "The response is well-structured, clear, and adheres to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
