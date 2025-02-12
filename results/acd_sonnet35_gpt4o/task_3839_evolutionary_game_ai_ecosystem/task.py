import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'ecosystem_type': 'predator-prey',
                'game_theory_concept': 'hawk-dove game',
                'evolutionary_pressure': 'resource scarcity',
                'desired_outcome': 'stable population cycles'
            },
            {
                'ecosystem_type': 'symbiotic network',
                'game_theory_concept': 'prisoner\'s dilemma',
                'evolutionary_pressure': 'environmental fluctuations',
                'desired_outcome': 'increased biodiversity'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an artificial ecosystem where multiple AI agents engage in evolutionary game theory scenarios, then propose interventions to achieve specific ecosystem outcomes. Your task has the following components:

1. Ecosystem Design (250-300 words):
   a) Describe the key components of your {t['ecosystem_type']} artificial ecosystem.
   b) Explain how you incorporate the {t['game_theory_concept']} into the interactions between AI agents.
   c) Detail how {t['evolutionary_pressure']} affects the evolutionary trajectories of the agents.
   d) Provide a visual representation of your ecosystem using ASCII art or Unicode characters (max 20 lines x 80 characters).
   e) Include at least one mathematical equation or model representing a key aspect of your ecosystem's dynamics.

2. Agent Architecture (200-250 words):
   a) Describe the decision-making architecture of the AI agents in your ecosystem.
   b) Explain how agents learn and adapt their strategies over time.
   c) Discuss how genetic algorithms or other evolutionary computation techniques are implemented.
   d) Provide a simple pseudocode snippet (5-10 lines) illustrating a key decision-making process of your agents.

3. Simulation and Analysis (250-300 words):
   a) Outline the parameters and initial conditions for simulating your ecosystem.
   b) Describe the emergent behaviors and patterns you expect to observe.
   c) Analyze how the {t['game_theory_concept']} influences the overall dynamics of the ecosystem.
   d) Discuss any unexpected or counterintuitive outcomes that might arise.
   e) Propose a method to quantitatively measure the stability or success of your ecosystem.

4. Intervention Design (200-250 words):
   a) Propose three potential interventions to achieve the desired outcome of {t['desired_outcome']}.
   b) For each intervention, explain the rationale and expected effects on the ecosystem.
   c) Discuss potential unintended consequences of each intervention.
   d) Rank your interventions in order of expected effectiveness and explain your reasoning.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of designing and intervening in artificial ecosystems.
   b) Consider issues such as agent autonomy, ecosystem stability, and the role of human oversight.
   c) Propose guidelines for responsible development and management of such systems.
   d) Address potential misuse or unintended applications of your ecosystem model.

6. Real-world Applications (150-200 words):
   a) Suggest two potential real-world applications of your ecosystem model and intervention strategies.
   b) Discuss how insights from your artificial ecosystem could inform approaches to managing natural ecosystems or complex social systems.
   c) Identify at least one limitation of applying your model to real-world scenarios.

Ensure your response demonstrates a deep understanding of game theory, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['game_theory_concept']}, {t['ecosystem_type']} dynamics, and evolutionary processes.",
            f"The ecosystem design effectively incorporates {t['game_theory_concept']} and addresses {t['evolutionary_pressure']}.",
            f"The proposed interventions are creative, well-reasoned, and aimed at achieving {t['desired_outcome']}.",
            "The response includes a clear ASCII art diagram of the ecosystem as requested.",
            "The response includes at least one relevant mathematical equation or model.",
            "The agent architecture section includes a simple pseudocode snippet as required.",
            "The simulation and analysis section proposes a quantitative method to measure ecosystem stability or success.",
            "The ethical implications and real-world applications are thoroughly discussed, including potential limitations.",
            "The response is well-structured, clear, and within the specified word count for each section and overall."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
