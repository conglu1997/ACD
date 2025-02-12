import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genres = [
            "science fiction",
            "mystery",
            "romance",
            "historical fiction"
        ]
        dna_bases = ['A', 'T', 'C', 'G']
        example_codons = [''.join(random.choices(dna_bases, k=3)) for _ in range(5)]
        return {
            "1": {"genre": random.choice(genres), "example_codons": example_codons},
            "2": {"genre": random.choice([g for g in genres if g != genres[0]]), "example_codons": example_codons}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a story encoding system using DNA base pairs (A, T, C, G), then use it to write a short {t['genre']} story that can be transcribed into a valid DNA sequence. Your task has the following parts:

1. Encoding System Design (200-250 words):
   a) Develop a system for encoding letters, punctuation, and spaces using combinations of DNA base pairs.
   b) Explain how your system maintains biological plausibility (e.g., avoiding long repeats, maintaining a realistic GC content).
   c) Provide a small example demonstrating how a word or short phrase would be encoded.
   d) You may use the following example codons as a starting point, but you must expand upon them: {', '.join(t['example_codons'])}

2. Story Composition (200-250 words):
   a) Write a short {t['genre']} story (50-75 words) using only the letters, punctuation, and spaces that can be encoded in your system.
   b) Ensure the story has a clear beginning, middle, and end, and fits the chosen genre.

3. DNA Sequence (100-150 words):
   a) Provide the complete DNA sequence for your story as a continuous string of A, T, C, and G without spaces or line breaks.
   b) Explain any special features or patterns in your sequence.

4. Biological Analysis (150-200 words):
   a) Calculate the GC content of your DNA sequence.
   b) Identify any potential issues that could arise if this DNA sequence were inserted into a living organism.
   c) Suggest one potential biological function this DNA sequence could have, based on its properties.

5. Information Theory Application (150-200 words):
   a) Discuss the information density of your encoding system compared to standard ASCII encoding.
   b) Explain how error correction could be implemented in your system.
   c) Propose a method for compressing your encoded story using a basic biologically-inspired algorithm.

6. Creative Extension (100-150 words):
   a) Suggest how your encoding system could be used to hide secret messages in actual organisms.
   b) Briefly describe an experiment that could demonstrate this concept.

Ensure your response demonstrates a deep understanding of genetics, information theory, and creative writing. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 900-1200 words.

Format your response using the following structure:
[Encoding System Design]
<Your response>

[Story Composition]
<Your response>

[DNA Sequence]
<Your response>

[Biological Analysis]
<Your response>

[Information Theory Application]
<Your response>

[Creative Extension]
<Your response>
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            "The encoding system is well-designed, biologically plausible, and expands upon the provided example codons.",
            "The story is coherent, fits the specified genre, and can be fully encoded using the designed system.",
            "The DNA sequence is provided as a continuous string of A, T, C, and G without spaces or line breaks, and correctly represents the encoded story.",
            "The biological analysis includes accurate GC content calculation and plausible functional suggestions.",
            "The information theory application demonstrates understanding of encoding efficiency and error correction.",
            "The creative extension proposes an innovative yet scientifically grounded application of the encoding system.",
            "The response follows the specified format structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
