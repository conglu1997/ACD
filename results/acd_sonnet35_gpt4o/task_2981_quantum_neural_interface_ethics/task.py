import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            "memory enhancement",
            "direct brain-to-brain communication",
            "treatment of neurological disorders",
            "human-AI symbiosis"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum error correction"
        ]
        return {
            "1": {
                "application": random.choice(applications),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "application": random.choice(applications),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural interface system leveraging the quantum principle of {t['quantum_principle']} for the application of {t['application']}. Then, analyze its potential benefits, risks, and ethical implications. Provide your response in the following format:

1. System Design (300-350 words):
   a) Describe the key components and functioning of your quantum-inspired neural interface.
   b) Explain how it incorporates the specified quantum principle.
   c) Detail how the system interacts with the human brain for the given application.
   d) Include a high-level diagram or pseudocode representing the system's architecture (describe it textually).

2. Application Analysis (250-300 words):
   a) Explain how your system could be used for the specified application.
   b) Discuss potential benefits and advantages over classical approaches.
   c) Analyze possible limitations or challenges in implementing the system.
   d) Propose a hypothetical experiment to test the efficacy of your system.

3. Quantum-Neural Integration (200-250 words):
   a) Discuss how quantum effects might influence or enhance neural processes.
   b) Explain any novel computational or cognitive capabilities enabled by this integration.
   c) Address potential challenges in maintaining quantum effects in a biological environment.

4. Ethical Implications (250-300 words):
   a) Identify at least three ethical concerns raised by your quantum-inspired neural interface.
   b) Analyze potential societal impacts, both positive and negative.
   c) Discuss issues of privacy, consent, and potential for misuse.
   d) Propose guidelines for responsible development and use of this technology.

5. Future Directions (150-200 words):
   a) Suggest two potential research directions to advance this field.
   b) Discuss how these directions could address current limitations or ethical concerns.
   c) Speculate on long-term implications for human cognition and society.

Ensure your response demonstrates a deep understanding of quantum computing principles, neuroscience, and ethics. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Your total response should be between 1150-1400 words. Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle and its potential application in neural interfaces.",
            "The system design is innovative, scientifically plausible, and clearly explained.",
            "The application analysis thoroughly explores benefits, limitations, and potential experiments.",
            "The quantum-neural integration discussion shows insight into both quantum and neural processes.",
            "Ethical implications are comprehensively analyzed, covering multiple perspectives.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The language used is technically accurate and appropriate for the interdisciplinary nature of the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
