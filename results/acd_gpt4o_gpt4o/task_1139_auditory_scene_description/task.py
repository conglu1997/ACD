class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "describe", "prompt": "Describe the sounds you might hear in a bustling city street during the day, including traffic, people, and any other typical city noises."},
            "2": {"type": "describe", "prompt": "Describe the sounds you might hear while walking through a dense forest at night, including wildlife, rustling leaves, and any other typical forest noises."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "describe":
            return f"""Your task is to describe the given auditory scene in detail. {t["prompt"]} Provide a vivid and coherent description of the various sounds, including their sources, characteristics, and any notable features. Structure your response in the following format: \n- Overview of the scene \n- Description of primary sounds \n- Description of background sounds \n- Any other notable auditory features."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the auditory scene based on the given prompt.",
            "The description should include primary and background sounds.",
            "The description should be vivid, coherent, and immersive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
