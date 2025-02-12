class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "triangle",
                "vertices": [(0, 0), (3, 0), (0, 4)],
                "transformation": "rotate 90 degrees clockwise around the origin"
            },
            "2": {
                "shape": "rectangle",
                "vertices": [(1, 1), (1, 4), (4, 4), (4, 1)],
                "transformation": "translate by (2, -1)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the specified transformation on the given {t['shape']} and provide the new coordinates of the vertices.

Shape: {t['shape']}
Vertices: {t['vertices']}
Transformation: {t['transformation']}

Submit your response as a list of tuples representing the new coordinates of the vertices in the format: [(x1, y1), (x2, y2), ...]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import math
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should be a list of tuples representing the new coordinates of the vertices."]
        if eval_with_llm_judge(instructions, submission, validation_criteria):
            def rotate_point(point, angle_deg):
                angle_rad = math.radians(angle_deg)
                x, y = point
                return (x * math.cos(angle_rad) - y * math.sin(angle_rad),
                        x * math.sin(angle_rad) + y * math.cos(angle_rad))

            def translate_point(point, translation):
                tx, ty = translation
                x, y = point
                return (x + tx, y + ty)

            if t['transformation'].startswith("rotate"):
                try:
                    angle = int(t['transformation'].split()[1])
                    new_vertices = [rotate_point(v, angle) for v in t['vertices']]
                except ValueError:
                    raise ValueError("Invalid rotation angle specified")
            elif t['transformation'].startswith("translate"):
                try:
                    translation_str = t['transformation'].split("translate by ")[1]
                    translation = tuple(map(int, translation_str.strip('()').split(',')))
                    new_vertices = [translate_point(v, translation) for v in t['vertices']]
                except (ValueError, IndexError):
                    raise ValueError("Invalid translation values specified")
            else:
                raise ValueError("Unsupported transformation")

            correct_answer = new_vertices
            return 1.0 if eval_with_llm_judge(instructions, submission, [f"The response should be {correct_answer}."]) else 0.0
        return 0.0
