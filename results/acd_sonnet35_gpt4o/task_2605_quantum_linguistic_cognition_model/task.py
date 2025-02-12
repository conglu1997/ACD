import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_phenomena = [
            "Syntactic ambiguity",
            "Semantic priming",
            "Phonological awareness",
            "Morphological processing"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum interference"
        ]
        return {
            "1": {
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Recent advancements in quantum computing have opened up new possibilities for modeling complex cognitive processes, including language processing. Your task is to design a theoretical model that uses quantum computing principles to simulate and analyze linguistic cognition, focusing on the linguistic phenomenon of {t['linguistic_phenomenon']} and utilizing the quantum principle of {t['quantum_principle']}. Then, apply your model to analyze this phenomenon and discuss its implications for AI language understanding.

For context, quantum principles have been applied to linguistics in various ways. For example, quantum superposition has been used to represent semantic ambiguity, where a word's meaning is considered to be in a superposition of all possible meanings until context 'collapses' it to a specific interpretation. Your task is to expand on these ideas or propose novel applications, specifically for {t['linguistic_phenomenon']} using {t['quantum_principle']}.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Describe the key components of your quantum linguistic cognition model.
   b) Explain how you integrate {t['quantum_principle']} into your model to represent {t['linguistic_phenomenon']}.
   c) Discuss how your model simulates cognitive processes involved in language processing.
   d) Provide a high-level mathematical or diagrammatic representation of your model. This should include:
      - A clear, labeled diagram illustrating the key components and their interactions
      - At least one mathematical equation representing a core aspect of your model
      - A brief explanation of how the diagram and equation relate to {t['linguistic_phenomenon']} and {t['quantum_principle']}

2. Application to {t['linguistic_phenomenon']} (250-300 words):
   a) Apply your model to analyze the chosen linguistic phenomenon.
   b) Explain how the quantum principle enhances our understanding of this phenomenon.
   c) Describe a hypothetical experiment that could test your model's predictions.
   d) Compare your quantum model with a classical computational approach, highlighting potential advantages.

3. Implications for AI Language Understanding (150-200 words):
   a) Analyze how your quantum linguistic cognition model could enhance AI language processing.
   b) Discuss potential advantages over classical computational approaches to language.
   c) Propose a specific AI application that could benefit from your model.

4. Technical Challenges and Future Directions (100-150 words):
   a) Identify key technical challenges in implementing your model.
   b) Suggest potential solutions or areas for future research.
   c) Discuss how your model could be extended to other linguistic phenomena.

5. Ethical Considerations (100-150 words):
   a) Analyze potential ethical implications of using quantum models for linguistic cognition.
   b) Discuss any risks or benefits to privacy, cognition, or human-AI interaction.
   c) Propose guidelines for responsible development and use of such models.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Remember to balance creativity with scientific rigor - your model should be novel and interesting, but also grounded in established principles of quantum mechanics and linguistics.

Use appropriate technical terminology and provide clear explanations where necessary. Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            f"The model clearly incorporates the quantum principle of {t['quantum_principle']} to analyze {t['linguistic_phenomenon']}.",
            "The response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science.",
            "The proposed model is innovative while maintaining scientific plausibility.",
            "The response includes a clear analysis of implications for AI language understanding and ethical considerations.",
            "The response provides a detailed mathematical equation or clear, labeled diagram illustrating the key components of the model and their interactions.",
            "The response includes a comparison between the quantum model and a classical computational approach, highlighting potential advantages."
        ]
        scores = [float(eval_with_llm_judge(instructions, submission, [criterion])) for criterion in criteria]
        return sum(scores) / len(scores)
