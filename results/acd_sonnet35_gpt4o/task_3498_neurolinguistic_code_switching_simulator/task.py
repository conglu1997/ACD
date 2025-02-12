import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Spanish', 'English', 'Arabic', 'Hindi', 'French']
        contexts = ['Business meeting', 'Family gathering', 'Academic conference', 'Social media interaction']
        cultural_factors = ['Power distance', 'Individualism vs. Collectivism', 'Long-term vs. Short-term orientation']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'language_pair': random.sample(languages, 2),
                'context': random.choice(contexts),
                'cultural_factor': random.choice(cultural_factors)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and simulates the neurological processes involved in multilingual code-switching between {t['language_pair'][0]} and {t['language_pair'][1]}, considering linguistic and cultural factors. Focus on the context of a {t['context']} and pay special attention to the cultural dimension of {t['cultural_factor']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling code-switching.
   b) Explain how your system integrates neurological, linguistic, and cultural factors.
   c) Detail the process of simulating code-switching in the given context.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Neurolinguistic Modeling (250-300 words):
   a) Explain how your system models the neurological processes involved in code-switching.
   b) Describe the specific brain regions and networks your model incorporates.
   c) Discuss how your model accounts for differences in language structure between {t['language_pair'][0]} and {t['language_pair'][1]}.

3. Cultural and Contextual Factors (200-250 words):
   a) Analyze how the context of a {t['context']} influences code-switching behavior.
   b) Explain how your system incorporates the cultural dimension of {t['cultural_factor']}.
   c) Discuss potential challenges in modeling cultural influences on code-switching.

4. Simulation and Output (200-250 words):
   a) Provide an example simulation of code-switching in the given context.
   b) Explain the patterns and features of code-switching your system predicts.
   c) Describe how your system represents and visualizes the simulation results.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy of your system's code-switching predictions.
   b) Discuss potential experimental designs to validate your model against real-world data.
   c) Address potential limitations or biases in your system's predictions.

6. Ethical Considerations (100-150 words):
   a) Identify ethical implications of modeling and simulating linguistic behavior.
   b) Discuss potential misuses of this technology and propose safeguards.
   c) Consider privacy concerns related to collecting and using multilingual speech data.

7. Future Research Directions (100-150 words):
   a) Suggest two potential expansions or applications of your system.
   b) Discuss how this research might contribute to our understanding of multilingualism and cognition.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, cultural studies, and AI principles. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, linguistics, cultural studies, and AI principles.",
            "The system architecture effectively integrates neurological, linguistic, and cultural factors in modeling code-switching.",
            f"The cultural dimension of {t['cultural_factor']} is thoroughly incorporated into the model.",
            f"The simulation example effectively demonstrates code-switching between {t['language_pair'][0]} and {t['language_pair'][1]} in the context of a {t['context']}.",
            "The proposed evaluation and validation methods are scientifically sound and appropriate for the task.",
            "Ethical considerations are thoroughly discussed with responsible guidelines proposed.",
            "The response is well-structured, addressing all required points comprehensively.",
            "The proposed system demonstrates creativity and innovation while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
