class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A young girl named Emily loses her beloved pet dog, Max, and finds solace in an unexpected friendship with her neighbor, Mrs. Anderson, who is also grieving the loss of her husband. The story should explore how this new friendship helps both characters cope with their losses."},
            "2": {
                "scenario": "An elderly man named Mr. Thompson reflects on his life after receiving a letter from his old friend, Sarah, whom he hasn't seen in over fifty years. The letter brings back a flood of memories and unresolved emotions, leading him to contemplate reaching out to Sarah."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short story based on the following emotional scenario and provide a rationale for the emotional arc of the story:

Scenario: {t['scenario']}

Your story should be between 300 to 500 words. After the story, include a rationale explaining the emotional journey of the characters. Your rationale should detail how the characters' emotions evolve throughout the story and how you chose to portray these emotions. Submit your response as a plain text string in the following format:

Story: [Your short story]\nRationale: [Your rationale for the emotional arc of the story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be emotionally engaging and coherent.",
            "The rationale should clearly explain the emotional journey of the characters and how these emotions were portrayed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
