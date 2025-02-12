class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776.", "context": "Rewrite this event as a scene in a science fiction novel, incorporating elements of advanced technology and interstellar politics."},
            "2": {"event": "The fall of the Berlin Wall in 1989.", "context": "Rewrite this event as a modern-day news article, focusing on the social media reaction and the role of digital communications."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to recontextualize the following historical event into a different genre or context while maintaining the core facts. Here is the event and the context: 

Event: {t["event"]}
Context: {t["context"]}

Provide your response in the following format:

1. Original Event: [the provided event]
2. Recontextualized Event: [your reimagined version of the event in the specified context]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should maintain the core facts of the historical event.",
            "The submission should effectively adapt the event to the specified context.",
            "The submission should incorporate the specific narrative elements or constraints provided in the context.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
