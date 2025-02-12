import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cell_types = [
            "Neuron",
            "Hepatocyte",
            "Cardiomyocyte",
            "Pancreatic beta cell",
            "Skeletal muscle cell"
        ]
        cellular_functions = [
            "Energy production",
            "Protein synthesis",
            "Waste management",
            "Cellular communication",
            "Stress response"
        ]
        return {
            "1": {"cell_type": random.choice(cell_types), "function": random.choice(cellular_functions)},
            "2": {"cell_type": random.choice(cell_types), "function": random.choice(cellular_functions)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial organelle for a {t['cell_type']} to enhance its {t['function']}. Your response should include:

1. Organelle Design (300-350 words):
   a) Describe the structure and components of your artificial organelle.
   b) Explain how it enhances the specified cellular function.
   c) Detail the organelle's integration with existing cellular structures.
   d) Provide a simple diagram or schematic of your organelle (describe it textually).

2. Cellular Interactions (250-300 words):
   a) Predict how your artificial organelle will interact with other cellular components.
   b) Discuss potential challenges in cellular integration and how to overcome them.
   c) Explain how the cell might regulate the artificial organelle's function.

3. Systems-Level Impact (200-250 words):
   a) Analyze how enhancing this cellular function might affect the overall organism.
   b) Discuss potential unintended consequences and how to mitigate them.
   c) Propose a method to monitor the artificial organelle's impact on the organism's health.

4. Potential Applications (200-250 words):
   a) Suggest three potential applications of your artificial organelle in medicine or biotechnology.
   b) Explain how each application could address current challenges in the field.
   c) Discuss any modifications needed to adapt your organelle for these applications.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to the development and use of artificial organelles.
   b) Discuss how these concerns might be addressed or mitigated.
   c) Propose guidelines for responsible research and application of this technology.

Ensure your response demonstrates a deep understanding of cellular biology, bioengineering, and systems biology. Use appropriate scientific terminology and provide clear explanations. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five sections as specified in the instructions.",
            "The artificial organelle design is creative, plausible, and well-explained.",
            "The response demonstrates a deep understanding of cellular biology and bioengineering.",
            "The systems-level impact and potential applications are thoughtfully analyzed.",
            "Ethical considerations are thoroughly discussed with proposed guidelines.",
            "The response uses appropriate scientific terminology and provides clear explanations.",
            "The total response is between 1100-1350 words."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
