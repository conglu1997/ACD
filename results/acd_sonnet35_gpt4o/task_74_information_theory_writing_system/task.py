import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Tonal Language A",
                "features": "4 tones, 20 consonants, 5 vowels, subject-verb-object word order"
            },
            {
                "name": "Agglutinative Language B",
                "features": "No tones, 15 consonants, 8 vowels, extensive use of suffixes, subject-object-verb word order"
            }
        ]
        return {
            "1": random.choice(languages),
            "2": random.choice(languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a new writing system for {t['name']} based on information theory principles. The language has the following features:

{t['features']}

Your task is to create an efficient and expressive writing system that optimizes information encoding. Your response should include:

1. A name for your writing system (be creative but descriptive).
2. A detailed explanation of how the writing system works, including:
   a) The basic units of the system (e.g., symbols, strokes, or patterns)
   b) How these units combine to represent sounds, words, or meanings
   c) Any special features that enhance efficiency or expressiveness
3. An explanation of how your system applies at least two principles from information theory (e.g., data compression, error correction, entropy). Cite the specific principles used.
4. A description of how the system is tailored to the given language features (2-3 sentences).
5. Three example 'words' or 'phrases' written in your system, along with their meanings and an explanation of how they demonstrate the system's efficiency.
6. One potential limitation of the writing system and a proposed solution or workaround (2-3 sentences).
7. A brief speculation on how this writing system might influence the language's evolution or its speakers' cognitive processes (2-3 sentences).

Ensure your writing system is innovative, grounded in information theory, and optimized for the given language features. Your design should balance efficiency with practicality and ease of use."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The writing system is innovative and distinct from existing systems.",
            "The explanation clearly demonstrates the application of at least two information theory principles.",
            "The system is well-tailored to the given language features.",
            "The example 'words' or 'phrases' effectively demonstrate the system's efficiency and expressiveness.",
            "The identified limitation and proposed solution are relevant and thoughtful.",
            "The speculation on linguistic or cognitive implications shows insight and creativity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
