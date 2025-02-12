import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_principles = [
            "Fibonacci sequence",
            "Golden ratio",
            "Fractal geometry",
            "Group theory",
            "Fourier analysis"
        ]
        cognitive_models = [
            "Gestalt principles",
            "Expectancy theory",
            "Auditory scene analysis",
            "Tonal hierarchy",
            "Temporal perception"
        ]
        musical_elements = [
            "Melody",
            "Harmony",
            "Rhythm",
            "Timbre",
            "Form"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "mathematical_principle": random.choice(mathematical_principles),
                "cognitive_model": random.choice(cognitive_models),
                "musical_element": random.choice(musical_elements)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates and analyzes novel musical structures based on mathematical principles and cognitive models of music perception, then compose and analyze a piece using this system. Your task focuses on the mathematical principle of {t['mathematical_principle']}, the cognitive model of {t['cognitive_model']}, and the musical element of {t['musical_element']}.

Your response should include the following sections:

1. System Design (300-350 words):
   a) Describe the key components of your system and how they interact.
   b) Explain how your system incorporates the specified mathematical principle.
   c) Detail how the cognitive model is integrated into the system's design.
   d) Discuss how your system generates and analyzes the specified musical element.

2. Mathematical-Musical Integration (250-300 words):
   a) Analyze how the mathematical principle is translated into musical structures.
   b) Provide at least two specific examples of how mathematical concepts manifest in the generated music.
   c) Discuss any challenges in adapting the mathematical principle to musical composition and how you addressed them.

3. Cognitive Model Application (250-300 words):
   a) Explain how the specified cognitive model influences the music generation and analysis processes.
   b) Describe how your system simulates or accounts for human perception of the specified musical element.
   c) Discuss potential insights into music cognition that your system might provide.

4. Composition Process (200-250 words):
   a) Describe the step-by-step process your system would follow to compose a short piece of music.
   b) Explain how the mathematical principle and cognitive model interact during the composition process.
   c) Provide a brief description or representation of the composed piece (e.g., a textual description of its structure, a mockup of sheet music, or a description of its audio characteristics).

5. Analysis of the Composed Piece (200-250 words):
   a) Analyze the composed piece in terms of its mathematical structure.
   b) Discuss how the piece reflects or challenges the integrated cognitive model.
   c) Evaluate the aesthetic qualities of the piece, considering both its mathematical basis and cognitive aspects.

6. Meta-analysis and Reflection (150-200 words):
   a) Reflect on the creative process of designing this system and composing with it.
   b) Discuss any unexpected emergent properties or results from the integration of mathematics, cognition, and music.
   c) Consider how this approach might inform or challenge current theories of musical creativity and composition.

7. Future Developments and Applications (150-200 words):
   a) Propose two potential improvements or extensions to your system.
   b) Discuss potential applications of this system in music education, therapy, or AI-assisted composition.
   c) Consider how this approach might be adapted to study other aspects of creativity or cognition.

Ensure your response demonstrates a deep understanding of music theory, mathematical concepts, and cognitive science. Use appropriate terminology and provide clear explanations for complex ideas. Be creative and innovative while maintaining scientific and artistic plausibility throughout your response.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all 7 required sections with appropriate content for each.",
            f"The system design effectively incorporates the mathematical principle of {t['mathematical_principle']}, the cognitive model of {t['cognitive_model']}, and focuses on the musical element of {t['musical_element']}.",
            "The response demonstrates a deep understanding of music theory, mathematical concepts, and cognitive science, using appropriate terminology.",
            "The composition process and analysis of the composed piece are clearly explained and show how the mathematical principle and cognitive model are applied.",
            "The response includes creative and innovative ideas while maintaining scientific and artistic plausibility.",
            "The meta-analysis and reflection show thoughtful consideration of the creative process and its implications.",
            "The proposed future developments and applications are relevant and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
