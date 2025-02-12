import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Quantum Physics",
            "Renaissance Art",
            "Ecological Systems",
            "Ancient Mythology",
            "Blockchain Technology",
            "Culinary Techniques",
            "Urban Planning",
            "Neuroscience"
        ]
        problems = [
            "Climate Change Mitigation",
            "Interstellar Communication",
            "Ethical AI Development",
            "Sustainable Urban Transportation",
            "Mental Health Treatment",
            "Space Colonization",
            "Universal Language Creation",
            "Renewable Energy Storage"
        ]
        
        tasks = [
            {
                "domain1": random.choice(domains),
                "domain2": random.choice(domains),
                "problem": random.choice(problems)
            },
            {
                "domain1": random.choice(domains),
                "domain2": random.choice(domains),
                "problem": random.choice(problems)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a conceptual blend between {t['domain1']} and {t['domain2']}, then apply it to generate novel insights or solutions for the problem of {t['problem']}. Your response should include:

1. Conceptual Blend Design (250-300 words):
   a) Describe the key concepts, principles, or elements you're selecting from each domain.
   b) Explain how you're combining these elements to create a novel conceptual blend.
   c) Discuss any emergent properties or ideas that arise from this blend.
   d) Provide a visual metaphor or analogy that represents your conceptual blend (describe it textually).

2. Cognitive Analysis (200-250 words):
   a) Analyze the cognitive processes involved in creating and understanding your conceptual blend.
   b) Discuss how this blend might challenge or extend existing theories of conceptual integration.
   c) Explain any potential cognitive biases or limitations that might affect the interpretation of your blend.

3. Problem Application (250-300 words):
   a) Apply your conceptual blend to the problem of {t['problem']}.
   b) Describe at least two novel insights or potential solutions that emerge from this application.
   c) Explain how these insights differ from traditional approaches to the problem.

4. Implications and Extensions (200-250 words):
   a) Discuss the broader implications of your conceptual blend for the involved domains and beyond.
   b) Propose two potential research questions or experiments inspired by your blend.
   c) Suggest how this blending approach could be extended or applied to other domains or problems.

5. Limitations and Ethical Considerations (150-200 words):
   a) Analyze potential limitations or drawbacks of your conceptual blend.
   b) Discuss any ethical considerations or potential misuse of ideas generated from this blend.
   c) Propose guidelines for responsible development and application of conceptual blending in problem-solving.

Ensure your response demonstrates deep understanding of both domains, creative and analytical thinking, and the ability to generate and evaluate novel ideas. Use clear and precise language, and provide thorough explanations of complex concepts.

Format your response with clear headings for each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both domains and their key concepts.",
            "The conceptual blend is creative, coherent, and well-explained.",
            "The cognitive analysis shows insight into the mental processes involved in conceptual blending.",
            "The application of the blend to the given problem generates novel and potentially valuable insights or solutions.",
            "The implications and extensions demonstrate the ability to think broadly about the impact and potential of the conceptual blend.",
            "The limitations and ethical considerations show critical thinking and responsible approach to the ideas generated.",
            "The overall response is well-structured, clear, and adheres to the specified format and word count.",
            "The ideas presented are innovative while maintaining logical consistency and plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
