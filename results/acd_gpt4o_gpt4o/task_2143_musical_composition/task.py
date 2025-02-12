class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "style": "classical",
                "length": "8 bars",
                "key": "C major",
                "time_signature": "4/4",
                "requirements": "Include a melody and harmony, with at least one modulation."
            },
            "2": {
                "style": "jazz",
                "length": "12 bars",
                "key": "F major",
                "time_signature": "3/4",
                "requirements": "Include a melody, harmony, and a simple improvisation section."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to compose a short piece of music in the {t['style']} style, based on the given constraints. Provide a detailed description of the composition, including the melody, harmony, and any other musical elements. Ensure that the composition meets the specified requirements and constraints.\n\nConstraints:\n- Length: {t['length']}\n- Key: {t['key']}\n- Time Signature: {t['time_signature']}\n- Requirements: {t['requirements']}\n\nProvide your composition in plain text format, using musical notation or a detailed description. Ensure that your description is clear enough for someone with musical knowledge to understand the composition. Additionally, explain the musical choices you made and how they contribute to the overall composition.\n\nFormat your response as follows:\n- Composition: [Your musical notation or detailed description]\n- Explanation: [Your explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The composition should meet the specified requirements and constraints.", "The melody and harmony should be coherent and stylistically appropriate.", "The explanation should clearly justify the musical choices made."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
