class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Introduction to Neural Networks",
                "answer": "N/A"
            },
            "2": {
                "topic": "How to Set Up a Virtual Private Network (VPN) on a Windows System",
                "answer": "N/A"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed tutorial on the given technical topic:

Topic:
{t['topic']}

Your tutorial should include the following sections:
1. Introduction: Provide an overview of the topic and its importance.
2. Detailed Explanation: Break down the topic into key concepts and explain each one clearly.
3. Step-by-Step Instructions: Provide practical instructions or examples if applicable.
4. Conclusion: Summarize the main points and mention any additional resources for further reading.

Submit your response as a plain text string in the following format:

Title: [Your title]
Content: [Your content]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The tutorial should be clear and easy to understand.",
            "The explanation should be detailed and cover all key concepts.",
            "The step-by-step instructions should be practical and easy to follow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
