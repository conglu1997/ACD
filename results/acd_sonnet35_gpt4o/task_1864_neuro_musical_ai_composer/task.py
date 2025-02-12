import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_genre": "Classical",
                "target_emotion": "Melancholy",
                "brain_region": "Amygdala"
            },
            {
                "musical_genre": "Jazz",
                "target_emotion": "Joy",
                "brain_region": "Nucleus Accumbens"
            },
            {
                "musical_genre": "Electronic",
                "target_emotion": "Anxiety",
                "brain_region": "Prefrontal Cortex"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes and analyzes music in the {t['musical_genre']} genre, aiming to evoke the emotion of {t['target_emotion']} while considering the activity in the {t['brain_region']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for music composition and analysis.
   b) Explain how it incorporates principles from neuroscience and music theory.
   c) Detail the key components, including modules for musical pattern generation, emotional mapping, and brain activity simulation.
   d) Discuss any novel machine learning techniques or algorithms used in your design.

2. Neuroscience-Music Theory Integration (250-300 words):
   a) Explain how your system integrates neuroscientific understanding of the {t['brain_region']} with music theory principles.
   b) Describe how these integrations influence the composition process to evoke {t['target_emotion']}.
   c) Discuss any challenges in mapping brain activity to musical elements and how your system addresses them.

3. Composition Process (250-300 words):
   a) Detail how your AI generates music in the {t['musical_genre']} genre.
   b) Explain how the system incorporates elements known to evoke {t['target_emotion']}.
   c) Describe any techniques used to ensure musical coherence and adherence to genre conventions.

4. Analysis and Feedback Loop (200-250 words):
   a) Explain how your system analyzes the emotional impact and brain activity patterns of the composed music.
   b) Describe the feedback mechanism that allows the system to refine its compositions based on the analysis.
   c) Discuss how this analysis could contribute to our understanding of the relationship between music, emotions, and brain activity.

5. Evaluation and Testing (200-250 words):
   a) Propose methods for evaluating the effectiveness of your system in evoking the target emotion and stimulating the specified brain region.
   b) Describe experiments to test whether the system's compositions elicit the intended emotional and neurological responses in human listeners.
   c) Suggest how you would validate the system's output with music theorists, neuroscientists, and listeners.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss potential applications of your AI system in fields such as music therapy, entertainment, or cognitive neuroscience.
   b) Address any ethical concerns related to using AI for emotional manipulation through music.
   c) Explore how this technology could be used to enhance our understanding of music perception and emotional processing in the brain.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a deep understanding of neuroscience, particularly related to the {t['brain_region']} and its role in emotional processing.",
            f"The system design should effectively integrate principles from music theory, especially those related to the {t['musical_genre']} genre.",
            f"The AI system should have a clear mechanism for evoking the emotion of {t['target_emotion']} through its musical compositions.",
            "The response should include innovative yet scientifically plausible approaches to AI-driven music composition and analysis.",
            "The proposed evaluation methods should be comprehensive and scientifically sound.",
            "The ethical considerations should be thoughtfully addressed, considering both potential benefits and risks of the technology.",
            "The response should be well-structured, following the outlined format and addressing all required sections.",
            "The technical terminology from neuroscience, music theory, and AI should be used appropriately and explained clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
