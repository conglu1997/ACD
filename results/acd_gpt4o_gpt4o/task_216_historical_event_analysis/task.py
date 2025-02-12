class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776.", "change": "The Continental Congress decided not to declare independence from Britain."},
            "2": {"event": "The fall of the Berlin Wall in 1989.", "change": "The Soviet Union decided to intervene militarily to maintain control."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze a historical event and predict alternative outcomes based on different initial conditions. Given the event: '{t["event"]}' and the change: '{t["change"]}', provide a detailed analysis that includes:
1. A brief description of the original historical event, including its causes and key players.
2. An explanation of the potential immediate consequences of the change, considering multiple factors or stakeholders.
3. A prediction of the long-term effects on the world, including political, social, and economic impacts.
4. The reasoning behind your predictions, ensuring a coherent and logical narrative.

Your response should be historically plausible, well-organized, and cover all required components in a clear manner."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief description of the original historical event, including its causes and key players.",
            "The response should explain the potential immediate consequences of the change, considering multiple factors or stakeholders.",
            "The response should predict the long-term effects on the world, including political, social, and economic impacts.",
            "The reasoning behind the predictions should be clear and logical, forming a coherent narrative.",
            "The analysis should be historically plausible and well-organized."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
