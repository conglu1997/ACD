class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Compose a short piece of music (4-8 lines) in the style of a classical waltz."},
            "2": {"music_piece": "The opening bars of Beethoven's 'Für Elise': E-D#-E-D#-E-B-D-C-A."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "criteria" in t:
            instructions = f"""Your task is to compose a short piece of music based on the following criteria:

{t['criteria']}

Ensure that your composition is coherent, adheres to the specified style, and is creatively engaging. Provide your composition in plain text format, structured as musical notation or described textually if notation is not possible. Format:

1. Musical Notation: [Provide notation]
2. Descriptive Text: [Describe the music if notation is not possible]"""
        else:
            instructions = f"""Your task is to interpret the following musical piece and provide a reasoned explanation of its meaning or the emotion it conveys:

{t['music_piece']}

Ensure that your interpretation is clear, coherent, and demonstrates an understanding of the musical elements and their impact on the listener. Provide your interpretation in plain text format, structured as follows:

1. Overview: [General impression of the piece]
2. Interpretation: [Detailed interpretation of the meaning or emotion]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "criteria" in t:
            criteria = ["The composition should adhere to the specified style.", "The composition should be coherent and creatively engaging."]
        else:
            criteria = ["The interpretation should provide a reasoned explanation of the meaning or emotion of the piece.", "The interpretation should demonstrate an understanding of the musical elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
