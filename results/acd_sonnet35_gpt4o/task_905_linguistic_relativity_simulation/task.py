import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "No concept of time",
            "Only collective nouns",
            "Verb-centric language structure",
            "Color perception limited to light and dark"
        ]
        problem_domains = [
            "Resource allocation",
            "Conflict resolution",
            "Scientific discovery",
            "Artistic expression"
        ]
        return {
            "1": {
                "feature": random.choice(linguistic_features),
                "problem": random.choice(problem_domains)
            },
            "2": {
                "feature": random.choice(linguistic_features),
                "problem": random.choice(problem_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a simulated language with the following key feature: {t['feature']}. Then, use this language to approach a problem in the domain of {t['problem']}. Your response should include:\n\n" \
               f"1. Language Design (200-250 words):\n" \
               f"   - Explain how you've implemented the key feature in your language.\n" \
               f"   - Describe other important aspects of your language that support or result from this feature.\n" \
               f"   - Provide 2-3 example sentences in your language with translations, highlighting how they embody the key feature.\n\n" \
               f"2. Cognitive Implications (150-200 words):\n" \
               f"   - Analyze how thinking in this language might affect cognition and perception.\n" \
               f"   - Discuss potential advantages and limitations this language might impose on its speakers' thought processes.\n\n" \
               f"3. Problem-Solving Approach (200-250 words):\n" \
               f"   - Describe a specific problem within the given domain of {t['problem']}.\n" \
               f"   - Explain how speakers of your language would approach this problem.\n" \
               f"   - Discuss how their approach might differ from speakers of a language without your key feature.\n\n" \
               f"4. Simulation Proposal (150-200 words):\n" \
               f"   - Propose an experiment or computational simulation to test the effects of your language on problem-solving in the given domain.\n" \
               f"   - Describe the methodology and what results would support or refute the linguistic relativity hypothesis.\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistic theory, cognitive science, and the principles of linguistic relativity. Be creative in your language design and problem-solving approach while maintaining scientific plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed language that clearly implements the feature: {t['feature']}.",
            "The cognitive implications analysis is insightful and well-reasoned.",
            f"The problem-solving approach in the domain of {t['problem']} is creative and logically consistent with the designed language.",
            "The simulation proposal is scientifically sound and directly tests the linguistic relativity hypothesis.",
            "The overall response demonstrates a deep understanding of linguistic theory, cognitive science, and interdisciplinary problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
