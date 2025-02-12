import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        elements = [
            {"symbol": "Au", "name": "Gold", "atomic_number": 79},
            {"symbol": "Ag", "name": "Silver", "atomic_number": 47},
            {"symbol": "Fe", "name": "Iron", "atomic_number": 26},
            {"symbol": "Hg", "name": "Mercury", "atomic_number": 80},
            {"symbol": "Ne", "name": "Neon", "atomic_number": 10},
            {"symbol": "He", "name": "Helium", "atomic_number": 2}
        ]
        return {
            "1": random.choice(elements),
            "2": random.choice(elements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a poem inspired by the chemical element {t['name']} (symbol: {t['symbol']}, atomic number: {t['atomic_number']}).

Your poem should:
1. Be exactly 4 lines long
2. Include the element's name, symbol, or atomic number
3. Reference at least one physical property or common use of the element
4. Use a metaphor or simile comparing the element to something unrelated to chemistry

Ensure your poem is creative, scientifically accurate, and follows the given constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The poem must be exactly 4 lines long.",
            f"The poem must include the element's name ({t['name']}), symbol ({t['symbol']}), or atomic number ({t['atomic_number']}).",
            "The poem must reference at least one physical property or common use of the element.",
            "The poem must use a metaphor or simile comparing the element to something unrelated to chemistry.",
            "The poem must be creative and scientifically accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
