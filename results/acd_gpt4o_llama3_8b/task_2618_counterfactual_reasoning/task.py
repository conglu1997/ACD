class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The industrial revolution never happened.",
                "prompt": "Imagine a world where the industrial revolution never happened. Describe the potential social, economic, and technological impacts of this counterfactual scenario."
            },
            "2": {
                "event": "Humans discovered fire 1,000 years later than they actually did.",
                "prompt": "Imagine a world where humans discovered fire 1,000 years later than they actually did. Describe the potential impacts on human evolution, society, and technological advancements."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Imagine the following counterfactual scenario and describe the potential impacts. Your response should be well-structured, logically coherent, and demonstrate a deep understanding of the implications of the scenario. Here is the scenario:

{t['event']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should logically explore the implications of the counterfactual scenario.",
            "The response should be well-structured and coherent.",
            "The response should demonstrate a deep understanding of the scenario's potential impacts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
