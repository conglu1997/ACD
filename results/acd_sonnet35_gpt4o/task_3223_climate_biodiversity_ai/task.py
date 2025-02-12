import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ecosystem": "Coral Reefs",
                "climate_factor": "Ocean Acidification",
                "time_frame": "50 years",
                "region": "Great Barrier Reef"
            },
            {
                "ecosystem": "Arctic Tundra",
                "climate_factor": "Permafrost Thaw",
                "time_frame": "30 years",
                "region": "Siberian Arctic"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an AI system for predicting and mitigating the impacts of climate change on biodiversity, focusing on the {t['ecosystem']} ecosystem and the specific climate factor of {t['climate_factor']}. Your system should make predictions for a {t['time_frame']} timeframe in the {t['region']} region. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system, including data inputs, processing modules, and output mechanisms.
   b) Explain how your system integrates climate models, ecological data, and biodiversity information.
   c) Detail the machine learning or AI techniques used for predictive modeling and decision-making.
   d) Discuss how your system handles uncertainty and variability in climate and ecological data.
   e) Include a text-based diagram illustrating the system's architecture and data flow.

2. Data Integration and Analysis (250-300 words):
   a) Specify the types of data your system would use (e.g., satellite imagery, species distribution data, climate projections).
   b) Explain how your system preprocesses and integrates diverse data sources.
   c) Describe any novel data analysis techniques employed by your system.
   d) Discuss how your system addresses challenges such as data gaps or inconsistencies.

3. Predictive Modeling (250-300 words):
   a) Explain the predictive modeling approach used to forecast biodiversity changes.
   b) Describe how your model accounts for complex ecological interactions and feedback loops.
   c) Discuss how your system quantifies and communicates prediction uncertainty.
   d) Provide an example of a specific prediction your system might make for the given ecosystem and climate factor.

4. Mitigation Strategies (200-250 words):
   a) Explain how your AI system generates or evaluates potential mitigation strategies.
   b) Describe the criteria used to assess the feasibility and effectiveness of proposed interventions.
   c) Discuss how your system balances short-term and long-term conservation goals.
   d) Provide an example of a mitigation strategy your system might propose for the given scenario.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues or unintended consequences of using AI for biodiversity conservation.
   b) Discuss how your system addresses biases in data or decision-making processes.
   c) Explain the limitations of your approach and areas where human expertise is still crucial.
   d) Propose guidelines for the responsible use of AI in climate and biodiversity research.

6. Interdisciplinary Applications and Future Directions (150-200 words):
   a) Suggest two potential applications of your AI system in fields outside of ecology and climate science.
   b) Propose a collaboration between experts in AI and another scientific discipline to further develop your system.
   c) Discuss how this technology might evolve in the next decade to address broader environmental challenges.

Ensure your response demonstrates a deep understanding of climate science, ecology, data analysis, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all six required sections with appropriate content and word count for each.",
            "The AI system architecture should be innovative, clearly described, and include a text-based diagram.",
            "The data integration and analysis section must specify relevant data types and address challenges in data preprocessing.",
            "The predictive modeling section should explain the approach used and provide a specific example prediction.",
            "The mitigation strategies section must include an example strategy relevant to the given scenario.",
            "The ethical considerations section should identify potential issues and propose responsible use guidelines.",
            "The interdisciplinary applications section must suggest applications outside ecology and climate science.",
            "The overall response should demonstrate a clear integration of knowledge from climate science, ecology, data analysis, and artificial intelligence, while being innovative and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
