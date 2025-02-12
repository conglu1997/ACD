class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "In the 19th century, the Industrial Revolution brought significant changes to society. It began in Great Britain and quickly spread to other parts of the world, transforming economies from agrarian to industrial.", "question": "What were two major societal changes brought by the Industrial Revolution?"},
            "2": {"context": "The Japanese tea ceremony, also known as 'chanoyu', is a traditional ritual influenced by Zen Buddhism. It involves the preparation and consumption of matcha, a powdered green tea. The ceremony emphasizes aesthetics, grace, and mindfulness.", "question": "What are two key elements of the Japanese tea ceremony?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following context and answer the question based on the provided information.

Context: {t["context"]}

Question: {t["question"]}
Provide your answer in a clear, concise format, listing the two elements or changes in bullet points."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
