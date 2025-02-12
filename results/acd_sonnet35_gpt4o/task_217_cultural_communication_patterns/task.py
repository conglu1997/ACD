import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Javanese",
                "hierarchy": "High",
                "collectivism": "High",
                "communication_style": "Indirect",
                "context": "High-context",
                "time_orientation": "Polychronic",
                "key_values": ["Harmony", "Respect", "Hierarchy"]
            },
            {
                "name": "Finnish",
                "hierarchy": "Low",
                "collectivism": "Low",
                "communication_style": "Direct",
                "context": "Low-context",
                "time_orientation": "Monochronic",
                "key_values": ["Equality", "Independence", "Privacy"]
            },
            {
                "name": "Maasai",
                "hierarchy": "Medium",
                "collectivism": "High",
                "communication_style": "Mixed",
                "context": "High-context",
                "time_orientation": "Polychronic",
                "key_values": ["Community", "Tradition", "Bravery"]
            }
        ]
        scenarios = [
            "Requesting a favor from a superior",
            "Declining an invitation from a friend",
            "Negotiating a business deal",
            "Expressing disagreement in a group setting",
            "Offering condolences to a grieving colleague",
            "Giving feedback to a subordinate",
            "Asking for directions from a stranger",
            "Mediating a conflict between family members"
        ]
        return {
            "1": {"culture": random.choice(cultures), "scenario": random.choice(scenarios)},
            "2": {"culture": random.choice(cultures), "scenario": random.choice(scenarios)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze and generate a culturally appropriate communication pattern for the following scenario:\n\nCulture: {t['culture']['name']}\nScenario: {t['scenario']}\n\nCultural characteristics:\n" + \
               '\n'.join([f"- {k}: {v}" for k, v in t['culture'].items() if k != 'name']) + "\n\n" + \
               "Your task:\n" + \
               "1. Explain how the given cultural characteristics would influence communication in this scenario (100-150 words).\n" + \
               "2. Generate a sample dialogue or monologue demonstrating the appropriate communication pattern (100-150 words).\n" + \
               "3. Analyze your generated communication, highlighting specific elements that reflect the culture's characteristics (100-150 words).\n\n" + \
               "Ensure your response demonstrates a deep understanding of cultural anthropology and linguistics, " + \
               "and shows how language use adapts to specific cultural contexts."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains how {t['culture']['name']} cultural characteristics influence communication in the given scenario.",
            "The generated dialogue or monologue demonstrates appropriate communication patterns for the specified culture and scenario.",
            "The analysis highlights specific elements in the generated communication that reflect the culture's characteristics.",
            "The response shows a deep understanding of cultural anthropology and linguistics.",
            "The explanation, dialogue/monologue, and analysis are each within the 100-150 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
