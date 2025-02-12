import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "decoherence"
        ]
        cellular_processes = [
            "DNA replication",
            "transcription",
            "translation",
            "protein folding"
        ]
        return {
            "1": {"quantum_concept": random.choice(quantum_concepts), "cellular_process": random.choice(cellular_processes)},
            "2": {"quantum_concept": random.choice(quantum_concepts), "cellular_process": random.choice(cellular_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model for quantum information processing in biological cells, focusing on the quantum concept of {t['quantum_concept']} in the cellular process of {t['cellular_process']}. 

Quantum information processing in biological systems refers to the potential role of quantum mechanical effects in the storage, transmission, and manipulation of information within living cells.

Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain the chosen quantum concept and its potential relevance to cellular processes.
   b) Describe how this quantum effect might influence or enhance information processing in cells.
   c) Propose a novel mechanism by which the quantum effect could interact with the specified cellular process.
   d) Discuss any existing research or theories that support or challenge your proposed model.

2. Model Design (250-300 words):
   a) Outline the key components and structure of your quantum cellular information processing model.
   b) Explain how your model incorporates both quantum mechanics and cellular biology principles.
   c) Describe how information is encoded, processed, and transmitted in your model.
   d) Propose a mathematical formalism or conceptual framework to represent your model.

3. Experimental Approach (200-250 words):
   a) Suggest an experimental setup to test your theoretical model.
   b) Describe the expected results and how they would support or refute your model.
   c) Discuss potential challenges in implementing such experiments and how they might be overcome.

4. Implications and Applications (150-200 words):
   a) Analyze the potential implications of your model for our understanding of life and information processing in biological systems.
   b) Propose potential applications in fields such as medicine, biotechnology, or quantum computing.
   c) Discuss how your model might influence the development of new technologies or therapeutic approaches.

5. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations or challenges of your proposed model.
   b) Suggest areas for future research or refinement of the model.
   c) Propose one novel research question that arises from your model.

Ensure your response demonstrates a deep understanding of quantum physics, molecular biology, and information theory. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology throughout your response and provide clear explanations where necessary.

Include at least one specific example or analogy in each section to illustrate complex concepts.

Format your response with clear headings for each section, numbered as above (1, 2, 3, 4, 5). Begin each section with the heading on a new line, followed by your response for that section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly incorporate the quantum concept of {t['quantum_concept']} into the model design.",
            f"The model should focus on the cellular process of {t['cellular_process']}.",
            "The proposed model should be novel and creative while remaining scientifically plausible.",
            "The response should demonstrate a deep understanding of quantum physics, molecular biology, and information theory.",
            "All five requested sections should be present and adequately addressed.",
            "Each section should include at least one specific example or analogy to illustrate complex concepts.",
            "The response should contain at least one novel idea or hypothesis related to quantum cellular information processing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
