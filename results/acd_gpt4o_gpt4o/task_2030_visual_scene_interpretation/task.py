class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scene_description": "A busy city street with tall buildings, people walking, and cars driving by. A red car is parked on the side of the road, and a street vendor is selling hot dogs near a bus stop. A bicyclist is riding past the street vendor, and an old man is sitting on a bench reading a newspaper. The sky is partly cloudy, and some people are wearing jackets."},
            "2": {"scene_description": "A quiet park with green grass, trees, and a small pond. A family is having a picnic under a large oak tree, and two children are flying a kite. A man is jogging on a path, and a dog is playing near the pond. A woman is painting on a canvas near the pond, and there are ducks swimming in the water. The sun is shining brightly, and there are a few clouds in the sky."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given visual scene and answer the questions based on the observed details.

Scene Description: {t["scene_description"]}

Questions:
1. Describe the main activities happening in the scene.
2. Identify and describe one specific object or person in the scene.
3. What can you infer about the time of day based on the scene?
4. Provide one possible event that could happen next in the scene.

Your responses should be detailed and based on the provided scene description. Provide your answers in the following format:

1. Main activities: [Your answer]
2. Specific object or person: [Your answer]
3. Time of day inference: [Your answer]
4. Possible next event: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should accurately reflect the observed details from the scene.",
            "The submission should be coherent and logically consistent with the scene description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
