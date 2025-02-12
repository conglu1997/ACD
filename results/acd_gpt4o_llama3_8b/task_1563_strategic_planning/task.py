class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the mayor of a growing city facing a significant environmental challenge. The city is experiencing severe air pollution due to industrial activities. Develop a strategic plan to reduce air pollution while maintaining economic growth. Consider factors such as public health, industrial regulations, economic impacts, and community engagement."
            },
            "2": {
                "scenario": "You are the CEO of a technology company that has seen rapid growth but is now facing fierce competition in the market. Develop a strategic plan to maintain your company's competitive edge over the next five years. Consider factors such as innovation, market trends, customer satisfaction, employee retention, and financial stability."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a strategic plan for the following scenario:

Scenario: {t['scenario']}

Ensure that your plan is comprehensive, considers all relevant factors, and outlines clear steps to achieve the objectives. Your plan should include:
1. An overview of the current situation
2. The main objectives to be achieved
3. Key strategies and actions to implement
4. Potential challenges and how to address them
5. A timeline for implementation
6. Metrics to measure success

Submit your plan as a plain text string in the following format:

Current Situation: [Description]
Objectives: [List of objectives]
Strategies and Actions: [Description of strategies and actions]
Challenges: [Description of potential challenges and solutions]
Timeline: [Timeline for implementation]
Metrics: [Metrics to measure success]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should be comprehensive and consider all relevant factors.",
            "The plan should outline clear steps to achieve the objectives.",
            "The response should follow the specified format precisely.",
            "The strategies and actions should be realistic and feasible.",
            "The plan should address potential challenges and provide solutions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
