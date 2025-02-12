import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Arabic', 'Swahili', 'Hindi']
        conceptual_domains = ['Quantum mechanics', 'Ecosystem dynamics', 'Economic systems', 'Musical theory']
        purposes = ['Facilitating interdisciplinary scientific collaboration',
                    'Enhancing empathy and emotional communication',
                    'Optimizing decision-making in complex systems',
                    'Expressing multi-dimensional artistic concepts']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'language': random.choice(languages),
                'conceptual_domain': random.choice(conceptual_domains),
                'purpose': random.choice(purposes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates a new language by blending {t['language']} with the conceptual domain of {t['conceptual_domain']}, for the purpose of {t['purpose']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for conceptual blending and language generation.
   b) Explain how your system integrates linguistic features from {t['language']} with concepts from {t['conceptual_domain']}.
   c) Detail how the system ensures the generated language is suitable for {t['purpose']}.

2. Conceptual Blending Process (200-250 words):
   a) Explain the specific conceptual blending techniques your system uses.
   b) Provide an example of how a particular concept from {t['conceptual_domain']} would be blended with a linguistic feature from {t['language']}.
   c) Discuss how your system resolves potential conflicts or incompatibilities in the blending process.

3. Language Features (200-250 words):
   a) Describe 3-4 key features of the generated language, explaining how they reflect both the source language and conceptual domain.
   b) Provide examples of words or phrases in the new language, with translations and explanations.
   c) Explain how these features contribute to the language's intended purpose.

4. Cognitive Implications (150-200 words):
   a) Discuss how using this blended language might influence thought patterns or problem-solving approaches.
   b) Explain how this relates to the Sapir-Whorf hypothesis or other relevant theories in cognitive linguistics.

5. Practical Application (150-200 words):
   a) Describe a specific scenario where this language would be used for its intended purpose.
   b) Explain the potential benefits and challenges of using this language in practice.

6. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical implications of creating and using such a blended language.
   b) Address limitations of your approach and areas for future research or improvement.

Ensure your response demonstrates a deep understanding of linguistics, the chosen conceptual domain, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your language design while maintaining scientific plausibility.

Your total response should be between 1050-1350 words. Organize your answer using clear headings for each section, numbered as above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of conceptual blending and its application to language generation.",
            "The AI system design is innovative, logically consistent, and well-explained.",
            "The generated language features show creative integration of the source language and conceptual domain.",
            "The discussion of cognitive implications and practical applications is insightful and well-reasoned.",
            "The response addresses ethical considerations and limitations thoughtfully."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
