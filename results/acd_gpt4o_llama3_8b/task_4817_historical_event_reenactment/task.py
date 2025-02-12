class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776.", "background": "In 1776, representatives from the Thirteen Colonies gathered in Philadelphia to declare independence from British rule. The signing of the Declaration of Independence was a pivotal moment in American history."},
            "2": {"event": "The fall of the Berlin Wall in 1989.", "background": "In 1989, the Berlin Wall, which had divided East and West Berlin for decades, fell, leading to the reunification of Germany. This event marked the end of the Cold War and was a significant moment in world history."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        background = t["background"]
        return f"""Recreate a detailed re-enactment of the following historical event, including dialogues and actions of the key historical figures involved. Your re-enactment should be between 300 to 500 words.\n\nEvent: {event}\n\nBackground: {background}\n\nYour response should include:\n1. A brief introduction setting the scene. (e.g., Describe the location, date, and overall atmosphere.)\n2. Detailed dialogues between the key figures. (e.g., Provide realistic conversations based on historical context.)\n3. Descriptions of actions and interactions among the figures. (e.g., Describe significant actions taken by the historical figures.)\n4. Any notable reactions from the surrounding people or audience. (e.g., Describe how the crowd or other individuals responded to the event.)\n5. Ensure that the re-enactment is historically accurate, contextually appropriate, and creatively written.\n6. Cover all the elements listed above to meet the criteria for a successful re-enactment. Each section must be included to achieve a full score."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The re-enactment should be historically accurate.",
            "The dialogues should be contextually appropriate and realistic.",
            "The actions and interactions should be coherent and fitting to the historical context.",
            "The narrative should be creatively written.",
            "The response should be between 300 to 500 words.",
            "The re-enactment should include a brief introduction, detailed dialogues, actions and interactions, and notable reactions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
