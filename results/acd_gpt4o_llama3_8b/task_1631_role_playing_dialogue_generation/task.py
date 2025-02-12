class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A customer is calling a tech support representative to resolve an issue with their new laptop.",
                "initial_exchanges": "Customer: Hi, I've been having trouble with my new laptop. It keeps shutting down randomly.\nTech Support: I'm sorry to hear that. Let's see if we can figure out what's going on. When does the laptop shut down?\nCustomer: It usually happens when I'm in the middle of working on something important. It's really frustrating."
            },
            "2": {
                "scenario": "A student is approaching a professor to discuss their concerns about an upcoming exam.",
                "initial_exchanges": "Student: Professor, I'm really anxious about the upcoming exam. I'm not sure if I'm prepared enough.\nProfessor: I understand your concern. Let's talk about what specifically you're worried about and see how we can address it.\nStudent: I'm struggling particularly with the essay questions. I find them challenging."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Continue the role-playing dialogue based on the following scenario and initial exchanges. Ensure that the conversation is coherent, contextually appropriate, and follows logically from the given exchanges. The conversation should remain professional and respectful. Submit your response as a plain text string. Here are the details:\n\nScenario:\n{t["scenario"]}\n\nInitial Exchanges:\n{t["initial_exchanges"]}\n\nContinue the dialogue from here. Make sure to include at least 3-4 additional exchanges in the conversation. Format your response as follows:\n[Character 1]: [Dialogue]\n[Character 2]: [Dialogue]\n...\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be coherent and contextually appropriate.",
            "The response should follow logically from the initial exchanges.",
            "The conversation should maintain a natural flow.",
            "The conversation should remain professional and respectful.",
            "The response should be relevant and helpful to the scenario.",
            "The response should include at least 3-4 additional exchanges."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
