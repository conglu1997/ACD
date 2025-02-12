class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "A serene morning in a forest",
                "constraints": "Use a 4/4 time signature and include at least one modulation."
            },
            "2": {
                "theme": "A bustling city at night",
                "constraints": "Use a 3/4 time signature and include a minor-to-major key change."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task:

Generate a musical composition based on the given theme and constraints. The composition should:
1. Be written in standard musical notation using ABC notation. Here are examples of ABC notation for simple melodies and modulations:

Example 1:
X: 1
T: Simple Melody
M: 4/4
K: C
G4 G4 | A4 A4 | G4 G4 | E4 E4 |

Example 2:
X: 2
T: Modulation Example
M: 4/4
K: C
G4 G4 | A4 A4 | G4 G4 | E4 E4 |
K: G
D4 D4 | E4 E4 | D4 D4 | B4 B4 |

2. Adhere to the specified time signature and include the required modulations or key changes. A modulation is a change from one key to another within a piece of music, and it should be clearly marked in the notation (e.g., 'K: G' for a modulation to G major).

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure that your composition is creative, coherent, and follows the given constraints. Submit your response as a plain text string in ABC notation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should follow the given theme.",
            "The composition should adhere to the specified time signature.",
            "The composition should include the required modulations or key changes, clearly marked in the notation.",
            "The composition should be written in standard musical notation (ABC notation)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
