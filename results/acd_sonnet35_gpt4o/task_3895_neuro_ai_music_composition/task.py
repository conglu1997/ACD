import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "neural_pattern": "default mode network",
                "music_style": "ambient",
                "application": "stress reduction therapy"
            },
            {
                "neural_pattern": "working memory",
                "music_style": "classical",
                "application": "cognitive enhancement"
            },
            {
                "neural_pattern": "emotional regulation",
                "music_style": "jazz",
                "application": "mood disorder treatment"
            },
            {
                "neural_pattern": "motor cortex activity",
                "music_style": "electronic dance music",
                "application": "movement disorder therapy"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes {t['music_style']} music based on {t['neural_pattern']} activity patterns, then analyze its potential applications in {t['application']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI music composition system.
   b) Explain how your system integrates neuroscientific data on {t['neural_pattern']} with music theory principles.
   c) Detail the AI techniques used for translating neural patterns into musical elements.

2. Neural-Musical Mapping (200-250 words):
   a) Propose a framework for mapping {t['neural_pattern']} activity to specific musical parameters.
   b) Explain how your system accounts for the temporal dynamics of neural activity in music composition.
   c) Discuss how you ensure the musical output adheres to {t['music_style']} conventions.

3. Composition Process (200-250 words):
   a) Describe the step-by-step process your AI system uses to compose a piece of music.
   b) Explain how your system handles musical structure, harmony, and rhythm.
   c) Discuss any novel approaches your system employs to ensure musical coherence and creativity.

4. Application Analysis (200-250 words):
   a) Analyze the potential applications of your system in {t['application']}.
   b) Discuss how the composed music might influence neural activity and behavior.
   c) Propose a method for evaluating the effectiveness of your system in this application.

5. Challenges and Limitations (150-200 words):
   a) Identify potential challenges in translating neural activity to music.
   b) Discuss limitations of your approach and propose ways to address them.
   c) Consider ethical implications of using AI-generated music based on neural data.

6. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how your approach could advance our understanding of the relationship between brain activity and music.
   c) Explore potential applications of your system beyond {t['application']}.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate terminology from these fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words.

Note: Your response will be evaluated based on the depth of understanding, innovation, scientific plausibility, and how well it addresses all aspects of the task. A perfect score requires excellence in all these areas."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['neural_pattern']}, {t['music_style']} music theory, and relevant AI techniques.",
            "The proposed system architecture and neural-musical mapping are innovative and scientifically plausible.",
            f"The analysis of applications in {t['application']} is well-developed and considers both benefits and challenges.",
            "The discussion of challenges, limitations, and future directions shows critical thinking and insight.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
