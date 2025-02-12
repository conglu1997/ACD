import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain": "Emotional Intelligence",
                "target_concept": "Empathy",
                "related_concepts": ["Compassion", "Understanding", "Perspective-taking", "Emotional resonance"]
            },
            {
                "domain": "Environmental Science",
                "target_concept": "Sustainability",
                "related_concepts": ["Renewable resources", "Ecosystem balance", "Carbon footprint", "Circular economy"]
            },
            {
                "domain": "Artificial Intelligence",
                "target_concept": "Machine Learning",
                "related_concepts": ["Neural networks", "Data mining", "Pattern recognition", "Algorithmic bias"]
            },
            {
                "domain": "Quantum Physics",
                "target_concept": "Entanglement",
                "related_concepts": ["Superposition", "Quantum information", "Non-locality", "Wave function collapse"]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an evolving semantic network that mimics human conceptual development in the domain of {t['domain']}, focusing on the target concept of '{t['target_concept']}'. Then, use this network to solve a complex language understanding problem. Your task has the following components:

1. Semantic Network Design (250-300 words):
   a) Describe the structure and key components of your semantic network.
   b) Explain how your network incorporates the target concept and related concepts: {', '.join(t['related_concepts'])}.
   c) Detail how your network evolves over time to mimic human conceptual development.
   d) Provide a visual representation or description of a small section of your network.

2. Cognitive Development Simulation (200-250 words):
   a) Outline the stages of cognitive development your network simulates.
   b) Explain how the semantic relationships change or expand at each stage.
   c) Describe how your model accounts for individual differences in conceptual understanding.

3. Language Understanding Application (200-250 words):
   a) Present a complex language understanding problem related to the given domain.
   b) Explain how your evolving semantic network would approach and solve this problem.
   c) Compare this approach to traditional natural language processing methods.

4. Network Analysis (150-200 words):
   a) Analyze the mathematical or computational properties of your semantic network.
   b) Discuss how these properties relate to human cognitive processes.
   c) Explain any emergent behaviors or unexpected relationships in your network.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns or societal impacts of implementing such a system.
   b) Propose guidelines for responsible development and use of evolving semantic networks.

6. Future Research Directions (100-150 words):
   a) Suggest at least two potential research questions or applications arising from your model.
   b) Briefly describe how these could advance our understanding of human cognition or AI capabilities.

Ensure your response demonstrates a deep understanding of semantic networks, cognitive development, and natural language processing. Be creative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of semantic networks and their application to language understanding",
            "The semantic network design is creative, well-structured, and incorporates the given concepts",
            "The cognitive development simulation is plausible and well-explained",
            "The language understanding application is complex and effectively utilizes the semantic network",
            "The network analysis shows insight into the mathematical and cognitive properties of the system",
            "Ethical and societal implications are thoughtfully considered",
            "Future research directions are innovative and relevant",
            "The response is well-organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
