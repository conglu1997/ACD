import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "problem_domain": "Climate Change Mitigation",
                "data_types": ["Satellite Imagery", "Time Series Data", "Research Papers"],
                "specific_task": "Predict the impact of reforestation efforts on global carbon sequestration",
                "synthetic_data": {
                    "satellite_imagery": "Time series of forest cover changes in the Amazon rainforest from 2000 to 2020",
                    "time_series_data": "Monthly atmospheric CO2 concentrations from 1980 to 2020",
                    "research_papers": "Abstracts of 100 peer-reviewed papers on carbon sequestration in tropical forests"
                }
            },
            {
                "problem_domain": "Pandemic Response",
                "data_types": ["Genomic Sequences", "Epidemiological Models", "Social Media Trends"],
                "specific_task": "Analyze the effectiveness of public health interventions on disease spread",
                "synthetic_data": {
                    "genomic_sequences": "100 SARS-CoV-2 genomic sequences from different geographical regions",
                    "epidemiological_models": "SIR model predictions for disease spread in 10 major cities",
                    "social_media_trends": "Twitter sentiment analysis data on mask-wearing from January to December 2020"
                }
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and interpreting multimodal scientific data to solve complex interdisciplinary problems, then apply it to the following scenario:

Problem Domain: {t['problem_domain']}
Data Types: {', '.join(t['data_types'])}
Specific Task: {t['specific_task']}

Synthetic Data Available:
{', '.join(f'{k}: {v}' for k, v in t['synthetic_data'].items())}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for multimodal scientific reasoning.
   b) Explain how your system integrates and processes different types of data.
   c) Detail any novel AI techniques or algorithms used in your design.
   d) Discuss how your system ensures scientific rigor and accuracy in its analysis.

2. Data Integration and Preprocessing (250-300 words):
   a) Explain how your system preprocesses and standardizes the different types of data.
   b) Describe any techniques used for feature extraction or representation learning.
   c) Discuss how your system handles potential inconsistencies or conflicts in the data.

3. Reasoning and Analysis Process (250-300 words):
   a) Provide a step-by-step explanation of how your AI system approaches the given task.
   b) Describe the scientific reasoning methods employed by your system.
   c) Explain how your system generates and tests hypotheses based on the multimodal data.

4. Output and Interpretation (200-250 words):
   a) Describe the format and content of your system's output for the given task.
   b) Explain how your system communicates uncertainty and confidence in its results.
   c) Discuss how your system's output could be used by human experts in the field.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the accuracy and reliability of your system's analysis.
   b) Describe how you would validate your system's results against existing scientific knowledge.
   c) Discuss potential limitations of your approach and how they might be addressed.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to using AI for scientific reasoning in this domain.
   b) Discuss how your system addresses concerns about bias, transparency, and accountability.
   c) Propose guidelines for the responsible development and use of such AI systems in scientific research.

Ensure your response demonstrates a deep understanding of the relevant scientific domains, data analysis techniques, and AI methodologies. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Begin each subsection with the corresponding letter (a, b, c, etc.). Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the relevant scientific domains, data analysis techniques, and AI methodologies.",
            "The proposed AI system effectively integrates and analyzes the provided multimodal data types.",
            "The reasoning and analysis process is scientifically sound, well-explained, and addresses the specific task.",
            "The response includes a clear and feasible method for preprocessing and integrating the different data types.",
            "The output and interpretation section provides a clear format for presenting results and communicating uncertainty.",
            "The evaluation and validation methods are appropriate and well-justified.",
            "The response addresses potential limitations, ethical considerations, and validation methods comprehensively.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
