class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {
                "name": "Kepler-442b",
                "mass": "2.34 Earth masses",
                "radius": "1.34 Earth radii",
                "orbital_period": "112.3 Earth days",
                "star_type": "K-type orange dwarf",
                "distance": "1,206 light-years",
                "atmosphere": "Unknown, potentially thin",
                "surface_temperature": "Estimated -40°C to 20°C"
            },
            {
                "name": "Gliese 667 Cc",
                "mass": "3.8 Earth masses",
                "radius": "1.5 Earth radii",
                "orbital_period": "28.1 Earth days",
                "star_type": "M-type red dwarf",
                "distance": "23.62 light-years",
                "atmosphere": "Unknown, potentially dense",
                "surface_temperature": "Estimated -25°C to 10°C"
            }
        ]
        return {
            "1": exoplanets[0],
            "2": exoplanets[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a detailed simulation of the terraforming process for the exoplanet {t['name']}. Your simulation should model the transformation of the planet into a habitable world over a 1000-year period. Include the following components in your response:

        1. Initial Assessment and Strategy (250-300 words):
           a) Analyze the given planetary characteristics and their implications for terraforming.
           b) Outline your overall terraforming strategy and key milestones.
           c) Identify at least three major challenges specific to this exoplanet and propose solutions.

        2. Atmospheric Engineering (250-300 words):
           a) Detail the process of modifying the planet's atmosphere to support life.
           b) Explain how you will adjust atmospheric composition, pressure, and temperature.
           c) Describe any novel technologies or methods used in this process.

        3. Hydrosphere Development (200-250 words):
           a) Explain your approach to establishing a stable water cycle on the planet.
           b) Discuss methods for introducing or managing water resources.
           c) Address any unique challenges related to the planet's characteristics.

        4. Ecosystem Design and Implementation (250-300 words):
           a) Propose a strategy for introducing and sustaining life on the planet.
           b) Describe the stages of ecosystem development over the 1000-year period.
           c) Explain how you will ensure ecosystem stability and biodiversity.

        5. Climate Control and Stabilization (200-250 words):
           a) Detail your methods for establishing and maintaining a stable climate.
           b) Discuss how you will manage extreme weather events or climate fluctuations.
           c) Explain any long-term climate engineering techniques employed.

        6. Simulation Modeling and Monitoring (200-250 words):
           a) Describe the computational models and algorithms used in your simulation.
           b) Explain how your simulation accounts for complex system interactions.
           c) Outline a plan for monitoring and adjusting the terraforming process based on simulation results.

        7. Ethical Considerations and Contingency Planning (150-200 words):
           a) Discuss ethical implications of terraforming this exoplanet.
           b) Propose safeguards against potential negative outcomes.
           c) Outline a contingency plan for a major setback in the terraforming process.

        Ensure your response demonstrates a deep understanding of planetary science, astrobiology, and advanced technologies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section. Your total response should be between 1500-1850 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of planetary science, astrobiology, and advanced technologies.",
            "The terraforming strategy is well-thought-out and addresses the specific characteristics of the given exoplanet.",
            "The simulation design incorporates complex system interactions and long-term planning.",
            "The proposed technologies and methods are innovative while maintaining scientific plausibility.",
            "Ethical considerations and contingency planning are adequately addressed.",
            "The response is well-structured, clear, and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
