import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_process': 'photosynthesis',
                'application_domain': 'sustainable energy production'
            },
            {
                'biological_process': 'DNA repair',
                'application_domain': 'personalized medicine'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Recent advancements in quantum biology have revealed that quantum effects play crucial roles in various biological processes. This discovery opens up new possibilities for developing quantum-inspired AI systems that can model and leverage these processes for practical applications. Your task is to design such a system and analyze its implications.

Design a quantum-inspired artificial intelligence system that models the biological process of {t['biological_process']} and analyze its ethical implications for {t['application_domain']}. Your response should include the following sections:

1. Quantum-Bio-AI System Design (300-350 words):
   a) Describe the key components of your quantum-inspired AI system for modeling {t['biological_process']}.
   b) Explain how quantum principles are incorporated into your AI model.
   c) Detail how your system captures and processes the complexity of {t['biological_process']}.
   d) Discuss any novel algorithms or data structures used in your system.
   e) Provide a high-level schematic or pseudocode of a key component in your system.

2. Quantum-Biological Interface (250-300 words):
   a) Explain how quantum effects in {t['biological_process']} are represented in your AI model.
   b) Describe how your system handles the transition between quantum and classical regimes in biological processes.
   c) Discuss any assumptions or simplifications made in your model and their potential impacts.
   d) Provide a specific example of how a quantum effect in {t['biological_process']} is modeled in your system.

3. AI Learning and Adaptation (200-250 words):
   a) Describe how your AI system learns and adapts its quantum-biological model.
   b) Explain how the system handles uncertainty and incomplete information.
   c) Discuss the potential for your system to generate new hypotheses or insights about {t['biological_process']}.
   d) Provide an example of a potential new insight your system might generate.

4. Application to {t['application_domain']} (250-300 words):
   a) Explain how your Quantum-Bio-AI system could be applied to {t['application_domain']}.
   b) Describe potential benefits and improvements over current approaches.
   c) Discuss any technical or practical challenges in implementing your system for this application.
   d) Provide a concrete scenario demonstrating the application of your system in {t['application_domain']}.

5. Ethical Implications (250-300 words):
   a) Analyze the ethical considerations of using your Quantum-Bio-AI system in {t['application_domain']}.
   b) Discuss potential societal impacts, both positive and negative.
   c) Address issues of data privacy, bias, and accountability in your system.
   d) Propose guidelines for the ethical development and use of Quantum-Bio-AI systems.
   e) Provide an example of a potential ethical dilemma arising from the use of your system and how it might be addressed.

6. Future Directions and Societal Impact (150-200 words):
   a) Suggest potential extensions or modifications to your system for future research.
   b) Discuss how widespread adoption of Quantum-Bio-AI systems might impact society and scientific research.
   c) Propose a strategy for fostering interdisciplinary collaboration in this field.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, artificial intelligence, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use numbered subsections (e.g., 1a, 1b, 1c) to organize your thoughts. Your total response should be between 1400-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system design effectively integrates quantum principles, AI, and the biological process of {t['biological_process']}, including a high-level schematic or pseudocode, demonstrating innovative application of quantum concepts.",
            "The quantum-biological interface is well-explained, addresses the transition between quantum and classical regimes, and provides a specific, scientifically plausible example.",
            "The AI learning and adaptation process is clearly described, accounts for uncertainty, and includes an example of a potential new insight that demonstrates deep understanding of both quantum mechanics and biology.",
            f"The application to {t['application_domain']} is well-reasoned, discusses benefits and challenges, and includes a concrete, feasible scenario that showcases the unique advantages of the quantum-bio-AI approach.",
            "The ethical implications are thoroughly analyzed, addressing important issues and providing an example of a potential ethical dilemma and its resolution, demonstrating foresight and consideration of complex societal impacts.",
            "The response demonstrates a deep understanding of quantum biology, AI, and complex systems, using appropriate technical terminology and explaining complex concepts clearly.",
            "The proposed future directions and societal impact analysis show insightful interdisciplinary thinking and potential for significant scientific advancement.",
            "All six required sections are present, adequately addressed, and formatted correctly with numbered subsections.",
            "The response falls within the specified word count range of 1400-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
