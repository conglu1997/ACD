import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_biology_problems = [
            {
                "quantum_principle": "Quantum tunneling",
                "biological_process": "Enzyme catalysis",
                "research_question": "How does quantum tunneling contribute to the efficiency of enzyme-catalyzed reactions?"
            },
            {
                "quantum_principle": "Quantum coherence",
                "biological_process": "Photosynthesis",
                "research_question": "Can quantum coherence explain the high efficiency of energy transfer in photosynthetic complexes?"
            }
        ]
        return {
            "1": random.choice(quantum_biology_problems),
            "2": random.choice(quantum_biology_problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Apply the quantum mechanical principle of {t['quantum_principle']} to the biological process of {t['biological_process']} to address the following research question: {t['research_question']}\n\n" + \
               "Your response should include:\n\n" + \
               "1. Theoretical Framework (250-300 words):\n" + \
               "   a) Explain the relevant quantum mechanical principle and its potential role in the biological process.\n" + \
               "   b) Describe the current understanding of the biological process and its challenges.\n" + \
               "   c) Propose a theoretical model that integrates the quantum principle into the biological process.\n\n" + \
               "2. Experimental Design (250-300 words):\n" + \
               "   a) Propose a detailed experimental setup to test your theoretical model.\n" + \
               "   b) Describe the methodology, including any specialized equipment or techniques required.\n" + \
               "   c) Explain how your experiment would differentiate between quantum and classical effects.\n" + \
               "   d) Discuss potential challenges and limitations of your experimental design.\n\n" + \
               "3. Predictions and Implications (200-250 words):\n" + \
               "   a) Describe the expected results if your model is correct.\n" + \
               "   b) Explain how these results would advance our understanding of quantum biology.\n" + \
               "   c) Discuss potential applications or implications for fields such as medicine, biotechnology, or energy.\n\n" + \
               "4. Interdisciplinary Connections (150-200 words):\n" + \
               "   a) Explore how your proposed quantum biological model might inform or be informed by other scientific disciplines.\n" + \
               "   b) Suggest potential collaborations or research directions that could further develop this area of study.\n\n" + \
               "5. Ethical Considerations (100-150 words):\n" + \
               "   a) Discuss any ethical implications of your research or its potential applications.\n" + \
               "   b) Propose guidelines for responsible development and use of quantum biology technologies.\n\n" + \
               "Ensure your response demonstrates a deep understanding of both quantum mechanics and biological systems. Be creative in your approach while maintaining scientific accuracy and plausibility. Use appropriate scientific terminology and provide clear explanations for complex concepts.\n\n" + \
               "Format your response with clear headings for each section. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the quantum mechanical principle and its potential role in the biological process",
            "The proposed theoretical model effectively integrates the quantum principle into the biological process",
            "The experimental design is well-thought-out, feasible, and addresses potential challenges",
            "The predictions and implications are logically derived and scientifically plausible",
            "The interdisciplinary connections and ethical considerations are thoughtfully addressed",
            "The overall response shows creativity and innovation in applying quantum mechanics to biology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
