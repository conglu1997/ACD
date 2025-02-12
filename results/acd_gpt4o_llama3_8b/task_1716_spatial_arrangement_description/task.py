class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clues": [
                    "1. The red ball is to the left of the blue ball.",
                    "2. The green ball is to the right of the yellow ball.",
                    "3. The yellow ball is between the red ball and the green ball."
                ],
                "objects": ["red ball", "blue ball", "green ball", "yellow ball"]
            },
            "2": {
                "clues": [
                    "1. The cat is sitting to the right of the dog.",
                    "2. The bird is sitting to the left of the dog.",
                    "3. The fish is between the cat and the bird."
                ],
                "objects": ["cat", "dog", "bird", "fish"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        clues = t["clues"]
        example_clues = [
            "1. The apple is to the left of the banana.",
            "2. The carrot is to the right of the banana.",
            "3. The banana is between the apple and the carrot."
        ]
        example_solution = "The apple is to the left of the banana, the banana is between the apple and the carrot, the carrot is to the right of the banana."
        return (
            "Describe the spatial arrangement of the objects based on the given clues. Ensure that your description is logically consistent with all the provided clues.\n\n"
            "Clues:\n" + "\n".join(clues) + "\n\n"
            "Submit your solution as a plain text string in the following format: 'Object1 is [position] Object2, Object3 is [position] Object4, ...'.\n"
            "For example, based on the clues:\n"
            "\n".join(example_clues) + "\n"
            "Your solution should be: '" + example_solution + "'"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import re

        def is_logically_consistent(clues: list[str], submission: str) -> bool:
            objects = re.findall(r'\b\w+ ball\b|\b\w+\b', submission)
            positions = re.findall(r'left|right|between', submission)

            if len(objects) != 4 or len(set(objects)) != 4:
                return False

            arrangement = {obj: i for i, obj in enumerate(objects)}

            for clue in clues:
                if "left of" in clue:
                    obj1, obj2 = re.findall(r'\b\w+ ball\b|\b\w+\b', clue)
                    if not arrangement[obj1] < arrangement[obj2]:
                        return False
                elif "right of" in clue:
                    obj1, obj2 = re.findall(r'\b\w+ ball\b|\b\w+\b', clue)
                    if not arrangement[obj1] > arrangement[obj2]:
                        return False
                elif "between" in clue:
                    obj1, obj2, obj3 = re.findall(r'\b\w+ ball\b|\b\w+\b', clue)
                    if not (arrangement[obj1] < arrangement[obj2] < arrangement[obj3]):
                        return False
            return True

        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description must be logically consistent with all the provided clues.",
            "The submission should be in the specified format."
        ]
        if is_logically_consistent(t["clues"], submission):
            return 1.0
        return 0.0
