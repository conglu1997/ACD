import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            'quantum coherence',
            'quantum entanglement',
            'quantum tunneling'
        ]
        applications = [
            'drug discovery',
            'climate modeling',
            'financial optimization'
        ]
        tasks = {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "application": random.choice(applications)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "application": random.choice(applications)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired quantum computing system based on the quantum effect of {t['quantum_effect']} observed in photosynthesis. Then, analyze its potential application in {t['application']}. Your response should include the following sections:

1. Quantum Biology Foundation (200-250 words):
   a) Explain the role of {t['quantum_effect']} in photosynthesis.
   b) Describe how this quantum effect enhances the efficiency of photosynthesis.
   c) Discuss current scientific understanding and any debates surrounding this phenomenon.

2. Bio-inspired Quantum Computing System Design (300-350 words):
   a) Propose a quantum computing architecture inspired by the {t['quantum_effect']} in photosynthesis.
   b) Explain how your system mimics or utilizes this quantum effect.
   c) Describe the key components and processes of your quantum computing system.
   d) Discuss any novel techniques or approaches used in your design.
   e) Include a conceptual diagram or detailed description of your system architecture.
      If using ASCII art, ensure it is at least 10 lines long and uses a variety of characters.
      If using a text description, provide a detailed, step-by-step explanation of the system components and their interactions.

3. Application Analysis: {t['application']} (250-300 words):
   a) Explain how your bio-inspired quantum computing system could be applied to {t['application']}.
   b) Describe the potential advantages of your system over classical computing approaches for this application.
   c) Discuss any challenges or limitations in implementing your system for this purpose.
   d) Propose a specific problem within {t['application']} that your system could address, and outline a solution approach.

4. Comparative Analysis (200-250 words):
   a) Compare your bio-inspired quantum computing approach to traditional quantum computing methods.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose a hypothetical experiment to evaluate the effectiveness of your system compared to existing quantum technologies.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the potential ethical considerations of developing and using bio-inspired quantum computing systems.
   b) Analyze the possible societal impacts of applying your system to {t['application']}.
   c) Propose guidelines for responsible development and use of such technology.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research or experimentation related to your bio-inspired quantum computing system.
   b) Discuss how advancements in quantum biology or other relevant fields might enhance or modify your design in the future.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and computer science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing practical considerations.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Quantum Biology Foundation:') on a new line, followed by your response for that section.

Your total response should be between 1250-1550 words, not including the headings and the conceptual diagram or detailed description in section 2."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all required sections with appropriate word counts, totaling between 1250-1550 words (excluding headings and diagrams).",
            f"The explanation of {t['quantum_effect']} in photosynthesis is accurate, clear, and demonstrates understanding of current scientific debates.",
            "The bio-inspired quantum computing system design is innovative, well-explained, and includes a detailed conceptual diagram or description.",
            f"The application analysis for {t['application']} demonstrates a thorough understanding of both the quantum computing system and the specific application, including a proposed problem and solution approach.",
            "The comparative analysis shows critical thinking and a good understanding of both bio-inspired and traditional quantum computing technologies, including a well-designed hypothetical experiment.",
            "The ethical and societal implications are thoughtfully considered, with specific guidelines proposed for responsible development and use.",
            "The future research directions are relevant, well-reasoned, and demonstrate foresight in the field of bio-inspired quantum computing.",
            "The overall response demonstrates interdisciplinary knowledge integration, creative problem-solving, and maintains scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
