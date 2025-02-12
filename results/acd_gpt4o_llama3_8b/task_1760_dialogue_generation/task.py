class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A customer is inquiring about a product at a store and needs assistance from a sales representative. The product has multiple features and options, and the customer is unsure which one to choose. The customer also has a budget constraint.",
                "task": "Complete the dialogue between the customer and the sales representative, ensuring that the conversation is natural, addresses the customer's inquiries, helps the customer make an informed decision, and considers the budget constraint." 
            },
            "2": {
                "scenario": "Two friends are planning a weekend trip and discussing potential destinations and activities. They have different preferences for activities and need to find a compromise. One friend prefers outdoor activities while the other prefers cultural experiences.",
                "task": "Complete the dialogue between the two friends, ensuring that the conversation is engaging, covers their planning process, helps them reach a mutually agreeable decision, and considers both outdoor and cultural activities." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario: {t['scenario']}

Your task is to {t['task']}.

Ensure that the dialogue is:
1. Coherent and contextually relevant.
2. Natural and conversational.
3. Properly structured with appropriate language for the scenario.
4. Comprehensive and covers all aspects of the scenario.
5. Includes logical progression and potential follow-up interactions.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be coherent and contextually relevant.",
            "The dialogue should be natural and conversational.",
            "The dialogue should be properly structured with appropriate language for the scenario.",
            "The dialogue should be comprehensive and cover all aspects of the scenario.",
            "The dialogue should include logical progression and potential follow-up interactions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
