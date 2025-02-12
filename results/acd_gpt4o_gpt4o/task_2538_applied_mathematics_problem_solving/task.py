class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "You are an engineer working on optimizing the design of a water distribution system for a city. The system needs to ensure that water is evenly distributed to all areas without exceeding the capacity of the pipes. The city is divided into four zones, each requiring a different amount of water daily: Zone A: 5000 liters, Zone B: 7000 liters, Zone C: 3000 liters, Zone D: 6000 liters. The main pipe can handle a maximum flow of 10000 liters per day. Design a solution to distribute the water efficiently.", "requirements": "Calculate the optimal flow distribution to ensure each zone receives the required amount of water without exceeding the pipe capacity. Provide a step-by-step explanation of your solution. Your response should include all relevant calculations and logical reasoning, including a clear explanation of how the flow is distributed among the zones."},
            "2": {"context": "You are a financial analyst tasked with evaluating an investment portfolio. The portfolio includes three types of investments: Stocks with a 7% annual return, Bonds with a 3% annual return, and Real Estate with a 5% annual return. The total investment amount is $100,000. The client wants a balanced portfolio with a maximum risk tolerance of 4%. Design a portfolio allocation that meets the client's requirements.", "requirements": "Determine the optimal allocation of the investment amount among the three types of investments to achieve the highest return while maintaining the risk tolerance. Provide a detailed explanation of your calculations and reasoning, including a clear breakdown of the allocation percentages for each type of investment."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        context = t["context"]
        requirements = t["requirements"]
        instructions = f"""Your task is to solve the following problem based on the given context:

{context}

Ensure that your solution meets the following requirements:
{requirements}

Provide a detailed, step-by-step explanation of your solution, including all calculations and reasoning. Your response should be clear, logical, and comprehensive. Format your response as follows:

1. Problem Statement: [Brief summary of the problem]
2. Solution Approach: [Your approach to solving the problem]
3. Calculations: [Detailed calculations]
4. Conclusion: [Your final solution and reasoning]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be logically sound and well-explained.",
            "All calculations should be correct and clearly presented.",
            "The solution should meet the specified requirements and constraints.",
            "The response should include a clear breakdown of the flow distribution or allocation percentages."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
