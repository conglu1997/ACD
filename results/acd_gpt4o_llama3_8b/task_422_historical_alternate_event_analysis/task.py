class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The American Revolution was unsuccessful, and the American colonies remained under British control.",
                "constraints": "Describe how the political, social, and economic landscape of North America might have evolved differently. Consider the impact on key historical events and figures."
            },
            "2": {
                "event": "The Roman Empire never fell and continued to expand and modernize.",
                "constraints": "Describe how the cultural, technological, and political landscape of Europe and the world might have evolved differently. Consider the impact on key historical events and figures."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and describe the potential alternate outcomes of the following historical event if it had occurred differently:

Event:
{t['event']}

Constraints:
{t['constraints']}

Your analysis should be logical, well-reasoned, and creative. Consider the broader implications on political, social, economic, and cultural aspects. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should be logical and well-reasoned.",
            "The analysis should be creative and consider broader implications.",
            "The response should address political, social, economic, and cultural aspects.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
