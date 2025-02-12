import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Chinese",
                "key_concepts": ["harmony", "balance", "nature"],
                "abstract_idea": "wisdom",
                "example_visual_metaphor": "A gnarled old tree with deep roots",
                "cultural_context": "Confucian philosophy emphasizes harmony with nature and respect for elders"
            },
            {
                "name": "Navajo",
                "key_concepts": ["harmony", "balance", "nature", "spirituality"],
                "abstract_idea": "balance",
                "example_visual_metaphor": "A sand painting depicting the four sacred mountains",
                "cultural_context": "Navajo culture views the world through the concept of hózhó, which represents balance and beauty"
            },
            {
                "name": "Ancient Egyptian",
                "key_concepts": ["afterlife", "divine order", "duality"],
                "abstract_idea": "eternity",
                "example_visual_metaphor": "The ouroboros (snake eating its own tail)",
                "cultural_context": "Ancient Egyptian beliefs centered around the cycle of death and rebirth, and the maintenance of cosmic order"
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting visual metaphors for the {t['name']} culture, focusing on their key cultural concepts {t['key_concepts']}. Consider the following cultural context: {t['cultural_context']}. Your task is to:

1. Visual Metaphor Analysis Framework (250-300 words):
   a) Explain the cognitive processes involved in understanding and creating visual metaphors.
   b) Describe how your AI system would implement these processes.
   c) Discuss how visual metaphors differ in the {t['name']} culture compared to Western cultures, considering cultural and cognitive factors.
   d) Explain how your system would account for the given cultural context in its analysis.

2. AI System Architecture (250-300 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Detail the components for visual processing, cultural knowledge representation, and metaphor generation/interpretation.
   c) Explain how the system handles context-dependent meaning and cultural nuances in visual metaphors.
   d) Describe any novel approaches or algorithms your system employs to address the challenges of cross-cultural visual metaphor processing.

3. Visual Metaphor Generation (250-300 words):
   a) Generate a complex visual metaphor in the {t['name']} cultural context that expresses the abstract idea of "{t['abstract_idea']}".
   b) Describe the generated visual metaphor in detail, explaining its components, symbolic meanings, and how it incorporates multiple layers of cultural significance.
   c) Explain the system's process for creating this visual metaphor, including any challenges encountered and how they were overcome.
   d) Discuss how your system ensures the generated metaphor is culturally appropriate and meaningful.

4. Visual Metaphor Interpretation (200-250 words):
   a) Describe how your AI system would interpret and explain the following {t['name']} visual metaphor: "{t['example_visual_metaphor']}".
   b) Address potential challenges in cultural and cognitive differences in interpretation.
   c) Explain how your system would handle ambiguity or multiple interpretations.
   d) Discuss how your system would validate its interpretation against cultural norms and expert knowledge.

5. Evaluation and Refinement (200-250 words):
   a) Propose a comprehensive method for evaluating the cultural appropriateness and effectiveness of the generated visual metaphors.
   b) Describe how your AI system would improve its process based on feedback from cultural experts and user interactions.
   c) Suggest specific metrics for measuring the system's performance in cross-cultural visual metaphor generation and interpretation.
   d) Outline a strategy for continuous learning and adaptation of the system to new cultural contexts.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical implications and societal impacts of an AI system capable of generating and interpreting cross-cultural visual metaphors.
   b) Address the importance of cultural sensitivity and potential misuse or misinterpretation of such a system.
   c) Propose detailed guidelines for responsible development and use of this technology.
   d) Discuss how your system could contribute to cross-cultural understanding and communication.

Ensure your response demonstrates a deep understanding of visual cognition, cultural studies, and AI system design. Be creative and innovative while maintaining scientific rigor and cultural sensitivity. Your total response should be between 1300-1600 words.

Format your response with clear headings for each section, numbered as above. Use appropriate subheadings where necessary to organize your thoughts clearly. Conclude with a brief summary (50-100 words) of the key innovations and potential impact of your proposed AI system."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design must be tailored to the {t['name']} culture, considering their key cultural concepts and the provided cultural context",
            "The visual metaphor analysis framework should be cognitively plausible, culturally sensitive, and demonstrate a deep understanding of both cognitive processes and cultural factors",
            "The system architecture should be logically consistent, technologically plausible, and include novel approaches to cross-cultural visual metaphor processing",
            f"The response should provide a specific, complex example of visual metaphor generation for the concept of '{t['abstract_idea']}', incorporating multiple layers of cultural significance",
            f"The response should include a detailed interpretation of the given {t['name']} visual metaphor: '{t['example_visual_metaphor']}', addressing potential challenges and ambiguities",
            "The analysis should consider cultural appropriateness, cognitive processes, and ethical implications in depth",
            "The response should discuss challenges and limitations specific to cross-cultural visual metaphor AI, proposing innovative solutions",
            "The proposed evaluation methods and future improvements should be comprehensive, relevant, and insightful",
            "The response should demonstrate exceptional interdisciplinary knowledge integration across visual cognition, cultural studies, and AI",
            "The response should be formatted with clear headings for each section, numbered as instructed, and include a concluding summary",
            "The total response should be between 1300-1600 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
