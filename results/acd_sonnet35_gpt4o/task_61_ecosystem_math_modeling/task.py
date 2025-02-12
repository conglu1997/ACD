import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Floating Sky Islands",
                "description": "A series of small, floating islands in the sky, each with its own unique flora and fauna."
            },
            {
                "name": "Subterranean Crystal Caves",
                "description": "A network of underground caves illuminated by bioluminescent crystals, supporting a diverse ecosystem of cave-dwelling organisms."
            }
        ]
        return {str(i+1): ecosystem for i, ecosystem in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a mathematical model of the fictional ecosystem: {t['name']} - {t['description']}

Your task is to develop a simple mathematical model that captures the key interactions and dynamics of this ecosystem. Follow these steps:

1. Identify 3-4 key species or components in the ecosystem.
2. Define variables to represent the population or quantity of each component.
3. Create a system of differential equations that model the interactions between these components. Consider factors such as growth rates, predator-prey relationships, resource limitations, and any unique aspects of the given ecosystem.
4. Analyze the stability of your model by identifying equilibrium points and discussing their stability.
5. Predict how a sudden change (e.g., introduction of a new species, climate change) would affect the ecosystem based on your model.

Provide your response in the following format:

Components:
1. [Component 1]: [Brief description]
2. [Component 2]: [Brief description]
3. [Component 3]: [Brief description]
(4. [Component 4]: [Brief description]) (if applicable)

Variables:
- x1 = [Definition]
- x2 = [Definition]
- x3 = [Definition]
(- x4 = [Definition]) (if applicable)

Differential Equations:
1. dx1/dt = [Equation]
2. dx2/dt = [Equation]
3. dx3/dt = [Equation]
(4. dx4/dt = [Equation]) (if applicable)

Stability Analysis:
[Your analysis of equilibrium points and their stability]

Predicted Response to Change:
[Your prediction and explanation]

Ensure that your model is mathematically sound, biologically plausible, and creatively adapted to the unique features of the given ecosystem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The model includes 3-4 key components of the ecosystem",
            "The differential equations are mathematically correct and biologically plausible",
            "The stability analysis correctly identifies equilibrium points and discusses their stability",
            "The predicted response to change is logical and based on the proposed model",
            "The model creatively incorporates unique features of the given ecosystem",
            "The response follows the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
