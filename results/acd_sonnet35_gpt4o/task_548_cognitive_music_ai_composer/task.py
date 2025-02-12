import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_models = [
            {
                "model": "Gestalt principles",
                "musical_element": "Melody",
                "genre": "Classical"
            },
            {
                "model": "Expectancy theory",
                "musical_element": "Harmony",
                "genre": "Jazz"
            },
            {
                "model": "Auditory scene analysis",
                "musical_element": "Texture",
                "genre": "Electronic"
            },
            {
                "model": "Embodied cognition",
                "musical_element": "Rhythm",
                "genre": "World music"
            }
        ]
        return {
            "1": random.choice(cognitive_models),
            "2": random.choice(cognitive_models)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an AI system that generates and evaluates musical compositions based on the cognitive model of {t['model']}, focusing on the musical element of {t['musical_element']} in the genre of {t['genre']}. Your task has five parts:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI music composition system.
   b) Explain how it incorporates the {t['model']} cognitive model.
   c) Detail how the system will generate and analyze {t['musical_element']} in the {t['genre']} genre.

2. Cognitive Model Integration (200-250 words):
   a) Explain the key principles of the {t['model']} cognitive model and how they relate to music perception.
   b) Describe how you've translated these principles into algorithmic or computational processes in your AI system.
   c) Discuss any challenges in this translation and how you've addressed them.

3. Music Generation Process (200-250 words):
   a) Outline the step-by-step process your AI system uses to generate a musical composition.
   b) Explain how the {t['model']} model influences the generation of {t['musical_element']}.
   c) Describe how your system ensures the output aligns with the conventions of {t['genre']} music.

4. Evaluation Mechanism (200-250 words):
   a) Describe how your AI system evaluates its own musical compositions.
   b) Explain how this evaluation process incorporates principles from the {t['model']} cognitive model.
   c) Discuss how the system might handle conflicts between cognitive model predictions and genre conventions.

5. Comparative Analysis and Reflection (150-200 words):
   a) Compare your AI system's approach to human composition processes in the {t['genre']} genre.
   b) Reflect on how this AI system might provide insights into human music cognition and creativity.
   c) Propose an experiment to test the musical and cognitive validity of your system's compositions.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of the {t['model']} cognitive model and its application to music perception and generation.",
            f"The AI system design effectively incorporates the {t['model']} model in generating and analyzing {t['musical_element']} in the {t['genre']} genre.",
            "The music generation process is well-explained and logically consistent with both the cognitive model and genre conventions.",
            "The evaluation mechanism demonstrates a nuanced understanding of how to apply cognitive principles to musical analysis.",
            "The comparative analysis and reflection show insightful connections between AI music generation and human cognition and creativity.",
            "The response is well-structured, addressing all required points comprehensively.",
            "The proposed system demonstrates creativity and innovation while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
