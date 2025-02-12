import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"name": "joy", "associated_brain_region": "nucleus accumbens"},
            {"name": "sadness", "associated_brain_region": "amygdala"},
            {"name": "fear", "associated_brain_region": "amygdala"},
            {"name": "anger", "associated_brain_region": "hypothalamus"},
            {"name": "surprise", "associated_brain_region": "locus coeruleus"}
        ]
        return {str(i+1): emotion for i, emotion in enumerate(random.sample(emotions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music to evoke the emotion of {t['name']} based on neurological data from the {t['associated_brain_region']}. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the overall structure of your AI music composition system.
   b) Explain how it incorporates neurological data into the composition process.
   c) Detail how the system maps brain activity to musical elements (e.g., rhythm, melody, harmony).

2. Music Theory Integration (150-200 words):
   a) Explain how your system incorporates music theory principles to evoke {t['name']}.
   b) Discuss any specific musical techniques or structures used to elicit this emotion.

3. AI and Machine Learning Approach (200-250 words):
   a) Describe the AI and machine learning techniques used in your system.
   b) Explain how the system learns to associate neurological patterns with musical elements.
   c) Discuss any novel approaches to AI-driven composition in your design.

4. Neurofeedback Loop (150-200 words):
   a) Propose a method for creating a neurofeedback loop in your system.
   b) Explain how this loop could refine and personalize the emotional impact of the music.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using neurological data for artistic creation.
   b) Address potential concerns about emotional manipulation through AI-generated music.
   c) Propose guidelines for the responsible development and use of this technology.

6. Cross-Cultural Analysis (100-150 words):
   a) Analyze how cultural differences might affect the emotional perception of the generated music.
   b) Propose how your system could adapt to different cultural contexts.

7. Future Research Directions (100-150 words):
   a) Suggest potential applications of this technology beyond artistic creation.
   b) Propose a research study that could further our understanding of the relationship between music, emotions, and the brain.

Ensure your response demonstrates a deep understanding of music theory, neuroscience, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and rigor. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of how to evoke the emotion of {t['name']} through music, based on neurological data from the {t['associated_brain_region']}.",
            "The AI system design should be innovative, logically consistent, and well-explained, integrating music theory, neuroscience, and AI principles.",
            "The response should thoughtfully address ethical considerations and cross-cultural implications of the proposed system.",
            "The proposed neurofeedback loop and future research directions should be insightful and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
