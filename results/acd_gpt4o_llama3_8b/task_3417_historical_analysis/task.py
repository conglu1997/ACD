class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Roman Empire", "argument": "Identify and argue the primary cause of the fall of the Roman Empire."},
            "2": {"event": "The Industrial Revolution", "argument": "Evaluate the most significant impact of the Industrial Revolution on modern society."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        argument = t["argument"]
        return f"""Analyze the following historical event and construct a coherent argument based on the given prompt.

Historical Event: {event}

Prompt: {argument}

Your analysis should include:
1. A brief overview of the historical event (2-3 sentences).
2. A well-structured argument supporting your point of view (2-3 paragraphs).
3. Relevant historical evidence and examples to support your argument (at least 3 pieces of evidence).
4. Consideration of potential counterarguments and rebuttals (1-2 paragraphs).

Submit your response as a plain text string in the following format:

Overview: [Your brief overview]
Argument: [Your argument]
Evidence: [Your supporting evidence]
Counterarguments: [Your consideration of counterarguments]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should include a brief and accurate overview of the historical event (2-3 sentences).",
            "The argument should be well-structured and coherent (2-3 paragraphs).",
            "The argument should be supported by at least 3 pieces of relevant historical evidence.",
            "Consideration of potential counterarguments and rebuttals should be included (1-2 paragraphs)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
