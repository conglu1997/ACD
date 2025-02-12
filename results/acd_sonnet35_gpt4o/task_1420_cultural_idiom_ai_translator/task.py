import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'source_language': 'Japanese',
                'target_language': 'English',
                'idiom': '猫の手も借りたい',
                'literal_translation': 'Want to borrow even a cat\'s paw',
                'context': 'A busy office worker during tax season'
            },
            '2': {
                'source_language': 'Spanish',
                'target_language': 'Mandarin Chinese',
                'idiom': 'Meter la pata',
                'literal_translation': 'To put the paw in',
                'context': 'A diplomat at an international conference'
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can accurately translate and explain the culturally-specific idiom from {t['source_language']} to {t['target_language']}, preserving its intended meaning and emotional impact. The idiom is \"{t['idiom']}\" (literal translation: \"{t['literal_translation']}\"), used in the context of {t['context']}.

Your response should include the following components:

1. Idiom Analysis (150-200 words):
   a) Explain the meaning and cultural significance of the idiom in its source language.
   b) Discuss any historical or cultural context that influences its usage.
   c) Analyze the emotional connotations and nuances of the idiom.

2. AI System Design (250-300 words):
   a) Outline the key components of your AI system for idiom translation.
   b) Explain how your system would process and understand the cultural context.
   c) Describe the approach for generating culturally appropriate translations.
   d) Discuss how your system would handle ambiguity and multiple interpretations.

3. Translation Output (100-150 words):
   a) Provide your system's translation of the idiom into the target language.
   b) Explain how this translation preserves the original meaning and emotional impact.
   c) Discuss any challenges in finding an equivalent expression in the target language.

4. Explanation Generation (150-200 words):
   a) Demonstrate how your AI system would generate an explanation of the idiom for speakers of the target language.
   b) Show how the explanation bridges cultural gaps and conveys implicit cultural knowledge.

5. Evaluation Metrics (150-200 words):
   a) Propose 3-4 specific metrics to evaluate the performance of your AI system.
   b) Explain how each metric assesses the accuracy, cultural appropriateness, and emotional equivalence of the translation.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of AI-driven cross-cultural communication.
   b) Address concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of your system.

7. Future Improvements (100-150 words):
   a) Suggest two potential enhancements to your system for handling more complex cultural expressions.
   b) Briefly describe how these improvements would be implemented and their expected impact.

Ensure your response demonstrates a deep understanding of both the source and target languages, their cultural contexts, and the challenges of cross-cultural communication. Be creative in your AI system design while maintaining feasibility and addressing real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1000-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the cultural and linguistic nuances of both the source and target languages.",
            "The proposed AI system design is innovative, well-explained, and addresses the challenges of cross-cultural idiom translation.",
            "The translation output and explanation effectively preserve the original meaning and emotional impact of the idiom.",
            "The evaluation metrics are specific, relevant, and well-justified for assessing the system's performance.",
            "Ethical considerations are thoughtfully addressed, with appropriate guidelines proposed for responsible use.",
            "The suggested future improvements are creative and would significantly enhance the system's capabilities.",
            "The response maintains a balance between creativity and feasibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0