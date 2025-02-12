class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are running for class president. Write a persuasive speech convincing your classmates to vote for you. Highlight your strengths, your plans for the school, and why you are the best candidate for the position.",
                "answer": "N/A"
            },
            "2": {
                "scenario": "A local park is in danger of being turned into a commercial shopping area. Write a persuasive essay arguing against the development and advocating for the preservation of the park. Include points about the environmental, social, and community benefits of keeping the park.",
                "answer": "N/A"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a persuasive piece based on the given scenario:

Scenario:
{t['scenario']}

Your writing should be compelling, logically structured, and clearly communicate your main points. Imagine your target audience and tailor your arguments to have the desired impact on them.

Submit your response as a plain text string in the following format:

Title: [Your title]
Content: [Your content]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The writing should be persuasive and compelling.",
            "The structure of the content should be logical and clear.",
            "The main points should be effectively communicated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
