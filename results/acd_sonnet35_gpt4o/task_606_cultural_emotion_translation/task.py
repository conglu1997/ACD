import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_culture': 'Japanese',
                'target_culture': 'Brazilian',
                'emotional_concept': 'Mono no aware (物の哀れ)',
                'context': 'Viewing cherry blossoms'
            },
            {
                'source_culture': 'Danish',
                'target_culture': 'Nigerian (Yoruba)',
                'emotional_concept': 'Hygge',
                'context': 'Family gathering'
            },
            {
                'source_culture': 'Russian',
                'target_culture': 'Indian (Hindi)',
                'emotional_concept': 'Toska (тоска)',
                'context': 'Reminiscing about childhood'
            },
            {
                'source_culture': 'German',
                'target_culture': 'Thai',
                'emotional_concept': 'Waldeinsamkeit',
                'context': 'Hiking in a dense forest'
            },
            {
                'source_culture': 'Arabic (Lebanese)',
                'target_culture': 'Finnish',
                'emotional_concept': 'Ya\'aburnee (يقبرني)',
                'context': 'Elderly couple celebrating anniversary'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Design an AI system capable of translating complex emotional states across cultures, considering linguistic, contextual, and cultural factors. Your task is to translate the emotional concept of {t['emotional_concept']} from {t['source_culture']} culture to {t['target_culture']} culture in the context of {t['context']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for cultural emotion translation.
   b) Explain how your system incorporates linguistic, psychological, and anthropological knowledge.
   c) Discuss any novel elements in your design that enable nuanced emotional translation across cultures.

2. Emotional Concept Analysis (150-200 words):
   a) Analyze the emotional concept {t['emotional_concept']} in the context of {t['source_culture']} culture.
   b) Explain its cultural significance and the nuances that make it unique to this culture.
   c) Describe how this emotion is typically expressed linguistically and behaviorally in {t['source_culture']} culture.

3. Cultural Translation Process (200-250 words):
   a) Describe how your AI system would translate {t['emotional_concept']} to a comparable emotional expression in {t['target_culture']} culture.
   b) Explain how your system accounts for the specific context of {t['context']}.
   c) Provide an example of how this emotion might be expressed in {t['target_culture']} culture, including linguistic and behavioral aspects.

4. Challenges and Solutions (150-200 words):
   a) Identify at least two major challenges in translating this emotional concept across these specific cultures.
   b) Propose solutions to these challenges, explaining how your AI system would implement them.

5. Evaluation Methodology (100-150 words):
   a) Propose a method to evaluate the accuracy and cultural appropriateness of your system\'s emotional translation.
   b) Describe metrics you would use to assess both linguistic and cultural fidelity.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for cross-cultural emotional translation.
   b) Propose guidelines to ensure responsible and culturally sensitive use of such a system.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Briefly describe how these extensions could enhance cross-cultural emotional understanding.

Ensure your response demonstrates a deep understanding of emotional intelligence, cultural anthropology, linguistics, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and cultural plausibility.

Format your response using clear headings for each section (e.g., \'1. System Architecture\', \'2. Emotional Concept Analysis\', etc.). Your total response should be between 1000-1350 words. Include a word count at the end of your response.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified emotional concept and its cultural context.",
            "The system architecture is well-designed and incorporates relevant interdisciplinary knowledge.",
            "The cultural translation process is thoughtfully explained and culturally sensitive.",
            "Challenges are accurately identified and creative solutions are proposed.",
            "The evaluation methodology and ethical considerations are well-reasoned and appropriate.",
            "The response is well-structured, following the specified format with clear headings for each section.",
            "The proposed AI system is innovative and plausible, demonstrating a strong grasp of both emotional intelligence and cultural nuances.",
            "The response includes all required sections: System Architecture, Emotional Concept Analysis, Cultural Translation Process, Challenges and Solutions, Evaluation Methodology, Ethical Considerations, and Future Directions.",
            "The total word count is between 1000-1350 words, as specified in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
