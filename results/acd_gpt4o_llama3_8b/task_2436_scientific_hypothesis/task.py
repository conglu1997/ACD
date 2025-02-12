class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A biologist observes that a certain species of plant tends to grow taller in shaded areas compared to areas with full sunlight. The biologist measures the average height of the plants in shaded areas (150 cm) and in full sunlight (120 cm). Formulate a hypothesis to explain this observation and suggest a possible experiment to test your hypothesis.",
                "solution": "Hypothesis: The plants grow taller in shaded areas because they are competing for limited light, which stimulates elongation growth. Experiment: Grow identical plants in controlled environments with varying levels of shade and full sunlight. Measure and compare the growth rates and final heights of the plants in different lighting conditions." 
            },
            "2": {
                "data": "A chemist notices that a certain chemical reaction proceeds faster at higher temperatures. The chemist records the reaction times at different temperatures: 30°C (10 minutes), 40°C (7 minutes), 50°C (5 minutes). Formulate a hypothesis to explain the effect of temperature on the reaction rate and propose an experiment to test your hypothesis.",
                "solution": "Hypothesis: The reaction rate increases with temperature because higher temperatures provide more kinetic energy to the reactant molecules, increasing the frequency of effective collisions. Experiment: Conduct the reaction at various temperatures (e.g., 20°C, 30°C, 40°C, 50°C, 60°C) and record the reaction times. Plot the reaction rate versus temperature to analyze the relationship." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following experimental data or observations, formulate a scientific hypothesis and suggest a possible experiment to test your hypothesis. Ensure that your hypothesis is clear, logical, and based on the provided data. Your proposed experiment should be detailed and feasible. Here is the data:

{t["data"]}

Submit your response as a plain text string in the following format:

Hypothesis: [Your hypothesis]
Experiment: [Your proposed experiment]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The hypothesis should be clear and logical.",
            "The hypothesis should be based on the provided data.",
            "The proposed experiment should be detailed and feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
