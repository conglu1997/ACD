import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_periods = [
            "Renaissance",
            "Industrial Revolution",
            "Roaring Twenties",
            "Post-World War II",
            "Digital Age",
            "Ancient Greece",
            "Ming Dynasty",
            "Victorian Era"
        ]
        cultural_movements = [
            "Romanticism",
            "Modernism",
            "Postmodernism",
            "Surrealism",
            "Cyberpunk",
            "Art Nouveau",
            "Dadaism",
            "Futurism"
        ]
        artifact_types = [
            "Visual Art",
            "Music",
            "Literature",
            "Fashion",
            "Architecture",
            "Film",
            "Dance",
            "Cuisine"
        ]
        return {
            "1": {
                "period": random.choice(historical_periods),
                "artifact": random.choice(artifact_types)
            },
            "2": {
                "movement": random.choice(cultural_movements),
                "artifact": random.choice(artifact_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = """Design an AI system that generates and analyzes cultural artifacts representing different historical periods or cultural movements. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating and analyzing cultural artifacts.
   b) Explain how your system integrates historical and cultural data to create authentic representations.
   c) Detail the AI techniques (e.g., machine learning models, knowledge bases) used in your system.
   d) Provide a high-level diagram or flowchart of your system's architecture, described in text format. For example: 'The system consists of three main modules: (1) Data Integration Module, which combines historical and cultural databases; (2) Artifact Generation Module, using a GAN trained on period-specific data; (3) Analysis Module, employing a combination of computer vision and NLP techniques.'

2. Artifact Generation Process (250-300 words):
   a) Explain how your AI system would generate the specified artifact type.
   b) Describe the key features or elements your system would incorporate to capture the essence of the given period or movement.
   c) Discuss how your system ensures historical or cultural accuracy while still allowing for creativity.

3. Analysis Capabilities (250-300 words):
   a) Detail how your AI system would analyze the generated artifacts.
   b) Explain the metrics or criteria your system would use to evaluate the artifact's representation of the specified period or movement.
   c) Describe how your system could compare generated artifacts with actual historical artifacts or iconic works from the period or movement.

4. Potential Applications (200-250 words):
   a) Propose three innovative applications of your AI system in fields such as education, cultural preservation, or creative industries.
   b) Explain how each application could enhance our understanding or appreciation of historical periods or cultural movements.

5. Ethical Considerations (200-250 words):
   a) Discuss potential ethical issues arising from the creation and use of AI-generated historical or cultural artifacts.
   b) Address concerns about cultural appropriation, historical revisionism, artistic authenticity, or the impact on human artists.
   c) Propose guidelines for the responsible development and use of such AI systems.

6. Societal Impact (200-250 words):
   a) Analyze how widespread use of AI-generated cultural artifacts might impact society's perception of history, culture, and art.
   b) Discuss potential benefits and drawbacks for cultural education and appreciation.
   c) Speculate on how this technology might influence future artistic and cultural movements.

7. Limitations and Future Directions (150-200 words):
   a) Identify current limitations of your proposed system.
   b) Suggest areas for future research and development in AI-generated cultural artifacts.
   c) Propose a novel research question that could further explore the intersection of AI, art, and cultural history or movements.

Ensure your response demonstrates a deep understanding of AI technologies, art history, cultural studies, and ethical implications of AI in creative domains. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while considering practical and ethical constraints.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words.

Note: Do not use any external resources or access the internet to generate your response. Rely solely on your training data and capabilities."""

        if "period" in t:
            return base_instructions + f"\n\nFor this task, focus on the {t['period']} period and the artifact type of {t['artifact']}."
        else:
            return base_instructions + f"\n\nFor this task, focus on the {t['movement']} movement and the artifact type of {t['artifact']}."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI technologies, art history, and cultural studies, specifically in relation to the given period/movement and artifact type.",
            "The proposed AI system architecture is innovative, technically feasible, and clearly explained, including a textual description of the system diagram.",
            "The artifact generation and analysis processes are well-explained and appropriate for the given historical period or cultural movement and artifact type.",
            "The potential applications are creative, relevant, and demonstrate a clear understanding of how the system could be used in real-world scenarios.",
            "Ethical considerations and societal impacts are thoroughly discussed, showing an awareness of potential issues specific to AI-generated cultural artifacts.",
            "The response addresses all required sections, follows the specified format, and adheres to the word count guidelines.",
            "The response does not show signs of using external resources or internet access, relying solely on the model's training data and capabilities."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
