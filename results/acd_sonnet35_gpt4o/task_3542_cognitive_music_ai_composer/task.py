import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'emotion': 'nostalgia',
                'cognitive_process': 'episodic memory retrieval',
                'musical_style': 'ambient electronic'
            },
            {
                'emotion': 'awe',
                'cognitive_process': 'pattern recognition',
                'musical_style': 'orchestral'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and analyze music based on specific emotional states and cognitive processes, integrating principles from music theory, cognitive science, and artificial intelligence. Your system should focus on the emotion of {t['emotion']}, the cognitive process of {t['cognitive_process']}, and generate music in the style of {t['musical_style']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and analyzing music.
   b) Explain how your system integrates music theory, cognitive science, and AI principles.
   c) Detail how your system models emotions and cognitive processes.
   d) Provide a high-level diagram or pseudocode representing the core algorithm of your system.

2. Emotional and Cognitive Modeling (250-300 words):
   a) Explain how your system represents and processes the given emotion ({t['emotion']}).
   b) Describe how you model the specified cognitive process ({t['cognitive_process']}).
   c) Discuss how these models influence the music generation and analysis.

3. Music Generation Process (250-300 words):
   a) Detail the steps your system takes to generate music in the specified style ({t['musical_style']}).
   b) Explain how emotional and cognitive models guide the composition process.
   c) Describe any novel techniques or algorithms used in your music generation system.

4. Music Analysis Capabilities (200-250 words):
   a) Explain how your system analyzes existing music for emotional content and cognitive processes.
   b) Describe the features or patterns your system looks for in this analysis.
   c) Discuss how this analysis could be used to improve the music generation process.

5. Evaluation and Validation (200-250 words):
   a) Propose a method to evaluate the effectiveness of your system in generating emotionally and cognitively appropriate music.
   b) Describe potential experiments or studies to validate your system's performance.
   c) Discuss how you would measure the 'success' of the generated music in conveying the intended emotion and cognitive process.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential biases or limitations in your system's approach to modeling emotions and cognition.
   b) Address ethical concerns related to AI-generated music and its potential impact on human creativity.
   c) Propose guidelines for the responsible use and development of emotion-based AI music generation systems.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use numbered subsections (e.g., 1a, 1b, 1c) to organize your thoughts. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence",
            "The proposed AI system is innovative and scientifically plausible",
            "The system architecture and processes are clearly explained and logically sound",
            "The response addresses all required sections and adheres to the specified word count",
            "The music generation and analysis processes are well-detailed and incorporate the specified emotion, cognitive process, and musical style",
            "The response includes a thoughtful discussion of evaluation methods and ethical considerations",
            "The proposed system effectively integrates principles from music theory, cognitive science, and AI",
            "The response is well-formatted with clear headings and numbered subsections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
