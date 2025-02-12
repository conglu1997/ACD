import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "culture": "Desert nomads with a rich oral tradition",
                "base_script": "Syllabary",
                "linguistic_feature": "Tonal language with four distinct tones"
            },
            {
                "culture": "Advanced underwater civilization",
                "base_script": "Logographic",
                "linguistic_feature": "Extensive use of evidentiality markers"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fictional writing system for the following culture and linguistic parameters:

Culture: {t['culture']}
Base Script Type: {t['base_script']}
Key Linguistic Feature: {t['linguistic_feature']}

Your task is to:

1. Writing System Design (250-300 words):
   a) Describe the key features of your writing system, explaining how it reflects the culture and linguistic feature.
   b) Explain how you've adapted the base script type to suit the culture and language.
   c) Provide examples of at least 5 basic symbols or characters in your system, describing what they represent.
   d) Explain any unique aspects of your writing system that make it particularly suited to the given culture.

2. Cultural Integration (150-200 words):
   a) Describe how this writing system would be used in the society.
   b) Explain any cultural or religious significance attached to writing in this culture.
   c) Discuss how the writing system might influence or be influenced by the culture's art, architecture, or daily life.

3. Linguistic Analysis (200-250 words):
   a) Explain how your writing system accounts for the key linguistic feature mentioned.
   b) Describe any challenges you encountered in incorporating this feature and how you resolved them.
   c) Discuss how this writing system might influence the development or evolution of the language.

4. Sample Text (100-150 words):
   a) Provide a short sample text written in your system (you can use English approximations for the symbols).
   b) Translate the text to English.
   c) Explain any notable features of the sample text that demonstrate the writing system's characteristics.

5. Decoding Challenge (100-150 words):
   a) Create a short encoded message using your writing system (again, you can use English approximations).
   b) Provide 3-4 clues that would help someone decode your message.
   c) Explain the solution to your decoding challenge.

Ensure your response is creative yet grounded in real linguistic principles. Use appropriate linguistic terminology where relevant and provide clear explanations for your design choices.

Format your response with clear headings for each section. Your total response should be between 800-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections.",
            "The writing system design is creative, coherent, and reflects the given culture and linguistic feature.",
            "The cultural integration and linguistic analysis demonstrate a deep understanding of writing systems and their societal impacts.",
            "The sample text and decoding challenge effectively illustrate the writing system's characteristics.",
            "The response uses appropriate linguistic terminology and provides clear explanations for design choices."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
