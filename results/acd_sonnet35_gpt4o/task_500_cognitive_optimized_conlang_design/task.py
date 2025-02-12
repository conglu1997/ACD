import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "purpose": "enhancing spatial reasoning",
                "constraint": "must use a three-dimensional writing system"
            },
            {
                "purpose": "facilitating rapid information transfer between AI systems",
                "constraint": "must be easily encodable in binary"
            },
            {
                "purpose": "improving human-AI collaboration in creative tasks",
                "constraint": "must incorporate both visual and auditory elements"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) optimized for the purpose of {t['purpose']}, with the constraint that it {t['constraint']}. Your task is to:

1. Language Design (300-350 words):
   a) Describe the key features of your conlang, explaining how they address the given purpose and constraint.
   b) Provide examples of at least 5 words or phrases in your conlang, with translations and explanations of their structure.
   c) Explain the grammar and syntax of your conlang, including any unique features that support its purpose.

2. Cognitive Science Analysis (200-250 words):
   a) Analyze how your conlang's design aligns with principles of cognitive science, particularly in relation to the specified purpose.
   b) Discuss potential cognitive benefits and challenges for humans learning and using this language.

3. Computational Linguistics Considerations (200-250 words):
   a) Explain how your conlang's design facilitates or challenges natural language processing and generation by AI systems.
   b) Describe potential applications of your conlang in AI research or human-AI interaction.

4. Practical Implementation (200-250 words):
   a) Propose a method for teaching this language to human learners, considering cognitive science principles.
   b) Describe how this language could be integrated into existing or future technologies.
   c) Discuss potential societal impacts of adopting this language for its intended purpose.

5. Comparative Analysis (150-200 words):
   Compare and contrast your conlang with existing natural and constructed languages, highlighting its unique features and potential advantages for its specific purpose.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and computational linguistics. Be creative in your design while maintaining scientific plausibility and practical considerations.

Format your response using clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang must be designed to optimize for {t['purpose']}",
            f"The conlang must adhere to the constraint: {t['constraint']}",
            "The language design should be detailed, creative, and linguistically plausible",
            "The cognitive science analysis should be well-reasoned and grounded in established principles",
            "The computational linguistics considerations should demonstrate understanding of AI language processing",
            "The practical implementation and societal impact discussion should be thoughtful and realistic",
            "The comparative analysis should highlight unique features of the conlang",
            "The response should be well-organized with clear headings for each section",
            "The total response should be between 1050-1300 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
