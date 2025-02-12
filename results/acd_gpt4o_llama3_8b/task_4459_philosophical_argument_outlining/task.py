class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Argue for or against the idea that free will is an illusion."},
            "2": {"prompt": "Discuss the ethical implications of artificial intelligence."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Create a structured outline for a philosophical argument based on the following prompt:

Prompt: {prompt}

Your outline should include:
1. Introduction: A brief introduction to the topic and your position.
2. Main Points: At least three main points supporting your argument, each with a brief explanation.
3. Counterarguments: At least two potential counterarguments and your responses to them.
4. Conclusion: A summary of your argument and final thoughts.

Submit your outline as a plain text string in the following format:

Introduction: [Your introduction]
Main Points: [List of main points with explanations]
Counterarguments: [List of counterarguments with responses]
Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The outline should include an introduction, at least three main points, counterarguments with responses, and a conclusion.", "The argument should be coherent and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
