import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            ("Plato's Theory of Forms", "Existentialism"),
            ("Utilitarianism", "Kantian Ethics"),
            ("Cartesian Dualism", "Buddhist concept of Non-self"),
            ("Nietzsche's Eternal Recurrence", "Locke's Tabula Rasa"),
            ("Hegelian Dialectic", "Epicurean Hedonism")
        ]
        return {str(i+1): {"concepts": pair} for i, pair in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to combine the following two philosophical concepts into a new, coherent philosophical idea:

1. {t['concepts'][0]}
2. {t['concepts'][1]}

By 'combine', we mean to create a meaningful synthesis of the two concepts, identifying common threads or complementary aspects to form a new, unified philosophical idea.

Follow these steps:

1. Briefly explain each of the original concepts (1-2 sentences each).
2. Create a new philosophical idea that meaningfully combines elements from both concepts (2-3 sentences).
3. Name your new philosophical concept (be creative but clear).
4. Explain the potential implications of this new concept for our understanding of reality, ethics, or human nature (2-3 sentences).
5. Provide a simple thought experiment or real-world example that illustrates your new concept (2-3 sentences).

Format your response as follows:

Concept 1 ({t['concepts'][0]}): [Your explanation]
Concept 2 ({t['concepts'][1]}): [Your explanation]
New Concept: [Name of your new concept]
Explanation: [Your explanation of the new concept]
Implications: [Potential implications]
Illustration: [Your thought experiment or example]

Ensure that your new concept is logically coherent, creative, and demonstrates a deep understanding of the original philosophical ideas."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include brief explanations of both {t['concepts'][0]} and {t['concepts'][1]}",
            "The new concept should meaningfully combine elements from both original concepts",
            "The new concept should be given a creative and clear name",
            "The response should explain potential implications of the new concept",
            "The response should provide a thought experiment or real-world example illustrating the new concept",
            "The new concept should be logically coherent and demonstrate understanding of the original philosophical ideas",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
