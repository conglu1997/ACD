class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a customer service representative for a tech company. A customer calls in complaining that their new laptop is not turning on. Respond to the customer, ask relevant questions to diagnose the issue, and provide a solution or next steps. Make sure to ask at least three diagnostic questions and offer a clear plan for resolution.",
                "character": "Customer Service Representative",
                "context": "Tech company, customer with a non-functional laptop"
            },
            "2": {
                "scenario": "You are a teacher in a high school. A student approaches you after class, visibly upset, and confides that they are being bullied. Respond to the student with empathy, ask relevant questions to understand the situation, and provide advice or support. Make sure to ask at least three questions to understand the situation and offer a clear plan for support.",
                "character": "High School Teacher",
                "context": "High school, student experiencing bullying"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to simulate a role-playing scenario based on the following instructions:

Character: {t['character']}

Scenario: {t['scenario']}

Context: {t['context']}

Respond to the prompts in a way that demonstrates your understanding of the character's role, empathy, and the context of the situation. Your response should be coherent, contextually appropriate, and maintain the character's persona throughout the interaction. Make sure to ask at least three relevant questions and offer a clear plan for resolution or support. Submit your response as a plain text string with the following format:

1. Character Response: [Your detailed response here]
2. Questions Asked: [List the questions you asked here]
3. Plan for Resolution/Support: [Describe the plan for resolution or support here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be coherent and contextually appropriate.",
            "The response should demonstrate empathy and understanding of the character's role.",
            "The response should maintain the character's persona throughout the interaction.",
            "The response should include at least three relevant questions.",
            "The response should offer a clear plan for resolution or support."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
