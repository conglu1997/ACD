import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Luminari",
                "biology": "Bioluminescent, telepathic aquatic beings",
                "environment": "Deep ocean with bioluminescent ecosystem",
                "cognitive_theory": "Embodied cognition"
            },
            {
                "name": "Gravitos",
                "biology": "Silicon-based lifeforms with variable gravity control",
                "environment": "Low-gravity planet with extreme temperature fluctuations",
                "cognitive_theory": "Predictive processing"
            }
        ]
        return {
            "1": random.choice(alien_species),
            "2": random.choice(alien_species)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language acquisition system for the {t['name']} species, which are {t['biology']} living in an environment characterized by {t['environment']}. Base your system on the cognitive theory of {t['cognitive_theory']}. Your response should include:

1. Alien Cognitive Model (200-250 words):
   a) Describe how the {t['name']}'s biology and environment might influence their cognitive processes.
   b) Explain how {t['cognitive_theory']} applies to their cognitive development.
   c) Propose unique cognitive features or limitations of this species.

2. Language Acquisition System Design (250-300 words):
   a) Outline the key components of your language acquisition system.
   b) Explain how it incorporates principles from {t['cognitive_theory']}.
   c) Describe how the system adapts to the {t['name']}'s biology and environment.
   d) Propose a novel mechanism or feature in your system specific to this species.

3. Language Structure Prediction (200-250 words):
   a) Based on your system, predict three unique features of the {t['name']}'s language.
   b) Explain the reasoning behind each prediction, linking to their cognitive model and environment.
   c) Provide a brief example of how each feature might manifest in their language.

4. Learning Process Simulation (150-200 words):
   a) Describe a hypothetical scenario of a young {t['name']} learning its first words or concepts.
   b) Explain how your acquisition system functions in this scenario.
   c) Highlight any differences from human language acquisition.

5. Implications for Linguistics and AI (200-250 words):
   a) Discuss how this alien language acquisition model challenges or extends current linguistic theories.
   b) Explore potential applications of your system in developing more advanced AI language models.
   c) Propose an experiment to test the effectiveness of your system in AI language acquisition.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and speculative biology. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cognitive theory and applies it creatively to the alien species.",
            "The language acquisition system design is innovative, coherent, and well-adapted to the alien biology and environment.",
            "The language structure predictions are logical, unique, and well-justified based on the cognitive model and environment.",
            "The learning process simulation effectively illustrates how the acquisition system would function for the alien species.",
            "The implications for linguistics and AI are insightful and demonstrate an understanding of current challenges in these fields.",
            "The response shows creativity and scientific plausibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
