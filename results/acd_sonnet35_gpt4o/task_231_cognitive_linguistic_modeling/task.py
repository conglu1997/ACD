import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "process": "Semantic Integration",
                "description": "The cognitive process of combining word meanings into a coherent sentence interpretation"
            },
            {
                "process": "Syntactic Parsing",
                "description": "The cognitive process of analyzing the grammatical structure of a sentence"
            },
            {
                "process": "Lexical Retrieval",
                "description": "The cognitive process of accessing and selecting words from mental lexicon during language production"
            },
            {
                "process": "Phonological Encoding",
                "description": "The cognitive process of converting abstract linguistic representations into speech sounds"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Model and analyze the cognitive linguistic process of {t['process']} ({t['description']}).

Your task is to create an abstract representation of this process and analyze its implications. Follow these steps:

1. Conceptual Model (150-200 words):
   Create an abstract model or flowchart of the {t['process']} process. Describe the key components and their interactions. Use analogies or metaphors if helpful.

2. Cognitive Mechanisms (100-150 words):
   Explain the underlying cognitive mechanisms involved in this process. How might the brain perform this task? Include relevant concepts from cognitive science or neuroscience.

3. Linguistic Implications (100-150 words):
   Discuss how this process influences or is influenced by linguistic phenomena. Consider aspects such as language universals, variation, or acquisition.

4. Computational Analogy (100-150 words):
   Draw an analogy between this cognitive process and a computational process. How might a computer perform a similar task? What are the similarities and differences?

5. Potential Disruptions (100-150 words):
   Describe potential disruptions to this process (e.g., cognitive disorders, environmental factors). How would these disruptions manifest in language use?

6. Metalinguistic Reflection (100-150 words):
   Reflect on your own experience of this process. How does your awareness of this process change your perception of your language use?

7. Interdisciplinary Connections (50-100 words):
   Suggest how understanding this process could inform or be informed by another field of study not yet mentioned.

Ensure your response demonstrates a deep understanding of linguistic and cognitive principles, creative abstract thinking, and the ability to draw meaningful connections across disciplines. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and adhere to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['process']} process.",
            "The conceptual model should be coherent, abstract, and effectively represent the cognitive process.",
            "The explanation of cognitive mechanisms should be scientifically plausible and well-reasoned.",
            "The linguistic implications should be logically derived and demonstrate understanding of linguistic principles.",
            "The computational analogy should be apt and reveal insights about both cognitive and computational processes.",
            "The discussion of potential disruptions should be realistic and demonstrate understanding of cognitive disorders or relevant factors.",
            "The metalinguistic reflection should show genuine insight into the agent's own language processing.",
            "The interdisciplinary connection should be novel and meaningful.",
            "The overall response should be creative, coherent, and demonstrate strong abstract reasoning about language and cognition.",
            "The response should adhere to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
