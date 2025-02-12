import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "urban air pollution",
            "marine plastic pollution",
            "soil contamination",
            "freshwater eutrophication"
        ]
        bio_inspirations = [
            "coral reefs",
            "mycorrhizal networks",
            "bioluminescent organisms",
            "extremophile bacteria"
        ]
        tasks = [
            {
                'environment': random.choice(environments),
                'bio_inspiration': random.choice(bio_inspirations),
                'location': random.choice(['city center', 'public park', 'waterfront', 'industrial zone'])
            },
            {
                'environment': random.choice(environments),
                'bio_inspiration': random.choice(bio_inspirations),
                'location': random.choice(['museum', 'school campus', 'community garden', 'nature reserve'])
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired art installation that functions as an environmental monitoring and remediation system for {t['environment']}, inspired by {t['bio_inspiration']}, to be installed in a {t['location']}. Your response should include:

1. Conceptual Design (300-350 words):
   a) Describe the overall concept and appearance of your installation.
   b) Explain how it incorporates elements inspired by {t['bio_inspiration']}.
   c) Detail how the installation interacts with and responds to its environment.
   d) Discuss how it addresses the issue of {t['environment']}.

2. Technical Specifications (250-300 words):
   a) Outline the key components of your installation and their functions.
   b) Explain the mechanisms for environmental monitoring and data collection.
   c) Describe the remediation processes and their expected effectiveness.
   d) Discuss any innovative materials or technologies used in the installation.

3. Artistic and Public Engagement (200-250 words):
   a) Analyze the aesthetic aspects of your installation and their significance.
   b) Describe how the public can interact with or contribute to the installation.
   c) Propose methods for communicating scientific data and environmental issues through the artwork.

4. Environmental Impact Assessment (200-250 words):
   a) Evaluate the potential positive and negative environmental impacts of your installation.
   b) Discuss any lifecycle considerations, including construction, maintenance, and eventual decommissioning.
   c) Compare the effectiveness of your installation to traditional remediation methods for {t['environment']}.

5. Ethical Considerations (150-200 words):
   a) Analyze potential ethical issues related to your installation (e.g., data privacy, environmental justice).
   b) Discuss how your design addresses or mitigates these ethical concerns.
   c) Propose guidelines for responsible development and use of bio-inspired environmental art systems.

6. Future Developments (150-200 words):
   a) Suggest two potential extensions or improvements to your installation.
   b) Describe how these extensions could enhance its environmental impact or public engagement.
   c) Discuss how your concept could be adapted for different environmental issues or locations.

Ensure your response demonstrates a deep understanding of biology, environmental science, art, and engineering principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biology, environmental science, art, and engineering principles.",
            "The installation design is innovative, scientifically plausible, and effectively addresses the specified environmental issue.",
            "The technical specifications are well-explained and demonstrate feasibility.",
            "The artistic and public engagement aspects are creative and effectively communicate environmental issues.",
            "The environmental impact assessment is thorough and considers both positive and negative effects.",
            "Ethical considerations are thoughtfully analyzed and addressed.",
            "Future developments are innovative and build upon the initial concept.",
            "The response is well-structured, within the specified word count, and uses technical terminology appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
