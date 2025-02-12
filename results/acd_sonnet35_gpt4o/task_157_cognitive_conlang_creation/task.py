import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        theories = [
            "Sapir-Whorf Hypothesis",
            "Chomsky's Universal Grammar",
            "Prototype Theory",
            "Conceptual Metaphor Theory",
            "Relevance Theory",
            "Embodied Cognition"
        ]
        features = [
            "phonology",
            "morphology",
            "syntax",
            "semantics",
            "pragmatics",
            "writing system"
        ]
        return {
            "1": {"theory": random.choice(theories), "feature": random.choice(features)},
            "2": {"theory": random.choice(theories), "feature": random.choice(features)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are a cognitive linguist tasked with creating a constructed language (conlang) based on the {t['theory']}. Focus particularly on how this theory would influence the {t['feature']} of your conlang.\n\n1. Briefly explain the key principles of {t['theory']} (2-3 sentences).\n\n2. Describe how you would design the {t['feature']} of your conlang to reflect these principles (3-4 sentences). Be specific and provide examples.\n\n3. Create a sample text in your conlang that demonstrates this feature (2-3 sentences or equivalent). Provide a literal translation and explain how it embodies the principles of the theory.\n\n4. Analyze how this language feature, as implemented in your conlang, might influence or reflect the thought patterns of its speakers (2-3 sentences).\n\n5. Propose an experiment that could test whether speakers of your conlang exhibit cognitive differences compared to speakers of natural languages, specifically related to the implemented feature (2-3 sentences).\n\nEnsure your response is creative, linguistically plausible, and grounded in the specified cognitive or linguistic theory. Your total response should not exceed 400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['theory']} and its principles.",
            f"The conlang's {t['feature']} is creatively designed to reflect the principles of the theory.",
            "The sample text effectively demonstrates the designed feature and is accompanied by a clear explanation.",
            "The analysis of potential cognitive influences is thoughtful and grounded in the theory.",
            "The proposed experiment is well-designed and relevant to testing the cognitive effects of the conlang feature.",
            "The overall response is creative, linguistically plausible, and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
