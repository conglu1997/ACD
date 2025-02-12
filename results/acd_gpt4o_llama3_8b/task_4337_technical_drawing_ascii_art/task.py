class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A simple gear with 8 teeth, each tooth being a triangle. The gear is circular and should fit within a 15x15 grid."},
            "2": {"description": "A rectangular box with a hinge on one side and a handle on the opposite side. The box should fit within a 20x10 grid."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following textual description of a mechanical component into an ASCII art representation. Ensure that the ASCII art accurately reflects the described object and fits within the specified grid dimensions.

Description: {t['description']}

Steps:
1. Read the description carefully and visualize the mechanical component.
2. Plan your ASCII art representation, keeping the grid dimensions in mind.
3. Use appropriate ASCII characters to create a clear and accurate depiction.
4. Ensure that the ASCII art fits within the specified grid dimensions.

Submit your ASCII art as a plain text string.

Example:
Description: A simple gear with 8 teeth, each tooth being a triangle. The gear is circular and should fit within a 15x15 grid.
ASCII Art (15x15 grid):

      /\     
     /  \    
    /    \   
   /      \  
  |        |
  |        |
  |        |
   \      /
    \    /
     \  /
      \/

Another Example:
Description: A rectangular box with a hinge on one side and a handle on the opposite side. The box should fit within a 20x10 grid.
ASCII Art (20x10 grid):

+------------------+
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
+------------------+

Ensure that your ASCII art fits within the specified grid dimensions and accurately reflects the given description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ASCII art should accurately reflect the described mechanical component.",
            "The ASCII art should fit within the specified grid dimensions.",
            "The ASCII art should be clear and well-structured.",
            "The ASCII art should use appropriate characters to represent the component.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
