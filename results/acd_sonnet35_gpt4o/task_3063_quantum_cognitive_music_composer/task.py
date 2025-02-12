import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_models = [
            "Working Memory Model",
            "Predictive Processing",
            "Embodied Cognition"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling"
        ]
        musical_elements = [
            "Harmony",
            "Rhythm",
            "Melody"
        ]
        music_genres = [
            "Classical",
            "Jazz",
            "Electronic"
        ]
        return {
            "1": {
                "cognitive_model": random.choice(cognitive_models),
                "quantum_principle": random.choice(quantum_principles),
                "musical_element": random.choice(musical_elements),
                "music_genre": random.choice(music_genres)
            },
            "2": {
                "cognitive_model": random.choice(cognitive_models),
                "quantum_principle": random.choice(quantum_principles),
                "musical_element": random.choice(musical_elements),
                "music_genre": random.choice(music_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system that composes and analyzes music based on cognitive models of music perception and quantum computing principles. Your system should focus on the cognitive model of {t['cognitive_model']}, incorporate the quantum principle of {t['quantum_principle']}, and emphasize the musical element of {t['musical_element']} in the genre of {t['music_genre']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired music AI system.
   b) Explain how your system incorporates the specified cognitive model and quantum principle.
   c) Detail how the system processes and generates music, focusing on the specified musical element and genre.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Quantum-Cognitive Integration (250-300 words):
   a) Explain how the chosen quantum principle ({t['quantum_principle']}) is applied to music composition and analysis.
   b) Describe how the cognitive model ({t['cognitive_model']}) informs the system's approach to music perception and generation.
   c) Discuss any challenges in integrating quantum computing concepts with cognitive models of music perception.

3. Music Generation Process (200-250 words):
   a) Outline the step-by-step process your AI system uses to compose music.
   b) Explain how the system emphasizes the specified musical element ({t['musical_element']}).
   c) Describe how your system ensures the output aligns with the conventions of the specified genre ({t['music_genre']}).

4. Music Analysis Capabilities (200-250 words):
   a) Describe how your system analyzes existing musical compositions.
   b) Explain how the quantum-cognitive approach provides novel insights into music structure and perception.
   c) Propose a method for comparing your system's analysis with human music perception.

5. Evaluation and Validation (150-200 words):
   a) Propose metrics for evaluating the quality and creativity of the generated music.
   b) Describe an experiment to validate your system's music analysis capabilities.
   c) Discuss how you would compare your system's performance to traditional AI music composition systems.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of using quantum-cognitive systems for music creation and analysis.
   b) Propose two novel research questions that arise from your system design.
   c) Suggest potential applications of your system beyond music composition and analysis.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear explanation of the AI system's architecture, incorporating the cognitive model of {t['cognitive_model']} and the quantum principle of {t['quantum_principle']}",
            f"The music generation process is clearly explained, emphasizing the musical element of {t['musical_element']} in the {t['music_genre']} genre",
            "The integration of quantum computing concepts and cognitive models is well-explained and scientifically plausible",
            "The music analysis capabilities are thoroughly described, with novel insights provided by the quantum-cognitive approach",
            "The evaluation and validation methods are well-thought-out and appropriate for the system",
            "Ethical considerations and future directions are thoughtfully discussed",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of quantum computing, cognitive science, music theory, and AI concepts",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
