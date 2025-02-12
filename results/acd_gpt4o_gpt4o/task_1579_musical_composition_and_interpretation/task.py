class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Compose a 4-bar melody in C major, using quarter notes and half notes only. The melody should start and end on a C note.", "type": "compose"},
            "2": {"scenario": "A piece of music starts with a slow, melancholic piano melody in a minor key, followed by a sudden transition to an upbeat, energetic section with a full orchestra. The transition should evoke a sense of hope and resolution.", "type": "interpret"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'compose':
            return f"""Your task is to compose a simple melody based on the given constraints. Ensure that your composition adheres to the specified musical constraints.

Constraints: {t['constraints']}

Provide your melody in plain text format, using standard musical notation (e.g., C4, D4, E4 for quarter notes; C4- for half notes)."""
        elif t['type'] == 'interpret':
            return f"""Your task is to interpret the following musical scenario. Describe in detail the emotions and imagery that the music evokes and explain how the musical elements contribute to these effects.

Scenario: {t['scenario']}

Provide your interpretation in plain text format, ensuring it is detailed and insightful. Your response should include a discussion of the key, tempo, dynamics, instrumentation, and any other relevant musical elements."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'compose':
            criteria = ["The melody should adhere to the given constraints (4-bars, C major, quarter and half notes only, starts and ends on a C note).", "The melody should be musically coherent."]
        elif t['type'] == 'interpret':
            criteria = ["The interpretation should accurately reflect the emotions and imagery evoked by the musical scenario.", "The explanation should detail how the musical elements contribute to these effects.", "The response should discuss key, tempo, dynamics, instrumentation, and other relevant musical elements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
