class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"script": "A young girl finds a mysterious key in her attic. She discovers it opens a hidden door that leads to a magical world where she meets various fantastical creatures."},
            "2": {"storyboard": "Panel 1: A girl in an attic, looking around.\nPanel 2: She finds a key in a dusty old box.\nPanel 3: She looks puzzled and examines the key.\nPanel 4: She discovers a hidden door behind some old furniture.\nPanel 5: She uses the key to unlock the door.\nPanel 6: The door opens to reveal a magical world with fantastical creatures."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "script" in t:
            return f"""Create a storyboard based on the following script. Your storyboard should consist of six panels, each describing a key moment from the script. Ensure that your descriptions are clear and concise, capturing the essence of each scene. Submit your storyboard as a plain text string in the format: Panel 1: [Description] Panel 2: [Description] Panel 3: [Description] Panel 4: [Description] Panel 5: [Description] Panel 6: [Description]

Script: {t["script"]}"""
        elif "storyboard" in t:
            return f"""Interpret the following storyboard and describe the narrative it is depicting. Ensure that your description is clear and captures the sequence of events as illustrated by the storyboard. Submit your narrative description as a plain text string.

Storyboard: {t["storyboard"]}"""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "script" in t:
            criteria = ["The storyboard should consist of six panels.", "Each panel should accurately reflect a key moment from the script.", "Descriptions should be clear and concise."]
        elif "storyboard" in t:
            criteria = ["The narrative description should accurately interpret the storyboard.", "The sequence of events should be logically consistent.", "The description should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
