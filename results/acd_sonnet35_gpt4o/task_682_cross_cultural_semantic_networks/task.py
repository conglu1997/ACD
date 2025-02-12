import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {"name": "Japanese", "concept": "time"},
            {"name": "Inuit", "concept": "family"},
            {"name": "Maasai", "concept": "wealth"},
            {"name": "Ancient Greek", "concept": "knowledge"}
        ]
        return {
            "1": random.choice(cultures),
            "2": random.choice(cultures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a semantic network for metaphor generation and interpretation in the {t['name']} culture, focusing on the concept of '{t['concept']}'. Your task has the following components:

1. Semantic Network Design (200-250 words):
   a) Create a semantic network with at least 10 nodes representing key concepts related to '{t['concept']}' in {t['name']} culture.
   b) Explain the relationships between the nodes, including any hierarchical structures or associations.
   c) Describe how cultural context influences the structure and content of your semantic network.

2. Metaphor Generation (150-200 words):
   a) Use your semantic network to generate three novel metaphors for '{t['concept']}' in {t['name']} culture.
   b) Explain the reasoning behind each metaphor, referencing specific nodes and relationships in your network.

3. Cross-cultural Comparison (150-200 words):
   a) Compare your semantic network for '{t['concept']}' in {t['name']} culture with a hypothetical network for the same concept in a Western culture.
   b) Identify key differences and similarities, explaining their cultural significance.
   c) Discuss how these differences might affect metaphor interpretation across cultures.

4. Cognitive Model (200-250 words):
   a) Propose a simple computational model for how an AI system might use your semantic network to generate and interpret metaphors.
   b) Explain how your model accounts for cultural context and ambiguity in metaphor interpretation.
   c) Discuss potential limitations of your model and suggest improvements.

5. Linguistic Relativity Analysis (150-200 words):
   a) Discuss how the structure of your semantic network might reflect or influence thought patterns in {t['name']} culture.
   b) Consider the Sapir-Whorf hypothesis and provide arguments for or against linguistic relativity based on your analysis.

6. Ethical Implications (100-150 words):
   a) Discuss potential ethical concerns or societal impacts of using AI-generated semantic networks for cross-cultural communication.
   b) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of semantic network theory, cultural linguistics, and cognitive science. Be creative in your metaphor generation while maintaining cultural sensitivity and plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 950-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-designed semantic network with at least 10 nodes related to the given concept in the specified culture",
            "Three novel and culturally appropriate metaphors are generated using the semantic network",
            "A clear cross-cultural comparison is provided, highlighting key differences and similarities",
            "A plausible computational model for metaphor generation and interpretation is proposed",
            "The analysis of linguistic relativity is thoughtful and well-reasoned",
            "Ethical implications are discussed, and responsible development guidelines are proposed",
            "The response demonstrates a deep understanding of semantic network theory, cultural linguistics, and cognitive science",
            "The writing is clear, well-organized, and adheres to the specified word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
