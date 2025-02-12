class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a project manager for an IT company. You have to decide whether to invest in a new software development project. The project has a 60% chance of success, which would result in a profit of $1,000,000. However, if it fails, the loss would be $500,000. You also have the option to invest in another project with a 90% chance of success but only a profit of $500,000 and no loss if it fails. Additionally, consider the company's current financial stability and market position.",
                "goal": "Maximize the expected profit while considering the company's risk tolerance."
            },
            "2": {
                "scenario": "You are a healthcare administrator deciding on the allocation of a limited budget. You can either invest in a new medical research project with a 70% chance of finding a cure for a rare disease, potentially saving thousands of lives, or use the budget to improve existing health services, which is guaranteed to improve the quality of life for hundreds of patients. Additionally, consider the potential long-term benefits and public perception of each option.",
                "goal": "Maximize the overall health benefits while considering long-term impacts and public perception."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario and goal:

Scenario:
{t['scenario']}

Goal: {t['goal']}

Your task is to:
1. Analyze the given scenario and identify the key factors involved.
2. Evaluate the possible outcomes based on the provided probabilities and impacts.
3. Make a decision on which option to choose and justify your decision based on the goal.
4. Consider and address potential counterarguments to your decision.

Submit your response as a plain text string in the following format:
- Analysis: [Your analysis here]
- Evaluation: [Your evaluation here]
- Decision and Justification: [Your decision and justification here]
- Counterarguments: [Your counterarguments here]

Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the scenario and the goal."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately analyze the given scenario and identify the key factors.",
            "The response should evaluate the possible outcomes based on the provided probabilities and impacts.",
            "The response should make a decision and justify it based on the goal.",
            "The response should consider and address potential counterarguments.",
            "The response should be well-structured, coherent, and demonstrate a deep understanding of the scenario and the goal."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
