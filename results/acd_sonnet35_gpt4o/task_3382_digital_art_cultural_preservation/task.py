import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_practices = [
            "Traditional Inuit throat singing",
            "Venetian glass bead making",
            "Mongolian horse head fiddle music",
            "Australian Aboriginal songlines"
        ]
        digital_technologies = [
            "Virtual Reality",
            "Augmented Reality",
            "Interactive Holography",
            "AI-driven Generative Art"
        ]
        
        tasks = {}
        for i in range(1, 3):
            practice = random.choice(endangered_practices)
            technology = random.choice(digital_technologies)
            tasks[str(i)] = {
                "endangered_practice": practice,
                "digital_technology": technology
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a digital art installation that preserves and interactively showcases the endangered cultural practice of {t['endangered_practice']}, primarily using {t['digital_technology']}. Then, analyze its potential impact on cultural preservation and education. Your response should include:\n\n1. Conceptual Design (250-300 words):\n   a) Describe the key features of your digital art installation.\n   b) Explain how it incorporates {t['digital_technology']} to showcase {t['endangered_practice']}.\n   c) Discuss how your design preserves the authenticity of the cultural practice.\n   d) Explain how users will interact with the installation.\n   e) Provide a brief visual description or sketch of the installation (50-100 words).\n\n2. Technical Implementation (200-250 words):\n   a) Outline the technical components required for your installation.\n   b) Explain how you'll capture and digitize the endangered cultural practice.\n   c) Describe any challenges in implementing this design and how you'd address them.\n   d) Include a simple diagram or pseudocode snippet illustrating a key aspect of your implementation.\n\n3. Cultural Preservation Analysis (200-250 words):\n   a) Discuss how your installation contributes to the preservation of {t['endangered_practice']}.\n   b) Analyze potential benefits and risks of digitizing this cultural practice.\n   c) Explain how your design maintains the cultural context and significance of the practice.\n\n4. Educational Impact (150-200 words):\n   a) Describe how your installation could be used as an educational tool.\n   b) Propose a specific educational program or curriculum that could incorporate your installation.\n   c) Discuss how this might enhance cross-cultural understanding and appreciation.\n\n5. Ethical Considerations (150-200 words):\n   a) Identify and discuss key ethical considerations in digitizing and showcasing {t['endangered_practice']}.\n   b) Explain how you've addressed these ethical concerns in your design.\n   c) Propose guidelines for the responsible development of similar cultural preservation projects.\n\n6. Future Developments (150-200 words):\n   a) Suggest two potential expansions or improvements to your installation.\n   b) Discuss how emerging technologies might further enhance cultural preservation efforts.\n   c) Propose a research study to evaluate the long-term impact of your installation on cultural preservation.\n\n7. Critical Analysis (100-150 words):\n   a) Consider potential criticisms or controversies that might arise from your installation.\n   b) Discuss how you would address these concerns and potentially modify your design in response.\n\nEnsure your response demonstrates a deep understanding of digital technologies, art installation design, and cultural anthropology. Be innovative in your approach while maintaining cultural sensitivity and ethical responsibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Conceptual Design:') followed by your response for that section. Your total response should be between 1200-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design effectively incorporates {t['digital_technology']} to showcase {t['endangered_practice']}",
            "The installation preserves the authenticity and cultural context of the practice",
            "The technical implementation is well-explained and addresses potential challenges",
            "The response demonstrates a deep understanding of cultural preservation issues",
            "The educational impact and potential applications are thoughtfully explored",
            "Ethical considerations are thoroughly addressed",
            "The response shows creativity and innovation while maintaining cultural sensitivity",
            "A visual description or sketch of the installation is provided",
            "Potential criticisms or controversies are considered and addressed",
            "All required sections (1-7) are present and adequately addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
