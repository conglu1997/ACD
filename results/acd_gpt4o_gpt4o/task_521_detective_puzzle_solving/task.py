class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A valuable painting has been stolen from a museum. The museum has three employees who had access to the painting: Alice, Bob, and Charlie. Here are the clues:\n1. Alice was seen near the painting just before it was stolen.\n2. Bob has a history of stealing art but claims he was out of town.\n3. Charlie was caught on camera leaving the museum with a suspicious package.\nWho stole the painting?",
                "solution": "Charlie"
            },
            "2": {
                "scenario": "During a company event, a laptop goes missing. The suspects are Daniel, Emma, and Frank. Here are the clues:\n1. Daniel was seen near the laptop just before it went missing.\n2. Emma has a reputation for borrowing items without asking but claims she was talking to a colleague.\n3. Frank was caught on camera putting something into his bag near the location where the laptop was last seen.\nWho took the laptop?",
                "solution": "Frank"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to analyze the given clues and solve the following detective puzzle:

Scenario: {scenario}

Based on the clues provided, identify the person responsible for the incident. Ensure your reasoning is clear and logical. Provide your answer in plain text format. Your response should be structured as follows:

Answer: [Your answer]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        solution = t["solution"]
        criteria = [f"The answer should be '{solution}'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
