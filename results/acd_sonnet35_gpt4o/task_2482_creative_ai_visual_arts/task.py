import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artistic_styles = [
            "Impressionism",
            "Cubism",
            "Surrealism",
            "Abstract Expressionism",
            "Pop Art"
        ]
        creative_processes = [
            "Analogical reasoning",
            "Conceptual blending",
            "Divergent thinking",
            "Insight problem solving",
            "Combinatorial creativity"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "artistic_style": random.choice(artistic_styles),
                "creative_process": random.choice(creative_processes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics human creative processes in visual arts, focusing on the {t['artistic_style']} style and incorporating the cognitive process of {t['creative_process']}. Then, analyze its implications for creativity and AI development. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI creativity system.
   b) Explain how it incorporates principles from cognitive science and art theory.
   c) Detail how your system models the {t['creative_process']} process.
   d) Provide a diagram or pseudocode representation of a key component in your system.

2. Artistic Style Modeling (200-250 words):
   a) Explain how your system captures the essence of {t['artistic_style']}.
   b) Discuss the specific features or techniques your AI uses to generate art in this style.
   c) Address any challenges in translating human artistic processes to AI.

3. Creative Process Simulation (200-250 words):
   a) Describe how your system simulates the {t['creative_process']} in generating artwork.
   b) Explain the cognitive principles underlying this creative process.
   c) Provide an example scenario of how your AI system might create a new artwork.

4. Evaluation Metrics (150-200 words):
   a) Propose methods for evaluating the creativity and artistic quality of your AI's outputs.
   b) Discuss the challenges in measuring machine creativity compared to human creativity.
   c) Suggest how your evaluation metrics might be applied to other AI creative systems.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the potential impact of AI-generated art on the art world and society.
   b) Address concerns about AI potentially replacing human artists.
   c) Explore the philosophical question: Can AI truly be creative?

6. Future Developments and Applications (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how this technology might be applied in other creative domains.
   c) Speculate on how AI creativity systems might evolve in the next decade.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and art theory. Be creative in your approach while maintaining scientific and artistic plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Adhere to the specified word count ranges for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content",
            f"The system design clearly incorporates the {t['creative_process']} process and addresses the {t['artistic_style']} style",
            "The response includes a diagram or pseudocode representation of a key system component",
            "The artistic style modeling section demonstrates a deep understanding of the chosen style",
            "The creative process simulation provides a clear example scenario",
            "The response proposes concrete methods for evaluating AI creativity",
            "The ethical and philosophical implications are thoughtfully discussed",
            "The response demonstrates a deep understanding of cognitive science, AI, and art theory",
            "The response is creative, scientifically plausible, and well-explained",
            "The response adheres to the specified word count ranges for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
