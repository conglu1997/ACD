import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_component": "topological quantum circuits with 50 qubits and 1 microsecond coherence time",
                "biological_component": "engineered protein networks with 100 synthetic proteins",
                "ai_component": "neuromorphic computing architecture with 1 million artificial neurons",
                "application_domain": "personalized medicine for rare genetic disorders",
                "ethical_focus": "privacy and ownership of genetic data"
            },
            "2": {
                "quantum_component": "quantum annealing processors with 2000 qubits and 100 microsecond annealing time",
                "biological_component": "synthetic gene circuits with 20 engineered genes",
                "ai_component": "federated learning systems with 1000 distributed nodes",
                "application_domain": "environmental remediation of heavy metal contamination",
                "ethical_focus": "ecological impact and biosecurity of engineered organisms"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for a symbiotic system integrating quantum computing, synthetic biology, and artificial intelligence, then analyze its potential applications and ethical implications. Your task focuses on the following specific scenario:

Quantum component: {t['quantum_component']}
Biological component: {t['biological_component']}
AI component: {t['ai_component']}
Application domain: {t['application_domain']}
Ethical focus: {t['ethical_focus']}

Your response should include the following sections:

1. Symbiotic System Framework (300-350 words):
   a) Describe the overall architecture of your quantum-bio-AI symbiotic system.
   b) Explain how the quantum, biological, and AI components interact and complement each other.
   c) Discuss the novel properties or capabilities that emerge from this integration.
   d) Provide a visual representation (using ASCII art or Unicode characters) of your system's architecture, clearly showing how the quantum, biological, and AI components are integrated.

2. Quantum-Bio-AI Integration (250-300 words):
   a) Detail how the specified quantum component enhances or interfaces with the biological and AI elements.
   b) Explain how the biological component is engineered to work with the quantum and AI systems.
   c) Describe how the AI component optimizes or controls the quantum and biological processes.
   d) Discuss any challenges in integrating these diverse technologies and how you address them.

3. Application Analysis (200-250 words):
   a) Analyze how your symbiotic system could be applied in the specified application domain.
   b) Describe the potential benefits and advantages over current technologies in this field.
   c) Discuss any limitations or potential risks associated with deploying your system in this domain.
   d) Propose a specific use case or experiment to demonstrate the system's capabilities.

4. Ethical Implications (200-250 words):
   a) Examine the ethical considerations related to the specified ethical focus.
   b) Discuss potential societal impacts of your symbiotic system, both positive and negative.
   c) Propose guidelines or safeguards to address ethical concerns in the development and deployment of such systems.
   d) Consider any long-term implications for human society and the nature of intelligence.

5. Future Directions and Challenges (150-200 words):
   a) Suggest potential improvements or extensions to your symbiotic system.
   b) Discuss how advancements in quantum computing, synthetic biology, or AI might enhance your system.
   c) Identify key research challenges that need to be addressed to realize such a system.
   d) Propose a novel research direction that arises from this integration of technologies.

Ensure your response demonstrates a deep understanding of quantum computing, synthetic biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative and speculative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Symbiotic System Framework') on a new line, followed by your response for that section. Use subheadings (a, b, c, d) within each section as outlined above. Your total response should be between 1100-1350 words.

NOTE: Do not use or reference any external resources. Your response should be based solely on your own knowledge and the information provided in this prompt."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all five required sections with appropriate content and word counts.",
            "The symbiotic system framework should coherently integrate the specified quantum, biological, and AI components, explicitly addressing their given parameters (e.g., number of qubits, coherence time, number of synthetic proteins, number of artificial neurons).",
            "The quantum-bio-AI integration should clearly explain how the three components interact and complement each other, addressing potential challenges related to the given specifications.",
            "The application analysis should provide a convincing argument for the system's use in the specified domain, including a concrete use case or experiment that leverages the given components and their parameters.",
            "The ethical implications section should thoroughly examine the specified ethical focus, proposing meaningful guidelines or safeguards that address the unique challenges of the given scenario.",
            "The response should demonstrate a deep understanding of quantum computing, synthetic biology, and artificial intelligence, using appropriate technical terminology and accurately referring to the given specifications throughout the answer.",
            "The proposed framework should be innovative and speculative while maintaining scientific plausibility and logical consistency with the given parameters.",
            "The response must include a visual representation of the system's architecture using ASCII art or Unicode characters that accurately reflects the given components and their integration.",
            "The future directions and challenges section should identify meaningful research challenges and propose a novel research direction that builds upon the specified quantum, biological, and AI components.",
            "The response should follow the specified format, including clear headings, subheadings, and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
