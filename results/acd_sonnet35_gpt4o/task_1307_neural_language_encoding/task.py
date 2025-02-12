import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        texts = [
            {
                "title": "The Raven",
                "author": "Edgar Allan Poe",
                "genre": "poetry"
            },
            {
                "title": "A Brief History of Time",
                "author": "Stephen Hawking",
                "genre": "non-fiction"
            }
        ]
        return {str(i+1): text for i, text in enumerate(texts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language encoding system inspired by neural networks and cognitive science, then use it to represent and analyze the text '{t['title']}' by {t['author']} (genre: {t['genre']}). Your task has the following components:

1. Encoding System Design (300-350 words):
   a) Describe the key features of your neural-inspired language encoding system.
   b) Explain how your system incorporates principles from neural networks and cognitive science.
   c) Detail how your system represents different linguistic elements (e.g., words, syntax, semantics).
   d) Provide at least 3 example encodings of common words or phrases, explaining their neural representation.

2. Text Analysis Process (250-300 words):
   a) Outline the steps to encode the given text using your system.
   b) Explain how your system would process and analyze the encoded text.
   c) Describe any unique insights or patterns your system might reveal about the text's structure or content.

3. Cognitive Science Connections (200-250 words):
   a) Discuss how your encoding system parallels or differs from human language processing.
   b) Explain how your system might shed light on cognitive processes involved in language comprehension.

4. AI Applications (200-250 words):
   a) Propose two novel AI applications that could benefit from your neural language encoding system.
   b) Explain how these applications might improve upon current language processing technologies.

5. Limitations and Future Directions (150-200 words):
   a) Identify at least two limitations of your proposed system.
   b) Suggest areas for future research or improvements.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The encoding system design must clearly incorporate principles from both neural networks and cognitive science.",
            "The text analysis process should be logically consistent with the proposed encoding system.",
            "The response should demonstrate a deep understanding of cognitive science and its relation to language processing.",
            "The proposed AI applications should be innovative and clearly benefit from the neural language encoding system.",
            "The limitations and future directions should show critical thinking about the proposed system.",
            "The overall response should exhibit high-level interdisciplinary thinking and creativity in approaching the complex problem of neural-inspired language encoding."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
