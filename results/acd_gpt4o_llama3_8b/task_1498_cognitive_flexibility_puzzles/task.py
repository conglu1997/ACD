class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have a 3-gallon jug and a 5-gallon jug. You need to measure exactly 4 gallons of water. Describe the steps to do this."},
            "2": {"puzzle": "You are in a room with three light switches, each of which controls one of three light bulbs in another room. You can only enter the room with the light bulbs once. How can you determine which switch controls which bulb?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["puzzle"] == "You have a 3-gallon jug and a 5-gallon jug. You need to measure exactly 4 gallons of water. Describe the steps to do this.":
            return "Solve the puzzle using logical reasoning and step-by-step problem-solving. Submit your response as a plain text string in the following format:\nSteps: [Your steps here]"
        elif t["puzzle"] == "You are in a room with three light switches, each of which controls one of three light bulbs in another room. You can only enter the room with the light bulbs once. How can you determine which switch controls which bulb?":
            return "Solve the puzzle using creative problem-solving and lateral thinking. Submit your response as a plain text string in the following format:\nSolution: [Your solution here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["puzzle"] == "You have a 3-gallon jug and a 5-gallon jug. You need to measure exactly 4 gallons of water. Describe the steps to do this.":
            criteria = [
                "The steps should logically lead to measuring exactly 4 gallons.",
                "The steps should be clear and follow a logical sequence."]
        elif t["puzzle"] == "You are in a room with three light switches, each of which controls one of three light bulbs in another room. You can only enter the room with the light bulbs once. How can you determine which switch controls which bulb?":
            criteria = [
                "The solution should use creative problem-solving.",
                "The solution should clearly determine which switch controls which bulb."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
