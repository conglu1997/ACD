import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        shapes = ['cube', 'sphere', 'pyramid', 'cylinder', 'cone']
        colors = ['red', 'blue', 'green', 'yellow', 'purple']
        positions = ['on top of', 'next to', 'in front of', 'behind', 'to the left of', 'to the right of']
        
        def generate_scene():
            scene_objects = random.sample(shapes, 3)
            scene_colors = random.sample(colors, 3)
            scene = f"A {scene_colors[0]} {scene_objects[0]} is {random.choice(positions)} a {scene_colors[1]} {scene_objects[1]}. "
            scene += f"A {scene_colors[2]} {scene_objects[2]} is {random.choice(positions)} the {scene_objects[1]}."
            return scene, scene_objects, scene_colors
        
        scene1, objects1, colors1 = generate_scene()
        scene2, objects2, colors2 = generate_scene()
        
        tasks = {
            "1": {
                "scene": scene1,
                "question": f"If the {colors1[0]} {objects1[0]} were to disappear, describe the new positions of the remaining shapes relative to each other."
            },
            "2": {
                "scene": scene2,
                "question": f"Imagine the {colors2[1]} {objects2[1]} grows to twice its size. Describe how this would affect the positions of the other shapes."
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Carefully read and visualize the following abstract scene:

{t['scene']}

Now, consider this question about the scene:

{t['question']}

To answer, follow these steps:
1. Visualize the initial scene in your mind.
2. Mentally perform the transformation described in the question.
3. Analyze the resulting mental image.
4. Describe your reasoning process.
5. Provide your final answer.

Format your response as follows:

Initial Visualization:
[Describe your mental image of the initial scene]

Transformation:
[Explain how you mentally transformed the scene]

Final Configuration:
[Describe the final arrangement of objects/shapes]

Reasoning:
[Explain your thought process and spatial reasoning]

Answer:
[Provide a concise answer to the question]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately describes the initial scene based on the given description.",
            "The mental transformation is correctly explained and consistent with the question asked.",
            "The final configuration logically follows from the initial scene and the described transformation.",
            "The reasoning demonstrates an understanding of spatial relationships and how they change under the given transformation.",
            "The answer addresses the question directly and is consistent with the explained reasoning.",
            "The response follows the specified format with all required sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
