import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        topics = [
            {
                "subject": "Ancient Greek Philosophy",
                "items": ["Socrates", "Plato", "Aristotle", "Stoicism", "Epicureanism"]
            },
            {
                "subject": "Quantum Physics Concepts",
                "items": ["Superposition", "Entanglement", "Wave-particle duality", "Uncertainty principle", "Quantum tunneling"]
            }
        ]
        return {str(i+1): topic for i, topic in enumerate(random.sample(topics, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a linguistic 'memory palace' to encode and retrieve information about {t['subject']}. Your task has the following components:

1. Memory Palace Creation (250-300 words):
   a) Design a unique and vivid spatial environment using only linguistic descriptions.
   b) Your environment should have at least 5 distinct locations or features.
   c) Each location should be described in sensory-rich language, focusing on visual, auditory, and tactile elements.
   d) Explain how the structure of your memory palace reflects or relates to the subject matter.

2. Information Encoding (200-250 words):
   a) Associate each of the following items with a specific location in your memory palace: {', '.join(t['items'])}
   b) For each item, create a vivid, unusual, and memorable image or scene that represents the concept.
   c) Explain how each image relates to its associated concept and location.

3. Retrieval Process (150-200 words):
   a) Describe the mental journey you would take through your memory palace to recall all the items.
   b) Explain how the spatial relationships and sensory details aid in retrieval.

4. Linguistic Analysis (150-200 words):
   a) Analyze the language you used to create your memory palace and encode information.
   b) Discuss how different types of words (e.g., concrete nouns, abstract concepts, sensory adjectives) contribute to the effectiveness of the technique.

5. Cognitive Implications (150-200 words):
   a) Discuss how this memory technique leverages spatial cognition and linguistic processing.
   b) Explain potential benefits and limitations of using language to create spatial-cognitive structures.

6. AI Application (100-150 words):
   a) Propose how this technique could be adapted for use in AI systems for information encoding and retrieval.
   b) Discuss potential challenges in implementing this method in a non-human cognitive system.

Ensure your response demonstrates creativity, spatial reasoning, and a deep understanding of both the subject matter and cognitive processes involved in the method of loci. Use clear and vivid language throughout your descriptions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The memory palace is vividly described with rich sensory details",
            "All required items are effectively encoded using memorable imagery",
            "The retrieval process is clearly explained and logically follows the spatial layout",
            "The linguistic analysis demonstrates insight into the role of language in spatial-cognitive techniques",
            "The cognitive implications and AI application sections show deep understanding and creative thinking"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
