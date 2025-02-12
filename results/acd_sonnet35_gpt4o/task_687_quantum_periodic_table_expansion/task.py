import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "Superposition stability: The ability to maintain quantum superposition at macroscopic scales.",
            "Entanglement amplification: The capacity to enhance and extend quantum entanglement effects.",
            "Quantum tunneling enhancement: Increased probability of quantum tunneling effects.",
            "Temporal dilation: The ability to manipulate the flow of time at the quantum level.",
            "Dimensional phase-shifting: The capacity to exist in or transition between multiple spatial dimensions."
        ]
        return {str(i+1): {"property": prop} for i, prop in enumerate(random.sample(quantum_properties, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical chemical element with the quantum property of {t['property']} for an expanded periodic table. Your task is to:

1. Element Description (150-200 words):
   a) Assign an atomic number (between 200 and 300) and a name to your element.
   b) Describe its basic physical and chemical properties.
   c) Explain how the quantum property {t['property']} manifests in this element.
   d) Propose a unique electron configuration that could account for this property.

2. Periodic Table Placement (100-150 words):
   a) Suggest where this element would be placed in an expanded periodic table.
   b) Explain how its placement relates to its properties and quantum behavior.
   c) Describe any new groups or periods that might be necessary to accommodate it.
   d) Provide a simple ASCII art diagram representing your element's placement in the expanded periodic table.

3. Theoretical Applications (150-200 words):
   a) Propose two potential applications of this element in advanced technology or scientific research.
   b) Explain how each application leverages the element's quantum property.
   c) Discuss any challenges that might arise in utilizing this element.

4. Speculative Interactions (100-150 words):
   a) Hypothesize how this element might interact with one conventional element from the standard periodic table.
   b) Describe a chemical reaction or physical phenomenon that could result from this interaction.
   c) Propose an experiment to test this interaction (you may assume access to advanced future technology).

5. Quantum Mechanics Implications (100-150 words):
   a) Discuss how the existence of this element might impact our understanding of quantum mechanics.
   b) Propose a modification or extension to a current quantum theory to account for this element's behavior.

6. Ethical Considerations (100-150 words):
   a) Discuss potential risks or ethical implications associated with the discovery and use of this element.
   b) Propose guidelines or safeguards for responsible research and application of this element.

Ensure your response demonstrates a deep understanding of chemistry, quantum physics, and materials science. Be creative in your design while maintaining scientific plausibility and internal consistency. Use appropriate scientific terminology and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed description of a hypothetical element with the quantum property of {t['property']}",
            "The element's placement in an expanded periodic table should be explained and visualized with ASCII art",
            "At least two potential applications of the element should be proposed",
            "A speculative interaction with a conventional element should be described",
            "The implications for quantum mechanics should be discussed",
            "Potential risks and ethical implications should be considered",
            "The response should demonstrate creativity while maintaining scientific plausibility",
            "Appropriate scientific terminology should be used throughout the response"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
