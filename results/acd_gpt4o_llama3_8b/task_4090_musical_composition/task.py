class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Compose a 16-bar piece of music in 4/4 time signature using a minor key. Include at least one modulation to a related key and return to the original key by the end. Include dynamics and articulations."},
            "2": {
                "constraints": "Compose a 12-bar blues progression in 12/8 time signature. Use the I-IV-V chord progression in a major key, and include at least two variations in the rhythm or harmony. Include dynamics and articulations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short piece of music based on the following constraints:

Constraints: {t['constraints']}

Your composition should be written in standard musical notation. You can use any method to generate the notation, but the final submission should be a plain text string in ABC notation format. ABC notation is a shorthand form of musical notation that uses letters and symbols to represent music. Ensure your ABC notation is syntactically correct and complete, including dynamics and articulations. Dynamics can be represented using symbols such as 'f' for forte and 'p' for piano, while articulations can be represented using symbols such as '>' for accents and '.' for staccato. Here is a brief example of ABC notation for reference:

X: 1
T: Simple Scale
M: 4/4
K: C
C D E F | G A B c |

Submit your response as a plain text string in the following format:

Composition: [Your ABC notation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The composition should adhere to the specified constraints.",
            "The composition should demonstrate a coherent musical structure and be musically engaging.",
            "The ABC notation should be syntactically correct and complete.",
            "Dynamics and articulations should be appropriately included."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
