import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['superposition', 'entanglement', 'tunneling', 'coherence']
        biological_processes = ['photosynthesis', 'magnetoreception', 'enzyme catalysis', 'olfaction']
        planetary_conditions = ['atmospheric composition', 'magnetic field strength', 'radiation levels', 'temperature range']
        
        tasks = []
        for i in range(2):
            qp = random.choice(quantum_principles)
            bp = random.choice(biological_processes)
            pc = random.choice(planetary_conditions)
            tasks.append({
                "quantum_principle": qp,
                "biological_process": bp,
                "planetary_condition": pc
            })
            quantum_principles.remove(qp)
            biological_processes.remove(bp)
            planetary_conditions.remove(pc)
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired system for detecting and analyzing potential biosignatures on exoplanets, integrating principles from quantum biology, astrobiology, and information theory. Your system should focus on the quantum principle of {t['quantum_principle']}, the biological process of {t['biological_process']}, and the planetary condition of {t['planetary_condition']}. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain how the specified quantum principle might influence the chosen biological process.
   b) Discuss how this quantum-biological interaction could manifest as a detectable biosignature.
   c) Describe how the given planetary condition might affect this quantum-biological process.

2. Detection System Design (250-300 words):
   a) Propose a detailed architecture for your quantum-inspired biosignature detection system.
   b) Explain how each component integrates principles from quantum mechanics, biology, and information theory.
   c) Describe the input data your system would require and the expected output.
   d) Include a high-level diagram or pseudocode of your system's architecture and processing flow.

3. Data Analysis and Interpretation (150-200 words):
   a) Explain how your system would process and analyze the detected signals.
   b) Describe how it would distinguish between potential biosignatures and abiotic phenomena.
   c) Discuss how your system would quantify and communicate the uncertainty in its detections.

4. Challenges and Limitations (150-200 words):
   a) Identify at least three major challenges in implementing your proposed system.
   b) Discuss any assumptions or simplifications made in your design.
   c) Propose potential solutions or areas for future research to address these challenges.

5. Implications and Applications (150-200 words):
   a) Discuss how your system could advance our understanding of quantum biology and astrobiology.
   b) Explore potential applications of your system beyond exoplanet biosignature detection.
   c) Consider the implications of your approach for the search for extraterrestrial life and our understanding of life's origins.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the quantum principle of {t['quantum_principle']}, the biological process of {t['biological_process']}, and the planetary condition of {t['planetary_condition']} in the system design.",
            "The proposed detection system architecture is clearly described and incorporates principles from quantum mechanics, biology, and information theory.",
            "The data analysis and interpretation section explains how the system would process signals and distinguish biosignatures from abiotic phenomena.",
            "At least three major challenges in implementing the system are identified and discussed.",
            "The implications and potential applications of the system are thoroughly explored.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The overall response is well-structured, clear, and within the specified word count (900-1150 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
