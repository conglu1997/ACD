import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "Prefrontal Cortex",
                "cognitive_function": "Decision Making",
                "ai_technique": "Reinforcement Learning"
            },
            {
                "brain_region": "Hippocampus",
                "cognitive_function": "Memory Formation",
                "ai_technique": "Recurrent Neural Networks"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) system that integrates neuroscience principles and AI algorithms, focusing on the {t['brain_region']} and its role in {t['cognitive_function']}. Your BCI design should incorporate {t['ai_technique']} as a key AI component. Then, analyze the ethical implications of your design and propose guidelines for its development and use.

A brain-computer interface (BCI) is a direct communication pathway between the brain and an external device, allowing for the translation of neural activity into commands or the introduction of information into the brain.

For example, a BCI might use machine learning algorithms to interpret neural signals from the motor cortex to control a prosthetic limb. This integration of AI and neuroscience allows for adaptive control based on the user's intentions.

Your response should include:

1. BCI System Design (300-350 words):
   a) Key components and mechanisms
   b) Interface with the {t['brain_region']} for {t['cognitive_function']}
   c) Integration of {t['ai_technique']}
   d) Potential advantages and limitations

2. Neuroscientific Basis (200-250 words):
   a) Relevant neuroscientific principles
   b) Accounting for neural plasticity and adaptation
   c) Potential short-term and long-term effects on brain function

3. AI Integration (200-250 words):
   a) Implementation of {t['ai_technique']}
   b) Data flow between biological and artificial components
   c) Learning and adaptation of the AI component

4. Ethical Analysis (250-300 words):
   a) At least three ethical issues
   b) Potential misuse scenarios and implications
   c) Privacy, autonomy, and cognitive liberty concerns

5. Development and Usage Guidelines (200-250 words):
   a) Ethical guidelines for development
   b) Testing and validation protocols
   c) Principles for responsible use and access

6. Societal Impact (150-200 words):
   a) Potential impact of widespread adoption
   b) Changes in human cognition, behavior, or social structures
   c) Positive and negative potential consequences

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Remember to balance innovative ideas with realistic constraints based on current scientific knowledge.

Format your response using clear headings for each section and address all subpoints. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The BCI system design effectively integrates the {t['brain_region']}, {t['cognitive_function']}, and {t['ai_technique']}.",
            "The response demonstrates a deep understanding of relevant neuroscientific principles.",
            f"The implementation of {t['ai_technique']} in the BCI system is well-explained and plausible.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The proposed guidelines for development and use are comprehensive and ethically sound.",
            "The discussion of societal impact is insightful and balanced.",
            "The overall response is creative, scientifically plausible, and well-structured.",
            "All required sections and subpoints are addressed in the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
