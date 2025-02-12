import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Working Memory Limitations",
            "Gestalt Principles of Perception",
            "Cognitive Load Theory",
            "Dual Coding Theory"
        ]
        musical_elements = [
            "Melody",
            "Harmony",
            "Rhythm",
            "Timbre"
        ]
        musical_genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "World Music"
        ]
        
        tasks = [
            {
                "cognitive_principle": principle,
                "musical_element": element,
                "musical_genre": genre
            }
            for principle in cognitive_principles
            for element in musical_elements
            for genre in musical_genres
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical system based on the cognitive principle of {t['cognitive_principle']}, focusing on the musical element of {t['musical_element']}, and apply it to the {t['musical_genre']} genre. Your task has the following parts:

1. Cognitive Principle Explanation (100-150 words):
   a) Briefly explain the cognitive principle and its key features.
   b) Discuss how this principle relates to music perception or processing.

2. Musical System Design (200-250 words):
   a) Describe your novel musical system that incorporates the cognitive principle.
   b) Explain how it specifically addresses the given musical element.
   c) Provide a musical notation, diagram, or mathematical formula that illustrates a key aspect of your system.

3. Composition Guidelines (150-200 words):
   a) Outline a set of rules or guidelines for composing music using your system.
   b) Explain how these guidelines reflect both the cognitive principle and the musical element.
   c) Discuss how your system could be applied to the specified musical genre.

4. Sample Composition (200-250 words):
   a) Describe a short musical piece (16-32 measures) composed using your system.
   b) Explain how your composition demonstrates the key features of your musical system.
   c) Discuss how the cognitive principle is reflected in the listening experience.
   d) Provide a brief musical notation or diagram representing a key part of your composition.

5. Analysis and Interpretation (150-200 words):
   a) Analyze your sample composition in terms of traditional music theory.
   b) Compare and contrast your system with conventional approaches to the given musical element.
   c) Interpret the potential cognitive effects of your composition on listeners.

6. Practical Applications (100-150 words):
   a) Propose two potential applications of your musical system outside of pure composition (e.g., music therapy, education, or AI-generated music).
   b) Briefly explain how each application leverages the cognitive aspects of your system.

Ensure your response demonstrates a deep understanding of both music theory and cognitive science. Be creative in your system design while maintaining scientific plausibility. Use appropriate musical and cognitive terminology throughout your answer.

Format your response using clear headings for each section. Your total response should be between 900-1200 words. Include at least one musical notation, diagram, or formula in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified cognitive principle and its relevance to music perception or processing.",
            "The musical system design is innovative, coherent, and effectively incorporates the cognitive principle and musical element.",
            "The composition guidelines are clear, logical, and reflect both the cognitive principle and musical element.",
            "The sample composition description effectively demonstrates the key features of the musical system and cognitive principle.",
            "The analysis and interpretation show a deep understanding of music theory and cognitive effects.",
            "The proposed practical applications are creative and leverage the cognitive aspects of the system.",
            "The response uses appropriate musical and cognitive terminology throughout.",
            "The response includes at least one musical notation, diagram, or formula that effectively illustrates the musical system or composition.",
            "The total word count of the response is between 900-1200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0