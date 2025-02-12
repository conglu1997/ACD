import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_journeys = [
            {
                "journey": "From grief to acceptance",
                "description": "A progression from deep sorrow through stages of denial, anger, and bargaining, finally arriving at a sense of peace and acceptance."
            },
            {
                "journey": "Falling in love",
                "description": "The emotional arc of meeting someone new, experiencing initial attraction, going through uncertainty and vulnerability, and finally embracing deep affection and commitment."
            }
        ]
        return {str(i+1): journey for i, journey in enumerate(emotional_journeys)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that maps emotions to musical elements, use it to compose a piece of music representing a complex emotional journey, and analyze its potential impact on human listeners and AI music generation. Focus on the emotional journey: {t['journey']} - {t['description']}

Your response should include the following sections:

1. Emotion-Music Mapping System (250-300 words):
   a) Design a system that maps specific emotions to musical elements (e.g., key, tempo, rhythm, instrumentation).
   b) Explain the rationale behind your mappings, drawing from music theory and psychology.
   c) Provide at least five example mappings, covering a range of emotions.
   d) Discuss how your system accounts for cultural differences in emotional interpretation of music.

2. Musical Composition (250-300 words):
   a) Use your mapping system to compose a piece of music representing the given emotional journey.
   b) Describe the structure of your composition, including how it progresses through the emotional stages.
   c) Explain your choice of key musical elements (e.g., key changes, tempo shifts, instrumental choices) for each stage of the journey.
   d) Discuss any challenges you encountered in translating the emotional journey into music and how you addressed them.

3. Listener Impact Analysis (200-250 words):
   a) Predict how human listeners might respond emotionally and physiologically to your composition.
   b) Discuss potential therapeutic applications of your emotion-mapped music.
   c) Analyze how cultural background or musical training might affect a listener's interpretation of your piece.
   d) Propose an experiment to test the emotional impact of your composition on human listeners.

4. AI Music Generation Implications (200-250 words):
   a) Discuss how your emotion-music mapping system could be used to train an AI for emotion-aware music generation.
   b) Analyze potential challenges in teaching an AI to understand and reproduce the nuanced emotional content of music.
   c) Explore how AI-generated emotion-mapped music might differ from human-composed pieces.
   d) Discuss ethical considerations in using AI to generate emotionally impactful music.

5. Future Directions (100-150 words):
   a) Propose two potential enhancements or applications of your emotion-music mapping system.
   b) Discuss how these developments might influence the fields of music therapy, AI-assisted composition, or emotional intelligence in AI.

Ensure your response demonstrates a deep understanding of music theory, psychology of emotions, and AI capabilities. Be creative in your approach while maintaining scientific plausibility. Format your response with clear headings for each section, and number your answers according to the structure provided. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The emotion-music mapping system must include at least five specific example mappings.",
            "The musical composition description should clearly relate to the given emotional journey.",
            "The response must include a proposed experiment to test the emotional impact of the composition.",
            "The AI music generation implications section should address both potential benefits and challenges.",
            "The response must follow the provided structure and word count guidelines.",
            "The overall response should demonstrate interdisciplinary thinking, creativity, and a deep understanding of music, psychology, and AI concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
