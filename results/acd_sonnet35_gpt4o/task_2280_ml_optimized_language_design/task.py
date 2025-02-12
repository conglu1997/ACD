import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ml_task': 'Natural Language Processing',
                'focus_area': 'Sentiment Analysis'
            },
            {
                'ml_task': 'Computer Vision',
                'focus_area': 'Object Recognition'
            },
            {
                'ml_task': 'Reinforcement Learning',
                'focus_area': 'Decision Making'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language specifically optimized for the machine learning task of {t['ml_task']}, with a focus on {t['focus_area']}. An artificial language is a constructed language designed for a specific purpose, in this case, to optimize machine learning tasks. Your language should be designed to make this specific ML task more efficient and accurate. Provide your response in the following format:

1. Language Overview (200-250 words):
   a) Describe the key features of your artificial language.
   b) Explain how these features are optimized for the given ML task and focus area.
   c) Compare your language to natural languages, highlighting key differences.

2. Phonology and Orthography (150-200 words):
   a) Describe the sound system (phonology) of your language.
   b) Explain the writing system (orthography) and how it relates to the phonology.
   c) Discuss how these aspects are optimized for machine processing.

3. Morphology and Syntax (200-250 words):
   a) Outline the word formation (morphology) rules of your language.
   b) Describe the sentence structure (syntax) and grammatical rules.
   c) Explain how these elements are designed to facilitate the specific ML task.

4. Semantics and Pragmatics (200-250 words):
   a) Describe how meaning is encoded in your language.
   b) Explain any unique semantic features that aid in the ML task.
   c) Discuss how context and usage (pragmatics) are handled in your language.

5. Computational Advantages (150-200 words):
   a) Explain how your language design improves efficiency in the given ML task.
   b) Discuss any potential improvements in accuracy or performance.
   c) Describe how your language might reduce computational complexity.

6. Learning and Adaptation (150-200 words):
   a) Describe how machine learning models would learn and adapt to your language.
   b) Explain any features that make your language easier for machines to acquire.
   c) Discuss potential challenges in implementing your language in ML systems.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using an ML-optimized language.
   b) Explain limitations of your language design, particularly in human usage.
   c) Propose guidelines for responsible development and use of ML-optimized languages.

8. Example Sentence (50-100 words):
   Provide a simple example sentence in your designed language. Include its translation to English and a brief explanation of how it demonstrates the key features of your language optimized for the given ML task.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and machine learning principles. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and machine learning principles.",
            f"The artificial language design is well-optimized for the given ML task of {t['ml_task']} and focus area of {t['focus_area']}.",
            "The language features are creative yet plausible and well-justified in terms of their optimization for machine learning.",
            "The response adequately covers all eight required sections with appropriate detail and within the specified word limits.",
            "The phonology, orthography, morphology, and syntax of the language are clearly described and optimized for machine processing.",
            "The semantics and pragmatics of the language are well-designed to facilitate the specific ML task.",
            "The computational advantages of the language design are clearly explained and justified.",
            "The response addresses how machine learning models would learn and adapt to the designed language.",
            "Ethical considerations and limitations of the language design are thoughtfully discussed.",
            "The response uses technical terminology appropriately and provides clear explanations for complex concepts.",
            "An example sentence is provided, demonstrating key features of the designed language and its optimization for the given ML task.",
            "The overall response demonstrates strong interdisciplinary knowledge integration, creative problem-solving, and understanding of linguistics, cognitive science, and machine learning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
