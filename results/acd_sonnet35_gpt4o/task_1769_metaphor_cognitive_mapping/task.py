import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_domain": "journey",
                "target_domain": "life",
                "cultural_context": "Western",
                "example_metaphor": "Life is a winding road with many crossroads."
            },
            {
                "source_domain": "harmony",
                "target_domain": "social relationships",
                "cultural_context": "East Asian",
                "example_metaphor": "A harmonious family is like a well-tuned orchestra."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive model for metaphor comprehension and generation, focusing on the metaphor '{t['source_domain']} is {t['target_domain']}' in the {t['cultural_context']} cultural context. Then, use your model to analyze existing metaphors and create novel ones. Your response should include:

1. Cognitive Model Design (300-350 words):
   a) Describe the key components of your cognitive model for metaphor processing.
   b) Explain how your model represents and maps conceptual domains.
   c) Detail the processes involved in comprehending and generating metaphors.
   d) Discuss how your model incorporates cultural context in metaphor processing.
   e) Include a diagram or flowchart of your model (describe it textually).

2. Metaphor Analysis (250-300 words):
   a) Use your model to analyze the given metaphor: "{t['example_metaphor']}"
   b) Explain the conceptual mappings and inferences in this metaphor.
   c) Discuss how the {t['cultural_context']} cultural context influences the interpretation.
   d) Identify potential challenges in comprehending this metaphor across cultures.

3. Novel Metaphor Generation (250-300 words):
   a) Use your model to generate two novel metaphors for the target domain '{t['target_domain']}'.
   b) Explain the reasoning behind your choices of source domains.
   c) Describe how your model ensures these metaphors are culturally appropriate.
   d) Discuss any creative or unexpected mappings that emerged in this process.

4. Cross-Cultural Adaptation (200-250 words):
   a) Propose how your model would adapt the original metaphor for a different cultural context.
   b) Explain the changes in conceptual mapping or expression.
   c) Discuss challenges and strategies in preserving metaphor meaning across cultures.

5. Computational Implementation (250-300 words):
   a) Describe how you would implement your cognitive model in a computational system.
   b) Explain any AI or machine learning techniques you would use.
   c) Discuss potential challenges in implementing metaphor processing in AI systems.
   d) Propose metrics for evaluating the performance of your computational model.

6. Implications and Future Directions (150-200 words):
   a) Discuss the implications of your model for understanding human cognition and creativity.
   b) Explore potential applications in fields such as AI, education, or cross-cultural communication.
   c) Suggest future research directions to extend or improve your model.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and cultural studies. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and length.",
            "The cognitive model design is well-explained, incorporates cultural context, and includes a clear diagram description.",
            f"The metaphor analysis demonstrates a deep understanding of conceptual mappings and cultural influences, specifically for the example metaphor: '{t['example_metaphor']}'.",
            f"The novel metaphor generation shows creativity and cultural appropriateness for the target domain '{t['target_domain']}'.",
            "The cross-cultural adaptation discussion is insightful and addresses challenges effectively.",
            "The computational implementation proposal is feasible, well-reasoned, and includes specific AI or machine learning techniques.",
            "The implications and future directions are thoughtfully considered and relevant to multiple fields.",
            "The response format follows the specified structure with clear headings and includes a word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
