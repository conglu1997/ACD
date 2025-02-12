import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_traditions = [
            {
                "tradition1": "Western classical",
                "tradition2": "Indian classical",
                "element": "Harmony"
            },
            {
                "tradition1": "Jazz",
                "tradition2": "African drumming",
                "element": "Rhythm"
            },
            {
                "tradition1": "Chinese opera",
                "tradition2": "Flamenco",
                "element": "Melody"
            },
            {
                "tradition1": "Electronic dance music",
                "tradition2": "Gamelan",
                "element": "Timbre"
            }
        ]
        return {
            "1": random.choice(musical_traditions),
            "2": random.choice(musical_traditions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of composing original music that fuses elements from {t['tradition1']} and {t['tradition2']} musical traditions, with a focus on the musical element of {t['element']}. Then, analyze its output and implications for creativity and cultural exchange. Your response should include:

1. AI Composer System Design (300-350 words):
   a) Describe the overall architecture of your AI music composition system.
   b) Explain how it incorporates knowledge of both {t['tradition1']} and {t['tradition2']} musical traditions.
   c) Detail how your system specifically handles the musical element of {t['element']}.
   d) Discuss any novel approaches or algorithms used in your design.

2. Musical Knowledge Integration (250-300 words):
   a) Explain how your system represents and combines musical elements from different traditions.
   b) Describe the challenges in merging {t['tradition1']} and {t['tradition2']} approaches to {t['element']}.
   c) Discuss how your system maintains cultural authenticity while creating fusion compositions.

3. Composition Process (200-250 words):
   a) Outline the step-by-step process your AI system uses to compose a piece of music.
   b) Explain how it balances elements from both musical traditions.
   c) Describe how the system ensures musical coherence and aesthetic value in its compositions.

4. Output Analysis (250-300 words):
   a) Provide a detailed description of a hypothetical piece composed by your AI system.
   b) Analyze how this piece incorporates elements from both musical traditions.
   c) Discuss the strengths and potential shortcomings of the AI-generated composition.
   d) Include a simple musical notation or representation (e.g., a short melody, rhythm pattern, or chord progression) of a key section from your AI-generated composition.

5. Creativity and Cultural Implications (200-250 words):
   a) Discuss the implications of your AI system for understanding musical creativity.
   b) Analyze potential impacts on cultural exchange and preservation of musical traditions.
   c) Explore how this technology might influence the future of music composition and cross-cultural collaboration.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to AI-generated cross-cultural music.
   b) Discuss concerns about cultural appropriation and how your system addresses them.
   c) Propose guidelines for the responsible development and use of AI in music composition.

7. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your AI composer system.
   b) Propose a research question that could further explore the intersection of AI, music, and cultural exchange.
   c) Discuss potential applications of your technology beyond music composition.

Ensure your response demonstrates a deep understanding of music theory, cultural studies, and AI technologies. Use appropriate musical and technical terminology, providing clear explanations for complex concepts. Be creative and innovative in your approach while maintaining cultural sensitivity and technical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1850 words.

Note: Your response will be evaluated based on the completeness and quality of each section, the depth of understanding demonstrated, the creativity and plausibility of your AI system design, and your consideration of cultural and ethical implications. A perfect score requires addressing all points thoroughly while staying within the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all seven sections as specified in the instructions.",
            f"The AI system design incorporates knowledge of both {t['tradition1']} and {t['tradition2']} musical traditions.",
            f"The response demonstrates a deep understanding of the musical element of {t['element']}.",
            "The composition process and output analysis are detailed and plausible.",
            "The response includes a simple musical notation or representation of the AI-generated composition.",
            "The response shows cultural sensitivity and awareness of ethical implications.",
            "The discussion of creativity and cultural implications is thoughtful and well-reasoned.",
            "The response uses appropriate musical and technical terminology.",
            "The total response is between 1550-1850 words."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
