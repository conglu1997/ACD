import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_stages = [
            "Babbling stage (0-6 months)",
            "One-word stage (6-18 months)",
            "Two-word stage (18-24 months)",
            "Telegraphic stage (24-30 months)",
            "Multi-word stage (30+ months)"
        ]
        linguistic_theories = [
            "Universal Grammar Theory",
            "Usage-Based Theory",
            "Connectionist Theory",
            "Social Interactionist Theory",
            "Statistical Learning Theory"
        ]
        tasks = {
            "1": {
                "stage": random.choice(language_stages),
                "theory": random.choice(linguistic_theories)
            },
            "2": {
                "stage": random.choice(language_stages),
                "theory": random.choice(linguistic_theories)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the process of language acquisition in humans, focusing on the {t['stage']} and incorporating principles from the {t['theory']}. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain the key principles of the {t['theory']} and how they relate to language acquisition.
   b) Describe the main characteristics and milestones of the {t['stage']}.
   c) Discuss how these principles and characteristics can be translated into computational models.

2. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI system designed to simulate language acquisition.
   b) Explain how each component of your architecture relates to the {t['theory']} and the {t['stage']}.
   c) Detail the data processing flow and learning mechanisms in your system.
   d) Include a high-level diagram of your architecture (described in words).

3. Language Learning Simulation (200-250 words):
   a) Explain how your system simulates key aspects of language acquisition during the {t['stage']}.
   b) Describe any novel algorithms or techniques used in this simulation.
   c) Discuss how your system handles the transition to the next stage of language development.

4. Input and Environment Modeling (150-200 words):
   a) Describe how your system models the linguistic input and environment of a language learner.
   b) Explain how social interactions and feedback are incorporated into the learning process.
   c) Discuss any challenges in creating realistic input for language acquisition simulation.

5. Evaluation and Benchmarking (150-200 words):
   a) Propose methods to evaluate your AI system's performance in simulating language acquisition.
   b) Suggest benchmarks or milestones that could be used to compare the system's progress to human language development.
   c) Discuss how you would validate the system's output against real-world language acquisition data.

6. Limitations and Ethical Considerations (100-150 words):
   a) Identify potential limitations of your approach to simulating language acquisition.
   b) Discuss ethical implications of creating systems that simulate human language learning.
   c) Propose guidelines for responsible development and use of language acquisition AI models.

7. Interdisciplinary Insights and Future Directions (150-200 words):
   a) Discuss how your AI system might provide insights into human language acquisition processes.
   b) Explore potential applications of this technology in fields such as education, speech therapy, or second language learning.
   c) Suggest two future research directions that could extend or improve your language acquisition simulation system.

Ensure your response demonstrates a deep understanding of language acquisition theories, AI architectures, and cognitive modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified language acquisition theory and developmental stage.",
            "The AI system architecture is well-designed and coherently integrates the theoretical framework with computational models.",
            "The language learning simulation process is clearly explained and addresses key aspects of the specified developmental stage.",
            "The approach to input and environment modeling is realistic and comprehensive.",
            "The proposed evaluation methods and benchmarks are appropriate and well-justified.",
            "Limitations and ethical considerations are thoroughly addressed.",
            "The interdisciplinary insights and future directions are thoughtful and demonstrate a broad understanding of the field.",
            "The overall response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
