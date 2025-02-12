class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "quantum_concept": "quantum annealing",
                "climate_focus": "ocean circulation patterns"
            },
            "2": {
                "quantum_concept": "quantum Fourier transform",
                "climate_focus": "atmospheric gas concentrations"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced artificial intelligence system for advanced climate modeling and prediction, focusing on {t['climate_focus']} and utilizing the quantum computing concept of {t['quantum_concept']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum-enhanced AI system for climate modeling.
   b) Explain how classical and quantum components interact in your design.
   c) Detail how your system incorporates {t['quantum_concept']} to enhance climate predictions.

2. Quantum-Classical Integration (200-250 words):
   a) Explain how your system leverages {t['quantum_concept']} to process climate data.
   b) Describe any novel algorithms or techniques your system uses to bridge quantum and classical computations.
   c) Discuss how this integration improves modeling of {t['climate_focus']}.

3. Data Processing and Analysis (200-250 words):
   a) Describe how your system handles large-scale climate data inputs.
   b) Explain any data preprocessing techniques specific to {t['climate_focus']}.
   c) Detail how quantum processing enhances data analysis for climate prediction.

4. Prediction Capabilities (200-250 words):
   a) Describe the specific climate predictions your system can make regarding {t['climate_focus']}.
   b) Explain how these predictions improve upon current classical methods.
   c) Discuss the potential impact of these improved predictions on climate science and policy.

5. Implementation Challenges (150-200 words):
   a) Identify potential obstacles in implementing your proposed system.
   b) Suggest approaches to overcome these challenges.
   c) Discuss any hardware or software requirements for your system.

6. Ethical Considerations and Societal Impact (150-200 words):
   a) Discuss ethical implications of using quantum AI for climate modeling.
   b) Analyze potential societal impacts of more accurate climate predictions.
   c) Propose guidelines for responsible use of this technology in climate science and policy-making.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and climate science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding and creative application of the specified quantum concept to climate modeling.",
            "The system architecture is coherent, innovative, and well-explained, showing a clear integration of quantum and classical components.",
            "The approach to data processing and analysis is sophisticated and tailored to the specific climate focus.",
            "The prediction capabilities are clearly defined and show significant potential improvement over classical methods.",
            "Implementation challenges and ethical considerations are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
