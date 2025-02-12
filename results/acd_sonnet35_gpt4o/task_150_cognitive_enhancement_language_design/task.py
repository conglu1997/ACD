class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "domain": "spatial reasoning",
                "cognitive_principles": ["mental rotation", "spatial relationships", "visual working memory"],
                "linguistic_features": ["agglutination", "evidentiality", "spatial deixis"]
            },
            "2": {
                "domain": "abstract problem-solving",
                "cognitive_principles": ["analogical reasoning", "concept formation", "cognitive flexibility"],
                "linguistic_features": ["recursion", "metaphorical mapping", "semantic networks"]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language specifically aimed at enhancing human cognitive abilities in the domain of {t['domain']}, based on the following cognitive principles and linguistic features:

Cognitive Principles: {', '.join(t['cognitive_principles'])}
Linguistic Features: {', '.join(t['linguistic_features'])}

Your task is to create a language that could potentially enhance cognitive abilities in this domain. Provide your response in the following format:

1. Language Overview (3-4 sentences):
   Briefly describe your language and how it aims to enhance cognitive abilities in the given domain.

2. Key Language Features (list 4-5 points):
   Describe the main features of your language, explaining how each relates to the given cognitive principles and linguistic features.

3. Vocabulary and Grammar (2-3 sentences each):
   a) Explain how the vocabulary is structured to support cognitive enhancement.
   b) Describe key grammatical features that contribute to cognitive enhancement.

4. Sample Expressions (provide 3 examples):
   Give examples of expressions in your language, along with their meanings and explanations of how they enhance cognition in the given domain.

5. Potential Cognitive Benefits (2-3 sentences):
   Speculate on how regular use of this language might enhance cognitive abilities in the given domain.

6. Learning Curve and Adoption (2-3 sentences):
   Discuss potential challenges in learning and adopting this language, and propose strategies to overcome them.

7. Ethical Considerations (2-3 sentences):
   Address potential ethical implications of a language designed to enhance cognitive abilities.

Ensure your language design is creative, theoretically grounded, and clearly demonstrates how it could potentially enhance cognitive abilities in the given domain."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design clearly incorporates the given cognitive principles and linguistic features.",
            "The response demonstrates a strong understanding of cognitive science and linguistics.",
            "The language features are creative and innovative, while remaining theoretically plausible.",
            "The explanation of potential cognitive benefits is well-reasoned and grounded in cognitive science.",
            "The response addresses ethical considerations thoughtfully.",
            "The sample expressions effectively demonstrate the language's cognitive enhancement potential."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
