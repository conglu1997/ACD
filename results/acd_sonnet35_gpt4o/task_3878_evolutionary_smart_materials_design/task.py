import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "material_property": "self-healing",
                "application_domain": "aerospace engineering",
                "environmental_constraint": "extreme temperature fluctuations"
            },
            {
                "material_property": "shape-memory",
                "application_domain": "biomedical implants",
                "environmental_constraint": "physiological conditions"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an evolutionary algorithm-based system for developing adaptive smart materials with {t['material_property']} properties for applications in {t['application_domain']}, considering the environmental constraint of {t['environmental_constraint']}. Your response should include:

1. Evolutionary Algorithm Design (300-350 words):
   a) Describe the key components of your evolutionary algorithm for smart material design.
   b) Explain how you represent material properties and structures in your algorithm.
   c) Detail your fitness function, selection method, and genetic operators.
   d) Discuss how your algorithm handles the specified environmental constraint.

2. Smart Material Characteristics (250-300 words):
   a) Describe the desired {t['material_property']} properties of your smart material.
   b) Explain the nanoscale structures or mechanisms that enable these properties.
   c) Discuss how your material adapts to changes in its environment, particularly {t['environmental_constraint']}.

3. Simulation and Optimization Process (200-250 words):
   a) Outline the steps in your simulation process for evaluating material fitness.
   b) Explain how you balance computational efficiency with accuracy in your simulations.
   c) Describe any novel techniques you use to accelerate the evolutionary process.

4. Application in {t['application_domain']} (200-250 words):
   a) Explain how your smart material could be applied in {t['application_domain']}.
   b) Discuss the potential benefits and challenges of using your material in this domain.
   c) Compare your smart material solution to existing technologies in the field.

5. Ethical Considerations and Societal Impact (150-200 words):
   a) Identify potential ethical issues related to the development and use of your smart material.
   b) Discuss the broader societal implications of widespread adoption of such materials.
   c) Propose guidelines for responsible development and application of smart materials.

6. Future Research Directions (150-200 words):
   a) Suggest two potential avenues for further research to enhance your smart material or design process.
   b) Discuss how advancements in nanotechnology or computational methods might influence future smart material development.

Ensure your response demonstrates a deep understanding of materials science, evolutionary algorithms, and the specified application domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary algorithms, materials science, and nanotechnology.",
            f"The proposed smart material convincingly exhibits {t['material_property']} properties and addresses the {t['environmental_constraint']} constraint.",
            f"The application in {t['application_domain']} is well-explained and plausible.",
            "The ethical considerations and future research directions are thoughtfully addressed.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
