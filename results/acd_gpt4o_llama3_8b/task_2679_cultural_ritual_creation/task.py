class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Harvest Festival",
                "context": "A fictional society that lives in a mountainous region and relies heavily on agriculture."
            },
            "2": {
                "theme": "Coming of Age Ceremony",
                "context": "A fictional society that lives on a tropical island and has a strong tradition of seafaring."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed description of a fictional cultural ritual based on the given theme and context.\n\nTheme: {t['theme']}\nContext: {t['context']}\n\nYour description should include the following elements:\n1. A brief overview of the ritual.\n2. The symbolic significance of the ritual.\n3. The steps and activities involved in the ritual.\n4. The role of different participants in the ritual.\n5. Any special attire, instruments, or artifacts used in the ritual.\n\nFormat your response as follows:\n- Overview: [Your overview]\n- Significance: [The symbolic significance]\n- Steps: [The steps and activities]\n- Participants: [The role of participants]\n- Attire and Artifacts: [Special attire, instruments, or artifacts]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be creative and coherent.",
            "The response should appropriately fit the given theme and context.",
            "The response should include all specified elements: overview, significance, steps, participants, attire and artifacts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
