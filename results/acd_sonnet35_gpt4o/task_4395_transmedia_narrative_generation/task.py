import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        narrative_themes = [
            "dystopian future",
            "time travel paradox",
            "alien first contact",
            "artificial intelligence rebellion",
            "parallel universe exploration"
        ]
        media_formats = [
            "social media posts",
            "interactive website",
            "podcast series",
            "virtual reality experience",
            "graphic novel",
            "augmented reality game",
            "short film"
        ]
        cultural_contexts = [
            "Western",
            "East Asian",
            "Middle Eastern",
            "African",
            "Latin American",
            "South Asian",
            "Oceanian"
        ]
        return {
            "1": {
                "theme": random.choice(narrative_themes),
                "formats": random.sample(media_formats, 3),
                "cultural_context": random.choice(cultural_contexts)
            },
            "2": {
                "theme": random.choice(narrative_themes),
                "formats": random.sample(media_formats, 3),
                "cultural_context": random.choice(cultural_contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a transmedia narrative system that creates and analyzes stories across multiple platforms. Your task is to develop a coherent narrative on the theme of '{t['theme']}' that spans the following media formats: {', '.join(t['formats'])}. The narrative should be culturally relevant to a {t['cultural_context']} context.

Your response should include:

1. Narrative Overview (250-300 words):
   a) Provide a synopsis of the main story, including key characters and plot points.
   b) Explain how the narrative theme is explored across the different media formats.
   c) Describe how the cultural context influences the story and its presentation.

2. Media-Specific Content (300-350 words):
   a) For each of the three media formats, describe specific content or elements of the story that would be presented.
   b) Explain how each format leverages its unique characteristics to enhance the narrative.
   c) Discuss how the different media components interconnect and complement each other.

3. Transmedia Coherence (200-250 words):
   a) Explain the strategies used to maintain narrative consistency across the different media formats.
   b) Describe how the system ensures that each media component can stand alone while also contributing to the larger narrative.
   c) Discuss any challenges in adapting the story across diverse platforms and how they are addressed.

4. Cultural Integration (200-250 words):
   a) Analyze how the {t['cultural_context']} context is reflected in the narrative and its presentation across media formats.
   b) Discuss any cultural-specific elements, symbols, or themes incorporated into the story.
   c) Explain how the system ensures cultural authenticity and avoids stereotypes or misrepresentations.

5. Audience Engagement (150-200 words):
   a) Describe strategies for encouraging audience participation and interaction with the transmedia narrative.
   b) Explain how the system adapts the narrative based on audience feedback or choices.
   c) Discuss potential methods for measuring audience engagement across the different platforms.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to creating AI-generated transmedia narratives.
   b) Discuss how the system addresses concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of AI in transmedia storytelling.

Ensure your response demonstrates a deep understanding of narrative structures, media-specific storytelling techniques, and cultural nuances. Be creative in your approach while maintaining coherence across the transmedia elements. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a coherent narrative overview that effectively incorporates the given theme and cultural context.",
            "The media-specific content is well-described and leverages the unique characteristics of each format.",
            "The explanation of transmedia coherence demonstrates a strong understanding of maintaining narrative consistency across platforms.",
            "The cultural integration analysis shows depth and sensitivity to the specified cultural context.",
            "The audience engagement strategies are innovative and appropriate for a transmedia narrative.",
            "The ethical considerations are thoughtfully addressed, with relevant guidelines proposed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
