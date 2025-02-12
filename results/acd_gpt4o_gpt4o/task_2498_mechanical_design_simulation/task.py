class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Design a simple catapult mechanism that can launch a small object (e.g., a ping pong ball) to a target 10 meters away. The catapult should be made using basic materials such as wood, rubber bands, and nails.", "requirements": "The design should be safe, feasible, and capable of launching the object accurately to the target."},
            "2": {"task": "Design a wind-powered car that can travel 20 meters on a flat surface. The car should be made using basic materials such as cardboard, plastic wheels, and a small fan.", "requirements": "The design should be efficient, feasible, and capable of traveling the specified distance using wind power only."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a mechanical design based on the given requirements. Provide a detailed explanation of your design, including how it meets the criteria and any relevant calculations or diagrams.

Task:
{t['task']}

Requirements:
{t['requirements']}

Provide your design and explanation below. Your response should include:
1. A detailed description of the design.
2. Step-by-step explanation of how the design meets the requirements.
3. Any relevant calculations or diagrams to support your design.
4. Consideration of potential challenges and how to address them."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The design should meet the specified requirements.", "The explanation should be detailed and clear.", "The design should be feasible and practical.", "The response should include relevant calculations or diagrams.", "The response should consider potential challenges and how to address them."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
