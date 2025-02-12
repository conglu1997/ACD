import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        nlp_techniques = [
            {
                "technique": "Anchoring",
                "description": "Creating a consistent response to a specific stimulus",
                "application": "Enhancing AI's contextual understanding"
            },
            {
                "technique": "Reframing",
                "description": "Changing the conceptual viewpoint of a situation",
                "application": "Improving AI's ability to provide alternative perspectives"
            }
        ]
        return {
            "1": random.choice(nlp_techniques),
            "2": random.choice(nlp_techniques)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that implements the neuro-linguistic programming technique of {t['technique']} to enhance human-AI communication, and analyze its potential impacts on cognition and language use. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how it incorporates the NLP technique of {t['technique']} ({t['description']}).
   c) Detail how your system applies this technique to {t['application']}.
   d) Discuss any novel algorithms or data structures required for your implementation.
   e) Provide a high-level pseudocode or flowchart of your system's main algorithm (describe it textually).

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying the chosen NLP technique.
   b) Discuss how your AI system models or mimics these neural processes.
   c) Analyze potential limitations in translating human neurolinguistic processes to AI systems.

3. Linguistic Analysis (200-250 words):
   a) Describe how your system might influence or alter language patterns in human-AI communication.
   b) Discuss potential impacts on semantic understanding and pragmatic use of language.
   c) Analyze how this technique might affect cross-cultural or multilingual communication.

4. Cognitive Impact Assessment (250-300 words):
   a) Predict potential cognitive effects on humans interacting with your AI system.
   b) Discuss how prolonged use of this system might influence human thought processes or decision-making.
   c) Analyze potential benefits and risks to human cognitive development.
   d) Propose a method to empirically measure these cognitive impacts.

5. Ethical Considerations (150-200 words):
   a) Identify at least three ethical concerns raised by the implementation of your system.
   b) Discuss potential misuse or unintended consequences of this technology.
   c) Propose guidelines for responsible development and use of NLP-enhanced AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your system.
   b) Propose a specific research question or hypothesis that emerges from your design.
   c) Discuss how insights from your system might contribute to our understanding of human cognition or AI development.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1250-1550 words.

Format your response with clear headings for each section, and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system that accurately incorporates the NLP technique of {t['technique']}.",
            "The system design is creative, plausible, and demonstrates a deep understanding of AI architecture and algorithms.",
            "The neuroscientific basis is accurately explained and well-connected to the AI implementation.",
            "The linguistic analysis demonstrates a thorough understanding of language patterns and potential impacts on communication.",
            "The cognitive impact assessment is comprehensive, addressing both potential benefits and risks.",
            "Ethical considerations are thoughtfully discussed with relevant guidelines proposed.",
            "Future research directions are innovative and well-grounded in the proposed system's implications.",
            "The overall response demonstrates a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
