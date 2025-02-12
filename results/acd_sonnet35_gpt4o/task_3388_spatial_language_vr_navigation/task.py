import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Ancient Mayan temple complex",
            "Futuristic space station",
            "Underwater bioluminescent cave system",
            "Escher-inspired impossible architecture",
            "Microscopic world inside a human cell"
        ]
        spatial_features = [
            "Non-Euclidean geometry",
            "Teleportation portals",
            "Gravity-defying pathways",
            "Shape-shifting rooms",
            "Time-dilated zones"
        ]
        navigation_challenges = [
            "Color-based puzzle locks",
            "Sound-activated bridges",
            "Memory-dependent pathways",
            "Perspective-shift obstacles",
            "Language-encoded riddles"
        ]
        
        return {
            "1": {
                "environment": random.choice(environments),
                "spatial_feature": random.choice(spatial_features),
                "navigation_challenge": random.choice(navigation_challenges)
            },
            "2": {
                "environment": random.choice(environments),
                "spatial_feature": random.choice(spatial_features),
                "navigation_challenge": random.choice(navigation_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system that translates natural language spatial descriptions into a navigable 3D virtual environment based on a {t['environment']} incorporating {t['spatial_feature']}, and then guides a user through this environment using generated linguistic instructions to overcome a {t['navigation_challenge']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your system for translating language to 3D environments.\n   b) Explain how your system generates navigational instructions.\n   c) Detail how you incorporate the specified spatial feature into the environment generation.\n   d) Discuss how you implement the navigation challenge in both the environment and instructions.\n   e) Include a high-level diagram or pseudocode to illustrate your system's architecture.\n\n2. Natural Language Processing (250-300 words):\n   a) Explain how your system interprets complex spatial descriptions in natural language.\n   b) Describe techniques used to handle ambiguity in spatial language.\n   c) Discuss how cultural or linguistic variations in spatial descriptions are addressed.\n   d) Provide an example of how your system would interpret a complex spatial description.\n\n3. 3D Environment Generation (250-300 words):\n   a) Detail the process of converting linguistic descriptions into 3D models.\n   b) Explain how you ensure coherence between the language and the generated environment.\n   c) Describe how you implement the specified spatial feature in the 3D world.\n   d) Discuss any novel algorithms or techniques you use for efficient 3D generation.\n\n4. Navigation Instruction Generation (250-300 words):\n   a) Explain how your system creates clear and accurate navigation instructions.\n   b) Describe how you adapt the language to the user's perspective in the virtual environment.\n   c) Detail how you incorporate the navigation challenge into the instructions.\n   d) Provide an example of a complex navigation instruction your system might generate.\n\n5. User Interaction and Feedback (200-250 words):\n   a) Describe how users interact with your system in the virtual environment.\n   b) Explain how you handle user confusion or mistakes in following instructions.\n   c) Discuss how user feedback is incorporated to improve the system.\n   d) Propose a method for measuring user engagement and learning in real-time.\n\n6. Evaluation Metrics (200-250 words):\n   a) Propose methods to evaluate the accuracy of your 3D environment generation.\n   b) Describe how you would assess the clarity and effectiveness of the navigation instructions.\n   c) Suggest ways to measure user engagement and learning in the virtual environment.\n   d) Discuss how you would validate the system's effectiveness across different user groups.\n\n7. Ethical Considerations and Limitations (150-200 words):\n   a) Discuss potential ethical issues related to spatial cognition manipulation in virtual environments.\n   b) Address limitations of your system and potential biases in language-to-3D translations.\n   c) Propose guidelines for responsible use of this technology in educational or therapeutic contexts.\n\n8. Case Study (200-250 words):\n   Provide a detailed case study of how your system would handle the specific environment, spatial feature, and navigation challenge given in this task. Include examples of generated 3D elements and navigation instructions.\n\nEnsure your response demonstrates a deep understanding of spatial cognition, linguistics, and virtual reality technologies. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1800-2200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of spatial cognition, linguistics, and virtual reality technologies.",
            "The system design effectively translates natural language spatial descriptions into 3D environments.",
            "The navigation instruction generation is clear, accurate, and adapts to the user's perspective.",
            "The specified spatial feature and navigation challenge are well-integrated into both the environment and instructions.",
            "The response addresses all required sections comprehensively and coherently.",
            "The proposed evaluation metrics and ethical considerations are thoughtful and relevant.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The case study effectively demonstrates the system's capabilities for the given scenario.",
            "The response includes appropriate examples and illustrations as requested.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
