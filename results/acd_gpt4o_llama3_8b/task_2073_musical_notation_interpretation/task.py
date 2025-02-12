class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sheet_music": "G4 E4 F4 D4 C4 G4 E4 F4 D4 C4",
                "context": "Interpret the given sheet music and provide a detailed description of the musical piece, including aspects like rhythm, tempo, and mood."
            },
            "2": {
                "sheet_music": "A4 A4 G4 F4 E4 D4 C4 A4 A4 G4 F4 E4 D4 C4",
                "context": "Interpret the given sheet music and provide a detailed description of the musical piece, including aspects like rhythm, tempo, and mood."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        sheet_music = t["sheet_music"]
        context = t["context"]
        return f"""Interpret the following sheet music: {sheet_music}.\n
{context}\n
Your description should include the following aspects:\n1. Rhythm\n2. Tempo\n3. Mood\n\nSubmit your response as a plain text string in the following format: 'Description: [Your detailed description of the musical piece, at least 100 words]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately interpret the musical notation.", "The response should provide a detailed and coherent description of the musical piece, covering rhythm, tempo, and mood.", "The response should be at least 100 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
