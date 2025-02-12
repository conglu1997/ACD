class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_prompt": "A young detective solving a mystery in an old mansion.", "condition": "The story must include an unexpected twist involving a hidden room and a long-lost family secret."},
            "2": {"initial_prompt": "A group of friends on an adventure in a magical forest.", "condition": "The story must introduce a talking animal that gives them crucial advice and a magical object that changes their journey."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_prompt = t["initial_prompt"]
        condition = t["condition"]
        instructions = f"""Your task is to generate a story based on the following initial prompt:

Initial Prompt: {initial_prompt}

Ensure that the story adapts to the following condition:

Condition: {condition}

Your story should be coherent, creative, and incorporate the given condition in a seamless manner. Provide your response in plain text format.

Response format:

<Your story>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story must be coherent and engaging.", "The condition must be incorporated seamlessly into the narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0