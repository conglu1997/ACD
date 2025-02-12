import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        material_types = [
            "Nanoporous metal-organic frameworks",
            "Artificial photosynthetic membranes",
            "Genetically engineered carbon-fixing bacteria"
        ]
        implementation_scales = [
            "Urban centers",
            "Coastal regions",
            "Global atmospheric deployment"
        ]
        tasks = [
            {
                "material_type": material,
                "implementation_scale": scale
            }
            for material in material_types
            for scale in implementation_scales
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an advanced material system for large-scale carbon capture and storage using {t['material_type']}, then simulate its implementation at the scale of {t['implementation_scale']} and analyze the impacts on climate, policy, and economics. Your response should include the following sections:

1. Material Design (300-350 words):
   a) Describe the key properties and structure of your {t['material_type']} for carbon capture and storage.
   b) Explain the scientific principles behind its carbon capture mechanism.
   c) Discuss any novel features or innovations in your design.
   d) Address potential challenges in manufacturing and scaling up production.

2. Implementation Strategy (250-300 words):
   a) Propose a detailed plan for implementing your material system at the scale of {t['implementation_scale']}.
   b) Describe the infrastructure and technology required for deployment.
   c) Discuss potential environmental and social impacts of the implementation.
   d) Estimate the timeline and major milestones for full-scale deployment.

3. Climate Impact Simulation (250-300 words):
   a) Describe a model for simulating the climate impact of your material system.
   b) Provide quantitative estimates of potential carbon capture rates and long-term storage capacity.
   c) Analyze the system's effectiveness in different climate scenarios.
   d) Discuss any potential unintended consequences or feedback loops.

4. Policy Implications (200-250 words):
   a) Analyze how the implementation of your system might influence international climate agreements.
   b) Propose policy frameworks to support the development and deployment of your technology.
   c) Discuss potential geopolitical implications of large-scale carbon capture capability.
   d) Address concerns about moral hazard in climate policy due to advanced carbon capture technology.

5. Economic Analysis (200-250 words):
   a) Estimate the costs associated with developing, implementing, and maintaining your system.
   b) Analyze potential economic benefits, including carbon credits and new industry development.
   c) Discuss how your system might impact existing industries and global economic structures.
   d) Propose economic incentives or mechanisms to support global adoption of your technology.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of large-scale manipulation of atmospheric composition.
   b) Address concerns about unequal access to climate mitigation technology.
   c) Analyze potential long-term consequences for future generations.
   d) Propose guidelines for responsible development and use of advanced climate intervention technologies.

Ensure your response demonstrates a deep understanding of materials science, climate systems, and global policy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should thoroughly address the material type {t['material_type']} and implementation scale {t['implementation_scale']}",
            "The material design should be scientifically plausible and innovative",
            "The climate impact simulation should provide quantitative estimates and consider multiple scenarios",
            "The policy and economic analyses should be comprehensive and consider global implications",
            "The response should demonstrate a deep understanding of materials science, climate systems, and global policy",
            "The ethical considerations should be thoughtful and address multiple perspectives"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
