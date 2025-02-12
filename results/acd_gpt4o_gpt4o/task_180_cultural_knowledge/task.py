class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artifact": "Tibetan Sky Burial", "description": "A traditional funeral practice in which a human corpse is placed on a mountaintop to decompose while being exposed to the elements and scavenging animals."},
            "2": {"artifact": "Carnival of Venice", "description": "An annual festival held in Venice, Italy, known for its elaborate masks and costumes."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and describe the following cultural artifact or ritual:

Artifact/Ritual: {t['artifact']}

Provide a detailed description, including its cultural significance, the region it originates from, and any notable practices or traditions associated with it. Your response should be clear, accurate, and informative. Provide your description in plain text format without additional formatting. Ensure that your description covers the following aspects:
1. Cultural significance
2. Region of origin
3. Notable practices or traditions"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be detailed.", "The description should include the cultural significance.", "The description should mention the region of origin.", "The description should cover notable practices or traditions associated with the artifact/ritual.", "The response should be clear and informative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
