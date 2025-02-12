class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the newly appointed CEO of a tech startup specializing in renewable energy solutions. Your company is facing stiff competition and declining market share. Devise a strategic plan to turn the company around and achieve a 20% market share within the next two years. Consider factors such as product innovation, marketing strategy, partnerships, and financial management.",
                "goal": "Achieve a 20% market share within two years."
            },
            "2": {
                "scenario": "You are the mayor of a mid-sized city experiencing rapid population growth. The city is facing challenges such as traffic congestion, housing shortages, and environmental concerns. Devise a strategic plan to address these issues and improve the quality of life for residents over the next five years. Consider factors such as urban planning, infrastructure development, public services, and sustainability.",
                "goal": "Improve the quality of life for residents over the next five years."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario:
{t['scenario']}

Your goal is to {t['goal']}.

Devise a comprehensive strategic plan that addresses the following points:
1. Identify the key challenges and opportunities in the scenario.
2. Propose specific actions and initiatives to achieve the goal.
3. Explain how you will measure the success of your plan.
4. Consider the potential risks and how you will mitigate them.

Submit your strategic plan as a plain text string. Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The plan should identify key challenges and opportunities.", "The plan should propose specific actions and initiatives.", "The plan should explain how success will be measured.", "The plan should consider potential risks and mitigation strategies.", "The response should be well-structured, coherent, and demonstrate a deep understanding of the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
