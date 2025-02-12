class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The signing of the Declaration of Independence in 1776.",
                "speculative_element": "What if the founding fathers had access to modern technology (e.g., smartphones, the internet)?"
            },
            "2": {
                "historical_event": "The fall of the Roman Empire in 476 AD.",
                "speculative_element": "What if the Roman Empire had discovered steam power and early industrial machinery?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a speculative fiction narrative based on the following historical event and speculative element. Your narrative should include:

1. A brief summary of the historical event, including accurate historical details.
2. A speculative twist based on the given speculative element.
3. A coherent and imaginative storyline that integrates both the historical facts and speculative element.
4. Ensure that the narrative is clear, engaging, and well-structured.

Submit your narrative as a plain text string in the following format:

Historical Event:
{t['historical_event']}

Speculative Element:
{t['speculative_element']}

Narrative:
[Your narrative here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should accurately summarize the historical event.",
            "The narrative should creatively integrate the speculative element.",
            "The narrative should be coherent, engaging, and well-structured.",
            "The narrative should demonstrate understanding of both historical facts and speculative fiction."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0