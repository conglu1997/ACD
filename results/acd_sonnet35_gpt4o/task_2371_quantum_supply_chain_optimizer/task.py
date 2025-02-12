import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Pharmaceutical distribution",
                "constraint": "Temperature-sensitive products",
                "optimization_goal": "Minimize delivery time while maintaining product integrity",
                "network_size": "10,000 distribution points across 50 countries",
                "key_parameter": "Temperature range: -20°C to 25°C"
            },
            {
                "name": "Semiconductor manufacturing",
                "constraint": "Just-in-time production",
                "optimization_goal": "Reduce inventory costs while ensuring continuous production",
                "network_size": "500 suppliers, 20 manufacturing plants, 1000 customers globally",
                "key_parameter": "Lead time variability: 1-30 days"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to optimize global supply chains for the {t['name']} industry. Your system should address the specific constraint of {t['constraint']} and focus on the optimization goal to {t['optimization_goal']}. Consider the network size of {t['network_size']} and the key parameter: {t['key_parameter']}. Provide a comprehensive response covering the following aspects:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum computing system for supply chain optimization.
   b) Explain how your system leverages quantum principles to address the given constraint and optimization goal.
   c) Discuss any hybrid classical-quantum approaches your system employs.
   d) Provide a high-level textual description of your system architecture (do not attempt to include an actual visual diagram).

2. Quantum Algorithm Design (250-300 words):
   a) Outline the quantum algorithm(s) your system uses for supply chain optimization.
   b) Explain how these algorithms outperform classical approaches for the given scenario.
   c) Describe how your algorithm handles uncertainty and variability in supply chain data.
   d) Include a brief pseudocode or mathematical formulation of a key part of your quantum algorithm.

3. Data Integration and Processing (200-250 words):
   a) Explain how your system integrates real-time supply chain data.
   b) Describe any pre-processing or encoding methods used to prepare data for quantum computation.
   c) Discuss how your system handles the interface between classical data and quantum states.

4. Optimization Process and Output (200-250 words):
   a) Detail the step-by-step process of how your system optimizes the supply chain.
   b) Explain how the system generates and evaluates potential solutions.
   c) Describe the output format and how it can be interpreted and implemented by supply chain managers.

5. Scalability and Error Mitigation (150-200 words):
   a) Discuss how your system can scale to handle the given network size.
   b) Explain any error correction or mitigation techniques used in your quantum system.
   c) Address potential limitations in current quantum hardware and how your design accounts for these.

6. Comparative Analysis (150-200 words):
   a) Compare your quantum approach to traditional supply chain optimization methods.
   b) Provide a quantitative estimate of the potential improvements in efficiency or cost savings.
   c) Discuss any trade-offs or potential drawbacks of using quantum computing for this application.

7. Ethical and Economic Implications (150-200 words):
   a) Discuss potential ethical concerns related to using quantum computing for supply chain optimization.
   b) Analyze the economic impact of implementing such a system on the global market and workforce.
   c) Propose guidelines for responsible development and use of quantum computing in supply chain management.

Ensure your response demonstrates a deep understanding of both quantum computing principles and supply chain management. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and practical considerations.

Format your response using clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific {t['name']} industry scenario, considering the constraint of {t['constraint']}, the optimization goal to {t['optimization_goal']}, the network size of {t['network_size']}, and the key parameter: {t['key_parameter']}.",
            "The quantum system architecture should be well-defined and leverage quantum principles appropriately for supply chain optimization.",
            "The quantum algorithm design should be clearly explained and demonstrate advantages over classical approaches, including a pseudocode or mathematical formulation.",
            "The response should include a comprehensive discussion of data integration, processing, and the optimization process, considering the specific industry requirements.",
            "The submission should address scalability for the given network size, error mitigation, and provide a comparative analysis with traditional methods.",
            "Ethical and economic implications of the proposed system should be thoroughly discussed, including guidelines for responsible development and use.",
            "The response should demonstrate a deep understanding of both quantum computing and supply chain management principles, using appropriate technical terminology.",
            "The submission should be well-structured, following the outlined format and word count guidelines, with clear headings and subheadings."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
