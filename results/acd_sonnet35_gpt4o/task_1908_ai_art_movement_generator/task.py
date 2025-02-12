import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'historical_movements': [
                    {'name': 'Surrealism', 'technique': 'Juxtaposition of unrelated objects', 'theme': 'Subconscious mind'},
                    {'name': 'Pop Art', 'technique': 'Mass media imagery', 'theme': 'Consumer culture'}
                ],
                'contemporary_trend': 'Climate change awareness',
                'artistic_medium': 'Digital art'
            },
            '2': {
                'historical_movements': [
                    {'name': 'Cubism', 'technique': 'Multiple perspectives in a single plane', 'theme': 'Fragmentation of reality'},
                    {'name': 'Abstract Expressionism', 'technique': 'Gestural brushstrokes', 'theme': 'Emotional intensity'}
                ],
                'contemporary_trend': 'Social media influence',
                'artistic_medium': 'Mixed media installations'
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate a new art movement by combining elements from {t['historical_movements'][0]['name']} and {t['historical_movements'][1]['name']}, while incorporating the contemporary trend of {t['contemporary_trend']}. The primary artistic medium for this new movement should be {t['artistic_medium']}.

Your response should include the following components:

1. Art Movement Analysis (200-250 words):
   a) Describe the key characteristics, techniques, and themes of {t['historical_movements'][0]['name']} and {t['historical_movements'][1]['name']}.
   b) Explain how these movements reflected their respective cultural contexts.
   c) Analyze the contemporary trend of {t['contemporary_trend']} and its potential impact on artistic expression.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system for generating a new art movement.
   b) Explain how your system would process and combine elements from the historical art movements.
   c) Describe how your system would incorporate the contemporary trend into its artistic generation.
   d) Discuss how your system would ensure the generated movement is novel and coherent.

3. New Art Movement Description (200-250 words):
   a) Provide a name and brief manifesto for the AI-generated art movement.
   b) Describe the key visual characteristics and philosophical underpinnings of the movement.
   c) Explain how the movement reflects elements from its source movements and the contemporary trend.
   d) Discuss how the movement utilizes {t['artistic_medium']} as its primary medium.

4. Sample Artwork Generation (200-250 words):
   a) Describe a hypothetical artwork that exemplifies the new movement.
   b) Include details on the artwork's composition, color palette, and use of {t['artistic_medium']}.
   c) Explain how this artwork incorporates techniques from {t['historical_movements'][0]['name']} ('{t['historical_movements'][0]['technique']}') and {t['historical_movements'][1]['name']} ('{t['historical_movements'][1]['technique']}').
   d) Discuss how the artwork addresses the theme of {t['contemporary_trend']}.
   e) Analyze the potential impact and interpretation of this artwork in the contemporary art world.

5. Evaluation Metrics (150-200 words):
   a) Propose 3-4 specific metrics to evaluate the success and coherence of the AI-generated art movement.
   b) Explain how each metric assesses the movement's novelty, artistic merit, and cultural relevance.
   c) Describe a potential experiment or study to test these metrics.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of AI-generated art movements.
   b) Address concerns about the role of AI in creative processes traditionally associated with human artists.
   c) Propose guidelines for responsible development and use of your AI system in the art world.

7. Future Implications (150-200 words):
   a) Discuss how AI-generated art movements might impact the future of art history and criticism.
   b) Explore potential collaborations between human artists and AI systems in creating new artistic paradigms.
   c) Speculate on how this technology might evolve and influence other creative fields.

Ensure your response demonstrates a deep understanding of art history, contemporary culture, and AI capabilities. Be creative in your approach while maintaining plausibility within the constraints of current AI technology. Use appropriate terminology from art theory and AI research.

Format your response with clear headings for each section and subsections labeled a, b, c, etc. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['historical_movements'][0]['name']} and {t['historical_movements'][1]['name']}, including their techniques and themes.",
            f"The proposed AI system design effectively combines elements from the historical movements and incorporates the trend of {t['contemporary_trend']}.",
            f"The generated art movement is creative, novel, and successfully utilizes {t['artistic_medium']} as its primary medium.",
            f"The sample artwork description effectively incorporates techniques from both historical movements and addresses the theme of {t['contemporary_trend']}.",
            "The evaluation metrics are specific, measurable, and relevant to assessing the success of an AI-generated art movement.",
            "The ethical considerations and future implications are thoughtfully addressed and show insight into the potential impact of AI on the art world.",
            "The response maintains a balance between creativity and plausibility throughout all sections, using appropriate art theory and AI terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0