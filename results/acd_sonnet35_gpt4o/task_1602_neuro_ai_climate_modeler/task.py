import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'neural_principle': 'Predictive coding',
                'climate_focus': 'Ocean acidification',
                'mitigation_strategy': 'Carbon sequestration',
                'example_data': 'pH levels in coastal waters have decreased by 0.1 units since the industrial revolution'
            },
            {
                'neural_principle': 'Hebbian learning',
                'climate_focus': 'Extreme weather events',
                'mitigation_strategy': 'Adaptive infrastructure',
                'example_data': 'Category 4 and 5 hurricanes have increased by 25-30% per degree Celsius of global warming'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Design an AI system that uses principles from neuroscience to model and mitigate climate change, integrating brain-inspired algorithms with climate science data. Your system should incorporate the neural principle of {t['neural_principle']}, focus on the climate issue of {t['climate_focus']}, and aim to implement the mitigation strategy of {t['mitigation_strategy']}. Consider this example data point in your design: {t['example_data']}.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your neuro-inspired climate AI system.
   b) Explain how it incorporates the specified neural principle in its design.
   c) Detail how the system will process and analyze climate data related to the given focus area.
   d) Discuss how the system will model and predict climate change impacts.
   e) Explain how the system will develop and optimize mitigation strategies.
   Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Neuroscience-Climate Interface (200-250 words):
   a) Explain how your system translates the specified neural principle into climate modeling algorithms.
   b) Describe how these algorithms are applied to the given climate focus area.
   c) Discuss any challenges in bridging neuroscience and climate science domains and how you address them.
   d) Provide a specific example of how your system would process the given example data point.

3. Mitigation Strategy Implementation (200-250 words):
   a) Propose a detailed approach for implementing the specified mitigation strategy using your AI system.
   b) Explain how this approach leverages the neural principle and climate modeling capabilities of your system.
   c) Describe how the system would adapt and improve its mitigation strategies over time.
   d) Provide a hypothetical timeline for implementing and scaling your mitigation strategy.

4. Predictive Capabilities (150-200 words):
   a) Describe a specific climate change scenario your system could model and predict.
   b) Explain how this prediction incorporates both the neural principle and climate science data.
   c) Discuss the potential accuracy and limitations of such predictions.
   d) Compare your system's predictive capabilities to current climate modeling approaches.

5. Ethical Implications and Governance (200-250 words):
   a) Discuss the potential ethical implications of using a neuro-inspired AI system for climate change mitigation.
   b) Address concerns about data privacy, algorithmic bias, and the concentration of decision-making power.
   c) Propose a governance framework for the responsible development and use of such systems.
   d) Suggest three specific policies or guidelines to ensure ethical use of your system.

6. Broader Impacts (150-200 words):
   a) Speculate on how this technology might affect climate policy, industry, and public perception of climate change.
   b) Discuss potential applications of your system beyond climate change mitigation.
   c) Consider any potential unintended consequences of widespread adoption of your system.
   d) Propose a method to monitor and evaluate the long-term impacts of your system.

7. Technical Challenges and Future Development (150-200 words):
   a) Identify the main technical hurdles in developing and deploying your neuro-inspired climate AI system.
   b) Suggest approaches to overcome these challenges.
   c) Outline a roadmap for future development and testing of the technology.
   d) Propose a specific experiment to validate a key aspect of your system's design.

Ensure your response demonstrates a deep understanding of neuroscience principles, artificial intelligence, and climate science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1300-1650 words, with each section adhering to the specified word count range.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['neural_principle']} and its application to modeling and mitigating {t['climate_focus']}.",
            "The system architecture is well-designed, clearly explained, and includes a high-level diagram or pseudocode.",
            f"The proposed implementation of {t['mitigation_strategy']} is innovative, practical, and leverages the strengths of the neuro-inspired AI system.",
            f"The response incorporates the example data point ({t['example_data']}) in its explanation of the system's functionality.",
            "The discussion of ethical implications and governance is thorough, including specific policies or guidelines.",
            "The response addresses all required sections with the specified word count ranges.",
            "The ideas presented are creative and scientifically plausible, demonstrating interdisciplinary knowledge synthesis.",
            "The response is well-structured, following the specified format with clear headings for each section and subsection."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
