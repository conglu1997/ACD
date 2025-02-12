class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A farmer has a rectangular field that is 150 meters long and 80 meters wide. He wants to create a triangular flower bed by cutting off one of the corners of the field such that the hypotenuse of the triangular bed is along the diagonal of the rectangle. Calculate the area of the triangular flower bed. Provide your answer in square meters.", "answer": 6000},
            "2": {"problem": "A car travels at a constant speed of 60 km/h. It needs to reach a destination that is 150 km away. However, after traveling for 1 hour, the car gets stuck in traffic and its speed reduces to 30 km/h for the rest of the journey. Calculate the total time taken for the car to reach the destination. Provide your answer in hours.", "answer": 4}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following real-world mathematical problem. Provide a detailed solution and ensure your answer is correct.

Problem: {t['problem']}

Provide your answer in the following format:
Answer: [Your answer]

Additionally, show your work and explain each step of your solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The answer should be {t['answer']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
