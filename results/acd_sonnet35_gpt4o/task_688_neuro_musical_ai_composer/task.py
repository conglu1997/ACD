import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "amygdala",
                "emotion": "fear",
                "musical_style": "atonal"
            },
            {
                "brain_region": "hippocampus",
                "cognitive_process": "memory formation",
                "musical_style": "minimalist"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes {t['musical_style']} music based on real-time neural activity in the {t['brain_region']}, associated with {'the emotion of ' + t['emotion'] if 'emotion' in t else t['cognitive_process']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, including its main components and their functions.
   b) Explain how the system processes neural input and translates it into musical elements.
   c) Detail the AI techniques or algorithms used in your system (e.g., neural networks, reinforcement learning).

2. Neural-Musical Mapping (200-250 words):
   a) Create a framework for mapping neural activity to musical elements (e.g., pitch, rhythm, harmony).
   b) Explain the neuroscientific and music theory principles that inform your mapping choices.
   c) Provide an example of how specific neural patterns would be represented musically.

3. Composition Process (200-250 words):
   a) Describe the process your AI system uses to generate musical compositions.
   b) Explain how the system ensures musical coherence while reflecting real-time neural changes.
   c) Discuss how the system handles the balance between neural input and musical structure.

4. Emotional/Cognitive Representation (150-200 words):
   a) Explain how your system captures and expresses the specific {'emotion' if 'emotion' in t else 'cognitive process'} in the musical output.
   b) Discuss potential challenges in accurately representing neural states musically.

5. Ethical and Practical Considerations (150-200 words):
   a) Discuss potential ethical implications of using neural activity for artistic creation.
   b) Address privacy concerns and propose guidelines for responsible use of such technology.
   c) Explain potential therapeutic or scientific applications of your system.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence principles.",
            "The system design is creative, innovative, and scientifically plausible.",
            "The neural-musical mapping is well-explained and grounded in both neuroscience and music theory.",
            "The composition process is clearly described and accounts for both neural input and musical coherence.",
            "Ethical and practical considerations are thoroughly addressed.",
            f"The system effectively captures and expresses the {'emotion' if 'emotion' in t else 'cognitive process'} associated with the {t['brain_region']}.",
            f"The proposed system is suitable for composing {t['musical_style']} music."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
