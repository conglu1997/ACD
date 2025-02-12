class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A park scene with various elements such as trees, benches, people, and a pond. The scene includes people engaging in different activities like jogging, reading, and feeding ducks. There are also children playing near the pond, a person flying a kite, and a couple having a picnic under a large oak tree."},
            "2": {"description": "A bustling city street with tall buildings, cars, pedestrians, and street vendors. The scene includes elements like traffic lights, crosswalks, and billboards. Additionally, there is a street musician playing a guitar, a food truck selling tacos, and a group of tourists taking pictures in front of a famous landmark."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to interpret and describe the visual scene based on the given textual description. Ensure that your description is detailed and coherent, capturing the essence of the scene and the spatial relationships between different elements. Provide specific details about the activities, interactions, and positions of the various elements described. Provide your response in plain text format. Format your response as follows:

1. Scene Description: [Detailed description of the visual scene]""".format(t["description"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately reflect the given textual description, capturing the essence of the scene and the spatial relationships between different elements, including specific details about activities and interactions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
