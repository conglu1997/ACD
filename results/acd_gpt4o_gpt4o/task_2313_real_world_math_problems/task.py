class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are planning a road trip across multiple cities. You need to calculate the total distance you will travel and the total amount of fuel required if your car's fuel efficiency is 25 miles per gallon. The distances between the cities in miles are as follows: City A to City B: 120 miles, City B to City C: 200 miles, City C to City D: 150 miles."},
            "2": {"scenario": "You are renovating your house and need to calculate the total cost of flooring for three rooms. The dimensions of the rooms are as follows: Room 1: 10ft x 12ft, Room 2: 15ft x 10ft, Room 3: 20ft x 15ft. The cost of flooring is $2.5 per square foot. Calculate the total cost and include a 10% extra for wastage."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to solve the following real-world mathematical problem based on the given scenario:

Scenario:
{scenario}

Provide your response in the following format:

Solution:
Step-by-step Solution: [Your detailed step-by-step solution showing all calculations and intermediate steps]
Final Answer: [Your final answer]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a correct and detailed step-by-step solution showing all calculations and intermediate steps.",
            "The final answer should accurately solve the problem based on the given scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
