import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "ecosystem": "aquatic",
                "environmental_factor": "temperature gradient",
                "initial_species": "bioluminescent fish"
            },
            "2": {
                "ecosystem": "aerial",
                "environmental_factor": "atmospheric density variations",
                "initial_species": "gas-filled floating organisms"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes evolutionary processes, focusing on speciation events, then apply it to a hypothetical alien ecosystem. Your task has the following components:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating evolutionary processes and speciation events.
   b) Explain how your system incorporates principles from evolutionary biology and artificial intelligence.
   c) Detail the algorithms or methods used for simulating genetic variation, natural selection, and speciation.
   d) Discuss how your system handles the temporal aspect of evolution and speciation.

2. Speciation Modeling (200-250 words):
   a) Explain how your system models different types of speciation (e.g., allopatric, sympatric, parapatric).
   b) Describe the parameters and variables your system uses to determine when and how speciation occurs.
   c) Discuss how your system accounts for factors such as genetic drift, gene flow, and adaptive radiation.

3. Alien Ecosystem Application (250-300 words):
   a) Apply your AI system to simulate evolution and speciation in a hypothetical alien {t['ecosystem']} ecosystem.
   b) Describe how your system would model the initial population of {t['initial_species']}.
   c) Explain how your system would simulate the effects of the {t['environmental_factor']} on the evolutionary process.
   d) Provide a brief narrative of a potential speciation event that could occur in this ecosystem, as simulated by your AI.

4. Data Analysis and Visualization (150-200 words):
   a) Describe how your system would analyze the data generated from the evolutionary simulation.
   b) Explain what types of visualizations or data representations your system would produce to illustrate speciation events and evolutionary trends.
   c) Discuss how these analyses could provide insights into real-world evolutionary processes.

5. Limitations and Ethical Considerations (150-200 words):
   a) Identify potential limitations or challenges in your AI system's ability to accurately model evolutionary processes.
   b) Discuss any ethical considerations related to simulating evolution and applying these models to real-world scenarios.
   c) Propose guidelines for the responsible development and use of AI systems in evolutionary biology research.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your AI system.
   b) Briefly describe how these extensions could enhance our understanding of evolution and speciation.

Ensure your response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and complex system modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a comprehensive system architecture for simulating evolutionary processes and speciation events",
            "The system effectively models different types of speciation and incorporates relevant evolutionary factors",
            f"The AI system is successfully applied to the hypothetical alien {t['ecosystem']} ecosystem, considering the {t['environmental_factor']} and {t['initial_species']}",
            "The response describes appropriate data analysis and visualization methods for the evolutionary simulation",
            "Limitations, ethical considerations, and future directions are thoroughly discussed",
            "The proposed system demonstrates deep understanding of evolutionary biology and AI, while being innovative and scientifically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
