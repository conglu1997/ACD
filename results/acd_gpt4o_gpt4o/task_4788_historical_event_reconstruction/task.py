class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"fragments": [
                "The Archduke was assassinated on June 28, 1914.",
                "Tensions were already high in Europe.",
                "This event is often cited as the spark that ignited World War I."
            ]},
            "2": {"fragments": [
                "The Berlin Wall fell on November 9, 1989.",
                "It symbolized the end of the Cold War.",
                "This event led to the reunification of Germany."
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to reconstruct the following historical event based on the provided fragments.

Fragments:
{t['fragments']}

Provide a detailed reconstruction of the event, explaining its causes, the event itself, and its consequences. Ensure that your narrative is coherent, historically accurate, and well-structured. Format your response as follows:

1. Background and Causes
2. The Event
3. Consequences and Significance
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The reconstruction must be historically accurate.",
            "The narrative must be coherent and well-structured.",
            "The response must cover background, the event, and its consequences."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
