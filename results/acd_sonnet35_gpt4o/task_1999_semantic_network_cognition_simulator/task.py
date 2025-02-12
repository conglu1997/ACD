import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_process": "Analogical Reasoning",
                "linguistic_feature": "Metaphor",
                "graph_property": "Centrality"
            },
            {
                "cognitive_process": "Concept Formation",
                "linguistic_feature": "Polysemy",
                "graph_property": "Clustering Coefficient"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a semantic network-based cognitive architecture for natural language understanding and generation. Your architecture should focus on the cognitive process of {t['cognitive_process']}, emphasize the linguistic feature of {t['linguistic_feature']}, and utilize the graph theory property of {t['graph_property']}.

Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen cognitive process and its role in language understanding and generation.
   b) Describe how this process relates to the specified linguistic feature.
   c) Discuss the relevance of the given graph theory property to semantic networks.

2. Cognitive Architecture Design (300-350 words):
   a) Design a semantic network-based system that implements the theoretical framework.
   b) Describe the key components of your system and how they interact.
   c) Explain how your system models the chosen cognitive process using semantic networks.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.

3. Natural Language Processing Simulation (200-250 words):
   a) Describe how your system would process a natural language input.
   b) Provide a specific example of how it would handle a sentence containing the specified linguistic feature.
   c) Explain how the system would use the graph theory property in its processing.

4. Language Generation Process (200-250 words):
   a) Describe how your system would generate natural language outputs.
   b) Provide an example of how it would create a sentence or phrase using the specified linguistic feature.
   c) Explain how the cognitive process and graph property influence language generation.

5. Evaluation and Cognitive Plausibility (200-250 words):
   a) Propose a method to evaluate the performance of your system in language tasks.
   b) Discuss how you would assess the cognitive plausibility of your architecture.
   c) Compare your approach to traditional natural language processing methods.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of using cognitive-inspired AI for language processing.
   b) Propose two potential applications of your system beyond basic NLP tasks.
   c) Suggest one area for future research to enhance the cognitive-linguistic capabilities of your architecture.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, graph theory, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and graph theory.",
            "The cognitive architecture design is innovative and well-explained.",
            "The natural language processing and generation examples are clear and relevant.",
            "The evaluation method and ethical analysis are thorough and insightful.",
            "The response shows clear integration of the specified cognitive process, linguistic feature, and graph property."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
