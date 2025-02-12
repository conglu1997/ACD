import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "Mandarin",
            "Spanish",
            "English",
            "Hindi",
            "Arabic",
            "Bengali",
            "Portuguese",
            "Russian",
            "Japanese",
            "Swahili"
        ]
        cognitive_factors = [
            "working memory capacity",
            "phonological awareness",
            "statistical learning ability",
            "executive function",
            "social cognition"
        ]
        environmental_factors = [
            "language exposure time",
            "socioeconomic status",
            "parental language proficiency",
            "educational setting",
            "cultural context"
        ]
        
        return {
            "1": {
                "languages": random.sample(languages, 3),
                "cognitive_factor": random.choice(cognitive_factors),
                "environmental_factor": random.choice(environmental_factors)
            },
            "2": {
                "languages": random.sample(languages, 3),
                "cognitive_factor": random.choice(cognitive_factors),
                "environmental_factor": random.choice(environmental_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human language acquisition across multiple languages, simulating the cognitive processes involved in early childhood multilingual development. Your system should focus on the simultaneous acquisition of {', '.join(t['languages'])}. Additionally, incorporate the cognitive factor of {t['cognitive_factor']} and the environmental factor of {t['environmental_factor']} into your model.

Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key theories of language acquisition that inform your AI model.
   b) Discuss how these theories apply to multilingual development.
   c) Describe how your model incorporates the specified cognitive and environmental factors.

2. AI System Architecture (250-300 words):
   a) Provide a detailed overview of your AI system's architecture.
   b) Explain how your system models the acquisition of multiple languages simultaneously.
   c) Describe the components that simulate cognitive processes and environmental influences.
   d) Discuss any novel approaches or algorithms used in your design.

3. Language Acquisition Simulation (200-250 words):
   a) Explain how your AI system simulates the process of acquiring the specified languages.
   b) Describe how the model handles cross-linguistic influence and transfer.
   c) Discuss how the system accounts for differences in language structure and complexity.

4. Cognitive and Environmental Factors (200-250 words):
   a) Detail how your model incorporates the specified cognitive factor.
   b) Explain how the system simulates the impact of the given environmental factor.
   c) Discuss how these factors interact with language acquisition in your model.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy of your AI model's simulations.
   b) Describe how you would validate the model against real-world data on multilingual development.
   c) Discuss potential limitations of your approach and how they might be addressed.

6. Applications and Implications (150-200 words):
   a) Suggest potential applications of your AI system in education or cognitive science research.
   b) Discuss the ethical implications of using such a system to study or influence language development.
   c) Propose future research directions based on your model.

Ensure your response demonstrates a deep understanding of language acquisition theories, cognitive science, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of language acquisition theories and their application to multilingual development.",
            "The AI system architecture is well-designed and clearly explained, with innovative approaches to modeling simultaneous language acquisition.",
            "The simulation of language acquisition accurately incorporates the specified cognitive and environmental factors.",
            "The proposed evaluation and validation methods are appropriate and well-reasoned.",
            "The discussion of applications and implications is insightful and considers ethical concerns.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
