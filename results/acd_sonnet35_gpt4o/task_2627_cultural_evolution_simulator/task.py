import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_factors = [
            "religion",
            "technology",
            "social_hierarchy",
            "economic_system",
            "environmental_conditions",
            "inter_group_conflict",
            "artistic_expression",
            "family_structure"
        ]
        simulation_durations = [100, 500, 1000, 2000]
        tasks = [
            {
                "cultural_factors": random.sample(cultural_factors, 2),
                "simulation_duration": random.choice(simulation_durations),
                "number_of_societies": random.randint(3, 6),
                "external_event": random.choice(["natural disaster", "technological breakthrough", "pandemic", "alien contact"])
            },
            {
                "cultural_factors": random.sample(cultural_factors, 2),
                "simulation_duration": random.choice(simulation_durations),
                "number_of_societies": random.randint(3, 6),
                "external_event": random.choice(["natural disaster", "technological breakthrough", "pandemic", "alien contact"])
            }
        ]
        return {"1": tasks[0], "2": tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and simulates the development and evolution of cultural practices and beliefs across different societies, focusing on the cultural factors of {t['cultural_factors'][0]} and {t['cultural_factors'][1]}. Your simulation should cover a period of {t['simulation_duration']} years and include {t['number_of_societies']} distinct societies. Additionally, your simulation should incorporate the impact of a significant external event: {t['external_event']}. Then, analyze the potential applications and ethical implications of your system. Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for modeling cultural evolution.
   b) Explain how your system incorporates principles from cultural anthropology, sociology, and cognitive science.
   c) Detail how your system simulates the interaction and influence between different societies.
   d) Describe how your system models the impact of the external event on cultural evolution.
   e) Include a simple diagram or flowchart of your system architecture (using ASCII art or a clear textual description).

2. Cultural Evolution Model (250-300 words):
   a) Explain how your system models the development and spread of cultural practices related to {t['cultural_factors'][0]} and {t['cultural_factors'][1]}.
   b) Describe the key variables and parameters your model considers.
   c) Discuss how your model accounts for historical events, environmental factors, and inter-societal interactions.
   d) Explain how your model simulates the impact of the {t['external_event']} on cultural practices.
   e) Provide an example of how a specific cultural practice might evolve in your simulation.

3. Simulation Results and Analysis (200-250 words):
   a) Present a high-level summary of the simulated cultural evolution over the {t['simulation_duration']} year period.
   b) Identify any emerging patterns or unexpected outcomes in your simulation.
   c) Analyze the differential impact of the {t['external_event']} on the {t['number_of_societies']} societies.
   d) Explain how your results might inform our understanding of real-world cultural dynamics.

4. Potential Applications (150-200 words):
   a) Propose two potential applications of your cultural evolution simulator in fields such as social science, policy-making, or education.
   b) Explain how these applications could benefit society or advance our understanding of cultural dynamics.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of using AI to model and predict cultural evolution.
   b) Address potential concerns about cultural determinism or the misuse of such simulations.
   c) Analyze the ethical implications of simulating extreme events like {t['external_event']}.
   d) Propose guidelines for the responsible development and use of cultural evolution simulators.

6. Limitations and Future Improvements (150-200 words):
   a) Identify the main limitations of your current system.
   b) Suggest two potential improvements or extensions to your cultural evolution simulator.
   c) Propose a research question that could be explored using an advanced version of your system.

Ensure your response demonstrates a deep understanding of cultural anthropology, sociology, artificial intelligence, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cultural anthropology, sociology, and AI principles.",
            "The AI system architecture is well-designed and clearly explained, incorporating relevant principles from multiple disciplines.",
            "The cultural evolution model is comprehensive and considers multiple factors influencing cultural development, including the impact of the external event.",
            "The simulation results are presented clearly and analyzed thoughtfully, including the differential impact of the external event on different societies.",
            "The proposed applications are innovative and well-justified.",
            "The ethical implications are thoroughly discussed, with thoughtful guidelines proposed, including considerations for simulating extreme events.",
            "The limitations and future improvements are insightful and demonstrate critical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
