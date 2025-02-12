import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "direction": "neural_to_music",
                "neural_pattern": "Default Mode Network activation during resting state",
                "musical_style": "Ambient electronic"
            },
            {
                "direction": "music_to_neural",
                "musical_piece": "Beethoven's Symphony No. 5, first movement",
                "brain_region": "Auditory cortex and limbic system"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bidirectional translation system between neural activity patterns and musical compositions. For this task, focus on the {t['direction']} direction, specifically dealing with the {t['neural_pattern'] if t['direction'] == 'neural_to_music' else t['musical_piece']} and {t['musical_style'] if t['direction'] == 'neural_to_music' else t['brain_region']}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your bidirectional translation system.
   b) Explain how it integrates principles from neuroscience, AI, and music theory.
   c) Detail the key components and their roles in the translation process.
   d) Include at least one equation or formal representation of a critical component in your system.

2. Neural Representation (200-250 words):
   a) Explain how neural activity patterns are encoded in your system.
   b) Describe the features or characteristics of neural activity that your system considers.
   c) Discuss how your representation accounts for the complexity and variability of brain activity.

3. Musical Representation (200-250 words):
   a) Describe how musical elements (e.g., pitch, rhythm, harmony) are represented in your system.
   b) Explain how your system captures the structural and emotional aspects of music.
   c) Discuss any novel approaches you've developed for representing music computationally.

4. Translation Process (250-300 words):
   a) Provide a step-by-step explanation of the translation process for the given direction.
   b) Describe any intermediate representations or transformations used in the process.
   c) Explain how your system ensures the translation preserves meaningful characteristics of the input.
   d) Discuss how your system handles ambiguity or multiple possible interpretations.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and quality of your system's translations.
   b) Describe key metrics or experiments that would validate your approach.
   c) Discuss how you would compare your system's output to human-generated alternatives.

6. Artistic and Scientific Implications (150-200 words):
   a) Discuss the potential impact of your system on both neuroscientific research and musical composition.
   b) Explore possible applications in brain-computer interfaces, music therapy, or AI-assisted creativity.
   c) Address any ethical considerations related to the interpretation and manipulation of neural activity or music.

7. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your proposed system.
   b) Suggest improvements or extensions to address these limitations.
   c) Propose two novel research questions that could be explored using your system.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all seven required sections with appropriate content and word counts.",
            "The system architecture should clearly integrate principles from neuroscience, AI, and music theory.",
            "The neural and musical representations should be well-defined and scientifically plausible.",
            "The translation process should be explained in detail, addressing the specific direction and elements given in the task.",
            "The response should demonstrate a deep understanding of neuroscience, AI, and music theory concepts.",
            "The proposed evaluation methods and implications should be thoughtful and well-reasoned.",
            "The response should exhibit creativity and innovation while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
