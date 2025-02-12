class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_prompt": "Once upon a time in a small village, there lived a young boy named Lucas who loved exploring the forest.", "continuation_input": "One day, Lucas found a mysterious map."},
            "2": {"initial_prompt": "In a distant galaxy, there was a spaceship captain named Zara who was on a mission to find a new habitable planet.", "continuation_input": "During her journey, Zara encountered an alien species."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_prompt = t["initial_prompt"]
        continuation_input = t["continuation_input"]
        instructions = f"""Your task is to generate a story based on the initial prompt provided below. Then, continue the story incorporating the new input provided.

Initial Prompt: {initial_prompt}

Continuation Input: {continuation_input}

Provide your response in the following format:

Story: [Your generated story based on the initial prompt]
Continuation: [Your continuation of the story based on the new input]

Ensure that:
1. The initial story is coherent, engaging, and logically follows from the prompt.
2. The continuation seamlessly integrates the new input and maintains the story's coherence and creativity.
3. The continuation does not contradict any elements of the initial story."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The initial story should be coherent, engaging, and logically follow from the prompt.",
            "The continuation should seamlessly integrate the new input and maintain the story's coherence and creativity.",
            "The continuation should not contradict any elements of the initial story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
