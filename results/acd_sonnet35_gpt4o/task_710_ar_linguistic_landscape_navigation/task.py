import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "city": "Tokyo",
                "native_language": "Japanese",
                "user_language": "English",
                "navigation_goal": "Find the nearest train station"
            },
            {
                "city": "Barcelona",
                "native_language": "Catalan and Spanish",
                "user_language": "Mandarin Chinese",
                "navigation_goal": "Locate a famous architectural landmark"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical augmented reality (AR) system that uses AI to dynamically translate and interpret the linguistic landscape of {t['city']} for a {t['user_language']} speaker, and analyze its impact on cognitive mapping and spatial navigation. The system should assist the user in achieving the navigation goal: {t['navigation_goal']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AR-AI system for real-time linguistic landscape interpretation.
   b) Explain how the system processes and translates {t['native_language']} text in the environment.
   c) Detail how the system integrates with spatial mapping and navigation functionalities.
   d) Propose a novel feature that enhances the user's understanding of the cultural context behind the linguistic landscape.

2. User Interface and Experience (200-250 words):
   a) Describe the AR interface from the user's perspective, including visual overlays and interaction methods.
   b) Explain how translated content is presented to the user in a way that preserves spatial relationships.
   c) Discuss how the system handles multi-lingual environments or code-switching scenarios.

3. Cognitive Impact Analysis (200-250 words):
   a) Analyze how this AR translation system might influence the user's cognitive mapping of {t['city']}.
   b) Discuss potential effects on spatial navigation strategies when relying on the system.
   c) Compare the cognitive processes involved in using this system versus traditional navigation methods.

4. Cultural and Linguistic Implications (150-200 words):
   a) Discuss how this technology might affect the user's engagement with the local culture and language.
   b) Analyze potential impacts on language learning and cultural immersion.
   c) Address concerns about cultural homogenization or loss of linguistic diversity.

5. Ethical Considerations and Challenges (150-200 words):
   a) Identify ethical issues related to privacy, data collection, and cultural representation.
   b) Discuss challenges in ensuring accurate translations and cultural interpretations.
   c) Propose guidelines for responsible development and use of such AR-AI systems.

6. Future Developments and Applications (150-200 words):
   a) Suggest two potential advancements or extensions of this technology.
   b) Discuss how this system could be applied to other domains beyond navigation.
   c) Speculate on the long-term implications for human-environment interactions.

Ensure your response demonstrates a deep understanding of augmented reality technology, artificial intelligence, linguistics, cognitive science, and cultural studies. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AR technology, AI, linguistics, cognitive science, and cultural studies.",
            "The system design is creative, innovative, and scientifically plausible.",
            "The analysis of cognitive impact and cultural implications is thorough and well-reasoned.",
            "Ethical considerations are comprehensively addressed.",
            f"The system effectively assists in achieving the navigation goal: {t['navigation_goal']}.",
            "The response is well-structured, clear, and adheres to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
