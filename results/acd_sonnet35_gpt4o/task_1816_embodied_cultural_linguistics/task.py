import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                'name': 'Japanese',
                'gesture': 'Bowing',
                'context': 'Formal greeting'
            },
            {
                'name': 'Italian',
                'gesture': 'Hand purse',
                'context': 'Expressing skepticism'
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(cultures)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates multimodal language processing with principles of embodied cognition to interpret and generate culturally-specific gestures and expressions. Then, apply your system to analyze and generate the '{t['gesture']}' gesture in {t['name']} culture, used in the context of '{t['context']}'. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for multimodal language processing and embodied cognition.
   b) Explain how your system integrates visual, linguistic, and kinesthetic information.
   c) Detail how your system incorporates cultural knowledge and context.
   d) Provide a diagram or flowchart of your system's architecture (describe it textually).

2. Gesture Analysis (250-300 words):
   a) Use your system to analyze the given gesture in its cultural context.
   b) Explain how your system interprets the gesture's physical components, associated linguistic elements, and cultural significance.
   c) Discuss how embodied cognition principles enhance your system's understanding of the gesture.

3. Gesture Generation (250-300 words):
   a) Describe how your system would generate the given gesture, including physical movement, timing, and accompanying verbal/facial expressions.
   b) Explain how your system ensures cultural authenticity in gesture production.
   c) Discuss any challenges in translating embodied cultural knowledge into AI-generated actions.

4. Cross-cultural Application (200-250 words):
   a) Explain how your system would handle the same gesture or context in a different culture.
   b) Discuss potential misunderstandings or faux pas that could arise from cultural differences in embodied communication.
   c) Propose a method for your system to adapt to new cultural contexts.

5. Ethical and Social Implications (200-250 words):
   a) Discuss ethical considerations in developing AI systems that interpret and generate culturally-specific embodied communication.
   b) Analyze potential social impacts of AI systems that can engage in culturally-authentic nonverbal communication.
   c) Propose guidelines for responsible development and use of such technology.

6. Future Directions (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how this technology might impact fields such as cross-cultural communication, anthropology, or human-computer interaction.
   c) Propose a related challenge in embodied cultural linguistics that could be addressed using a similar approach.

Ensure your response demonstrates a deep understanding of multimodal language processing, embodied cognition, and cultural linguistics. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of multimodal language processing, embodied cognition, and cultural linguistics.",
            "The system architecture is well-explained and integrates visual, linguistic, and kinesthetic information effectively.",
            "The gesture analysis and generation processes are thoroughly described and culturally authentic.",
            "The cross-cultural application is thoughtfully explored, including potential challenges and adaptations.",
            "Ethical and social implications are comprehensively discussed with insightful guidelines proposed.",
            "Future directions and improvements are creative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
