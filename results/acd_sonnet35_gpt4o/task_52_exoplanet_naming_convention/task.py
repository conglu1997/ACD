import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'system': 'Alpha Centauri',
                'planets': [
                    {'mass': 1.1, 'composition': 'rocky', 'atmosphere': 'thin', 'temperature': 'hot'},
                    {'mass': 0.3, 'composition': 'icy', 'atmosphere': 'thick', 'temperature': 'cold'},
                    {'mass': 15.0, 'composition': 'gas giant', 'atmosphere': 'stormy', 'temperature': 'warm'}
                ]
            },
            {
                'system': 'Trappist',
                'planets': [
                    {'mass': 0.8, 'composition': 'rocky', 'atmosphere': 'none', 'temperature': 'extreme hot'},
                    {'mass': 1.2, 'composition': 'rocky', 'atmosphere': 'thin', 'temperature': 'temperate'},
                    {'mass': 5.0, 'composition': 'gas dwarf', 'atmosphere': 'dense', 'temperature': 'cold'}
                ]
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a systematic naming convention for exoplanets based on their physical characteristics, and apply it to the newly discovered planets in the {t['system']} system. Your task:

1. Design a naming system that incorporates information about a planet's mass, composition, atmosphere, and temperature. The system should be logical, consistent, and allow for easy interpretation of a planet's key features from its name.

2. Explain your naming convention, including how each characteristic is represented (e.g., prefixes, suffixes, numerical codes). Your explanation should be clear and concise (3-4 sentences).

3. Apply your naming convention to name the following planets in the {t['system']} system:

{', '.join(f"Planet {i+1}: " + ', '.join(f"{k}: {v}" for k, v in planet.items()) for i, planet in enumerate(t['planets']))}

4. For each planet, provide its new name and a brief explanation of how the name reflects its characteristics (1-2 sentences per planet).

Ensure your naming convention is scientific, logical, and allows for easy expansion to include more planets and characteristics in the future."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The naming convention is logical, consistent, and incorporates all four given characteristics (mass, composition, atmosphere, temperature).",
            "The explanation of the naming convention is clear and concise.",
            "The convention is applied correctly and consistently to all given planets.",
            "Each planet's name accurately reflects its characteristics according to the established convention.",
            "The naming system is flexible enough to accommodate a wide range of planetary characteristics and future discoveries."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
