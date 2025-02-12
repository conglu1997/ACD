import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'nano_component': 'Carbon capture nanoparticles',
                'genetic_component': 'Engineered photosynthetic bacteria',
                'ai_component': 'Adaptive resource allocation',
                'climate_target': 'Atmospheric CO2 reduction',
                'constraint': 'Must operate in marine environments',
                'efficiency_target': '500 million tons CO2/year'
            },
            {
                'nano_component': 'Self-assembling solar cells',
                'genetic_component': 'Heat-resistant crop varieties',
                'ai_component': 'Predictive climate modeling',
                'climate_target': 'Global temperature stabilization',
                'constraint': 'Must be deployable in arid regions',
                'efficiency_target': '0.1°C reduction in 5 years'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical system that combines nanotechnology, genetic engineering, and artificial intelligence to address global climate change, focusing on {t['climate_target']}. Your system should incorporate {t['nano_component']}, {t['genetic_component']}, and {t['ai_component']}. The system {t['constraint']} and should aim for an efficiency of {t['efficiency_target']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the overall structure and components of your integrated system.
   b) Explain how nanotechnology, genetic engineering, and AI interact within your design.
   c) Detail how your system specifically targets {t['climate_target']}.
   d) Include a high-level diagram or flowchart of your system (describe it textually).

2. Nanotechnology Component (200-250 words):
   a) Elaborate on the design and function of the {t['nano_component']}.
   b) Explain how this nanotechnology interacts with the environment to address climate change.
   c) Discuss any novel properties or behaviors of your nanotech solution.

3. Genetic Engineering Component (200-250 words):
   a) Describe the genetic modifications involved in creating {t['genetic_component']}.
   b) Explain how these engineered organisms contribute to climate change mitigation.
   c) Discuss potential ecological interactions and safeguards.

4. AI Component (200-250 words):
   a) Detail the architecture and functionality of the {t['ai_component']} system.
   b) Explain how AI optimizes the performance of the nanotech and genetic components.
   c) Describe how the AI adapts to changing environmental conditions.

5. Impact Analysis (250-300 words):
   a) Predict the potential effectiveness of your system in addressing {t['climate_target']}.
   b) Compare your approach to existing climate change mitigation strategies.
   c) Discuss any potential unintended consequences and how they might be mitigated.
   d) Provide quantitative estimates of your system's impact over time, including how it meets the efficiency target of {t['efficiency_target']}.
   e) Analyze potential risks and failure modes of your proposed system.

6. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues related to your system's deployment.
   b) Discuss the implications of using such advanced technologies to manipulate the environment.
   c) Propose guidelines for responsible development and implementation of your system.

7. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how your approach might be adapted to address other global challenges.
   c) Speculate on how this technology might shape the future of climate science and environmental management.

8. Case Study (200-250 words):
   a) Provide a specific example of how your system would be implemented in a real-world scenario.
   b) Describe the steps involved in deploying your system in this case.
   c) Discuss potential challenges and how they would be overcome.

Ensure your response demonstrates a deep understanding of nanotechnology, genetic engineering, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1700-2100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of nanotechnology, genetic engineering, AI, and climate science, particularly in relation to {t['climate_target']}.",
            f"The system architecture effectively integrates {t['nano_component']}, {t['genetic_component']}, and {t['ai_component']}, and addresses the constraint: {t['constraint']}.",
            f"The impact analysis includes quantitative estimates that address the efficiency target of {t['efficiency_target']}, provides a comparison to existing strategies, and analyzes potential risks and failure modes.",
            "The ethical considerations are thoughtful, comprehensive, and consider long-term implications.",
            "The case study provides a concrete, realistic example of the system's implementation, including deployment steps and potential challenges.",
            "The response is creative and innovative while maintaining scientific plausibility and internal consistency.",
            "The response addresses all required sections (System Architecture, Nanotechnology Component, Genetic Engineering Component, AI Component, Impact Analysis, Ethical Considerations, Future Developments, and Case Study) in the specified format.",
            "The response follows the specified format and word count guidelines (1700-2100 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
