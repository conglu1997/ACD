class TaskFamily:
    import base64

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A mobile banking app home screen.",
                "screenshot": "<base64_encoded_image_1>"
            },
            "2": {
                "description": "A social media app profile page.",
                "screenshot": "<base64_encoded_image_2>"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to analyze and critique the following user interface design based on the provided screenshot and description.

Description: {description}

In your critique, you should:
1. Evaluate the overall aesthetics of the design.
2. Discuss the usability and navigation of the interface.
3. Identify any potential issues or improvements.
4. Consider the user experience principles and how well they are applied.

Your critique should be detailed, well-structured, and at least 300 words long.

Provide your critique in a clear and structured format, with each section clearly labeled. Format your response as follows:

Critique:
[Your detailed critique]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The critique should evaluate the overall aesthetics of the design.",
            "The usability and navigation of the interface should be discussed.",
            "Potential issues or improvements should be identified.",
            "User experience principles should be considered and discussed.",
            "The critique should be at least 300 words long.",
            "The critique should be detailed and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
