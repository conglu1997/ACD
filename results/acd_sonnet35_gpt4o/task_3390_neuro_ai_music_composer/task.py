import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        music_styles = ['Classical', 'Jazz', 'Electronic']
        analysis_tasks = ['Emotion Recognition', 'Style Classification', 'Structural Analysis']
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'music_style': random.choice(music_styles),
                'analysis_task': random.choice(analysis_tasks)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the human auditory system and music cognition, then use it to compose and analyze music. Your task focuses on {t['music_style']} music and includes {t['analysis_task']} as an analytical component. Your response should include the following sections:

1. Neural Architecture Design (250-300 words):
   a) Describe the key components of your neural network, explaining how they parallel structures in the human auditory system and music processing areas of the brain.
   b) Explain how your architecture incorporates principles from music theory and cognition.
   c) Discuss any novel features or innovations in your design that are particularly suited for music composition and analysis.

2. Music Composition Process (200-250 words):
   a) Explain how your neural network generates {t['music_style']} music.
   b) Describe the training process, including the type of data used and any pre-processing steps.
   c) Discuss how your system ensures the generated music adheres to the principles and structures of {t['music_style']}.

3. Music Analysis Capability (200-250 words):
   a) Detail how your system performs {t['analysis_task']} on musical pieces.
   b) Explain the features or patterns your network looks for during this analysis.
   c) Describe how the results of this analysis could be used to improve the composition process or provide insights into music cognition.

4. Comparative Analysis (150-200 words):
   a) Compare your neural architecture to traditional approaches in AI music composition and analysis.
   b) Discuss potential advantages and limitations of your biologically-inspired approach.

5. Experiment Design (200-250 words):
   a) Propose an experiment to evaluate both the composition and analysis capabilities of your system.
   b) Describe the methodology, including how you would measure the quality and authenticity of the composed music.
   c) Explain how you would validate the accuracy and usefulness of the {t['analysis_task']} component.

6. Ethical and Creative Implications (150-200 words):
   a) Discuss the ethical implications of using AI for music composition and analysis.
   b) Explore how this technology might impact human creativity and the music industry.
   c) Propose guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed neural network architecture design inspired by the human auditory system and music cognition",
            f"The explanation of the music composition process for {t['music_style']} is clear and plausible",
            f"The system's capability for {t['analysis_task']} is well-described and relevant",
            "The comparative analysis shows a deep understanding of AI and traditional approaches in music",
            "The proposed experiment is well-designed and addresses both composition and analysis aspects",
            "The discussion of ethical and creative implications is thoughtful and comprehensive",
            "The response demonstrates interdisciplinary knowledge integration and creative problem-solving",
            "The ideas presented are innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
