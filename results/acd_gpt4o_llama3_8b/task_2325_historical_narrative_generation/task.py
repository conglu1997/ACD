class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The French Revolution",
                "perspective": "from the viewpoint of a common citizen",
                "elements": "economic hardship, political unrest, key events"
            },
            "2": {
                "event": "The Industrial Revolution",
                "perspective": "from the viewpoint of a factory worker",
                "elements": "working conditions, technological advancements, societal changes"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with generating a detailed narrative about a specific historical event or period. Use the information provided to guide your narrative. Ensure that your narrative is historically accurate, engaging, and incorporates the given elements or perspectives.

Historical Event: {t['event']}
Perspective: {t['perspective']}
Elements to Include: {t['elements']}

Your narrative should be at least 300 words long and should provide a vivid description of the historical context, key events, and the given perspective. Remember to maintain historical accuracy and ensure the narrative is engaging. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be historically accurate.",
            "The narrative should incorporate the given perspective and elements.",
            "The narrative should be at least 300 words long.",
            "The narrative should be engaging and well-written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
