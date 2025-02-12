import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        humor_types = [
            {
                'type': 'wordplay',
                'culture': 'British',
                'example': 'Why did the scarecrow win an award? He was outstanding in his field.'
            },
            {
                'type': 'situational comedy',
                'culture': 'Japanese',
                'example': 'A salaryman accidentally bowing to a vending machine.'
            }
        ]
        return {str(i+1): humor for i, humor in enumerate(random.sample(humor_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can simulate and analyze the cognitive processes involved in humor creation and appreciation, focusing on {t['type']} humor in {t['culture']} culture. Your response should include:

1. Cognitive Model (250-300 words):
   a) Describe the key cognitive processes involved in creating and appreciating {t['type']} humor.
   b) Explain how these processes might be influenced by {t['culture']} cultural norms and values.
   c) Propose a model of how these processes interact in humor comprehension and generation.

2. AI System Architecture (300-350 words):
   a) Design an AI system that implements your cognitive model for humor analysis and generation.
   b) Describe the key components of your system and how they interact.
   c) Explain how your system incorporates cultural knowledge and linguistic nuances.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.

3. Humor Analysis (200-250 words):
   a) Apply your AI system to analyze the following example of {t['type']} humor in {t['culture']} culture:
      "{t['example']}"
   b) Provide a step-by-step breakdown of how your system would process and interpret this example.
   c) Explain how your system would identify the key elements that make this example humorous.

4. Humor Generation (200-250 words):
   a) Describe how your AI system would generate a new instance of {t['type']} humor appropriate for {t['culture']} culture.
   b) Provide an example of humor your system might generate.
   c) Explain the reasoning behind each element of the generated humor.

5. Cross-cultural Adaptation (150-200 words):
   a) Discuss how your system could be adapted to analyze and generate humor in other cultures.
   b) Identify potential challenges in this cross-cultural adaptation.
   c) Propose a method for evaluating the cultural appropriateness and humor effectiveness of your system's output.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical issues in using AI for humor analysis and generation.
   b) Propose guidelines for responsible development and use of humor AI systems.

7. Reflection and Future Directions (100-150 words):
   a) Discuss the limitations of your approach and potential areas for improvement.
   b) Suggest one novel application of your humor AI system beyond entertainment.
   c) Propose a future research direction to enhance AI understanding of humor and cultural nuances.

Ensure your response demonstrates a deep understanding of cognitive science, cultural studies, linguistics, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section and subsections. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive processes involved in {t['type']} humor, particularly in {t['culture']} culture.",
            "The AI system architecture is well-designed, incorporating both cognitive and cultural elements.",
            f"The humor analysis of the given example (\"{t['example']}\") is thorough and insightful.",
            f"The generated humor example is appropriate for {t['type']} humor and {t['culture']} culture.",
            "The cross-cultural adaptation discussion is thoughtful and addresses potential challenges.",
            "Ethical considerations are adequately addressed.",
            "The reflection shows critical thinking about the system's limitations and future potential.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
