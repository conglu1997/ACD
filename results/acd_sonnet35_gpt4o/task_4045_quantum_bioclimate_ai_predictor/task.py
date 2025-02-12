class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ecosystem": "Great Barrier Reef",
                "climate_phenomenon": "El Niño",
                "biological_process": "coral bleaching",
                "quantum_concept": "superposition",
                "ai_technique": "quantum neural networks"
            },
            "2": {
                "ecosystem": "Amazon Rainforest",
                "climate_phenomenon": "drought cycles",
                "biological_process": "carbon sequestration",
                "quantum_concept": "entanglement",
                "ai_technique": "quantum-inspired evolutionary algorithms"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for modeling and predicting complex climate phenomena and their impacts on biological systems. Apply your system to the following scenario:

Ecosystem: {t['ecosystem']}
Climate Phenomenon: {t['climate_phenomenon']}
Biological Process: {t['biological_process']}
Quantum Concept to Incorporate: {t['quantum_concept']}
AI Technique to Use: {t['ai_technique']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired AI system for climate and biological modeling.
   b) Explain how you incorporate the specified quantum concept into your system design.
   c) Detail how the chosen AI technique is implemented and integrated with the quantum-inspired components.
   d) Discuss how your system interfaces with climate data and biological process models.
   e) Provide a high-level diagram of your system architecture (described in words).

2. Climate-Biological Modeling Mechanism (250-300 words):
   a) Explain how your system models the specified climate phenomenon and its impact on the biological process.
   b) Describe how the quantum-inspired approach enhances the modeling capabilities compared to classical methods.
   c) Detail the data inputs, processing steps, and outputs of your system.
   d) Discuss how your system handles the complexity and uncertainty inherent in climate and biological systems.

3. Prediction and Analysis Capabilities (200-250 words):
   a) Explain the types of predictions and analyses your system can generate.
   b) Describe how the system quantifies and communicates uncertainty in its predictions.
   c) Discuss the temporal and spatial scales at which your system operates.
   d) Provide an example of a specific insight or prediction your system might generate for the given scenario.

4. Validation and Refinement Process (200-250 words):
   a) Propose a method for validating the accuracy and reliability of your system's predictions.
   b) Explain how your system learns and improves from new data and feedback.
   c) Discuss potential challenges in validating predictions for complex, long-term ecological processes.
   d) Describe how your system could be refined or expanded to improve its predictive capabilities.

5. Interdisciplinary Implications (200-250 words):
   a) Discuss how your quantum-inspired AI approach might influence climate science and ecology research methodologies.
   b) Explain potential applications of your system in climate policy, conservation efforts, or ecosystem management.
   c) Consider how this technology might bridge gaps between quantum computing, artificial intelligence, and environmental sciences.
   d) Propose a novel research question that your system might help address in the future.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns or risks associated with using your system for climate and ecosystem predictions.
   b) Discuss the limitations of your approach and potential consequences of relying too heavily on AI-generated predictions.
   c) Propose guidelines for the responsible development and use of quantum-inspired AI in climate and ecological modeling.

Ensure your response demonstrates a deep understanding of quantum computing concepts, climate science, ecology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex ideas. Be innovative in your approach while maintaining scientific plausibility and practical considerations.

Strike a balance between technical depth and clarity of explanation. Your response should be comprehensible to an interdisciplinary audience while still showcasing advanced knowledge in the relevant fields.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1300-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing concepts, climate science, ecology, and artificial intelligence.",
            "The system architecture effectively incorporates the specified quantum concept and AI technique, with a clear explanation of how they enhance the modeling process.",
            "The climate-biological modeling mechanism clearly explains how the system models the given climate phenomenon and its impact on the biological process, including handling of complexity and uncertainty.",
            "The prediction and analysis capabilities are well-defined, relevant to the given scenario, and include a specific example of an insight or prediction.",
            "The validation and refinement process is thorough, addresses the challenges of predicting complex ecological processes, and includes a clear method for improvement.",
            "The interdisciplinary implications are insightful, propose novel connections between fields, and include a specific research question for future exploration.",
            "Ethical considerations and limitations are thoughtfully discussed with proposed guidelines for responsible use and acknowledgment of potential risks.",
            "The response strikes a balance between technical depth and clarity of explanation, making it accessible to an interdisciplinary audience.",
            "The response is well-structured, following the specified format and word count guidelines (1300-1700 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
