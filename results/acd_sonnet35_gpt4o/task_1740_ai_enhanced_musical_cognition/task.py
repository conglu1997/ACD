import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        cognitive_processes = [
            "auditory working memory",
            "pattern recognition",
            "emotional processing",
            "motor planning"
        ]
        musical_genres = [
            "classical",
            "jazz",
            "electronic",
            "world music"
        ]
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_genre": random.choice(musical_genres)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and enhances human musical cognition and creativity in composition, focusing on the musical element of {t['musical_element']}, the cognitive process of {t['cognitive_process']}, and the musical genre of {t['musical_genre']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for modeling and enhancing musical cognition and creativity.
   b) Explain how your system incorporates principles from cognitive science, music theory, and artificial intelligence.
   c) Discuss how your system models the specified cognitive process in the context of musical composition.
   d) Explain how your system addresses the given musical element and genre.

2. Cognitive-Musical Mapping (200-250 words):
   a) Describe how your system represents and processes the specified musical element.
   b) Explain the mechanisms for modeling the given cognitive process in the context of musical composition.
   c) Discuss how your system integrates these cognitive and musical aspects to enhance creativity.
   d) Provide an example of how your system might generate or modify a musical idea based on this integration.

3. Learning and Adaptation (200-250 words):
   a) Explain how your system learns from existing musical compositions and human cognitive patterns.
   b) Describe the training process and data requirements for your system.
   c) Discuss how your system adapts to individual users' musical styles and cognitive preferences.
   d) Address potential challenges in balancing machine learning with preserving human creativity.

4. Creative Enhancement Features (250-300 words):
   a) Describe specific features of your system designed to enhance human musical creativity.
   b) Explain how these features interact with the modeled cognitive process and musical element.
   c) Discuss how your system maintains a balance between AI assistance and human creative control.
   d) Propose a novel technique for creative enhancement specific to the given musical genre.

5. Evaluation and Analysis (200-250 words):
   a) Propose methods to evaluate the effectiveness of your system in enhancing musical creativity.
   b) Describe potential experiments to compare human-only compositions with those created using your AI system.
   c) Discuss how you would analyze the impact of your system on the cognitive process involved in musical composition.
   d) Address potential biases or limitations in evaluating AI-enhanced musical creativity.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI to enhance human creativity in music.
   b) Address concerns about AI potentially replacing human composers or homogenizing musical styles.
   c) Propose guidelines for the responsible development and use of AI in musical composition.
   d) Suggest future research directions or expansions of your system to other areas of artistic creation.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence. Use appropriate terminology from all fields and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively models and enhances creativity related to the musical element of {t['musical_element']}, the cognitive process of {t['cognitive_process']}, and the musical genre of {t['musical_genre']}",
            "The response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence",
            "The proposed AI system is innovative and scientifically plausible",
            "The response addresses all required sections with appropriate depth and clarity",
            "The system architecture and cognitive-musical mapping are well-explained and theoretically grounded",
            "The learning, adaptation, and creative enhancement features are well-designed and could yield meaningful improvements in musical creativity",
            "The evaluation methods and ethical considerations are thoughtfully discussed",
            "The response proposes novel ideas or techniques for enhancing musical creativity through AI"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
