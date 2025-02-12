import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = [
            "spatial relationships",
            "force dynamics",
            "time perception",
            "emotional states",
            "social interactions"
        ]
        programming_concepts = [
            "variable assignment",
            "control flow",
            "data structures",
            "functions/methods",
            "error handling"
        ]
        return {
            "1": {"cognitive_domain": random.choice(cognitive_domains), "programming_concept": random.choice(programming_concepts)},
            "2": {"cognitive_domain": random.choice(cognitive_domains), "programming_concept": random.choice(programming_concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a programming language feature based on cognitive linguistics principles, specifically metaphor theory and embodied cognition. Focus on the cognitive domain of {t['cognitive_domain']} and apply it to the programming concept of {t['programming_concept']}.\n\n" + \
               "Your response should include:\n\n" + \
               "1. Explanation (100-150 words):\n" + \
               "   Describe how the chosen cognitive domain is understood through embodied experience and metaphor. Explain how this understanding can be applied to the given programming concept.\n\n" + \
               "2. Language Feature Design (150-200 words):\n" + \
               "   Design a specific language feature or syntax that incorporates the cognitive domain into the programming concept. Provide examples of how it would be used in code.\n\n" + \
               "3. Advantages and Challenges (100-150 words):\n" + \
               "   Discuss the potential benefits of this feature for programmers' understanding and use of the concept. Address any challenges or limitations of this approach.\n\n" + \
               "4. Cognitive Impact (100-150 words):\n" + \
               "   Speculate on how using this language feature might influence programmers' thinking or problem-solving approaches in the long term.\n\n" + \
               "5. Code Sample (50-100 words):\n" + \
               "   Provide a short code sample (3-5 lines) demonstrating the use of your designed feature. Explain how it embodies the cognitive linguistics principles.\n\n" + \
               "Ensure your response demonstrates a deep understanding of both cognitive linguistics and programming language design, while showcasing creativity in bridging these disciplines."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains how the cognitive domain of {t['cognitive_domain']} is understood through embodied experience and metaphor, and applies this understanding to {t['programming_concept']}.",
            "The designed language feature or syntax effectively incorporates the cognitive domain into the programming concept, with clear examples of its use in code.",
            "The response thoughtfully discusses advantages, challenges, and potential cognitive impacts of the designed feature.",
            "The provided code sample demonstrates the use of the designed feature and clearly embodies cognitive linguistics principles.",
            "The response shows a deep understanding of both cognitive linguistics and programming language design, creatively bridging these disciplines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
