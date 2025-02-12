class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "image_description": "A sunny beach with people playing beach volleyball, a lifeguard tower in the distance, and a few seagulls flying close to the shore."
            },
            "2": {
                "image_description": "A busy city street with skyscrapers on both sides, yellow taxis driving past, and people walking on the sidewalks holding umbrellas as it rains."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to generate a detailed visual description based on the given image description. "
            "Ensure your description is vivid, coherent, and captures the essence of the scene. "
            "Provide your response in plain text format, including a detailed description of the visual elements. "
            "Your response should be structured as follows: \n\n"
            "1. Overall setting of the scene \n"
            "2. Key elements and their spatial arrangement \n"
            "3. Activities or actions taking place \n"
            "4. Any additional details that enhance the scene"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should vividly describe the overall setting of the scene.",
            "The response should mention key elements and their spatial arrangement accurately.",
            "The activities or actions described should be coherent and match the given scene.",
            "The additional details should enhance the visual imagery and make the scene more vivid."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
