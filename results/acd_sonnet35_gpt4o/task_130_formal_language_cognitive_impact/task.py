import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        formal_languages = [
            {
                "name": "Lambda Calculus",
                "description": "A formal system in mathematical logic for expressing computation based on function abstraction and application",
                "key_feature": "Use of lambda abstraction to define functions"
            },
            {
                "name": "Prolog",
                "description": "A logic programming language based on first-order predicate calculus",
                "key_feature": "Use of Horn clauses to express facts and rules"
            }
        ]
        return {
            "1": random.choice(formal_languages),
            "2": random.choice(formal_languages)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the formal language {t['name']} and create a new formal language inspired by it. Then, speculate on the potential cognitive effects of your new language. Complete the following steps:

1. Analysis of {t['name']} (3-4 sentences):
   Explain the key concepts and features of {t['name']}, focusing on its {t['key_feature']}. Discuss how it represents and manipulates information.

2. Create a New Formal Language (5-6 sentences):
   Design a new formal language inspired by {t['name']} but with a novel twist. Describe its syntax, semantics, and key features. Explain how it differs from and improves upon {t['name']}. Provide a simple example of how to express a computation or logical statement in your language.

3. Cognitive Impact Speculation (4-5 sentences):
   Speculate on how regular use of your new formal language might influence cognitive processes. Consider aspects such as problem-solving approaches, abstract thinking, or logical reasoning. Draw on principles from cognitive science to support your speculation.

4. Potential Applications (2-3 sentences):
   Suggest potential real-world applications or domains where your new formal language could be particularly useful or insightful.

5. Limitations and Future Directions (2-3 sentences):
   Discuss any potential limitations of your formal language and propose directions for future development or research.

Ensure your response demonstrates a deep understanding of formal languages, their relationship to cognition, and creative problem-solving in combining these concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the given formal language and its key features.",
            "The new formal language is creative, well-defined, and shows a clear inspiration from the original while introducing novel elements.",
            "The speculation on cognitive impacts is well-reasoned and grounded in cognitive science principles.",
            "The proposed applications are innovative and relevant to the language's features.",
            "The discussion of limitations and future directions shows critical thinking and insight.",
            "The overall response is coherent, well-structured, and demonstrates strong interdisciplinary reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
