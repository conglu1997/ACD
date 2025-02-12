import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "rhythm",
            "melody",
            "harmony",
            "form",
            "timbre"
        ]
        operations = [
            "analyze",
            "modify",
            "create"
        ]
        constraints = [
            "using only prime numbers",
            "based on the Fibonacci sequence",
            "using a specific scale or mode",
            "incorporating golden ratio proportions",
            "using a mathematical sequence as a basis"
        ]
        return {
            "1": {
                "element": random.choice(musical_elements),
                "operation": random.choice(operations),
                "constraint": random.choice(constraints)
            },
            "2": {
                "element": random.choice(musical_elements),
                "operation": random.choice(operations),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to {t['operation']} a musical {t['element']} {t['constraint']}. Your response should include:

1. A brief explanation of the musical {t['element']} and the given constraint (2-3 sentences)
2. Your approach to {t['operation']}ing the {t['element']} based on the constraint (3-4 sentences)
3. A specific example of your result, using standard musical notation, ASCII representation, or clear verbal description (5-6 sentences)
4. An analysis of how your result adheres to both musical principles and the given mathematical constraint (3-4 sentences)

Ensure that your response demonstrates a deep understanding of both music theory and the mathematical concept involved. Be creative in your approach while maintaining musical coherence and mathematical accuracy. Use standard musical terminology and concepts throughout your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the musical {t['element']} and the given constraint.",
            f"The approach to {t['operation']}ing the {t['element']} is clear, creative, and follows the constraint.",
            "The example provided is specific, well-described, and musically coherent.",
            "The analysis demonstrates a deep understanding of both music theory and the mathematical concept.",
            "The response adheres to the requested format and sentence counts.",
            "Standard musical terminology and concepts are used throughout the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
