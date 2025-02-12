import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        texts = [
            "The water cycle, also known as the hydrologic cycle, describes the continuous movement of water within the Earth and atmosphere. It is a complex system that includes many different processes such as evaporation, condensation, precipitation, and runoff. The sun's energy drives the cycle by heating water in oceans and lakes, causing it to evaporate. Water vapor rises into the atmosphere, forming clouds through condensation. When the clouds become saturated, water falls back to Earth as precipitation. Some of this water flows into rivers and eventually returns to the oceans, while some seeps into the ground, replenishing groundwater supplies.",
            "Artificial intelligence (AI) is a branch of computer science that aims to create intelligent machines that can perform tasks that typically require human intelligence. These tasks include visual perception, speech recognition, decision-making, and language translation. AI systems are built using various approaches, such as machine learning, deep learning, and natural language processing. Machine learning involves algorithms that can learn from and make predictions or decisions based on data. Deep learning, a subset of machine learning, uses artificial neural networks inspired by the human brain to process complex patterns in large amounts of data. Natural language processing focuses on the interaction between computers and human language, enabling machines to understand, interpret, and generate human language in a valuable way."
        ]
        return {
            "1": {"text": random.choice(texts)},
            "2": {"text": random.choice(texts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following text and complete the tasks below:

"{t['text']}"

1. Create a semantic network:
   - Identify key concepts and entities in the text.
   - Establish relationships between these concepts.
   - Represent the network as a list of nodes and edges, where each node is a concept and each edge is a labeled relationship between two concepts.

2. Answer the following questions using your semantic network:
   a) What are the three most central concepts in the network, and why?
   b) Identify two implicit relationships that are not directly stated in the text but can be inferred from the network.

3. Generate new content:
   - Create a short paragraph (3-4 sentences) that expands on the original text by introducing a new concept that logically fits into the semantic network.
   - Explain how this new concept connects to at least two existing concepts in the network.

Format your response as follows:

1. Semantic Network:
[Your network representation here]

2. Questions:
a) [Your answer here]
b) [Your answer here]

3. New Content:
[Your generated paragraph here]
[Your explanation of connections here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The semantic network accurately represents the key concepts and relationships in the text.",
            "The answers to the questions demonstrate a deep understanding of the semantic network and its implications.",
            "The generated content introduces a relevant new concept and logically connects it to the existing network.",
            "The response shows creativity and insight in analyzing and expanding upon the given text."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
