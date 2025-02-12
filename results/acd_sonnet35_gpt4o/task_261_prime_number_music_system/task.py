import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        prime_sets = [
            [2, 3, 5, 7, 11, 13, 17, 19],
            [23, 29, 31, 37, 41, 43, 47, 53],
            [59, 61, 67, 71, 73, 79, 83, 89],
            [97, 101, 103, 107, 109, 113, 127, 131]
        ]
        return {
            "1": {"primes": random.choice(prime_sets)},
            "2": {"primes": random.choice(prime_sets)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        primes = t['primes']
        return f"""Design a novel musical system based on the following set of prime numbers: {primes}. Your task is to:

1. Create a musical scale (150-200 words):
   a) Assign each prime number to a specific frequency or note, using scientifically grounded reasoning.
   b) Explain the mathematical relationships between the notes.
   c) Describe how this scale differs from traditional Western scales.

2. Develop compositional rules (150-200 words):
   a) Explain how melodies can be created using your prime number system.
   b) Describe harmonic principles based on the mathematical properties of the prime numbers.
   c) Propose a unique rhythmic structure that incorporates the prime numbers.

3. Analyze potential cognitive effects (200-250 words):
   a) Hypothesize how listening to music composed in this system might affect brain activity, citing relevant neuroscientific principles.
   b) Speculate on potential emotional responses to this music, based on current understanding of music psychology.
   c) Discuss how this system might influence memory formation or recall compared to traditional music, referencing cognitive science theories.

4. Propose an experiment (150-200 words):
   Design a scientific study to test the cognitive or emotional effects of your prime number music system. Include:
   a) Hypothesis
   b) Experimental setup
   c) Measurement methods
   d) Potential implications of the results

5. Create a sample composition (100-150 words):
   Describe a short musical piece using your system. Explain how it embodies the principles you've developed and what emotional or cognitive effects you intend it to have.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and cognitive science. Be creative and original in your approach while maintaining scientific plausibility and citing relevant theories or principles where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five required sections comprehensively.",
            "The musical scale design demonstrates a clear understanding of the relationship between prime numbers and frequency, with scientifically grounded reasoning.",
            "The compositional rules are logically derived from the prime number system and show creativity and originality.",
            "The analysis of potential cognitive effects is well-reasoned and grounded in current understanding of music psychology and neuroscience, with relevant theories or principles cited.",
            "The proposed experiment is scientifically sound and directly relates to testing the effects of the prime number music system.",
            "The sample composition description clearly illustrates the principles of the designed music system and its intended cognitive or emotional effects.",
            "The overall response shows interdisciplinary thinking, combining music theory, mathematics, and cognitive science in a novel and insightful way.",
            "The response demonstrates originality and does not simply repeat well-known concepts without adding new insights."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
