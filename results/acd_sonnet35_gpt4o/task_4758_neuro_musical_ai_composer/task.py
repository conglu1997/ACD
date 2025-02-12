import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre']
        neural_processes = ['auditory processing', 'emotional response', 'memory retrieval', 'pattern recognition']
        music_genres = ['classical', 'jazz', 'electronic', 'world music']
        cognitive_effects = ['attention', 'emotion regulation', 'spatial reasoning', 'language processing']
        
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "neural_process": random.choice(neural_processes),
                "music_genre": random.choice(music_genres),
                "cognitive_effect": random.choice(cognitive_effects)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "neural_process": random.choice(neural_processes),
                "music_genre": random.choice(music_genres),
                "cognitive_effect": random.choice(cognitive_effects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the neural processes involved in music composition and perception, focusing on the musical element of {t['musical_element']}, the neural process of {t['neural_process']}, and the music genre of {t['music_genre']}. Then use this system to generate and analyze a novel musical piece, considering its potential {t['cognitive_effect']} effects. Your response should include:

1. Neural-Musical Model Architecture (300-350 words):
   a) Describe the overall structure of your AI system that integrates neural processes with music composition and perception.
   b) Explain how it models the specified neural process ({t['neural_process']}) in relation to music.
   c) Detail how the system incorporates music theory principles, especially regarding {t['musical_element']}.
   d) Discuss any novel algorithms or approaches used in your design.
   e) Include a high-level diagram or pseudocode snippet illustrating a key component of your system.

2. Music Generation Process (250-300 words):
   a) Explain the step-by-step process your AI system follows to generate a new musical piece in the {t['music_genre']} genre.
   b) Describe how the focus on {t['musical_element']} influences the generation process.
   c) Discuss how the modeled neural process ({t['neural_process']}) contributes to the composition.
   d) Provide a detailed description or notation of a segment (at least 8 measures) of the generated music, including specific musical features (e.g., key, time signature, chord progressions, melodic contour).

3. Musical Analysis (200-250 words):
   a) Describe how your AI system analyzes the generated musical piece.
   b) Explain how this analysis incorporates both music theory principles (e.g., harmonic analysis, form analysis) and neuroscientific concepts (e.g., neural responses to specific musical features).
   c) Discuss any insights or patterns your system might identify that traditional music analysis might miss.
   d) Provide a specific example of how your system would analyze a particular aspect of the generated music segment.

4. Cognitive Effects Evaluation (200-250 words):
   a) Explain how your system evaluates the potential {t['cognitive_effect']} effects of the generated music.
   b) Describe the criteria or methods used for this evaluation, referencing relevant neuroscientific research.
   c) Discuss how these effects might vary for different listeners and why, considering factors such as musical training, cultural background, or individual differences in brain structure/function.

5. Practical Applications and Limitations (200-250 words):
   a) Propose two potential real-world applications of your neuro-musical AI system.
   b) Discuss the limitations of your approach and potential areas for improvement.
   c) Consider how this technology might evolve in the next decade.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to compose music, considering issues of creativity, authorship, and artistic value.
   b) Address potential concerns about using this technology to manipulate cognitive states through music.
   c) Propose guidelines for the responsible development and use of neuro-musical AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately incorporates and explains the musical element of {t['musical_element']} in the AI system design and music generation process.",
            f"The model effectively integrates the neural process of {t['neural_process']} in its architecture and function.",
            f"The approach to generating and analyzing music in the {t['music_genre']} genre is creative, scientifically plausible, and properly incorporates both neuroscientific and music theory principles.",
            f"The evaluation of potential {t['cognitive_effect']} effects is comprehensive and based on current scientific understanding.",
            "The proposed applications, limitations, and ethical considerations demonstrate a nuanced understanding of the intersection between AI, neuroscience, and music.",
            "The response follows the specified format, including all required sections, and adheres to the given word limit.",
            "The proposed AI system demonstrates novelty and potential for advancing our understanding of music perception, composition, and cognitive effects.",
            "The response provides concrete examples and detailed explanations throughout, demonstrating a deep understanding of the subject matter."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
