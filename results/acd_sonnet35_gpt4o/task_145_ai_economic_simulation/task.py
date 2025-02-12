import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Resource Allocation in Space Colonies",
                "agents": ["Human Colonists", "AI Resource Managers", "Robotic Workers"],
                "resources": ["Oxygen", "Water", "Food", "Energy", "Raw Materials"],
                "constraints": ["Limited resupply from Earth", "Harsh environment", "Long-term sustainability required"],
                "goal": "Maximize colony growth while ensuring long-term survival"
            },
            {
                "name": "Post-Scarcity Economy Transition",
                "agents": ["Traditional Workers", "Universal Basic Income Recipients", "AI Corporations"],
                "resources": ["Goods", "Services", "Information", "Energy", "Creativity"],
                "constraints": ["Rapid technological change", "Shifting societal values", "Environmental concerns"],
                "goal": "Achieve a stable and equitable post-scarcity economy"
            }
        ]
        selected_scenarios = random.sample(scenarios, 2)
        return {
            "1": selected_scenarios[0],
            "2": selected_scenarios[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze an AI-driven economic simulation based on the following scenario:\n\nScenario: {t['name']}\n\nAgents: {', '.join(t['agents'])}\nResources: {', '.join(t['resources'])}\nConstraints: {', '.join(t['constraints'])}\nGoal: {t['goal']}\n\nYour task:\n\n1. Simulation Design (200-250 words):\n   Describe the key components and mechanics of your economic simulation. Explain how the agents interact, how resources are produced and consumed, and how the constraints affect the system. Include at least one innovative feature that makes your simulation unique.\n\n2. Game Theory Analysis (150-200 words):\n   Analyze the strategic interactions between the agents using game theory concepts. Identify at least one potential equilibrium state and explain why it might emerge.\n\n3. Emergent Behaviors (150-200 words):\n   Predict and explain two emergent behaviors or phenomena that might arise in your simulation. Discuss how these behaviors relate to real-world economic systems.\n\n4. Economic Intervention (200-250 words):\n   Propose an intervention to steer the simulated economy towards the specified goal. Describe the intervention in detail, explain your reasoning, and predict its potential consequences (both intended and unintended).\n\n5. Evaluation Metrics (100-150 words):\n   Design a set of quantitative and qualitative metrics to evaluate the success of your intervention and the overall health of the simulated economy. Explain how these metrics relate to the scenario's goal.\n\n6. Ethical Considerations (100-150 words):\n   Discuss two ethical implications or challenges arising from your simulation design or proposed intervention. Consider concepts such as fairness, autonomy, and long-term consequences.\n\nEnsure your response is creative yet grounded in economic principles and complex systems theory. Use clear headings for each section of your response. Your total response should be between 900-1200 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The simulation design is comprehensive, innovative, and consistent with the given scenario.",
            "The game theory analysis demonstrates a clear understanding of strategic interactions and equilibrium concepts.",
            "The predicted emergent behaviors are plausible and well-explained, showing insight into complex economic systems.",
            "The proposed intervention is creative, well-reasoned, and addresses the specified goal.",
            "The evaluation metrics are appropriate and well-designed for assessing the simulation and intervention.",
            "The ethical considerations show depth of thought and awareness of potential consequences.",
            "The overall response demonstrates a strong grasp of economic principles, game theory, and complex adaptive systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
