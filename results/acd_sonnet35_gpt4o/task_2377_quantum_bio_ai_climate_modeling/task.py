import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum coherence",
            "quantum entanglement",
            "quantum tunneling"
        ]
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "DNA mutation"
        ]
        climate_impacts = [
            "ocean acidification",
            "extreme weather events",
            "biodiversity loss"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "climate_impact": random.choice(climate_impacts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_process": random.choice(biological_processes),
                "climate_impact": random.choice(climate_impacts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that leverages quantum biological principles to model and predict climate change impacts on ecosystems. Your system should focus on the quantum principle of {t['quantum_principle']}, primarily applied to the biological process of {t['biological_process']}, and be used to predict and analyze the climate impact of {t['climate_impact']}.

Your response should include the following sections:

1. Quantum-Biological Framework (300-350 words):
   a) Explain the chosen quantum principle and its relevance to the specified biological process.
   b) Describe current scientific understanding of how this quantum effect influences the biological process.
   c) Discuss potential links between this quantum-biological interaction and the specified climate impact.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for modeling quantum-biological processes.
   b) Explain how your system incorporates quantum computing or quantum-inspired algorithms.
   c) Describe how the AI integrates data from various sources (e.g., quantum biology experiments, climate models, ecological surveys).
   d) Discuss any novel features or innovations in your AI design for this specific application.

3. Climate Impact Modeling (250-300 words):
   a) Explain how your AI system models the specified climate impact using quantum-biological insights.
   b) Describe the types of predictions or analyses your system can generate.
   c) Discuss how your approach differs from traditional climate modeling techniques.
   d) Provide a hypothetical example of a specific prediction or insight your system might generate.

4. Data Requirements and Challenges (200-250 words):
   a) Specify the types of data your AI system would require for training and operation.
   b) Discuss challenges in obtaining or generating relevant quantum biological and climate data.
   c) Propose innovative solutions to address these data-related challenges.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Identify potential ethical issues in using quantum-biological AI for climate prediction.
   b) Discuss the potential societal impacts of your system's predictions and how they should be communicated.
   c) Propose guidelines for responsible development and use of such advanced climate modeling systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your system for future research.
   b) Discuss how your approach could be applied to other areas of environmental science or biology.

7. Conclusion (100-150 words):
   Summarize the key aspects of your quantum-biological AI system for climate modeling, highlighting its potential impact and importance in addressing climate change challenges.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, artificial intelligence, and climate science. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering strictly to the word limits provided. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and its application to {t['biological_process']}.",
            f"The AI system design effectively incorporates quantum or quantum-inspired algorithms to model {t['climate_impact']}.",
            "The approach shows innovative integration of quantum biology, AI, and climate science.",
            "Ethical considerations and societal impacts are thoroughly addressed.",
            "The response is well-structured, comprehensive, and within the specified word count.",
            "The conclusion effectively summarizes the key aspects of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
