class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"excerpt": "The unexamined life is not worth living. - Socrates", "context": "From Plato's Apology, where Socrates defends his practice of questioning and examining life."},
            "2": {"excerpt": "One cannot step twice in the same river. - Heraclitus", "context": "A reference to Heraclitus' doctrine of change, emphasizing the constant flux of life."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and analyze the following philosophical text.

Text:
{t['excerpt']}

Context:
{t['context']}

Provide a detailed analysis of the text, explaining its meaning, context, and significance. Discuss the philosophical ideas presented and offer your evaluation of the argument. Ensure your response is well-structured, coherent, and demonstrates a deep understanding of the text.

Format your response as follows:

1. Interpretation of the text
2. Context and significance
3. Analysis of philosophical ideas
4. Evaluation of the argument
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must accurately interpret the text.",
            "The response must provide relevant context and significance.",
            "The analysis must demonstrate understanding of philosophical ideas.",
            "The evaluation must be coherent and well-argued."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
