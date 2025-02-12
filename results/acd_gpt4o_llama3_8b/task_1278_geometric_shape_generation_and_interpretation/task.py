class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "triangle",
                "properties": "Equilateral, each side 5 units"
            },
            "2": {
                "shape": "rectangle",
                "properties": "Width 4 units, Height 2 units"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a geometric shape based on the given properties:

Shape: {t['shape']}
Properties: {t['properties']}

Ensure that the shape is accurate based on the properties provided. Submit your shape as a description and an image encoded in base64 format in the following format:

Description: [Your description here]
Image: [Base64 encoded image here]"""

    @staticmethod
    def generate_shape_image(shape: str, properties: str) -> str:
        import matplotlib.pyplot as plt
        import numpy as np
        from io import BytesIO
        import base64

        fig, ax = plt.subplots()
        if shape == "triangle":
            side = 5
            height = (np.sqrt(3)/2) * side
            triangle = plt.Polygon(((0, 0), (side/2, height), (side, 0)), closed=True, edgecolor='r')
            ax.add_patch(triangle)
        elif shape == "rectangle":
            width, height = 4, 2
            rectangle = plt.Rectangle((0, 0), width, height, edgecolor='r', facecolor='none')
            ax.add_patch(rectangle)
        ax.set_xlim(-1, 6)
        ax.set_ylim(-1, 6)
        ax.set_aspect('equal', adjustable='box')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return img_str

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        shape_image = TaskFamily.generate_shape_image(t['shape'], t['properties'])
        validation_criteria = [
            "The description should accurately describe the shape.",
            "The image should be clear and accurately represent the shape based on the given properties."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
