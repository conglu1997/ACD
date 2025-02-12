import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'challenge': 'Ocean microplastic pollution',
                'inspiration': 'Lotus leaf water-repellent properties',
                'target_efficiency': '85%',
                'deployment_area': 'North Pacific Gyre'
            },
            {
                'challenge': 'Urban air pollution',
                'inspiration': 'Spider silk strength and elasticity',
                'target_efficiency': '75%',
                'deployment_area': 'Beijing metropolitan area'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic nanotechnology system inspired by {t['inspiration']} to address the environmental challenge of {t['challenge']}. Your system should aim for a target efficiency of {t['target_efficiency']} and be deployable in the {t['deployment_area']}. Then, analyze its potential ecological impacts and ethical implications. Provide your response in the following format:

1. System Design (250-300 words):
   a) Describe the key components and functionality of your biomimetic nanotechnology system.
   b) Explain how it incorporates principles from {t['inspiration']}.
   c) Detail how your system addresses {t['challenge']} in the {t['deployment_area']}.
   d) Include a diagram or schematic representation of your system (describe it textually).

2. Nanotechnology Integration (200-250 words):
   a) Specify the nanomaterials or nanostructures used in your system.
   b) Explain the unique properties of these nanomaterials that make them suitable for your design.
   c) Describe any novel nanofabrication techniques required for your system.

3. Environmental Impact Analysis (200-250 words):
   a) Assess the potential positive impacts of your system on the environment.
   b) Identify and analyze any potential negative ecological consequences.
   c) Propose methods to mitigate any adverse effects.

4. Scalability and Implementation (150-200 words):
   a) Discuss the feasibility of scaling up your system to achieve the target efficiency of {t['target_efficiency']}.
   b) Identify potential challenges in implementation specific to the {t['deployment_area']} and propose solutions.
   c) Estimate the timeline and resources required for development and deployment.

5. Ethical Implications (200-250 words):
   a) Analyze the ethical considerations of deploying your nanotechnology system in the {t['deployment_area']}.
   b) Discuss potential unintended consequences and how they might be addressed.
   c) Propose guidelines for responsible development and use of your technology.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your design integrates knowledge from biology, engineering, materials science, and environmental studies.
   b) Propose a novel research question that arises from the interdisciplinary nature of your system.

Ensure your response demonstrates a deep understanding of biomimetics, nanotechnology, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biomimetics, nanotechnology, and environmental science.",
            f"The system design is innovative, plausible, and clearly explains how it addresses {t['challenge']} in the {t['deployment_area']}.",
            "The nanotechnology integration is well-reasoned and specific, with clear explanations of nanomaterial properties and fabrication techniques.",
            "The environmental impact analysis is comprehensive and balanced, considering both positive and negative effects.",
            f"The scalability and implementation discussion is realistic and detailed, addressing the target efficiency of {t['target_efficiency']}.",
            f"The ethical implications are thoroughly explored, considering the specific context of the {t['deployment_area']}.",
            "The interdisciplinary connections are insightful and well-articulated.",
            "The response includes a clear diagram or schematic representation of the system (described textually).",
            "The overall response shows strong integration of knowledge from multiple disciplines.",
            "The proposed solution is creative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits for each section and overall length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
