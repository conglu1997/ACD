class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Compose a 16-bar melody in C major, 4/4 time signature, using only quarter notes and eighth notes."},
            "2": {"piece": "C D E F | G A B C | D E F G | A B C D | E F G A | B C D E | F G A B | C D E F", "question": "Identify the key, time signature, and structure of the provided musical piece."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            constraints = t["constraints"]
            instructions = f"""Your task is to generate a short piece of music based on the following constraints:

Constraints: {constraints}

Ensure that your composition adheres to the given constraints and is musically coherent. Provide your composition in plain text format using a simple notation (e.g., ABC notation or a textual description of the melody). Example format: C D E F | G A B C | D E F G | A B C D | E F G A | B C D E | F G A B | C D E F."""
        else:
            piece = t["piece"]
            question = t["question"]
            instructions = f"""Your task is to analyze the provided musical piece and answer the following question:

Piece: {piece}

Question: {question}

Ensure that your analysis is accurate and includes all relevant musical features. Provide your analysis in plain text format. Your analysis should include the key (e.g., C major), time signature (e.g., 4/4), and the structure (e.g., 16 bars)."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            criteria = ["The composition adheres to the given constraints.", "The composition is musically coherent."]
        else:
            criteria = ["The analysis correctly identifies the key (C major), time signature (4/4), and structure (16 bars)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
