import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {"name": "Coral Reef", "challenge": "Ocean Acidification"},
            {"name": "Amazon Rainforest", "challenge": "Deforestation"},
            {"name": "Arctic Tundra", "challenge": "Permafrost Thaw"},
            {"name": "Savanna Grassland", "challenge": "Desertification"},
            {"name": "Urban Ecosystem", "challenge": "Air Pollution"}
        ]
        interventions = [
            "Geoengineering",
            "Biotechnology",
            "Smart City Technologies",
            "Carbon Capture and Storage",
            "Artificial Species Introduction"
        ]
        return {
            "1": {"ecosystem": random.choice(ecosystems), "intervention": random.choice(interventions)},
            "2": {"ecosystem": random.choice(ecosystems), "intervention": random.choice(interventions)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered ecosystem simulator for a {t['ecosystem']['name']} facing the challenge of {t['ecosystem']['challenge']}. Your simulator should model complex environmental interactions and evaluate the ethical implications of using {t['intervention']} as an intervention. Your response should include:

1. Simulator Architecture (250-300 words):
   a) Describe the key components of your AI-powered ecosystem simulator.
   b) Explain how your simulator models complex environmental interactions specific to the {t['ecosystem']['name']}.
   c) Discuss how your system incorporates the challenge of {t['ecosystem']['challenge']} into its models.
   d) Outline how the simulator evaluates the potential impacts of {t['intervention']}.

2. AI and Data Integration (200-250 words):
   a) Specify the types of AI techniques and algorithms your simulator employs.
   b) Describe the data sources and types your simulator would use.
   c) Explain how your system handles uncertainty and variability in environmental data.
   d) Discuss any novel AI approaches you've incorporated to enhance the simulator's predictive capabilities.

3. Ethical Framework (200-250 words):
   a) Outline the ethical framework your simulator uses to evaluate interventions.
   b) Explain how this framework is integrated into the simulation process.
   c) Describe how your system balances short-term benefits with long-term consequences.
   d) Discuss how your simulator accounts for different stakeholder perspectives in its ethical evaluations.

4. Simulation Scenario (250-300 words):
   a) Describe a specific scenario where your simulator is used to evaluate the impact of {t['intervention']} on the {t['ecosystem']['name']}.
   b) Provide a sample output of your simulator, including both environmental and ethical implications.
   c) Analyze the trade-offs identified by your simulator in this scenario.
   d) Explain how the simulator's output could inform decision-making processes.

5. Limitations and Future Improvements (150-200 words):
   a) Identify potential limitations or biases in your simulator design.
   b) Propose methods to validate and improve the accuracy of your simulator.
   c) Suggest potential future enhancements to your system, considering advancements in AI and environmental science.

Ensure your response demonstrates a deep understanding of environmental science, AI technologies, and ethical reasoning. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and adhere to the word count guidelines provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed description of an AI-powered ecosystem simulator for a {t['ecosystem']['name']} facing the challenge of {t['ecosystem']['challenge']}.",
            f"The simulator design must incorporate complex environmental interactions and evaluate the ethical implications of using {t['intervention']} as an intervention.",
            "The response should demonstrate a deep understanding of environmental science, AI technologies, and ethical reasoning.",
            "The proposed simulator should be innovative while maintaining scientific plausibility.",
            "All five sections (Simulator Architecture, AI and Data Integration, Ethical Framework, Simulation Scenario, and Limitations and Future Improvements) must be addressed comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
