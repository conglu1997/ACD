import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Maori",
            "Inuit",
            "Yoruba",
            "Navajo",
            "Balinese"
        ]
        memory_types = [
            "oral traditions",
            "rituals and ceremonies",
            "art and symbolism",
            "ecological knowledge",
            "social structures and kinship systems"
        ]
        cognitive_principles = [
            "episodic memory",
            "semantic memory",
            "procedural memory",
            "working memory",
            "long-term potentiation"
        ]
        return {
            "1": {
                "culture": random.choice(cultures),
                "memory_type": random.choice(memory_types),
                "cognitive_principle": random.choice(cognitive_principles)
            },
            "2": {
                "culture": random.choice(cultures),
                "memory_type": random.choice(memory_types),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a natural language processing system that models and preserves cultural memory for the {t['culture']} culture, focusing on {t['memory_type']} and incorporating the cognitive science principle of {t['cognitive_principle']}. Your task has five parts:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your NLP system.
   b) Explain how it incorporates {t['cognitive_principle']} in its design.
   c) Detail how the system will capture and represent {t['memory_type']} from {t['culture']} culture.

2. Data Collection and Processing (200-250 words):
   a) Propose methods for collecting cultural data related to {t['memory_type']}.
   b) Describe how you would preprocess and encode this data for your system.
   c) Discuss any ethical considerations in data collection and usage.

3. Memory Modeling (200-250 words):
   a) Explain how your system models {t['memory_type']} using NLP techniques.
   b) Describe how {t['cognitive_principle']} influences this modeling process.
   c) Discuss how your system handles the dynamic nature of cultural memory.

4. Retrieval and Interaction (200-250 words):
   a) Describe how users would interact with your system to access cultural memories.
   b) Explain how the system determines relevant information to retrieve.
   c) Discuss how the retrieval process reflects both NLP capabilities and {t['cognitive_principle']}.

5. Evaluation and Cultural Impact (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system in preserving {t['culture']} {t['memory_type']}.
   b) Discuss potential positive and negative impacts of your system on {t['culture']} culture.
   c) Suggest ways to involve the {t['culture']} community in the development and use of the system.

Ensure your response demonstrates a deep understanding of NLP, cognitive science, and cultural anthropology. Be creative in your approach while maintaining scientific and ethical plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of {t['culture']} culture and {t['memory_type']}.",
            f"The system design should effectively incorporate the cognitive principle of {t['cognitive_principle']}.",
            "The NLP techniques proposed should be appropriate and well-explained.",
            "The response should address ethical considerations and community involvement.",
            "The proposed evaluation methods should be relevant and well-thought-out."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
