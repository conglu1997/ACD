import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        topics = [
            {
                "subject": "World History",
                "items": ["French Revolution", "Industrial Revolution", "World War II", "Renaissance", "Cold War"],
                "constraint": "Use only words with 3 syllables or fewer"
            },
            {
                "subject": "Biology",
                "items": ["Photosynthesis", "DNA replication", "Natural selection", "Cell division", "Protein synthesis"],
                "constraint": "Incorporate a rhyme scheme in your memory palace"
            },
            {
                "subject": "Physics",
                "items": ["Quantum entanglement", "General relativity", "Thermodynamics", "Wave-particle duality", "Electromagnetism"],
                "constraint": "Use a palindromic structure in your memory palace"
            }
        ]
        return {
            "1": random.choice(topics),
            "2": random.choice(topics)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create and then decode a linguistic memory palace for the subject of {t['subject']}, with an additional constraint. Follow these steps:

1. Memory Palace Creation (250-300 words):
   a) Construct a 'linguistic memory palace' that encodes information about the following items: {', '.join(t['items'])}.
   b) Use a complex sentence structure where each main clause represents a 'room' in your memory palace.
   c) Embed information about each item within the syntactic structure and semantic relationships of your sentences.
   d) Ensure that the order and relationships between clauses reflect meaningful connections between the items.
   e) Additional constraint: {t['constraint']}. Incorporate this constraint throughout your memory palace.

2. Encoding Explanation (150-200 words):
   Explain your encoding method, detailing how you've used linguistic features (e.g., word order, embedded clauses, semantic fields) to represent and connect the items. Also, explain how you incorporated the additional constraint.

3. Decoding Instructions (150-200 words):
   Provide a set of instructions for decoding your memory palace. These should explain how to extract the original items and their relationships from your linguistic structure, including how to navigate the additional constraint.

4. Memory Palace Analysis (200-250 words):
   Analyze the effectiveness of your linguistic memory palace. Discuss its strengths and potential limitations in terms of memorability, information density, and ease of decoding. Include an assessment of how the additional constraint affected these aspects.

5. Cross-linguistic Consideration (150-200 words):
   Discuss how your approach to creating this linguistic memory palace, including the additional constraint, might need to be adapted for a language with a significantly different structure (e.g., a language with a different word order, case system, or phonological structure).

Ensure your response demonstrates a deep understanding of linguistic structures, memory techniques, and the subject matter being encoded. Be creative in your approach while maintaining clarity and logical consistency."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The linguistic memory palace effectively encodes all required items using complex sentence structures",
            "The additional constraint is successfully incorporated throughout the memory palace",
            "The encoding explanation clearly describes the linguistic features used and how the constraint was addressed",
            "The decoding instructions are clear and would allow someone to extract the original items from the memory palace",
            "The analysis demonstrates a thoughtful consideration of the memory palace's effectiveness, including the impact of the constraint",
            "The cross-linguistic consideration shows an understanding of how language structure and the constraint might interact in different languages",
            "The response demonstrates creativity, a deep understanding of linguistic structures, and an ability to work within constraints"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
