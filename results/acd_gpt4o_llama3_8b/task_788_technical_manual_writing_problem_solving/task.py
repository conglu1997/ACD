class TaskFamily:
    manual_text = ""

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a detailed technical manual for a fictional device called 'Quantum Coffee Maker'. The manual should include sections on Setup, Operation, Maintenance, and Troubleshooting."},
            "2": {"prompt": "Based on the following manual excerpt for the 'Quantum Coffee Maker', solve the described problem: 'The coffee maker is not brewing coffee even though it is powered on and the water reservoir is full.'\nManual Excerpt: [manual_text]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Quantum Coffee Maker" in t["prompt"] and "manual" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that the manual is detailed, clear, and logically structured. It should include the following sections:
1. Setup: How to set up the device.
2. Operation: How to operate the device.
3. Maintenance: How to maintain the device.
4. Troubleshooting: Common issues and their solutions.

Submit your technical manual as a plain text string."""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Based on the provided manual excerpt, solve the described problem: 'The coffee maker is not brewing coffee even though it is powered on and the water reservoir is full.' Ensure your solution is clear, logical, and follows the instructions given in the manual.

Submit your solution as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "Quantum Coffee Maker" in t["prompt"] and "manual" in t["prompt"]:
            criteria = ["The manual should include sections on Setup, Operation, Maintenance, and Troubleshooting.", "The manual should be detailed, clear, and logically structured."]
            TaskFamily.manual_text = submission  # Store the manual text for use in Task 2.
        else:
            criteria = ["The solution should be clear, logical, and follow the instructions given in the manual excerpt."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
