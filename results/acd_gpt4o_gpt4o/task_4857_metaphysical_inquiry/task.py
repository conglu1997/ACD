class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "explain", "concept": "The nature of time"},
            "2": {"task": "argue", "statement": "Free will is an illusion."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "explain":
            return f"Your task is to explain the following metaphysical concept: '{t['concept']}'. Provide a detailed and coherent explanation, including different perspectives and theories related to the concept. Ensure your explanation is well-structured and demonstrates a deep understanding of the topic. Provide your explanation in plain text format."
        elif t["task"] == "argue":
            return f"Your task is to argue for or against the following philosophical statement: '{t['statement']}'. Provide a well-structured and logical argument, clearly stating your position and supporting it with relevant reasoning and evidence. Ensure your argument is coherent and demonstrates a deep understanding of the topic. Provide your argument in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "explain":
            criteria = [
                "The explanation should be detailed and coherent.",
                "The explanation should include different perspectives and theories.",
                "The explanation should demonstrate a deep understanding of the topic."
            ]
        elif t["task"] == "argue":
            criteria = [
                "The argument should be well-structured and logical.",
                "The argument should clearly state the position and support it with relevant reasoning and evidence.",
                "The argument should demonstrate a deep understanding of the topic."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
