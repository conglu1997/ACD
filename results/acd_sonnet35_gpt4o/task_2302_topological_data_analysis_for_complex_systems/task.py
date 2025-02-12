import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "complex_system": "Financial markets",
                "analysis_goal": "Predict market crashes"
            },
            "2": {
                "complex_system": "Brain connectome",
                "analysis_goal": "Identify patterns related to neurological disorders"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that applies topological data analysis (TDA) techniques to analyze and visualize high-dimensional data from the complex system of {t['complex_system']}, with the goal to {t['analysis_goal']}. Your response should include the following sections:

1. Topological Framework (250-300 words):
   a) Explain the key topological concepts and tools you will use in your analysis.
   b) Describe how these topological methods are particularly suited for analyzing the given complex system.
   c) Discuss any novel topological approaches or extensions you've developed for this specific application.

2. Data Representation and Processing (200-250 words):
   a) Describe how you would represent the high-dimensional data from the complex system in a form suitable for topological analysis.
   b) Explain any data preprocessing steps necessary for your analysis.
   c) Discuss how you handle challenges related to noise, missing data, or high dimensionality.

3. Analysis and Visualization Techniques (250-300 words):
   a) Detail the specific TDA techniques you will use to analyze the data (e.g., persistent homology, mapper algorithm).
   b) Explain how you will visualize the results of your topological analysis.
   c) Describe how your visualization techniques help in interpreting the complex system's behavior.
   d) Include a simple diagram or pseudocode representation of your TDA process (this can be described textually).

4. Interpretation and Problem Solving (200-250 words):
   a) Explain how you would interpret the results of your topological analysis in the context of the given complex system.
   b) Describe how your analysis contributes to the specified goal of {t['analysis_goal']}.
   c) Provide a hypothetical example of a pattern or structure your analysis might reveal and its significance.

5. Comparative Analysis (150-200 words):
   a) Compare your topological approach to traditional data analysis methods for this complex system.
   b) Discuss potential advantages and limitations of your TDA-based approach.

6. Ethical Considerations and Societal Impact (100-150 words):
   a) Identify potential ethical concerns or societal impacts of applying TDA to {t['complex_system']}.
   b) Propose guidelines for responsible development and use of TDA in this context.

7. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your TDA system.
   b) Briefly describe how these extensions could enhance its capabilities or applications.

Ensure your response demonstrates a deep understanding of topology, data analysis, and the specified complex system. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining mathematical and scientific rigor.

Format your response using clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of topological data analysis and its application to complex systems",
            f"The proposed system is well-designed to analyze {t['complex_system']} and address the goal of {t['analysis_goal']}",
            "The topological framework and analysis techniques are clearly explained and justified",
            "The data representation and processing methods are appropriate and well-described",
            "The interpretation of results is insightful and relevant to the problem at hand",
            "The comparative analysis shows a good understanding of the advantages and limitations of the TDA approach",
            "Ethical considerations are thoughtfully addressed",
            "The proposed future research directions are relevant and innovative",
            "A diagram or pseudocode representation of the TDA process is included and well-explained"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
