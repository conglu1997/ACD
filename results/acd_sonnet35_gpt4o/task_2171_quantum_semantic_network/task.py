import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "concept": "time",
                "related_words": ["clock", "future", "past", "present", "duration"]
            },
            "2": {
                "concept": "love",
                "related_words": ["affection", "romance", "passion", "attachment", "care"]
            },
            "3": {
                "concept": "power",
                "related_words": ["strength", "authority", "energy", "influence", "control"]
            },
            "4": {
                "concept": "freedom",
                "related_words": ["liberty", "independence", "autonomy", "choice", "rights"]
            }
        }
        selected_tasks = random.sample(list(tasks.items()), 2)
        return dict(selected_tasks)

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired semantic network for natural language understanding that uses quantum principles to model word meanings and relationships. Your task is to create a quantum semantic representation for the concept '{t['concept']}' and its related words: {', '.join(t['related_words'])}.

Your response should include the following sections:

1. Quantum Semantic Representation (250-300 words):
   a) Explain how you will use quantum superposition to represent the multiple meanings or contexts of '{t['concept']}'.
   b) Describe how quantum entanglement can be used to model the relationships between '{t['concept']}' and its related words.
   c) Provide a mathematical or formal representation of your quantum semantic network for this concept and its related words.
   d) Include a concrete example of how a specific word pair would be represented in your quantum semantic network.

2. Semantic Operations (200-250 words):
   a) Describe how semantic similarity between words can be calculated using your quantum representation.
   b) Explain how context-dependent meaning can be extracted from your quantum semantic network.
   c) Propose a method for updating word meanings based on new information or contexts.
   d) Provide an example of how your system would perform one of these operations.

3. Natural Language Understanding Application (200-250 words):
   a) Describe how your quantum semantic network could be used in a specific NLU task (e.g., sentiment analysis, machine translation, or question answering).
   b) Explain the potential advantages of your quantum-inspired approach over classical NLP methods for this task.
   c) Discuss any challenges or limitations of applying your quantum semantic network to real-world NLU problems.
   d) Illustrate with a brief example of how your system would process a sample input for the chosen NLU task.

4. Quantum-Classical Interface (150-200 words):
   a) Explain how classical text data would be encoded into your quantum semantic representation.
   b) Describe the process of measuring or extracting meaningful results from your quantum semantic network.
   c) Discuss any hybrid quantum-classical approaches that could be used in implementing your system.

5. Ethical and Philosophical Implications (100-150 words):
   a) Discuss potential ethical concerns related to using quantum-inspired models for natural language understanding.
   b) Explore the philosophical implications of representing human language and meaning using quantum principles.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and natural language processing. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of quantum computing principles and their application to semantic representation.",
            "The quantum semantic representation is clearly explained and includes a plausible mathematical or formal representation.",
            "The semantic operations are well-defined and logically connected to the quantum representation.",
            "The application to a specific NLU task is well-reasoned and highlights potential advantages over classical methods.",
            "The quantum-classical interface is adequately addressed, including data encoding and result extraction.",
            "Ethical and philosophical implications are thoughtfully discussed.",
            "The response is creative and innovative, proposing a novel approach to quantum-inspired semantic networks.",
            "Concrete examples are provided for key concepts and operations.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0