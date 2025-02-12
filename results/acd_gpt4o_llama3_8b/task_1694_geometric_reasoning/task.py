class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Construct a shape based on the following description: A quadrilateral with two pairs of parallel sides, each pair being of different lengths. Provide the name of this shape and a brief description of its properties."},
            "2": {"prompt": "Solve the following geometric puzzle: You have a triangle with sides of lengths 3 cm, 4 cm, and 5 cm. What is the area of this triangle? Provide a step-by-step explanation of how you arrived at the answer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Construct a shape" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Submit your response as a plain text string in the following format:
- Shape Name: [Name of the shape]
- Properties: [Description of the shape's properties]

Ensure that your description includes key properties such as parallel sides, equal lengths, and any other distinguishing features. Also describe the angles formed by the sides."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Submit your response as a plain text string in the following format:
- Area: [Calculated area in square centimeters]
- Explanation: [Step-by-step explanation of how you arrived at the answer]

Ensure that your explanation includes the use of appropriate geometric formulas such as the Pythagorean theorem or Heron's formula."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "Construct a shape" in t["prompt"]:
            criteria = ["The shape should be correctly identified as a parallelogram.", "The description should include properties such as opposite sides being equal and parallel, and the angles formed by the sides.", "The response should specify that the pairs of parallel sides are of different lengths."]
        else:
            criteria = ["The solution should correctly identify the area as 6 square centimeters.", "The explanation should include the use of the Pythagorean theorem or Heron's formula with correct calculations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
