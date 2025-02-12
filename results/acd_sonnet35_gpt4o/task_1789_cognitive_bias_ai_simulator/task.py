import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "Confirmation bias",
            "Anchoring bias",
            "Availability heuristic",
            "Framing effect",
            "Sunk cost fallacy",
            "Overconfidence effect",
            "Loss aversion"
        ]
        geopolitical_scenarios = [
            "International trade negotiation",
            "Climate change summit",
            "Territorial dispute resolution",
            "Global pandemic response",
            "Cybersecurity alliance formation"
        ]
        scenario_data = {
            "International trade negotiation": {"GDP impact": "2.5%", "Timeline": "5 years"},
            "Climate change summit": {"Emission reduction target": "30%", "Deadline": "2030"},
            "Territorial dispute resolution": {"Area contested": "50,000 sq km", "Population affected": "2 million"},
            "Global pandemic response": {"Infection rate": "3%", "Mortality rate": "0.5%"},
            "Cybersecurity alliance formation": {"Annual cyber attacks": "500,000", "Average cost per attack": "$1 million"}
        }
        task1 = {"biases": random.sample(cognitive_biases, 3), "scenario": random.choice(geopolitical_scenarios)}
        task1["data"] = scenario_data[task1["scenario"]]
        task2 = {"biases": random.sample(cognitive_biases, 3), "scenario": random.choice(geopolitical_scenarios)}
        task2["data"] = scenario_data[task2["scenario"]]
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human cognitive biases and heuristics, then apply it to a complex geopolitical decision-making scenario. Your system should incorporate the following cognitive biases: {', '.join(t['biases'])}. Apply your system to the following geopolitical scenario: {t['scenario']}.

Scenario data: {t['data']}

Provide your response in the following format:

1. Cognitive Bias Simulation (250-300 words):
   a) Explain how your AI system models each of the given cognitive biases.
   b) Describe the algorithms or techniques used to implement these biases in decision-making processes.
   c) Discuss how your system balances multiple, potentially conflicting biases.

2. AI System Architecture (300-350 words):
   a) Outline the overall architecture of your cognitive bias simulation system.
   b) Explain how your system represents and processes information.
   c) Describe how your system incorporates uncertainty and probabilistic reasoning.
   d) Discuss any novel features that distinguish your system from traditional AI decision-making models.

3. Application to Geopolitical Scenario (250-300 words):
   a) Briefly describe the key aspects and stakeholders in the given geopolitical scenario.
   b) Apply your AI system to the scenario, detailing the decision-making process.
   c) Explain how each simulated cognitive bias influences the decisions made.
   d) Provide at least two alternative outcomes based on different bias interactions.

4. Comparative Analysis (200-250 words):
   a) Compare your system's decision-making process to that of an ideal rational agent.
   b) Analyze how the simulated cognitive biases led to suboptimal or irrational decisions.
   c) Discuss the potential real-world implications of these biased decisions in the given scenario.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss the ethical implications of creating AI systems that simulate human cognitive biases.
   b) Explore potential misuses or unintended consequences of such systems.
   c) Propose guidelines for the responsible development and use of cognitive bias simulation in AI.
   d) Acknowledge limitations of your approach and suggest areas for future research.

Ensure your response demonstrates a deep understanding of cognitive psychology, AI system design, and geopolitical analysis. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts. Include concrete examples and quantitative analysis where appropriate, especially when discussing the application of your system to the given scenario.

Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all three cognitive biases: {', '.join(t['biases'])}",
            f"The AI system must be applied to the geopolitical scenario: {t['scenario']}",
            "The response must include all five required sections with appropriate word counts",
            "The AI system design must be logically consistent and demonstrate understanding of both cognitive biases and AI architecture",
            "The application to the geopolitical scenario must be thorough and show how each bias influences decisions",
            "The comparative analysis must provide insightful differences between the biased AI and a rational agent",
            "The ethical considerations must be thoughtful and address potential misuses of the technology",
            "The response must include concrete examples and quantitative analysis, especially in the application section",
            f"The response must incorporate the provided scenario data: {t['data']}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
