class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "philosophical_text": "In his 'Meditations on First Philosophy', René Descartes famously posits 'Cogito, ergo sum' (I think, therefore I am) as a fundamental element of his epistemological framework. He argues that the very act of doubt implies a doubter, thus establishing his existence as a thinking entity. Descartes further explores the nature of the mind and its distinction from the body, leading to his dualist theory of mind and body.",
                "task_type": "analyze"
            },
            "2": {
                "philosophical_topic": "Is free will compatible with determinism? Present an argument either in favor of or against the compatibility of free will and determinism. Your argument should be clear, logically structured, and consider possible counterarguments.",
                "task_type": "construct"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "analyze":
            return f"""Analyze the following philosophical text. Identify the main argument presented by the philosopher, and explain its significance within the broader philosophical context. Your analysis should be clear, concise, and provide a thorough understanding of the text.

Philosophical Text:
{t['philosophical_text']}

Submit your analysis as a plain text string in the following format:
'Analysis: [Your analysis here]'"""
        elif t["task_type"] == "construct":
            return f"""Construct a coherent argument on the given philosophical topic. Present an argument either in favor of or against the topic, ensuring that your argument is clear, logically structured, and considers possible counterarguments.

Philosophical Topic:
{t['philosophical_topic']}

Submit your argument as a plain text string in the following format:
'Argument: [Your argument here]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "analyze":
            validation_criteria = ["The analysis should identify the main argument presented by the philosopher.", "The analysis should explain the significance of the argument within the broader philosophical context.", "The analysis should be clear and concise."]
        elif t["task_type"] == "construct":
            validation_criteria = ["The argument should be clear and logically structured.", "The argument should consider possible counterarguments.", "The argument should provide a thorough understanding of the philosophical topic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
