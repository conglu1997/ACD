class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Observations: 1. Plants exposed to classical music seem to grow faster. 2. Plants not exposed to any music grow at a normal rate. 3. The faster growth is observed consistently across different types of plants. 4. Growth rate is measured by height increase over a month.",
                "instructions": "Based on the above observations, generate a scientific hypothesis and design an experiment to test it."
            },
            "2": {
                "data": "Observations: 1. A group of people who took a specific supplement reported reduced anxiety levels. 2. A control group who did not take the supplement reported no change in anxiety levels. 3. The supplement is taken once daily for a month. 4. Anxiety levels are measured using a standard questionnaire.",
                "instructions": "Based on the above observations, generate a scientific hypothesis and design an experiment to test it."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following observations, generate a scientific hypothesis and design an experiment to test it. Ensure that your hypothesis is clear and your experimental design is detailed and feasible. The experiment should include the following clearly labeled sections: Hypothesis, Variables, Method, and Expected Results. Here are the observations:

{t["data"]}

Submit your response as a plain text string with each section clearly labeled."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a clear and testable hypothesis.",
            "The experimental design should be detailed and feasible.",
            "The response should include clearly labeled sections for Hypothesis, Variables, Method, and Expected Results."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
