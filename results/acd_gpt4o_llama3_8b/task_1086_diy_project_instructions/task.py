class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "project": "Build a birdhouse",
                "materials": [
                    "Wooden planks",
                    "Nails",
                    "Hammer",
                    "Saw",
                    "Sandpaper",
                    "Wood glue",
                    "Paint",
                    "Paintbrush"
                ]
            },
            "2": {
                "project": "Create a homemade candle",
                "materials": [
                    "Wax",
                    "Wick",
                    "Essential oils",
                    "Dye",
                    "Mold",
                    "Double boiler",
                    "Thermometer"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        import json
        return f"""Generate detailed step-by-step instructions for completing the following DIY project: {t['project']}. The materials available are: {', '.join(t['materials'])}. Ensure that the instructions are clear, logically sequenced, and cover all necessary steps from start to finish. Provide a brief description of the project and then list the steps in a numbered format. Submit your response as a plain text string in the following format:

Project Description: [Brief description of the project]
Step 1: [First step]
Step 2: [Second step]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should include all steps necessary to complete the project.",
            "The instructions should be logically sequenced and easy to follow.",
            "The instructions should make appropriate use of all listed materials.",
            "The instructions should be in the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
