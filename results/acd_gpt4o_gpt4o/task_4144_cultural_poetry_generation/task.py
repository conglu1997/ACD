class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "blossoming love in spring", "culture": "Japanese", "form": "haiku"},
            "2": {"theme": "a stormy night by the sea", "culture": "Irish", "form": "quatrain"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a poem based on the given theme and cultural context. Ensure that the poem adheres to the specified form and reflects the cultural nuances appropriately.

Theme: {t['theme']}
Culture: {t['culture']}
Form: {t['form']}

Provide your poem in plain text format.

Your response format:
Poem: [Your poem]

Note: Pay special attention to cultural elements that are characteristic of the specified culture. For example, a Japanese haiku often reflects nature and seasons, while an Irish quatrain might include elements of the natural landscape or folklore."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the specified form.",
            "The poem should reflect the given theme.",
            "The poem should include cultural elements appropriate to the specified culture.",
            "The poem should be creative and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
