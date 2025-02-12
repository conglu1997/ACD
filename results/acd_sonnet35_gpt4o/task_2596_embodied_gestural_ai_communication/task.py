import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'context': 'Design an AI system for gestural communication in a collaborative robotics environment',
                'focus_area': 'Spatial reasoning and object manipulation'
            },
            {
                'context': 'Develop an AI-powered sign language interpreter and generator for cross-cultural communication',
                'focus_area': 'Emotional expression and cultural nuances'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating complex gestural languages based on principles of embodied cognition. Your task is to create a system that can effectively communicate through gestures in the following context: {t['context']}. Focus particularly on {t['focus_area']}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for gestural communication.
   b) Explain how it integrates principles from embodied cognition, gesture studies, and AI.
   c) Detail how your system processes and generates gestural information.
   d) Discuss any novel technologies or theoretical concepts your system employs.

2. Embodied Cognition Integration (200-250 words):
   a) Explain how your system incorporates theories of embodied cognition.
   b) Describe how physical embodiment influences the AI's understanding and generation of gestures.
   c) Discuss how your system addresses challenges specific to embodied communication.

3. Gesture Processing and Generation (200-250 words):
   a) Explain the methods your system uses to recognize and interpret gestures.
   b) Describe how it generates appropriate gestural responses.
   c) Discuss how context and cultural factors are considered in gesture interpretation and production.

4. Learning and Adaptation (150-200 words):
   a) Describe how your system learns new gestures and refines its understanding over time.
   b) Explain how it adapts to different users and contexts.
   c) Discuss any potential limitations or biases in the learning process.

5. Application Scenario (150-200 words):
   Provide a specific example of how your system would operate in the given context, demonstrating its gestural communication capabilities.

6. Implications for Human-AI Interaction (200-250 words):
   a) Analyze how gestural communication might enhance human-AI interaction.
   b) Discuss potential benefits and challenges of embodied AI communication.
   c) Explore how this approach might contribute to developing more intuitive and natural AI interfaces.

7. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of creating AI systems capable of nuanced gestural communication.
   b) Address potential issues related to privacy, consent, and cultural sensitivity.
   c) Propose guidelines for responsible development and use of gestural AI systems.

8. Future Directions (150-200 words):
   a) Suggest potential advancements or extensions of your system.
   b) Discuss how this technology might contribute to the development of artificial general intelligence.
   c) Propose an experiment to evaluate the effectiveness of your gestural AI system compared to traditional communication interfaces.

Ensure your response demonstrates a deep understanding of embodied cognition, gesture studies, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of embodied cognition, gesture studies, and artificial intelligence.",
            "The proposed AI system is innovative and integrates principles from multiple disciplines effectively.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "The system architecture and gesture processing methods are well-explained and scientifically plausible.",
            "The application scenario effectively illustrates the system's capabilities in the given context.",
            "Ethical considerations and future directions are thoughtfully discussed.",
            "The response is well-structured, using appropriate terminology and providing clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
