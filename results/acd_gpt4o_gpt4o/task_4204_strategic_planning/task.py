class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the manager of a small retail store. Your goal is to increase monthly sales by 20% within the next three months. You have a budget of $5,000 for marketing and promotions. Develop a strategic plan detailing the steps you will take, including marketing strategies, promotional events, and any other actions to achieve this goal.", "constraints": "Budget is limited to $5,000. The plan must be feasible within three months. The plan should include at least one social media campaign, one in-store event, and one new product launch."},
            "2": {"scenario": "You are the project manager for a software development team. Your goal is to launch a new mobile application within six months. You have a team of 5 developers, 2 designers, and 1 project coordinator. Develop a strategic plan detailing the steps you will take, including task assignments, timeline, and any risk management strategies to ensure the project is completed on time.", "constraints": "Team size is fixed. The plan must be feasible within six months. The plan should include a detailed timeline with at least three milestones, a risk management section, and a testing phase."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to develop a strategic plan based on the following scenario:

Scenario: {t['scenario']}

Ensure your plan addresses the following constraints:
{t['constraints']}

Provide a detailed and justified strategic plan in plain text format. Your plan should include clear steps, timeline, and rationale for each action. Clearly explain how your plan will achieve the specified goal within the given constraints.

Response format:
1. Steps: [Detailed steps]
2. Timeline: [Detailed timeline]
3. Rationale: [Justification for each action]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The plan should address all given constraints.", "The plan should provide a clear and logical sequence of steps.", "The plan should include a timeline and rationale for each action.", "The plan should be feasible and realistic within the given constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
