import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'visual_input': 'facial expressions',
                'linguistic_input': 'sentiment analysis',
                'brain_region': 'fusiform face area and superior temporal sulcus',
                'ai_application': 'emotion recognition in human-robot interaction'
            },
            {
                'visual_input': 'object recognition',
                'linguistic_input': 'semantic parsing',
                'brain_region': 'inferior temporal cortex and Wernicke\'s area',
                'ai_application': 'visual question answering'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neurosymbolic AI system that integrates visual information processing for {t['visual_input']} and linguistic information processing for {t['linguistic_input']}, inspired by the multimodal integration mechanisms in the human brain, particularly in the {t['brain_region']}. Your system should be applicable to {t['ai_application']}. Provide your response in the following format:

1. Neuroscientific Basis (200-250 words):
   Explain the relevant neuroscientific principles of multimodal integration in the specified brain regions. Discuss how these regions process and combine visual and linguistic information.

2. System Architecture (250-300 words):
   Describe the key components of your neurosymbolic AI system and how they interact. Explain how your system mimics the brain's multimodal integration processes. Include a high-level diagram or pseudocode to illustrate your system's architecture.

3. Visual Processing Module (150-200 words):
   Detail how your system processes the specified visual input. Explain any novel approaches or algorithms used, and how they relate to biological visual processing.

4. Linguistic Processing Module (150-200 words):
   Describe how your system handles the specified linguistic input. Discuss any innovative techniques employed and their relation to human language processing.

5. Neurosymbolic Integration (200-250 words):
   Explain how your system integrates visual and linguistic information. Discuss the symbolic and neural components of your system and how they interact. Provide an example of how this integration would work for a specific input.

6. Application to {t['ai_application']} (150-200 words):
   Describe how your neurosymbolic AI system would be applied to the specified AI application. Discuss potential benefits and challenges of using your system in this context.

7. Evaluation and Testable Predictions (150-200 words):
   Propose methods to evaluate your system's performance. Suggest at least one testable prediction about human cognition that could be derived from your model.

8. Ethical Considerations and Limitations (100-150 words):
   Discuss potential ethical implications of your system. Address any limitations of your approach and suggest areas for future improvement.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and linguistic processing. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of multimodal integration in the {t['brain_region']}.",
            f"The system effectively integrates visual processing for {t['visual_input']} and linguistic processing for {t['linguistic_input']}.",
            f"The neurosymbolic AI system design is innovative, scientifically plausible, and well-explained.",
            f"The application to {t['ai_application']} is thoroughly discussed with clear benefits and challenges.",
            "The response includes all required sections with appropriate depth and clarity.",
            "The proposed evaluation methods and testable predictions are scientifically sound.",
            "Ethical considerations and limitations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
