class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poem": "Do not go gentle into that good night,\nOld age should burn and rave at close of day;\nRage, rage against the dying of the light.",
                "task_type": "interpret"
            },
            "2": {
                "prompt": "Generate a poem based on the theme of 'hope in adversity'. Your poem should be between 4-8 lines and use at least one poetic device (e.g., metaphor, simile, alliteration).",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            return f"""Interpret the following poem. Provide an in-depth analysis of its meaning, themes, and any poetic devices used. Discuss how the form and structure contribute to the overall impact of the poem.

Poem:
{t['poem']}

Submit your interpretation as a plain text string in the following format:
'Meaning: [Your interpretation of the poem's meaning]'
'Themes: [The themes you identified]'
'Poetic Devices: [The poetic devices you identified and how they are used]'
'Form and Structure: [How the form and structure contribute to the poem]"""
        elif t["task_type"] == "generate":
            return f"""Generate a new poem based on the given theme and constraints. Ensure your poem is original, creative, and uses at least one poetic device.

Prompt:
{t['prompt']}

Submit your poem as a plain text string in the following format:
'Poem: [Your poem here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            validation_criteria = ["The interpretation must accurately reflect the poem's meaning, themes, poetic devices, and consider the form and structure."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated poem must be original, creative, and use at least one poetic device."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
