import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_elements = [
            "Tonal system (e.g., major/minor scales, modes)",
            "Rhythmic patterns",
            "Harmonic progressions",
            "Melodic contours",
            "Timbre and instrumentation"
        ]
        applications = [
            "Non-verbal communication for individuals with speech impairments",
            "Interspecies communication",
            "Encoding complex emotional states",
            "Data sonification for scientific analysis",
            "Cross-cultural diplomacy"
        ]
        return {
            "1": {
                "language_elements": random.sample(language_elements, 3),
                "application": random.choice(applications)
            },
            "2": {
                "language_elements": random.sample(language_elements, 3),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a musical language system and analyze its implications. Your task includes:

1. Language Design (300-350 words):
   a) Create a language system using the following musical elements: {', '.join(t['language_elements'])}.
   b) Explain how each element contributes to conveying meaning.
   c) Provide at least three examples of 'phrases' in your language, explaining their construction and meaning.
   d) Include a simple musical notation or representation for one of your example phrases.
   e) Describe the basic 'grammar' or rules of your musical language.

2. Cognitive Analysis (200-250 words):
   a) Analyze how your musical language might be processed by the human brain.
   b) Compare and contrast the cognitive load of your system with traditional spoken/written languages.
   c) Discuss potential advantages or challenges in learning and using this language.

3. Application Exploration (200-250 words):
   Explore how your musical language could be applied to: {t['application']}
   a) Describe specific use cases within this application.
   b) Discuss potential benefits and limitations of using your musical language in this context.
   c) Propose one innovation that could enhance the effectiveness of your language in this application.

4. Cross-domain Implications (150-200 words):
   a) Discuss how your musical language system might influence or be influenced by other domains (e.g., psychology, neuroscience, computer science).
   b) Propose a research question that arises from the intersection of your musical language with another field.

5. Ethical Considerations (100-150 words):
   Identify and discuss at least two potential ethical issues or societal impacts of implementing your musical language system.

Ensure your response demonstrates a deep understanding of linguistics, music theory, and cognitive science. Be creative in your design while maintaining scientific plausibility. Use clear headings for each section, and aim for a total response between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts.",
            "The musical language design is creative, coherent, and effectively uses the specified musical elements.",
            "A simple musical notation or representation is provided for one example phrase.",
            "The cognitive analysis demonstrates a strong understanding of language processing and cognitive science principles.",
            "The application exploration is thorough and presents innovative ideas for using the musical language.",
            "Cross-domain implications and ethical considerations are thoughtfully discussed.",
            "The overall response shows a deep integration of knowledge from linguistics, music theory, and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
