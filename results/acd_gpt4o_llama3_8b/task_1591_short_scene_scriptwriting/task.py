class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characters": [
                    "Alice",
                    "Bob"
                ],
                "setting": "a small café in the evening",
                "plot_prompt": "Alice confronts Bob about a secret he has been keeping."
            },
            "2": {
                "characters": [
                    "John",
                    "Sarah"
                ],
                "setting": "a park bench on a sunny day",
                "plot_prompt": "John reveals his true feelings to Sarah."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a script for a short scene based on the provided information:

Characters: {', '.join(t['characters'])}
Setting: {t['setting']}
Plot Prompt: {t['plot_prompt']}

Ensure that your script includes dialogues, character actions, and descriptions of the setting. The scene should be coherent, with well-developed characters and a clear narrative flow. Submit your script as a plain text string in the following format:

[Your script here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The script should include dialogues, character actions, and descriptions of the setting.",
            "The scene should be coherent, with well-developed characters and a clear narrative flow.",
            "The response should demonstrate creativity and narrative consistency."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
