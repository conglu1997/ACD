import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Luminarians",
                "biology": "Bioluminescent skin cells that can rapidly change color and pattern",
                "environment": "Deep ocean planet with no sunlight"
            },
            {
                "name": "Olfactorians",
                "biology": "Highly developed olfactory system with the ability to produce and detect complex pheromones",
                "environment": "Dense jungle world with limited visibility"
            }
        ]
        return {
            "1": random.choice(alien_species),
            "2": random.choice(alien_species)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system for the {t['name']}, an alien species with the following characteristics:

Biology: {t['biology']}
Environment: {t['environment']}

Your task is to create a detailed and scientifically plausible communication system that utilizes the unique biological features of this species and is adapted to their environment. Your response should include:

1. A name for your communication system (be creative but descriptive).
2. A detailed explanation of how the communication system works, including:
   a) The primary method of information encoding (e.g., patterns, sequences, combinations)
   b) The range of expressible concepts or ideas
   c) Any syntax or grammar rules, if applicable
3. An explanation of how the system leverages the species' unique biology (2-3 sentences).
4. A description of how the system is adapted to the species' environment (2-3 sentences).
5. Three example 'messages' in this system, along with their meanings. Each message should demonstrate a different aspect of the system's capabilities.
6. One potential limitation of the communication system and a proposed solution or workaround (2-3 sentences).
7. A brief speculation on how this communication system might influence the alien species' culture or social structure (2-3 sentences).

Ensure your communication system is creative, scientifically grounded, and logically consistent with the given biological and environmental constraints. Your design should go beyond simple visual or auditory languages and truly leverage the unique aspects of the alien biology."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The communication system is creative and original, going beyond simple adaptations of human communication methods.",
            "The system effectively utilizes the unique biological features of the alien species.",
            "The communication method is well-adapted to the given environmental conditions.",
            "The explanation of the system is scientifically plausible and logically consistent.",
            "The range of expressible concepts and any syntax or grammar rules are clearly defined.",
            "The example 'messages' effectively demonstrate different aspects of the system's capabilities.",
            "The identified limitation and proposed solution are relevant and thoughtful.",
            "The speculation on cultural/social implications shows insight and creativity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
