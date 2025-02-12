class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Imagine a futuristic cityscape at night, with towering skyscrapers, flying vehicles, and vibrant neon lights. Describe this scene in detail, capturing the atmosphere, colors, sounds, and any notable features."
            },
            "2": {
                "prompt": "Imagine an enchanted forest where the trees glow with bioluminescence, mythical creatures roam, and a hidden waterfall flows into a crystal-clear pond. Describe this scene in detail, capturing the magical elements, colors, sounds, and any notable features."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t['prompt']
        return f"""Generate a detailed and vivid description of an imaginary scene or object based on the given visual prompt. Ensure your description captures the atmosphere, colors, sounds, and any notable features.
\nPrompt: {prompt}
\nSubmit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and detailed, capturing the atmosphere, colors, sounds, and notable features of the scene.",
            "The description should be coherent and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
