import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "initial_alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "time_periods": 3,
                "cultural_events": ["Trade expansion", "Technological revolution", "Cultural assimilation"]
            },
            {
                "initial_alphabet": "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ",
                "time_periods": 4,
                "cultural_events": ["War and conquest", "Religious reformation", "Scientific enlightenment", "Global communication"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an evolving cryptographic system based on linguistic principles and information theory. Your system will start with the initial alphabet: {t['initial_alphabet']} and evolve over {t['time_periods']} time periods, influenced by the following cultural events: {', '.join(t['cultural_events'])}.

Your task is to:

1. Initial System (200-250 words):
   a) Design a basic cryptographic system using the initial alphabet.
   b) Explain how it encodes and decodes messages.
   c) Discuss its strengths and weaknesses in terms of information theory.

2. Evolution Simulation (300-350 words):
   For each time period and corresponding cultural event:
   a) Describe how the cryptographic system evolves in response to the event.
   b) Explain changes in the alphabet, encoding methods, or security features.
   c) Discuss how these changes reflect linguistic evolution and information theory principles.

3. Final System Analysis (200-250 words):
   a) Describe the final state of your cryptographic system after all evolutions.
   b) Compare its complexity, security, and efficiency to the initial system.
   c) Explain how it reflects the cumulative impact of the cultural events.

4. Linguistic Impact (150-200 words):
   a) Discuss how your evolving cryptosystem might influence the development of the language itself.
   b) Propose one new linguistic feature (e.g., a new phoneme, grammatical structure) that could emerge as a result.

5. Decryption Challenge (100-150 words):
   a) Provide a short encrypted message (10-15 words) using your final system.
   b) Offer three clues that hint at your system's structure or evolution, without directly revealing the decryption method.

Ensure your response demonstrates a deep understanding of cryptography, linguistics, and information theory. Be creative in your approach while maintaining scientific and logical consistency throughout the system's evolution.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cryptography, linguistics, and information theory.",
            "The cryptographic system evolves logically and creatively in response to each cultural event.",
            "The final system analysis shows clear progression and improvement from the initial system.",
            "The linguistic impact discussion is insightful and well-reasoned.",
            "The decryption challenge is solvable with the given clues but not trivially easy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
