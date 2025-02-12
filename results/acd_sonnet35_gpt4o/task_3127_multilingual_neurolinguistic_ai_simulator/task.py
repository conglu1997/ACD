import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "trilingual household (English, Mandarin, Spanish)",
                "age_range": "0-5 years",
                "learning_challenge": "distinguishing between tonal and non-tonal languages"
            },
            {
                "environment": "bilingual school (French, Arabic)",
                "age_range": "6-12 years",
                "learning_challenge": "mastering different writing systems"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates multilingual language acquisition based on neural plasticity and cognitive development theories, then use it to model language learning in a {t['environment']} for children aged {t['age_range']}, with a focus on {t['learning_challenge']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating multilingual language acquisition.
   b) Explain how your system incorporates principles of neural plasticity and cognitive development.
   c) Detail how the AI models the interaction between multiple languages during the acquisition process.
   d) Include a brief diagram or flowchart representing your system's architecture (use ASCII art or a clear textual description).

2. Neurolinguistic Model (250-300 words):
   a) Explain how your system models the neural processes involved in multilingual language acquisition.
   b) Describe how it simulates the development of language-specific neural networks.
   c) Discuss how your model accounts for critical periods in language learning.

3. Language Interaction Simulation (250-300 words):
   a) Detail how your system simulates the interaction between the languages in the given multilingual environment.
   b) Explain how it models potential language interference or transfer effects.
   c) Describe how the system accounts for the specific learning challenge mentioned.

4. Developmental Trajectory Prediction (200-250 words):
   a) Explain how your AI system predicts the language development trajectory for the given age range.
   b) Describe specific milestones or benchmarks your system uses to measure language acquisition progress.
   c) Discuss how your model accounts for individual differences in language learning ability.

5. Application to Specified Scenario (250-300 words):
   a) Apply your AI system to model language learning in the given multilingual environment.
   b) Provide a detailed example of how a child might progress in their language acquisition according to your model.
   c) Explain how your system addresses the specific learning challenge mentioned.

6. Validation and Empirical Grounding (150-200 words):
   a) Propose methods for validating your AI system's predictions against real-world data.
   b) Discuss how your model could be refined based on empirical observations of multilingual children.
   c) Suggest potential applications of your system in language education or speech therapy.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to model child language acquisition.
   b) Address limitations of your model and areas where human expertise remains crucial.
   c) Propose guidelines for the responsible use of your AI system in research or clinical settings.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Cite relevant research or theories where appropriate to ground your design in current scientific understanding.

Format your response with clear headings for each section. Your total response should be between 1550-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neural plasticity, cognitive development, and multilingual language acquisition",
            "The proposed AI system is innovative and scientifically plausible",
            f"The model effectively addresses the given scenario: {t['environment']} for children aged {t['age_range']}",
            f"The design considers and accounts for the specified learning challenge: {t['learning_challenge']}",
            "The neurolinguistic model is well-grounded in current scientific understanding",
            "The language interaction simulation is detailed and accounts for complex interlingual effects",
            "The developmental trajectory prediction is realistic and considers individual differences",
            "The application to the specified scenario is thorough and illustrative",
            "The proposed validation methods and ethical considerations are thoughtful and comprehensive",
            "The response includes relevant citations or references to current research in the field",
            "The AI system architecture is clearly described and includes innovative elements",
            "The response addresses potential limitations and proposes future improvements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
