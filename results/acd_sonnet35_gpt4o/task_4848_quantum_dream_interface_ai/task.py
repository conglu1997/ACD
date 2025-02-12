import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling"
        ]
        dream_aspects = [
            "Lucid dreaming",
            "Emotional regulation",
            "Memory consolidation"
        ]
        applications = [
            "Therapy for PTSD",
            "Enhanced learning during sleep",
            "Creativity boosting"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "quantum_principle": random.choice(quantum_principles),
                "dream_aspect": random.choice(dream_aspects),
                "application": random.choice(applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that utilizes quantum computing principles to interface with and manipulate human dreams, then analyze its potential applications and ethical implications. Your system should focus on the quantum principle of {t['quantum_principle']}, address the dream aspect of {t['dream_aspect']}, and consider the potential application of {t['application']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum dream interface AI system.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your system.
   c) Describe how your system interfaces with and influences the dream aspect of {t['dream_aspect']}.
   d) Explain how these elements come together to enable dream manipulation.
   e) Include a simple diagram or schematic representation of your system (using ASCII art or a clear textual description).

2. Dream Interaction Mechanism (250-300 words):
   a) Explain the theoretical basis for how your system interacts with human dreams.
   b) Describe the process of initiating, maintaining, and terminating a dream interaction session.
   c) Discuss how your quantum approach might offer advantages over classical methods for dream interaction.

3. AI Dream Analysis and Manipulation (200-250 words):
   a) Describe how your AI system analyzes dream content and structures.
   b) Explain the methods your system uses to influence or manipulate dreams, focusing on {t['dream_aspect']}.
   c) Discuss any limitations or potential risks in your system's dream manipulation capabilities.

4. Potential Applications (200-250 words):
   a) Elaborate on how your system could be used for {t['application']}.
   b) Propose another potential application of your quantum dream interface AI.
   c) For each application, explain the potential benefits and any challenges in implementation.

5. Ethical Implications (250-300 words):
   a) Identify three potential ethical concerns raised by your quantum dream interface AI system.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, deontology, virtue ethics).
   c) Propose guidelines or safeguards to address these ethical issues.
   d) Discuss the broader societal implications of using such advanced systems for dream manipulation.

6. Future Research Directions (150-200 words):
   a) Suggest two areas for further research to enhance or expand your quantum dream interface AI system.
   b) Explain how these research directions could address current limitations or open up new possibilities.
   c) Discuss potential interdisciplinary collaborations that could drive innovation in this field.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words, not including the system diagram. The system diagram should be included as a separate, clearly labeled section after the main text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections and subsections",
            "The system architecture is well-described and incorporates the specified quantum principle and dream aspect",
            "The dream interaction mechanism and AI analysis/manipulation processes are clearly explained",
            "The potential applications, including the specified one, are thoroughly discussed",
            "Ethical implications are thoughtfully analyzed and addressed",
            "The response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence",
            "The proposed ideas are creative and speculative while maintaining scientific plausibility",
            "The response is well-structured and within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
