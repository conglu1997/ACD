import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            "protein folding",
            "gene regulation",
            "cellular metabolism",
            "neural signaling"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        
        tasks = {}
        for i in range(1, 3):
            bio_process = random.choice(biological_processes)
            quantum_concept = random.choice(quantum_concepts)
            tasks[str(i)] = {"biological_process": bio_process, "quantum_concept": quantum_concept}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system to model and predict the complex biological process of {t['biological_process']}, incorporating the quantum concept of {t['quantum_concept']}. Then, use your system to simulate this biological phenomenon and analyze the results. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI system for modeling {t['biological_process']}.
   b) Explain how your system incorporates {t['quantum_concept']} in its design or functioning.
   c) Detail how classical AI techniques are integrated with quantum-inspired elements.
   d) Include a diagram or pseudocode snippet illustrating a key aspect of your system architecture.

2. Biological Process Modeling (250-300 words):
   a) Explain how your system models the specific biological process of {t['biological_process']}.
   b) Describe the key variables and parameters your system tracks and simulates.
   c) Discuss how quantum-inspired techniques enhance the modeling of this biological process.

3. Simulation Design (200-250 words):
   a) Outline the steps involved in simulating {t['biological_process']} using your system.
   b) Describe the input data required and how it's processed by your quantum-inspired AI.
   c) Explain how you handle the interface between quantum-inspired components and classical biological data.
   d) Provide a concrete example or case study of how your system would simulate a specific aspect of {t['biological_process']}.

4. Results Analysis (250-300 words):
   a) Present and interpret the results of your simulation of {t['biological_process']}.
   b) Compare your quantum-inspired AI's predictions with known biological data or classical models.
   c) Discuss any novel insights or unexpected outcomes from your simulation.

5. Advantages and Limitations (200-250 words):
   a) Analyze the advantages of your quantum-inspired approach over classical methods for modeling {t['biological_process']}.
   b) Discuss the limitations of your system and potential challenges in its implementation.
   c) Suggest ways to validate the accuracy and reliability of your system's predictions.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss the potential impact of your system on the fields of quantum computing, AI, and biology.
   b) Propose how your approach could be extended to other biological processes or scientific domains.

7. Ethical Considerations (100-150 words):
   a) Identify and discuss at least two ethical considerations related to using quantum-inspired AI for biological modeling.
   b) Propose guidelines for the responsible development and use of such technology in scientific research.

8. Glossary (100-150 words):
   Provide a brief glossary of 5-7 key technical terms used in your response, ensuring clarity and demonstrating proper use of terminology from quantum computing, AI, and biology.

Ensure your response demonstrates a deep understanding of quantum computing principles, artificial intelligence techniques, and the biological process you're modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, artificial intelligence, and biology",
            "The proposed quantum-inspired AI system is innovative, plausible, and well-justified",
            "The simulation design and results analysis show a clear understanding of the biological process and how quantum concepts can enhance its modeling",
            "The response effectively integrates knowledge from multiple disciplines and proposes novel solutions",
            "The advantages, limitations, and ethical considerations are thoughtfully discussed",
            "The response is well-structured, following the specified format and word count guidelines",
            "Technical terminology is used appropriately and complex concepts are clearly explained",
            "The response demonstrates creativity and original thinking while maintaining scientific plausibility",
            "A concrete example or case study is provided in the simulation design section",
            "The glossary accurately defines key technical terms from quantum computing, AI, and biology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
