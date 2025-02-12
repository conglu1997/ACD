class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A farmer has a rectangular field that is 150 meters long and 80 meters wide. He wants to divide the field into smaller rectangular plots, each 30 meters by 20 meters. How many plots can he create? Additionally, if he plants 3 rows of corn in each plot, with each row requiring 10 meters of space, how many rows of corn can he plant in total?",
                "instructions": "Solve the given word problem and provide the total number of plots and the total number of rows of corn planted. Submit your response as a plain text string in the following format: 'Total plots: [number], Total rows of corn: [number]'. Ensure your calculations are correct and clearly presented, and follow the specified response format exactly. Double-check your work for accuracy."
            },
            "2": {
                "problem": "A cylindrical tank with a radius of 5 meters and a height of 10 meters is filled with water. A small leak at the bottom of the tank causes water to drain out at a rate of 0.2 cubic meters per minute. How long will it take for half of the water to drain out?",
                "instructions": "Solve the given word problem and provide the time required for half of the water to drain out. Submit your response as a plain text string in the following format: 'Time required: [number] minutes'. Ensure your calculations are correct and clearly presented, and follow the specified response format exactly. Double-check your work for accuracy."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t["instructions"]

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include accurate calculations to solve the problem.",
            "The format of the response should match the specified format in the instructions exactly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
