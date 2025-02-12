import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "time", "love", "justice", "knowledge", "freedom",
            "chaos", "harmony", "growth", "decay", "balance"
        ]
        concrete_domains = [
            "nature", "technology", "architecture", "food", "transportation",
            "sports", "music", "art", "medicine", "finance"
        ]
        cultures = [
            "Western", "Eastern", "African", "Latin American", "Middle Eastern",
            "Nordic", "Oceanic", "South Asian", "Southeast Asian", "Indigenous"
        ]
        return {
            "1": {
                "abstract_concept": random.choice(abstract_concepts),
                "concrete_domain": random.choice(concrete_domains),
                "culture": random.choice(cultures)
            },
            "2": {
                "abstract_concept": random.choice(abstract_concepts),
                "concrete_domain": random.choice(concrete_domains),
                "culture": random.choice(cultures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a semantic network for the abstract concept of {t['abstract_concept']} and use it to generate novel metaphors within the concrete domain of {t['concrete_domain']}. Then, analyze the effectiveness and cultural implications of these metaphors from the perspective of {t['culture']} culture. Your task involves the following steps:

1. Semantic Network Design (200-250 words):
   a) Create a semantic network for the concept of {t['abstract_concept']} with at least 10 nodes and 15 edges.
   b) Explain the relationships between nodes and justify your network structure.
   c) Describe how this network captures the essence of {t['abstract_concept']}.

2. Metaphor Generation (200-250 words):
   a) Using your semantic network, generate three novel metaphors that relate {t['abstract_concept']} to elements from the domain of {t['concrete_domain']}.
   b) Explain how each metaphor is derived from the semantic network.
   c) Discuss how these metaphors illuminate different aspects of {t['abstract_concept']}.

3. Cognitive Analysis (150-200 words):
   a) Analyze how these metaphors might influence cognitive understanding of {t['abstract_concept']}.
   b) Discuss potential cognitive biases or limitations in understanding introduced by these metaphors.
   c) Explain how these metaphors might facilitate or hinder learning about {t['abstract_concept']}.

4. Cultural Implications (200-250 words):
   a) Examine how these metaphors might be perceived within {t['culture']} culture.
   b) Discuss any cultural nuances or potential misinterpretations of these metaphors.
   c) Analyze how these metaphors might influence cultural attitudes towards {t['abstract_concept']}.

5. Cross-Cultural Comparison (150-200 words):
   a) Compare your generated metaphors with traditional metaphors for {t['abstract_concept']} in {t['culture']} culture.
   b) Discuss similarities and differences in conceptualization.
   c) Analyze potential reasons for these similarities or differences.

6. AI and Metaphor (100-150 words):
   a) Discuss the implications of using AI-generated metaphors for cross-cultural communication.
   b) Analyze potential benefits and risks of relying on AI for metaphor generation and interpretation.

Ensure your response demonstrates a deep understanding of semantic networks, metaphor theory, cognitive science, and cultural anthropology. Be creative in your metaphor generation while maintaining logical connections to your semantic network. Use appropriate terminology and provide clear explanations for your reasoning throughout.

Format your response with clear headings for each section and adhere to the specified word limits."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-structured semantic network for {t['abstract_concept']} with at least 10 nodes and 15 edges.",
            f"Three novel metaphors relating {t['abstract_concept']} to {t['concrete_domain']} must be generated and explained.",
            f"The analysis should demonstrate a deep understanding of cognitive science and cultural anthropology, particularly in relation to {t['culture']} culture.",
            "The response must include all six required sections with appropriate content and adherence to word limits.",
            "The metaphors and analysis should be creative yet logically connected to the semantic network and cultural context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
