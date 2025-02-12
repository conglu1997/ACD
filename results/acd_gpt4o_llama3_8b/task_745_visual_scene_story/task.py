class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene": "A bustling medieval marketplace with vendors selling various goods like fruits, fabrics, and pottery. Children are playing near a fountain, and a knight in shining armor is talking to a merchant at a stall. The sun is setting in the background, casting a golden hue over the scene and creating long shadows. A bard is playing a lute, adding a melodic background to the lively atmosphere."
            },
            "2": {
                "scene": "A futuristic cityscape with flying cars zipping through the air, towering skyscrapers adorned with neon lights, and robots walking alongside humans on the streets. In the foreground, a young girl is staring in awe at a giant holographic advertisement that displays a new virtual reality game. The sky is a deep purple, dotted with stars and the faint glow of distant planets. A street vendor is selling exotic food from a hover cart, adding to the vibrant scene."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed and coherent story based on the following visual scene description:

{t['scene']}

Your story should be at least 300 words long, capturing the essence of the scene and weaving it into a compelling narrative. Ensure that your story includes vivid descriptions, character interactions, and a clear plot. Submit your story as a plain text string with the following format:

Story: [Your detailed story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be at least 300 words long.",
            "The story should be coherent and compelling.",
            "The story should accurately reflect the visual scene description.",
            "The story should include vivid descriptions, character interactions, and a clear plot."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
