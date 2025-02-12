import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            "conflicted nostalgia",
            "serene anticipation",
            "melancholic hope",
            "excited trepidation",
            "bittersweet triumph"
        ]
        musical_elements = [
            "harmonic progression",
            "rhythmic pattern",
            "melodic contour",
            "timbral texture",
            "dynamic range"
        ]
        return {
            "1": {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithmic composition system that translates the complex emotional state of '{t['emotional_state']}' into musical structures, with a particular focus on the musical element of '{t['musical_element']}'. Your response should include:

1. Emotional State Analysis (150-200 words):
   a) Deconstruct the given emotional state into its component parts or dimensions.
   b) Explain how this emotional state might be experienced or expressed by humans.

2. Musical Element Exploration (150-200 words):
   a) Describe the specified musical element and its role in conveying emotion in music.
   b) Discuss how this element is typically used or manipulated in different musical genres or styles.

3. Algorithmic System Design (250-300 words):
   a) Propose a novel algorithmic system that maps the emotional state to the musical element.
   b) Describe the key components and processes of your system.
   c) Explain how your design integrates principles from music theory, psychology, and mathematics.

4. Mathematical Representation (150-200 words):
   a) Provide a mathematical formula or set of equations that represent a core aspect of your algorithmic system.
   b) Explain how this mathematical representation captures the relationship between emotion and music.

5. Implementation Example (200-250 words):
   a) Walk through a specific example of how your system would generate a musical output for the given emotional state.
   b) Describe the resulting musical structure and how it reflects the intended emotion.

6. Evaluation and Limitations (150-200 words):
   a) Propose a method to evaluate the effectiveness of your system in conveying the intended emotion.
   b) Discuss potential limitations or challenges in implementing your system.
   c) Suggest areas for future research or improvement.

Ensure your response demonstrates a deep understanding of music theory, psychology of emotion, and algorithmic composition techniques. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithmic composition system must translate the emotional state of {t['emotional_state']} into musical structures, focusing on the musical element of {t['musical_element']}.",
            "The response must include a clear analysis of the given emotional state and its components.",
            "An exploration of the specified musical element and its role in conveying emotion must be provided.",
            "The proposed algorithmic system must integrate principles from music theory, psychology, and mathematics in a novel and plausible way.",
            "A mathematical representation (formula or equations) of a core aspect of the system must be included and explained.",
            "A specific implementation example must be provided, demonstrating how the system generates musical output for the given emotional state.",
            "The response must include a proposed evaluation method and discussion of limitations or challenges.",
            "The response must demonstrate a deep understanding of music theory, psychology of emotion, and algorithmic composition techniques.",
            "The response must be creative while maintaining scientific plausibility.",
            "The response must be formatted with clear headings for each section and numbered paragraphs within each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
