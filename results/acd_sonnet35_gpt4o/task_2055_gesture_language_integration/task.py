import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        gestures = [
            {
                'gesture_type': 'Deictic (pointing)',
                'cultural_context': 'Western',
                'linguistic_domain': 'Spatial relations'
            },
            {
                'gesture_type': 'Emblematic (thumbs up)',
                'cultural_context': 'Japanese',
                'linguistic_domain': 'Pragmatics'
            },
            {
                'gesture_type': 'Iconic (miming)',
                'cultural_context': 'Brazilian',
                'linguistic_domain': 'Verb semantics'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(gestures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multimodal AI system that integrates gesture recognition with natural language processing, focusing on the {t['gesture_type']} gesture type in the context of {t['cultural_context']} culture and the linguistic domain of {t['linguistic_domain']}. Your system should incorporate principles of embodied cognition. Provide a comprehensive response covering the following aspects:

1. System Architecture (300-350 words):
   a) Describe the key components of your multimodal AI system, including gesture recognition and natural language processing modules.
   b) Explain how your system incorporates principles of embodied cognition.
   c) Detail how the system integrates gesture and language information.
   d) Provide a high-level diagram of your system architecture (described in words).
   e) Describe any novel algorithms or techniques used in your system.

2. Gesture-Language Mapping (250-300 words):
   a) Explain how your system processes and represents gesture data for the specified gesture type.
   b) Describe how the system maps gestures to linguistic elements in the given domain.
   c) Provide an example of how your system would process a specific gesture-language combination.
   d) Discuss how cultural context influences this mapping process.

3. Embodied Cognition Integration (200-250 words):
   a) Explain how your system implements key principles of embodied cognition.
   b) Discuss how this embodied approach enhances the gesture-language integration.
   c) Provide an example of how embodied cognition principles improve the system's performance or capabilities.

4. Cross-cultural Considerations (200-250 words):
   a) Analyze how your system would handle gesture-language mappings in different cultural contexts.
   b) Discuss potential challenges in adapting the system to other cultures.
   c) Propose strategies for making the system more culturally adaptive.

5. Performance Evaluation (150-200 words):
   a) Suggest three specific metrics to evaluate your system's performance.
   b) Describe an experiment to test the system's effectiveness in real-world scenarios.
   c) Discuss potential limitations of your evaluation approach.

6. Ethical and Societal Implications (150-200 words):
   a) Identify three potential ethical concerns raised by your system.
   b) Discuss the broader societal implications of widespread adoption of such technology.
   c) Propose guidelines for responsible development and use of gesture-language AI systems.

7. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how your approach could contribute to advancing our understanding of human communication and cognition.

Ensure your response demonstrates a deep understanding of gesture recognition, natural language processing, embodied cognition, and cross-cultural communication. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response using numbered sections as outlined above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of gesture recognition, natural language processing, embodied cognition, and cross-cultural communication.",
            "The system design effectively integrates gesture recognition with natural language processing for the specified gesture type, cultural context, and linguistic domain.",
            "The approach to embodied cognition is well-explained and meaningfully incorporated into the system design.",
            "The response adequately covers all seven required sections with appropriate detail and within the specified word limits.",
            "The gesture-language mapping process is clearly explained and takes into account the cultural context.",
            "Cross-cultural considerations are thoughtfully addressed, including potential challenges and adaptation strategies.",
            "The proposed evaluation metrics and experimental design are appropriate and well-justified.",
            "Ethical and societal implications are thoroughly explored with relevant examples.",
            "The response uses technical terminology appropriately and provides clear explanations for complex concepts.",
            "The overall response demonstrates strong interdisciplinary knowledge integration, creative system design, and innovative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
