import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "democracy",
                "domain": "political science"
            },
            {
                "concept": "quantum entanglement",
                "domain": "physics"
            },
            {
                "concept": "neural plasticity",
                "domain": "neuroscience"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In this task, you will work with a hypothetical synesthetic language system where words have inherent sensory properties. Your goal is to translate the concept of '{t['concept']}' from the domain of {t['domain']} into this synesthetic language and then use it to create a complex description.

Follow these steps:

1. Synesthetic Alphabet (100-150 words):
   Create a brief synesthetic alphabet where each letter is associated with a specific sensory experience (e.g., 'A' might taste like cinnamon, 'B' might feel like velvet). Provide at least 10 letter-sensory associations.

2. Concept Translation (150-200 words):
   Translate the given concept into the synesthetic language. Explain how the sensory properties of the letters combine to create a multi-sensory representation of the concept.

3. Synesthetic Description (200-250 words):
   Using your synesthetic translation, create a vivid, sensory-rich description of the concept. This description should evoke a complex, multi-sensory experience that captures the essence of the concept.

4. Reverse Translation (100-150 words):
   Translate your synesthetic description back into regular English, explaining how the sensory associations contribute to a deeper understanding of the original concept.

5. Analysis (150-200 words):
   Reflect on this process. How does thinking about concepts in terms of sensory experiences change or enhance our understanding? What are the limitations or challenges of this approach?

Be creative and imaginative in your responses while maintaining a connection to the original concept. Your total response should be between 700-950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a synesthetic alphabet with at least 10 letter-sensory associations",
            f"The response should translate the concept of '{t['concept']}' into the synesthetic language",
            "The response should provide a vivid, sensory-rich description using the synesthetic language",
            "The response should include a reverse translation from the synesthetic description to regular English",
            "The response should analyze the process and reflect on its implications and limitations",
            "The response should demonstrate creativity and abstract thinking while maintaining relevance to the original concept",
            "The response should follow the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
