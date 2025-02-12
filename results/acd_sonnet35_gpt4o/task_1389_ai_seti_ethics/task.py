import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "scenario": "Deep space signal detection",
                "ai_focus": "Pattern recognition in radio signals",
                "ethical_concern": "Unintended disclosure of Earth's location"
            },
            {
                "scenario": "Exoplanet atmospheric analysis",
                "ai_focus": "Identifying potential biosignatures",
                "ethical_concern": "Misinterpretation leading to unnecessary resource allocation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for detecting and communicating with extraterrestrial intelligence, focusing on the scenario of {t['scenario']}. Your AI system should emphasize {t['ai_focus']}. Then, analyze its ethical implications and potential consequences, paying particular attention to the ethical concern of {t['ethical_concern']}. Your response should include:

1. AI System Design (250-300 words):
   a) Describe the key components and functionality of your AI system.
   b) Explain how it addresses the specific scenario and AI focus.
   c) Discuss any novel algorithms or approaches used in your system.
   d) Ensure your design is scientifically plausible and grounded in current technological capabilities.

2. Scientific Foundation (200-250 words):
   a) Explain the scientific principles underlying your AI system's approach.
   b) Discuss how your system integrates knowledge from astrobiology and computer science.
   c) Address any scientific challenges or uncertainties in your approach.

3. Ethical Analysis (200-250 words):
   a) Analyze the ethical implications of deploying your AI system, focusing on the specified ethical concern.
   b) Discuss potential unintended consequences of your system's operation.
   c) Propose guidelines for responsible development and use of your AI system.

4. Communication Protocol (150-200 words):
   a) Describe how your AI system would attempt to communicate with detected extraterrestrial intelligence.
   b) Explain the rationale behind your chosen communication method.
   c) Discuss potential challenges in cross-species communication and how your system addresses them.

5. Societal Impact (150-200 words):
   a) Analyze the potential impact of your AI system on human society and scientific understanding.
   b) Discuss how the use of AI in SETI might change our approach to space exploration and our place in the universe.
   c) Consider potential risks and benefits to humanity.

Ensure your response demonstrates a deep understanding of astrobiology, artificial intelligence, and philosophical concepts related to extraterrestrial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 950-1200 words, adhering to the word count guidelines for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of astrobiology, artificial intelligence, and philosophical concepts related to extraterrestrial intelligence.",
            "The AI system design is creative, scientifically plausible, and addresses the specific scenario and AI focus.",
            "The ethical analysis is thorough and considers multiple perspectives, including the specified ethical concern.",
            "The communication protocol is well-reasoned and considers the challenges of cross-species communication.",
            "The societal impact analysis is thoughtful and considers both potential risks and benefits.",
            "The response is well-structured, clear, and within the specified word limit.",
            "All parts of the task (AI System Design, Scientific Foundation, Ethical Analysis, Communication Protocol, and Societal Impact) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
