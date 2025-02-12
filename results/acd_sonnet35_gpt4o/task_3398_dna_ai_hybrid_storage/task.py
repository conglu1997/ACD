import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        storage_types = ['text', 'image', 'audio', 'video']
        retrieval_methods = ['sequence-based', 'structure-based', 'chemical-based']
        ai_techniques = ['neural networks', 'reinforcement learning', 'evolutionary algorithms']
        return {
            "1": {
                "storage_type": random.choice(storage_types),
                "retrieval_method": random.choice(retrieval_methods),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "storage_type": random.choice(storage_types),
                "retrieval_method": random.choice(retrieval_methods),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hybrid DNA-AI system for ultra-dense information storage and retrieval, focusing on {t['storage_type']} data storage, {t['retrieval_method']} retrieval, and using {t['ai_technique']} for optimization and control. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your hybrid DNA-AI storage system.
   b) Explain how DNA is used for data storage and how AI is integrated into the system.
   c) Detail the encoding and decoding processes for {t['storage_type']} data.
   d) Include a diagram or pseudocode snippet illustrating a key aspect of your system.

2. DNA Storage Mechanism (250-300 words):
   a) Explain your method for encoding {t['storage_type']} data into DNA sequences.
   b) Discuss how your encoding scheme optimizes for storage density and error correction.
   c) Provide an example of how a specific data point would be encoded, including the actual DNA sequence used.
   d) Calculate the theoretical maximum storage density of your system in bits/cm³.

3. AI-Driven Retrieval and Optimization (250-300 words):
   a) Describe how your system uses {t['ai_technique']} for data retrieval and system optimization.
   b) Explain the {t['retrieval_method']} approach and how AI enhances its efficiency.
   c) Discuss any novel AI approaches you've incorporated for this specific task.
   d) Provide a specific example of how AI improves the retrieval process for {t['storage_type']} data.

4. Error Correction and Data Integrity (200-250 words):
   a) Explain the error correction mechanisms in your DNA storage system.
   b) Describe how AI is used to detect and correct errors in stored data.
   c) Discuss the system's robustness against DNA degradation and mutation.
   d) Propose a method for ensuring long-term data integrity in your system.

5. Quantitative Performance Analysis (250-300 words):
   a) Provide a detailed quantitative analysis of your system's performance, including specific metrics such as read/write speeds, error rates, and storage density.
   b) Compare these metrics to current electronic storage systems and other DNA storage technologies.
   c) Use mathematical formulas or equations where appropriate to support your analysis.
   d) Discuss how these performance metrics might scale with increasing data volumes.

6. Comparison with Existing Technology (200-250 words):
   a) Compare your proposed system to the DNA fountain technology for DNA data storage.
   b) Analyze the strengths and weaknesses of both approaches.
   c) Explain how your system improves upon or differs from DNA fountain.
   d) Discuss any potential synergies or ways to integrate the best aspects of both technologies.

7. Interdisciplinary Applications (200-250 words):
   a) Propose three potential applications of your hybrid DNA-AI storage system in fields beyond data storage.
   b) Explain how each application leverages the unique features of your system.
   c) Discuss any modifications needed to adapt your system for these applications.
   d) Analyze the potential impact of these applications on their respective fields.

8. Environmental Impact Assessment (200-250 words):
   a) Discuss the environmental impact of your proposed system, including energy consumption and resource use.
   b) Compare the environmental footprint of your system to traditional electronic storage methods.
   c) Propose strategies to minimize the environmental impact of DNA-AI hybrid storage systems.
   d) Analyze potential long-term environmental benefits or risks of widespread adoption of this technology.

9. Ethical and Security Considerations (150-200 words):
   a) Discuss potential ethical implications of storing data in biological molecules.
   b) Address security concerns related to DNA-based data storage.
   c) Propose guidelines for responsible development and use of this technology.
   d) Discuss how your system ensures data privacy and prevents unauthorized access.

10. Novel Research Proposal (200-250 words):
    a) Propose a novel research direction or experiment that could further advance the field of DNA-AI hybrid storage systems.
    b) Clearly state the research question or hypothesis.
    c) Outline the methodology for this proposed research, including any required technologies or techniques.
    d) Discuss the potential impact of this research on the field and its real-world applications.

11. Summary (100-150 words):
    Provide a concise summary of your hybrid DNA-AI storage system, highlighting its key innovations, potential impact, and future research directions.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 2300-2850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of how to encode and store {t['storage_type']} data in DNA.",
            f"The system design should effectively incorporate {t['ai_technique']} for optimization and control of the DNA storage system.",
            f"The retrieval process should clearly explain how the {t['retrieval_method']} approach is implemented and enhanced by AI.",
            "The response should show interdisciplinary knowledge integration across molecular biology, information theory, and artificial intelligence.",
            "The quantitative performance analysis should include specific metrics and comparisons to existing technologies.",
            "The comparison with DNA fountain technology should be thorough and insightful.",
            "The interdisciplinary applications should be innovative and well-reasoned.",
            "The environmental impact assessment should be comprehensive and balanced.",
            "The novel research proposal should be innovative and well-reasoned.",
            "The summary should effectively synthesize the key aspects of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
