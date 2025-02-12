import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "musical_element": "Harmonic progression",
                "linguistic_element": "Syntactic structure",
                "hint": "Consider how chord progressions might map to sentence structures."
            },
            {
                "musical_element": "Rhythmic patterns",
                "linguistic_element": "Prosodic features",
                "hint": "Think about how musical rhythm could correspond to speech rhythm and intonation."
            },
            {
                "musical_element": "Melodic contour",
                "linguistic_element": "Semantic structure",
                "hint": "Explore how the rise and fall of a melody might relate to the meaning and emotional content of language."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that transposes the musical element of {t['musical_element']} into the linguistic element of {t['linguistic_element']}, and vice versa. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components and architecture of your transposition system.
   b) Explain how it maps {t['musical_element']} to {t['linguistic_element']} and vice versa.
   c) Discuss any novel algorithms or data structures required for your implementation.
   d) Provide a high-level pseudocode or flowchart of your system's main algorithm (describe it textually).

2. Cognitive Model (200-250 words):
   a) Explain the cognitive principles underlying your transposition system.
   b) Discuss how your system models or mimics brain processes involved in music and language processing.
   c) Analyze potential limitations in translating between musical and linguistic domains.

3. Example Transposition (200-250 words):
   a) Provide a specific example of how your system would transpose a {t['musical_element']} into a {t['linguistic_element']}.
   b) Explain the reverse process, transposing the resulting {t['linguistic_element']} back into a {t['musical_element']}.
   c) Discuss any loss or gain of information during this bidirectional transposition.

4. Cognitive Implications (250-300 words):
   a) Analyze how this transposition process might inform our understanding of music and language processing in the brain.
   b) Discuss potential insights into the relationship between musical and linguistic cognition.
   c) Propose a hypothesis about shared cognitive mechanisms for music and language based on your system's behavior.

5. Practical Applications (150-200 words):
   a) Suggest two potential applications of your transposition system in fields such as cognitive science, music therapy, or language learning.
   b) Explain how these applications could benefit from the music-language connection your system establishes.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns or unintended consequences of using this transposition system.
   b) Propose guidelines for responsible development and use of music-language transposition technologies.

Ensure your response demonstrates a deep understanding of music theory, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Hint to get you started: {t['hint']}

Your total response should be between 1200-1500 words.

Format your response with clear headings for each section, and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively transposes {t['musical_element']} to {t['linguistic_element']} and vice versa. (0.3 points)",
            "The response demonstrates a deep understanding of music theory, linguistics, and cognitive science. (0.2 points)",
            "The cognitive model and implications are well-reasoned and scientifically plausible. (0.2 points)",
            "The example transposition is clear, detailed, and illustrates the system's functionality. (0.2 points)",
            "The practical applications and ethical considerations are thoughtful and relevant. (0.1 points)"
        ]
        score = eval_with_llm_judge(instructions, submission, criteria)
        return score if score is not None else 0.0