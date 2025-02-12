class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"system": "predator_prey", "parameters": {"prey_birth_rate": 0.1, "predator_death_rate": 0.1, "predation_rate": 0.02, "predator_efficiency": 0.01}, "initial_conditions": {"prey_population": 40, "predator_population": 9}, "time_steps": 100},
            "2": {"system": "epidemic_spread", "parameters": {"transmission_rate": 0.3, "recovery_rate": 0.1}, "initial_conditions": {"susceptible_population": 990, "infected_population": 10, "recovered_population": 0}, "time_steps": 50}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['system'] == "predator_prey":
            return ("Your task is to model a predator-prey dynamic system using the Lotka-Volterra equations. "
                    "Use the given parameters and initial conditions to simulate the system over the specified number of time steps. "
                    "Provide a plot of the prey and predator populations over time and an interpretation of the results, including any observed patterns or behaviors. "
                    "Parameters: prey_birth_rate = {prey_birth_rate}, predator_death_rate = {predator_death_rate}, predation_rate = {predation_rate}, predator_efficiency = {predator_efficiency}. "
                    "Initial conditions: {prey_population} prey, {predator_population} predators. "
                    "Time steps: {time_steps}. "
                    "Response format: Provide the plot as an image and the interpretation as plain text. "
                    "Ensure your plot is clear and accurately represents the populations over time. Your interpretation should be at least 150 words long and thoroughly explain any observed patterns or behaviors, including any deviations from expected results.")
        elif t['system'] == "epidemic_spread":
            return ("Your task is to model the spread of an epidemic using the SIR (Susceptible-Infected-Recovered) model. "
                    "Use the given parameters and initial conditions to simulate the system over the specified number of time steps. "
                    "Provide a plot of the susceptible, infected, and recovered populations over time and an interpretation of the results, including any observed patterns or behaviors. "
                    "Parameters: transmission_rate = {transmission_rate}, recovery_rate = {recovery_rate}. "
                    "Initial conditions: {susceptible_population} susceptible, {infected_population} infected, {recovered_population} recovered. "
                    "Time steps: {time_steps}. "
                    "Response format: Provide the plot as an image and the interpretation as plain text. "
                    "Ensure your plot is clear and accurately represents the populations over time. Your interpretation should be at least 150 words long and thoroughly explain any observed patterns or behaviors, including any deviations from expected results.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The simulation must use the given parameters and initial conditions.",
                    "The plot must accurately represent the populations over time and be clear.",
                    "The interpretation must be clear, at least 150 words long, and thoroughly explain observed patterns or behaviors, including any deviations from expected results."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0