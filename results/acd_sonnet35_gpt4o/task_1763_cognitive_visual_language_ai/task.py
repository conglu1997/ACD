import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_principle': 'Prototype theory',
                'visual_element': 'Shape',
                'cultural_context': 'East Asian',
                'communication_scenario': 'Expressing emotions',
                'example_concept': 'Happiness',
                'example_shape': 'Circle'
            },
            {
                'cognitive_principle': 'Conceptual metaphor theory',
                'visual_element': 'Color',
                'cultural_context': 'Middle Eastern',
                'communication_scenario': 'Conveying abstract concepts',
                'example_concept': 'Progress',
                'example_color': 'Green'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract visual languages based on cognitive principles, and apply it to cross-cultural communication scenarios. Your system should focus on the cognitive principle of {t['cognitive_principle']}, primarily utilize the visual element of {t['visual_element']}, and be tailored for {t['cultural_context']} cultural contexts. The system should be applied to the communication scenario of {t['communication_scenario']}.

Your response should include the following sections, with the specified word limits:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system integrates principles from linguistics, cognitive science, and AI.
   c) Detail how the system incorporates {t['cognitive_principle']} in its design and processing.
   d) Discuss how the system is adapted to work with {t['visual_element']} as the primary visual element.
   e) Explain how the system accounts for {t['cultural_context']} cultural contexts in its processing.

2. Visual Language Generation (250-300 words):
   a) Describe the process by which your system generates abstract visual language elements.
   b) Explain how {t['cognitive_principle']} guides the generation process.
   c) Provide an example of how the system would generate a visual representation for the concept of {t['example_concept']} using {t['visual_element']} as the primary element.
   d) Discuss how the system ensures cultural appropriateness in its generated visual language.

3. Visual Language Interpretation (250-300 words):
   a) Explain how your system interprets and derives meaning from abstract visual language elements.
   b) Describe how {t['cognitive_principle']} is applied in the interpretation process.
   c) Discuss how the system handles ambiguity or multiple possible interpretations.
   d) Provide an example of how the system would interpret a given abstract visual representation of a {t['example_shape' if 'example_shape' in t else 'example_color']} in the context of {t['communication_scenario']}.

4. Cross-Cultural Application (200-250 words):
   a) Describe how your system could be used to facilitate communication across different cultures.
   b) Explain how the system adapts its visual language for {t['cultural_context']} audiences.
   c) Discuss potential challenges in cross-cultural visual communication and how your system addresses them.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues related to using AI-generated visual languages for cross-cultural communication.
   b) Discuss how your system addresses concerns about cultural appropriation or misrepresentation.
   c) Describe limitations of your system and areas for future improvement.

6. Evaluation Framework (200-250 words):
   a) Propose a method for evaluating the effectiveness of your system in generating and interpreting visual languages.
   b) Describe how you would measure the system's performance in {t['communication_scenario']} scenarios.
   c) Explain how you would assess the cultural appropriateness and accuracy of the system's outputs.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering strictly to the word limits provided. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture clearly incorporates {t['cognitive_principle']} and is tailored for {t['cultural_context']} cultural contexts.",
            f"The visual language generation process effectively utilizes {t['visual_element']} as the primary visual element and provides a concrete example for the concept of {t['example_concept']}.",
            f"The visual language interpretation process demonstrates how the system would interpret a {t['example_shape' if 'example_shape' in t else 'example_color']} in the context of {t['communication_scenario']}.",
            f"The cross-cultural application convincingly demonstrates how the system facilitates communication in {t['communication_scenario']} scenarios for {t['cultural_context']} audiences.",
            "The response addresses ethical considerations, including cultural appropriation and misrepresentation, and acknowledges limitations of the proposed system.",
            "The evaluation framework provides a comprehensive method for assessing the system's performance, cultural appropriateness, and accuracy in generating and interpreting visual languages.",
            "The overall response demonstrates deep understanding and creative integration of linguistics, cognitive science, and AI concepts, while adhering to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
