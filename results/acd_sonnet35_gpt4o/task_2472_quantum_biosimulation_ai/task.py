import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_process": "Protein Folding",
                "quantum_principle": "Quantum Annealing",
                "ai_technique": "Reinforcement Learning"
            },
            {
                "biological_process": "Enzyme Catalysis",
                "quantum_principle": "Quantum Entanglement",
                "ai_technique": "Generative Adversarial Networks"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates the biological process of {t['biological_process']} using the quantum principle of {t['quantum_principle']}, and employs {t['ai_technique']} for optimizing drug discovery. Your response should include the following sections:

1. Quantum-Biological Interface (200-250 words):
   a) Explain how your system models {t['biological_process']} using quantum states and operations.
   b) Describe how {t['quantum_principle']} is utilized to enhance simulation accuracy or efficiency.
   c) Include a simplified quantum circuit diagram or pseudocode for a key component of your system (described in text).

2. AI-Driven Optimization (150-200 words):
   a) Detail how {t['ai_technique']} is integrated with the quantum simulation for drug discovery.
   b) Explain the optimization objectives and constraints in the context of {t['biological_process']}.
   c) Describe how the AI component interacts with and interprets the quantum simulation results.

3. System Architecture (150-200 words):
   a) Provide a high-level overview of your system's architecture, including quantum and classical components.
   b) Explain how data flows between the quantum simulation, AI optimization, and classical analysis parts.

4. Error Analysis and Mitigation (100-150 words):
   a) Identify potential sources of error in your quantum-biological interface.
   b) Propose at least two specific error mitigation strategies for your system.

5. Performance Analysis (100-150 words):
   a) Analyze the theoretical speedup or accuracy improvements offered by your quantum approach compared to classical methods.
   b) Propose a specific benchmark or experiment to validate the performance of your system.

6. Limitations and Challenges (100-150 words):
   a) Discuss at least three potential limitations or challenges in implementing your system on current or near-term quantum hardware.
   b) For each limitation, suggest a possible approach to address or mitigate it.

7. Case Study (150-200 words):
   Provide a specific example of how your system would be applied to discover a drug targeting a known protein involved in a disease process. Include:
   a) The target protein and associated disease.
   b) How your quantum-AI system would approach the drug discovery process for this target.
   c) Potential advantages of your approach compared to traditional drug discovery methods.

Ensure your response demonstrates a deep understanding of quantum computing, molecular biology, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1300 words. Include the word count for each section in parentheses at the end of the section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the chosen quantum principle and its application to the biological process.",
            "The AI-driven optimization approach is well-integrated with the quantum simulation and appropriate for drug discovery.",
            "The system architecture and data flow are logically explained.",
            "Error analysis and mitigation strategies are specific and relevant to the proposed system.",
            "The performance analysis includes a realistic assessment of the system's potential advantages and a specific benchmark proposal.",
            "Limitations and challenges are thoughtfully discussed with potential mitigation approaches.",
            "The case study provides a concrete and relevant example of the system's application in drug discovery.",
            "The response includes a simplified quantum circuit diagram or pseudocode as requested.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        return sum([0.11 if eval_with_llm_judge(instructions, submission, [criterion]) else 0 for criterion in criteria])
