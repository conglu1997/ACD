import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cosmic_phenomena = [
            "Black holes",
            "Dark matter",
            "Cosmic inflation",
            "Quantum entanglement"
        ]
        linguistic_concepts = [
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Phonology"
        ]
        information_processes = [
            "Encoding",
            "Compression",
            "Error correction",
            "Encryption"
        ]
        tasks = {}
        for i in range(1, 3):
            phenomenon = random.choice(cosmic_phenomena)
            concept = random.choice(linguistic_concepts)
            process = random.choice(information_processes)
            tasks[str(i)] = {"phenomenon": phenomenon, "concept": concept, "process": process}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical model that conceptualizes the universe as a vast computational linguistic structure, focusing on the cosmic phenomenon of {t['phenomenon']}, the linguistic concept of {t['concept']}, and the information process of {t['process']}. Your response should include the following sections, with the specified word counts:\n\n1. Theoretical Framework (300-350 words):\n   a) Outline the key principles of your cosmic linguistic model.\n   b) Explain how your model integrates concepts from physics, cosmology, linguistics, and information theory.\n   c) Describe the fundamental 'grammar' or 'syntax' of your universal language.\n   d) Discuss how your model addresses the problem of observer-independent reality.\n\n2. Cosmic Phenomenon Analysis (250-300 words):\n   a) Explain how your model interprets {t['phenomenon']} as a linguistic or computational process.\n   b) Describe the 'semantics' of this phenomenon within your universal language.\n   c) Discuss how this interpretation might lead to new insights or predictions about {t['phenomenon']}.\n\n3. Linguistic Concept Application (200-250 words):\n   a) Elaborate on how the linguistic concept of {t['concept']} is manifested in cosmic processes.\n   b) Provide an example of how this concept might be observed or measured in astronomical data.\n   c) Discuss any implications this application might have for our understanding of language or the universe.\n\n4. Information Processing Mechanism (200-250 words):\n   a) Describe how the information process of {t['process']} operates within your cosmic linguistic model.\n   b) Explain how this process relates to the evolution or structure of the universe.\n   c) Discuss any potential technological applications inspired by this cosmic information processing.\n\n5. Mathematical Formulation (150-200 words):\n   a) Provide at least one mathematical equation or formal logical statement that expresses a key aspect of your model.\n   b) Explain the variables and operations in your formulation.\n   c) Discuss how this formulation could be tested or validated.\n\n6. Visual Representation (100-150 words):\n   a) Describe, in words, a visual representation or diagram of your cosmic linguistic model.\n   b) Explain how this visual representation illustrates the key concepts of your theory.\n\n7. Implications and Predictions (200-250 words):\n   a) Discuss the philosophical implications of your cosmic linguistic model.\n   b) Propose at least two testable predictions derived from your model.\n   c) Explain how your model might influence future research in cosmology, linguistics, or information theory.\n\n8. Limitations and Future Directions (150-200 words):\n   a) Identify potential limitations or criticisms of your model.\n   b) Suggest areas for future research or refinement of your theory.\n   c) Discuss how your model might be extended to incorporate other aspects of physics or linguistics.\n\nEnsure your response demonstrates a deep understanding of theoretical physics, cosmology, linguistics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered exactly as above. Your total response should be between 1550-1950 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['phenomenon']}, {t['concept']}, and {t['process']} in the context of a cosmic linguistic model",
            "The theoretical framework is coherent and integrates concepts from physics, cosmology, linguistics, and information theory",
            "The mathematical formulation is relevant and well-explained",
            "The model proposes novel and testable predictions",
            "The response addresses potential limitations and future research directions",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The ideas presented are innovative while maintaining scientific plausibility",
            "The response includes all required sections with appropriate word counts",
            "A visual representation of the model is described clearly and effectively"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
