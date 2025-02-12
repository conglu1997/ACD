class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"clues": "A rainy night in a bustling city, with neon lights reflecting off wet streets, people huddled under umbrellas, and a street musician playing a melancholic tune.", "synthetic_examples": ["Clue: A sunny day at a beach, with children building sandcastles, seagulls flying overhead, and surfers riding the waves.", "Clue: A quiet library, with rows of bookshelves, soft lighting, and a few people lost in their books.", "Clue: A lively carnival, with colorful rides, people enjoying cotton candy, and a clown performing tricks.", "Clue: A serene lakeside at sunset, with a small boat floating gently, and the sky painted in hues of orange and pink."]},
            "2": {"clues": "A tranquil forest clearing at dawn, with rays of sunlight filtering through the trees, a deer grazing, and birds chirping melodiously.", "synthetic_examples": ["Clue: A bustling farmer's market, with vendors selling fresh produce, the aroma of baked goods in the air, and people chatting animatedly.", "Clue: A snowy mountain village, with smoke rising from chimneys, children playing in the snow, and a distant sound of a church bell ringing.", "Clue: A cozy cabin by a lake, with a fireplace burning inside, and the sound of water gently lapping against the shore.", "Clue: A vibrant autumn park, with leaves of red and gold, people walking their dogs, and kids playing in piles of leaves."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"""Generate a detailed description of the following visual scene based on the provided textual clues, and then create a coherent story or narrative based on that scene. Ensure your description is vivid and captures the essence of the scene, and your story is engaging and logically follows from the scene.

Clues: {t['clues']}

Submit your response in the following format:

Description: [Your description]
Story: [Your story]

Additional examples:\n{examples}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a detailed and vivid description of the scene.", "The story should be coherent, engaging, and logically follow from the scene description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
