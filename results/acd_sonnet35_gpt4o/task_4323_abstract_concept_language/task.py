import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "entropy",
            "recursion",
            "emergence",
            "duality",
            "symmetry",
            "infinity",
            "complexity",
            "paradox"
        ]
        complex_ideas = [
            "the nature of consciousness",
            "the concept of free will",
            "the origins of the universe",
            "the essence of creativity"
        ]
        tasks = {
            "1": {"concepts": random.sample(abstract_concepts, 3), "idea": random.choice(complex_ideas)},
            "2": {"concepts": random.sample(abstract_concepts, 3), "idea": random.choice(complex_ideas)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language based on the following abstract concepts: {', '.join(t['concepts'])}. Then use this language to communicate the complex idea of {t['idea']}. Your response should include:

1. Language Design (250-300 words):
   a) Explain the basic principles and structure of your abstract concept language.
   b) Describe how each of the given abstract concepts is incorporated into the language.
   c) Provide examples of basic expressions or sentences in your language, with translations.

2. Complex Idea Communication (200-250 words):
   a) Express the given complex idea ({t['idea']}) using your abstract concept language.
   b) Provide a detailed explanation of how your language conveys this idea.
   c) Discuss any unique insights or perspectives that your language brings to this concept.

3. Analysis of Language (200-250 words):
   a) Analyze the strengths and limitations of your abstract concept language.
   b) Compare it to natural languages and discuss potential advantages or disadvantages.
   c) Explore how this language might influence thought processes and problem-solving approaches.

4. Potential Applications (150-200 words):
   a) Propose at least two fields where your abstract concept language could be beneficially applied.
   b) Explain how it could enhance understanding or communication in these areas.

5. Learning and Adoption Challenges (100-150 words):
   a) Discuss potential difficulties in learning and adopting this language.
   b) Propose strategies to overcome these challenges.

Ensure your response demonstrates creativity, logical consistency, and a deep understanding of abstract concepts and linguistic principles. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language design incorporates all given abstract concepts coherently.",
            f"The complex idea of {t['idea']} is effectively communicated using the designed language.",
            "The analysis of the language's strengths, limitations, and comparisons to natural languages is insightful.",
            "The proposed applications of the language are creative and well-reasoned.",
            "The discussion of learning and adoption challenges is realistic and includes plausible strategies.",
            "The response demonstrates a high level of creativity and abstract thinking.",
            "The response is well-structured and adheres to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
