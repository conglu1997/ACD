class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "Stacking Objects",
                "objects": "A metal cube (5cm x 5cm x 5cm), a wooden cylinder (height 10cm, diameter 5cm), and a glass sphere (diameter 5cm).",
                "task_description": "Describe the most stable way to stack these objects on top of each other, considering their shapes and material properties."
            },
            "2": {
                "title": "Predicting Motion",
                "scenario": "A marble (diameter 1cm) is placed at the top of a 30-degree inclined ramp (length 1 meter, made of smooth metal).",
                "task_description": "Predict the motion of the marble as it rolls down the ramp. Include details about its speed, direction, and any changes in its motion."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['title'] == "Stacking Objects":
            instructions = f"""Your task is to reason about the physical properties and spatial relationships of the given objects to determine the most stable way to stack them.

Objects: {t['objects']}

Consider factors such as shape, material properties, and stability. Describe the stacking order and explain why this configuration is the most stable. Provide your response in plain text format, structured in paragraphs.

Response format:
Stacking Order: [Describe the order of objects]
Explanation: [Provide your explanation]"""
        elif t['title'] == "Predicting Motion":
            instructions = f"""Your task is to predict the motion of a marble placed at the top of a ramp with a 30-degree incline.

Scenario: {t['scenario']}

Include details about the marble's speed, direction, and any changes in its motion as it rolls down the ramp. Consider factors such as gravity, friction, and the incline angle. Provide your response in plain text format, structured in paragraphs.

Response format:
Motion Prediction: [Describe the motion of the marble]
Explanation: [Provide your explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['title'] == "Stacking Objects":
            criteria = [
                "The stacking order should consider the shapes and material properties of the objects.",
                "The explanation should demonstrate an understanding of stability and balance.",
                "The response should be logically coherent and plausible based on physical principles."
            ]
        elif t['title'] == "Predicting Motion":
            criteria = [
                "The prediction should include details about the marble's speed, direction, and motion changes.",
                "The explanation should consider gravity, friction, and the incline angle.",
                "The response should be logically coherent and plausible based on physical principles."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
