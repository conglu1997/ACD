class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "document": "Alice and Bob are colleagues working on a project. They have different approaches to solving a particular problem. Alice prefers a data-driven approach, while Bob believes in a more intuitive and creative solution. They often have discussions to find a middle ground. Recently, they encountered a major roadblock in their project due to conflicting ideas. Alice suggests conducting a detailed data analysis to identify the root cause of the problem, while Bob proposes brainstorming sessions to come up with innovative ideas. Both approaches have their merits, but they need to decide on one to move forward. In this context, write an email from Alice to Bob proposing a balanced approach that incorporates both their methods.",
                "scenario": "Write an email from Alice to Bob proposing a balanced approach that incorporates both their methods."
            },
            "2": {
                "document": "The year is 2030, and climate change has become an even more pressing issue. Governments around the world are implementing stricter regulations to curb carbon emissions. Renewable energy sources like solar and wind power are becoming more prevalent, but there are still significant challenges to be addressed. The cost of transitioning to renewable energy is high, and there are political and economic hurdles. Additionally, the technology for storing renewable energy efficiently is still in its nascent stages. In this scenario, draft a policy proposal that outlines a comprehensive plan to accelerate the transition to renewable energy while addressing the associated challenges.",
                "scenario": "Draft a policy proposal that outlines a comprehensive plan to accelerate the transition to renewable energy while addressing the associated challenges."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to read the provided document and synthesize a coherent and contextually appropriate response based on the given scenario. Ensure that your response is well-structured, logical, and addresses all the key points mentioned in the scenario.\n\nDocument:\n\"{t['document']}\"\n\nScenario:\n\"{t['scenario']}\"\n\nProvide your response in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be coherent and contextually appropriate.",
            "The response should address all the key points mentioned in the scenario.",
            "The response should be well-structured and logical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
