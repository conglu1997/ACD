import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            'causality',
            'simultaneity',
            'entropy',
            'recursion',
            'emergence',
            'symmetry'
        ]
        return {
            '1': {'concept': random.choice(concepts)},
            '2': {'concept': random.choice(concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting a 'temporal language' - a communication system that encodes information primarily in temporal sequences rather than spatial patterns. Then, use this system to express the abstract concept of {t['concept']}. Your response should include:

1. Temporal Language Design (300-350 words):
   a) Describe the key features of your temporal language, explaining how it encodes information in time-based patterns.
   b) Detail at least three unique aspects of this language (e.g., syntax, semantics, 'phonology' of temporal units).
   c) Explain how your AI system generates and interprets this temporal language.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system that enable it to process and generate temporal sequences.
   b) Explain how the system integrates concepts from linguistics, cognitive science, and computer science.
   c) Describe any novel algorithms or techniques used in your system.

3. Expressing the Abstract Concept (250-300 words):
   a) Use your temporal language to express the concept of {t['concept']}.
   b) Provide a detailed 'translation' or explanation of how this concept is conveyed in the temporal language.
   c) Discuss any unique advantages or limitations of expressing {t['concept']} in this temporal form compared to traditional languages.
   d) Include a visual or textual representation of the temporal sequence that encodes this concept.

4. Cognitive and AI Implications (200-250 words):
   a) Analyze how creating and using this temporal language might influence AI cognitive processes.
   b) Discuss potential applications of this system in enhancing human-AI interaction or AI-AI communication.
   c) Explore how this approach might contribute to our understanding of time perception, language, and cognition.

5. Challenges and Future Directions (200-250 words):
   a) Identify at least three major challenges in developing and implementing this temporal language system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Suggest two extensions or modifications to your system for future research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering scientific plausibility throughout your response.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The temporal language design is innovative and well-explained.",
            "The AI system architecture is clearly described and integrates concepts from multiple disciplines.",
            "The abstract concept is expressed effectively in the temporal language, with a clear explanation provided.",
            "The cognitive and AI implications are thoughtfully analyzed.",
            "Challenges and future directions are identified and discussed insightfully.",
            "The response is well-structured and adheres to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
