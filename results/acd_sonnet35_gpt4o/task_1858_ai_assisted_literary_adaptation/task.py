import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        literary_works = [
            "Pride and Prejudice by Jane Austen",
            "1984 by George Orwell",
            "To Kill a Mockingbird by Harper Lee",
            "The Great Gatsby by F. Scott Fitzgerald",
            "Frankenstein by Mary Shelley"
        ]
        adaptation_types = [
            "Interactive visual novel",
            "Branching narrative podcast",
            "Augmented reality experience",
            "Social media storytelling",
            "AI-generated continuation"
        ]
        
        task1 = {
            'literary_work': random.choice(literary_works),
            'adaptation_type': random.choice(adaptation_types)
        }
        
        task2 = {
            'literary_work': random.choice(literary_works),
            'adaptation_type': random.choice(adaptation_types)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that adapts the classic literary work '{t['literary_work']}' into a modern, interactive narrative in the form of a {t['adaptation_type']}, while preserving the essence of the original work. Then, analyze its implications for art, education, and copyright. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for literary adaptation.
   b) Explain how your system analyzes and understands the original text.
   c) Detail the process of generating the adapted narrative.
   d) Discuss how your system ensures preservation of the original work's themes and style.

2. Adaptation Concept (200-250 words):
   a) Provide a brief overview of your adaptation concept.
   b) Explain how the {t['adaptation_type']} format enhances or transforms the original narrative.
   c) Describe one key scene or element from the original work and how it's adapted in your concept.

3. Interactive Elements (150-200 words):
   a) Describe the interactive features of your adaptation.
   b) Explain how these features engage the audience while respecting the original work.
   c) Discuss how user interactions might influence the narrative progression.

4. Ethical Considerations (200-250 words):
   a) Analyze potential copyright issues and propose solutions.
   b) Discuss the ethical implications of using AI to adapt classic literature.
   c) Address concerns about AI potentially replacing human creativity in literature.

5. Educational and Artistic Impact (200-250 words):
   a) Explain how your AI-assisted adaptation could be used in educational settings.
   b) Discuss the potential impact on literary appreciation and analysis.
   c) Analyze how this technology might influence the future of storytelling and artistic expression.

6. Technical Challenges and Future Work (150-200 words):
   a) Identify key technical challenges in implementing your system.
   b) Propose solutions or areas for future research to address these challenges.
   c) Suggest potential expansions or applications of your system beyond literary adaptation.

Ensure your response demonstrates a deep understanding of literature, natural language processing, and AI ethics. Be creative in your adaptation concept while maintaining respect for the original work. Use appropriate terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the original literary work and its key elements.",
            "The AI system architecture is well-designed and adequately explained.",
            "The adaptation concept is creative and effectively utilizes the specified format.",
            "Interactive elements are innovative and enhance the narrative experience.",
            "Ethical considerations, including copyright issues, are thoroughly addressed.",
            "The educational and artistic impact of the adaptation is insightfully analyzed.",
            "Technical challenges are identified and potential solutions are proposed.",
            "The response maintains a balance between technological innovation and respect for the original work."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
