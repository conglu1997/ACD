class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A population of rabbits in a closed ecosystem grows according to a logistic model. The initial population is 50 rabbits, the carrying capacity is 500 rabbits, and the growth rate is 0.1 per month. Create a mathematical model for this scenario and simulate the population growth for 24 months."},
            "2": {"scenario": "A company manufactures widgets. The production cost per widget is $5, and the selling price per widget is $10. The fixed monthly costs are $2000. Create a mathematical model to determine the break-even point and simulate the profit over 12 months if the company produces and sells 500 widgets per month."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a mathematical model for the following scenario and simulate it to predict outcomes. Provide your model, simulation code, and the predicted outcomes in a human-readable format.

Scenario:
{t['scenario']}

Your submission should be a Python script containing the following:
1. The mathematical model.
2. The simulation code.
3. The predicted outcomes in a human-readable format.

Ensure that your code is executable and that the predicted outcomes are stored in a variable named 'predicted_outcomes'. Submit your response as a plain text Python script."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            exec_globals = {}
            exec(submission, exec_globals)
            if 'predicted_outcomes' not in exec_globals:
                return 0.0
            # Verify the correctness of the predicted outcomes based on the model
            if t['scenario'].startswith('A population of rabbits'):
                # Expected outcome for task 1 (rabbit population growth using logistic model)
                import numpy as np
                r = 0.1
                K = 500
                P0 = 50
                months = 24
                expected_outcomes = [P0 * K / ((K - P0) * np.exp(-r * t) + P0) for t in range(months)]
                if all(abs(a - b) < 1.0 for a, b in zip(exec_globals['predicted_outcomes'], expected_outcomes)):
                    return 1.0
            elif t['scenario'].startswith('A company manufactures widgets'):
                # Expected outcome for task 2 (company profit simulation)
                production_cost = 5
                selling_price = 10
                fixed_costs = 2000
                widgets_per_month = 500
                expected_outcomes = [(selling_price - production_cost) * widgets_per_month * i - fixed_costs * i for i in range(1, 13)]
                if all(abs(a - b) < 1.0 for a, b in zip(exec_globals['predicted_outcomes'], expected_outcomes)):
                    return 1.0
            return 0.0
        except Exception:
            return 0.0
