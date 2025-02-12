class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"visual_scene": "A park with children playing on swings, joggers on a path, people sitting on benches reading books, a dog chasing a ball, and a fountain in the center."},
            "2": {"criteria": "Describe a bustling market scene with various stalls selling fruits, vegetables, clothing, and spices, people haggling, children running around, street performers entertaining, and a food stall with a long queue."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "visual_scene" in t:
            instructions = f"""Your task is to describe the following visual scene in detail:

{t['visual_scene']}

Provide a vivid and coherent description of the scene, including all notable features, objects, and activities. Your description should be clear and detailed, allowing someone to visualize the scene based on your words. Provide your description in plain text format, structured as follows:

1. Overview of the scene
2. Description of primary elements
3. Description of secondary elements
4. Any additional notable details"""
        else:
            instructions = f"""Your task is to generate a detailed description of a visual scene based on the following criteria:

{t['criteria']}

Ensure your description includes various elements, objects, and activities that fit the criteria. Your description should be vivid, coherent, and detailed, allowing someone to visualize the scene based on your words. Provide your description in plain text format, structured as follows:

1. Overview of the scene
2. Description of primary elements
3. Description of secondary elements
4. Any additional notable details"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "visual_scene" in t:
            criteria = ["The response should provide a vivid and coherent description of the given visual scene.", "The description should include all notable features, objects, and activities mentioned in the visual scene."]
        else:
            criteria = ["The response should generate a detailed description that fits the provided criteria.", "The description should be vivid, coherent, and include various elements, objects, and activities that align with the criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
