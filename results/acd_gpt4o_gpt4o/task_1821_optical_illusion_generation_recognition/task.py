class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "recognize", "description": "A set of parallel lines appears to be non-parallel due to the presence of converging lines or intersecting shapes."},
            "2": {"task_type": "generate", "phenomenon": "Motion illusion", "prompt": "Describe an optical illusion that creates the illusion of motion even though the image is static."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'recognize':
            return f"""Your task is to identify the optical illusion described below and explain the visual phenomenon it illustrates.\n\nDescription: {t['description']}\n\nEnsure your explanation includes:\n- The name of the optical illusion (if known).\n- A detailed description of the visual phenomenon.\n- Why this illusion occurs from a perceptual perspective.\n\nProvide your response in the following format:\n\nRecognition:\n- Name: [Name of the optical illusion]\n- Description: [Your detailed description]\n- Perceptual Explanation: [Why the illusion occurs]\n\nExample Response:\nRecognition:\n- Name: The Müller-Lyer Illusion\n- Description: Two sets of parallel lines that seem non-parallel due to intersecting shapes.\n- Perceptual Explanation: The brain is tricked by the surrounding lines into perceiving non-parallelism."""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a description of an optical illusion that matches the given phenomenon.\n\nPhenomenon: {t['phenomenon']}\n\nPrompt: {t['prompt']}\n\nEnsure your description is vivid and clearly explains how the illusion creates the visual phenomenon. Provide your response in the following format:\n\nGeneration:\n- Description: [Your description of the optical illusion]\n- Explanation: [Why the illusion creates the phenomenon]\n\nExample Response:\nGeneration:\n- Description: A static image with black and white patterns that create the illusion of motion.\n- Explanation: The repetitive patterns trick the brain into perceiving movement even though the image is static."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'recognize':
            criteria = ["The response should include the name of the optical illusion (if known).", "The description must be detailed and relevant to the given description.", "The perceptual explanation must be accurate and relevant."]
        elif t['task_type'] == 'generate':
            criteria = ["The response should include a detailed description of the optical illusion.", "The explanation must accurately describe why the illusion creates the phenomenon."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
