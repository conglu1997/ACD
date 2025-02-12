import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {"type": "Gas giant moon", "gravity": "Low", "atmosphere": "Methane-rich", "day_length": "10 Earth days"},
            {"type": "Rocky planet", "gravity": "High", "atmosphere": "Thin, CO2-rich", "day_length": "36 Earth hours"},
            {"type": "Ocean world", "gravity": "Earth-like", "atmosphere": "Dense, Nitrogen-rich", "day_length": "72 Earth hours"}
        ]
        
        alien_biologies = [
            {"sensory_organs": "Echolocation and electroreception", "communication_method": "Bioluminescent patterns", "lifespan": "1000 Earth years"},
            {"sensory_organs": "Infrared vision and chemoreception", "communication_method": "Pheromone release", "lifespan": "50 Earth years"},
            {"sensory_organs": "Magnetic field detection and sonar", "communication_method": "Vibrational signals", "lifespan": "200 Earth years"}
        ]
        
        return {
            "1": {"environment": random.choice(environments), "biology": random.choice(alien_biologies)},
            "2": {"environment": random.choice(environments), "biology": random.choice(alien_biologies)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to model and simulate the evolution of language and thought patterns in a hypothetical extraterrestrial civilization, based on the following parameters:

Environment:
- Type: {t['environment']['type']}
- Gravity: {t['environment']['gravity']}
- Atmosphere: {t['environment']['atmosphere']}
- Day length: {t['environment']['day_length']}

Alien Biology:
- Sensory organs: {t['biology']['sensory_organs']}
- Communication method: {t['biology']['communication_method']}
- Lifespan: {t['biology']['lifespan']}

Your response should include:

1. Cognitive Model Design (300-350 words):
   a) Describe the key components of your AI system for modeling alien cognition.
   b) Explain how your model incorporates the given environmental and biological parameters.
   c) Detail how your system simulates the development of language and thought patterns.
   d) Discuss how your model accounts for the unique sensory and communication capabilities of the aliens.

2. Language Evolution Simulation (250-300 words):
   a) Explain the process by which your AI system simulates language evolution.
   b) Describe key linguistic features that might emerge, given the aliens' environment and biology.
   c) Provide an example of a simulated language construct, explaining its relevance to the aliens' context.

3. Thought Pattern Analysis (250-300 words):
   a) Describe how your system models the aliens' thought patterns and cognitive processes.
   b) Explain how the environmental and biological factors influence these patterns.
   c) Compare and contrast the simulated alien cognition with human thought processes.

4. Technological Implications (200-250 words):
   a) Based on the simulated language and thought patterns, predict potential technological developments.
   b) Explain how the aliens' unique cognition might lead to different approaches to problem-solving and innovation.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss the ethical implications of simulating alien cognition and language.
   b) Address the limitations of your model and potential biases in its design.
   c) Suggest guidelines for the responsible use and interpretation of your AI system's outputs.

6. Future Research Directions (100-150 words):
   a) Propose two potential expansions or modifications to your system for future research.
   b) Explain how these additions could enhance our understanding of cognition and language evolution.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The AI system design effectively incorporates the given environmental and biological parameters.",
            "The language evolution simulation and thought pattern analysis are creative and scientifically plausible.",
            "The response includes innovative ideas while maintaining logical consistency.",
            "Ethical considerations and limitations of the model are thoughtfully addressed.",
            "The response is well-structured, clear, and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
