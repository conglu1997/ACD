import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Pirahã",
                "features": "Lacks number words and color terms, has a 'here and now' focus"
            },
            {
                "name": "Guugu Yimithirr",
                "features": "Uses absolute spatial references instead of relative ones"
            }
        ]
        return {
            "1": random.choice(languages),
            "2": random.choice(languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture for an AI system based on the {t['name']} language, which {t['features']}. Then, analyze how this AI would approach problem-solving compared to architectures based on more common languages like English. Your response should include:

1. Cognitive Architecture Design (300-350 words):
   a) Describe the key components of your AI's cognitive architecture, explicitly incorporating the unique features of {t['name']}.
   b) Explain how the language's characteristics influence the AI's internal representations and processing mechanisms.
   c) Discuss how this architecture might differ from one based on a more common language like English.

2. Problem-Solving Approach (250-300 words):
   a) Choose a specific problem domain (e.g., spatial navigation, time management, or abstract reasoning).
   b) Describe how your AI would approach problem-solving in this domain, given its language-based cognitive architecture.
   c) Compare this approach to how an English-based AI might tackle the same problem.

3. Strengths and Limitations (200-250 words):
   a) Identify potential advantages of your {t['name']}-based AI in certain types of tasks or environments.
   b) Discuss limitations or challenges this AI might face, particularly in tasks that don't align well with the language's features.
   c) Propose ways to mitigate these limitations while preserving the unique aspects of the language-based architecture.

4. Implications for AI Development (200-250 words):
   a) Discuss how insights from this thought experiment might inform real-world AI development and cognitive modeling.
   b) Explore potential applications or research directions inspired by language-based cognitive architectures.
   c) Consider ethical implications of developing AIs based on diverse linguistic structures.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test the performance of your {t['name']}-based AI against a conventional AI.
   b) Describe the methodology, including task selection, performance metrics, and control measures.
   c) Predict potential outcomes and their implications for our understanding of language and cognition.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the chosen language's unique features and how they might influence cognitive processes.",
            "The cognitive architecture design clearly incorporates the language's characteristics in innovative and plausible ways.",
            "The problem-solving approach analysis shows a clear contrast between the language-based AI and a conventional English-based AI.",
            "The discussion of strengths, limitations, and mitigation strategies is thoughtful and well-reasoned.",
            "The implications for AI development and proposed experimental design are insightful and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
