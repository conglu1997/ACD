import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Embodied Cognition",
            "Conceptual Metaphor",
            "Image Schemas",
            "Prototype Theory",
            "Frame Semantics",
            "Cognitive Grammar"
        ]
        programming_paradigms = [
            "Object-Oriented",
            "Functional",
            "Logic",
            "Declarative",
            "Imperative",
            "Event-Driven"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "cognitive_principle": random.choice(cognitive_principles),
                "programming_paradigm": random.choice(programming_paradigms)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on the cognitive linguistics principle of {t['cognitive_principle']} and incorporate elements of the {t['programming_paradigm']} programming paradigm. Your response should include:

1. Language Design (300-350 words):
   a) Explain the key features of your programming language and how they relate to {t['cognitive_principle']}.
   b) Describe how your language incorporates elements of the {t['programming_paradigm']} paradigm.
   c) Provide examples of basic syntax and structure in your language.
   d) Explain how your language differs from traditional programming languages.

2. Cognitive Foundations (250-300 words):
   a) Briefly explain the cognitive linguistics principle of {t['cognitive_principle']}.
   b) Discuss how this principle influences human cognition and natural language processing.
   c) Explain how your programming language leverages this principle to potentially enhance programmer cognition or code comprehension.

3. Sample Program (200-250 words):
   a) Write a simple program in your language that demonstrates its key features.
   b) Explain how this program reflects both the cognitive principle and the programming paradigm.
   c) Compare this to how the same program might be written in a traditional programming language.

4. Potential Applications (200-250 words):
   a) Suggest potential applications or domains where your language might be particularly useful.
   b) Explain how the cognitive linguistics basis of your language could benefit these applications.
   c) Discuss any potential advantages in terms of learnability, readability, or expressiveness.

5. Implementation Considerations (150-200 words):
   a) Discuss potential challenges in implementing a compiler or interpreter for your language.
   b) Explain how existing programming language technologies might be adapted for your language.
   c) Suggest any novel approaches that might be needed to fully realize your language design.

6. Cognitive Impact Analysis (200-250 words):
   a) Hypothesize how programming in your language might affect a developer's cognitive processes.
   b) Propose an experiment to test the cognitive effects of using your language compared to traditional languages.
   c) Discuss potential long-term impacts on software development practices and computer science education.

7. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or drawbacks of your language design.
   b) Suggest areas for future research or expansion of your language concept.
   c) Discuss how your approach might influence the broader field of programming language design.

Ensure your response demonstrates a deep understanding of both cognitive linguistics and computer science principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your language design while maintaining practical considerations for actual implementation and use.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and word counts.",
            "The language design demonstrates a clear understanding and application of the specified cognitive linguistics principle and programming paradigm.",
            "The cognitive foundations section accurately explains the principle and its relevance to the language design.",
            "The sample program effectively demonstrates the key features of the proposed language.",
            "The potential applications and cognitive impact analysis sections show thoughtful consideration of the language's implications.",
            "The response demonstrates creativity and innovation in language design while maintaining scientific and practical plausibility.",
            "The overall response shows a deep understanding of both cognitive linguistics and computer science principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
