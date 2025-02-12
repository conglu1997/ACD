import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "energy sector decarbonization",
            "global carbon taxation",
            "geoengineering implementation",
            "biodiversity preservation"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum annealing",
            "quantum error correction"
        ]
        return {
            "1": {"scenario": random.choice(scenarios), "quantum_principle": random.choice(quantum_principles)},
            "2": {"scenario": random.choice(scenarios), "quantum_principle": random.choice(quantum_principles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for global climate modeling and ethical decision-making in climate change mitigation strategies. Focus on the scenario: {t['scenario']}. Your system must incorporate the quantum principle of {t['quantum_principle']}. Your response should include:

1. Quantum-Enhanced Climate Modeling System (300-350 words):
   a) Describe the key components and architecture of your quantum-enhanced AI system for climate modeling.
   b) Explain how your system incorporates the quantum principle of {t['quantum_principle']} to enhance climate modeling capabilities.
   c) Discuss how quantum computing could improve the accuracy and efficiency of climate predictions compared to classical methods.
   d) Provide an example of how your system would model a specific climate phenomenon, demonstrating the advantage of the quantum approach.
   e) Include a hypothetical quantum circuit diagram (using ASCII art or a detailed text description) that illustrates a key component of your system.

2. Ethical Decision-Making Framework (300-350 words):
   a) Develop an ethical framework for your AI system to evaluate and recommend climate change mitigation strategies.
   b) Explain how your system balances competing ethical considerations (e.g., short-term economic impact vs. long-term environmental benefits).
   c) Describe how the quantum aspects of your system contribute to ethical reasoning or decision-making processes.
   d) Discuss potential biases or limitations in your ethical framework and how you would address them.
   e) Provide a specific example of an ethical dilemma your system might encounter and how it would resolve it.

3. Application to Scenario (250-300 words):
   a) Apply your quantum-enhanced AI system to the given scenario: {t['scenario']}.
   b) Describe how your system would model the climate impacts of this scenario, including specific variables and quantum operations used.
   c) Explain the ethical considerations your system would take into account, referencing your ethical framework.
   d) Provide a sample output or recommendation from your system for this scenario, including both climate projections and ethical analysis.

4. Technical Challenges and Solutions (200-250 words):
   a) Identify at least three key technical challenges in implementing your quantum-enhanced climate modeling and ethical AI system.
   b) Propose innovative solutions to these challenges, considering both current and near-future quantum technologies.
   c) Discuss any limitations of your approach and areas where classical computing might still be necessary or preferable.

5. Societal and Policy Implications (200-250 words):
   a) Analyze the potential societal impacts of using a quantum-enhanced AI system for climate policy decision-making.
   b) Discuss how policymakers and the public might interact with or interpret the outputs of such a system.
   c) Address concerns about the 'black box' nature of complex AI systems and how you would ensure transparency and accountability.
   d) Propose at least three specific guidelines for the ethical development and deployment of quantum AI systems in climate policy.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research that could enhance your quantum-enhanced climate ethics AI system.
   b) Explain how these research directions could address current limitations or open up new possibilities in climate modeling and ethical decision-making.
   c) Propose a specific experiment or study design for one of these research directions.

Ensure your response demonstrates a deep understanding of quantum computing, climate science, and ethical philosophy. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Quantum-Enhanced Climate Modeling System:') followed by your response for that section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, climate science, and ethical philosophy, using appropriate technical terminology throughout.",
            f"The quantum-enhanced climate modeling system clearly incorporates the quantum principle of {t['quantum_principle']} and includes a plausible quantum circuit diagram or description.",
            "The ethical decision-making framework is comprehensive, addressing multiple ethical considerations and providing a specific example of resolving an ethical dilemma.",
            f"The application to the scenario '{t['scenario']}' is thorough, including specific variables and quantum operations, and provides a plausible sample output with both climate projections and ethical analysis.",
            "At least three technical challenges are identified, with innovative solutions proposed that consider current and near-future quantum technologies.",
            "Societal and policy implications are thoughtfully analyzed, including at least three specific guidelines for ethical development and deployment of quantum AI systems in climate policy.",
            "Future research directions are insightful, addressing current limitations, and include a specific experiment or study design for one direction.",
            "The response adheres to the specified format, with clear headings for each section and falls within the 1400-1700 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
