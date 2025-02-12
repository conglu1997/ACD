import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {
                "name": "Proxima Centauri b",
                "conditions": "Tidally locked, strong radiation, potential liquid water"
            },
            {
                "name": "TRAPPIST-1e",
                "conditions": "Rocky, potentially habitable, frequent solar flares"
            }
        ]
        evolutionary_factors = [
            "Extreme temperature fluctuations",
            "High-pressure atmosphere",
            "Low gravity environment",
            "Periodic bursts of intense radiation"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "exoplanet": random.choice(exoplanets),
                "evolutionary_factor": random.choice(evolutionary_factors)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to simulate and predict the evolution of life forms under the extreme extraterrestrial conditions of {t['exoplanet']['name']}, then use it to analyze potential biodiversity on this exoplanet. Your system should focus on the evolutionary factor of {t['evolutionary_factor']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system models and simulates evolutionary processes.
   c) Detail how the system incorporates the specific conditions of {t['exoplanet']['name']} and the evolutionary factor of {t['evolutionary_factor']}.
   d) Discuss any novel algorithms or techniques your system uses for long-term evolutionary prediction.

2. Evolutionary Model (250-300 words):
   a) Describe the key parameters and variables in your evolutionary model.
   b) Explain how your model accounts for the unique conditions on {t['exoplanet']['name']}.
   c) Detail how the model simulates the effects of {t['evolutionary_factor']} on evolving life forms.
   d) Discuss how your model handles the uncertainty inherent in long-term evolutionary predictions.

3. Biodiversity Analysis (250-300 words):
   a) Describe three potential life forms that your system predicts could evolve on {t['exoplanet']['name']}.
   b) Explain how these life forms are adapted to the planet's conditions and the evolutionary factor of {t['evolutionary_factor']}.
   c) Discuss the potential ecosystem interactions between these life forms.
   d) Compare the predicted biodiversity to known extremophiles on Earth.

4. Simulation Results (200-250 words):
   a) Present a hypothetical timeline of evolutionary milestones on {t['exoplanet']['name']}.
   b) Describe any recurring patterns or trends observed in multiple simulation runs.
   c) Discuss how the evolutionary factor of {t['evolutionary_factor']} influenced the overall evolutionary trajectory.

5. Scientific Implications (200-250 words):
   a) Discuss how your simulation results might inform our understanding of evolution and the potential for life in the universe.
   b) Propose three testable hypotheses based on your simulation results.
   c) Suggest how your system could be used to guide future exoplanet exploration and research.

6. Limitations and Future Improvements (150-200 words):
   a) Identify the main limitations of your current system and evolutionary model.
   b) Propose three specific improvements or extensions to your system.
   c) Discuss the challenges in validating such a system given our limited knowledge of exoplanets and potential alien life.

Ensure your response demonstrates a deep understanding of evolutionary biology, astrobiology, and AI simulation techniques. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections and subsections",
            "The system architecture is well-described and incorporates the specific exoplanet conditions and evolutionary factor",
            "The evolutionary model is detailed and accounts for the unique exoplanet environment",
            "The biodiversity analysis presents plausible and creative predictions for potential life forms",
            "The simulation results and scientific implications are logically derived and insightful",
            "The response demonstrates a deep understanding of evolutionary biology, astrobiology, and AI simulation techniques",
            "The proposed ideas are creative while maintaining scientific plausibility",
            "The response is well-structured and within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
