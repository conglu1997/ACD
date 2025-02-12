import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Japanese",
                "concept": "Wabi-sabi (imperfection and transience)",
                "domain": "Art and aesthetics",
                "ai_technique": "Generative Adversarial Networks (GANs)"
            },
            {
                "name": "Inuit",
                "concept": "Sila (weather-wisdom and life force)",
                "domain": "Nature and spirituality",
                "ai_technique": "Recurrent Neural Networks (RNNs)"
            },
            {
                "name": "Ancient Greek",
                "concept": "Arete (excellence and virtue)",
                "domain": "Ethics and personal development",
                "ai_technique": "Transformer models"
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting culturally-specific metaphors for the {t['name']} culture, focusing on the concept of {t['concept']} in the domain of {t['domain']}. Your system must incorporate {t['ai_technique']} in its architecture. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor generation and interpretation.
   b) Explain how your system incorporates cultural knowledge and linguistic patterns.
   c) Detail how {t['ai_technique']} is integrated into your system's architecture.
   d) Discuss any novel approaches or techniques used in your design.
   e) Include a high-level diagram or pseudocode of your system's architecture.

2. Cultural and Linguistic Analysis (250-300 words):
   a) Analyze the cultural significance of {t['concept']} in {t['name']} culture.
   b) Explain how this concept is typically expressed in {t['name']} language and literature.
   c) Discuss any unique linguistic features or patterns relevant to metaphor creation in this culture.
   d) Provide two examples of existing metaphors in this culture related to {t['concept']}.

3. Metaphor Generation Process (250-300 words):
   a) Describe how your AI system would generate a metaphor related to {t['concept']}.
   b) Provide three examples of generated metaphors and explain their cultural relevance.
   c) Discuss how your system ensures the metaphors are culturally appropriate and meaningful.
   d) Explain how {t['ai_technique']} contributes to the metaphor generation process.

4. Metaphor Interpretation Capabilities (250-300 words):
   a) Explain how your AI system would interpret and analyze culturally-specific metaphors.
   b) Describe the challenges in cross-cultural metaphor interpretation and how your system addresses them.
   c) Provide an example of how your system would interpret a complex {t['name']} metaphor related to {t['concept']}.
   d) Discuss how {t['ai_technique']} enhances the interpretation process.

5. Potential Applications and Implications (200-250 words):
   a) Propose three potential applications of your cultural metaphor AI system.
   b) Discuss the implications of this technology for cross-cultural communication and understanding.
   c) Address any ethical considerations or potential misuses of AI-generated cultural metaphors.
   d) Suggest guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of linguistics, cultural studies, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining cultural authenticity and scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1250-1500 words, with each section adhering to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific {t['name']} culture and the concept of {t['concept']}",
            f"The AI system design should incorporate {t['ai_technique']} and be well-explained, integrating cultural and linguistic elements",
            "The cultural and linguistic analysis should demonstrate deep understanding of the specified culture and provide two relevant existing metaphors",
            "The metaphor generation process should be clearly described, with three culturally relevant generated metaphors provided",
            "The metaphor interpretation capabilities should be thoroughly explained, including a specific example of interpreting a complex metaphor",
            "Three potential applications and implications should be thoughtfully considered, including ethical aspects and guidelines for responsible use",
            "The response should be well-organized, using appropriate technical terminology from linguistics, cultural studies, and AI",
            "Each section should adhere to the specified word count range, with the total response between 1250-1500 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
