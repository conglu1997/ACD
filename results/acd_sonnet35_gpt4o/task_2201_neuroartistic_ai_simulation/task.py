import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artists = [
            {
                "name": "Vincent van Gogh",
                "style": "Post-Impressionism",
                "notable_work": "The Starry Night",
                "neurological_feature": "Synesthesia",
                "color_palette": "Vibrant yellows, blues, and greens"
            },
            {
                "name": "Salvador Dalí",
                "style": "Surrealism",
                "notable_work": "The Persistence of Memory",
                "neurological_feature": "Hypnagogic imagery",
                "color_palette": "Muted earth tones with pops of bright color"
            },
            {
                "name": "Frida Kahlo",
                "style": "Naïve Art/Primitivism",
                "notable_work": "The Two Fridas",
                "neurological_feature": "Chronic pain perception",
                "color_palette": "Rich, vibrant colors inspired by Mexican folk art"
            },
            {
                "name": "Jackson Pollock",
                "style": "Abstract Expressionism",
                "notable_work": "No. 5, 1948",
                "neurological_feature": "Kinesthetic awareness",
                "color_palette": "Layered splatters of various colors"
            }
        ]
        return {
            "1": random.choice(artists),
            "2": random.choice(artists)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates the cognitive processes of {t['name']}, known for their {t['style']} style and the artwork '{t['notable_work']}'. Your system should focus on modeling the artist's {t['neurological_feature']} and its influence on their artistic process, considering their typical color palette: {t['color_palette']}. Your response should include:\n\n" + \
               "1. Neurocognitive Model (250-300 words):\n" + \
               "   a) Describe the key components of your AI system's neurocognitive model.\n" + \
               "   b) Explain how you incorporate the artist's specific neurological feature into the model.\n" + \
               "   c) Discuss how your model simulates the interaction between perception, memory, and creativity.\n\n" + \
               "2. Artistic Style Simulation (200-250 words):\n" + \
               "   a) Detail how your AI system captures and reproduces the artist's unique style and color palette.\n" + \
               "   b) Explain any novel approaches to representing artistic techniques in your model.\n" + \
               "   c) Describe how your system balances imitation of existing works with novel creation.\n\n" + \
               "3. Training and Data Processing (200-250 words):\n" + \
               "   a) Outline the data sources and types you would use to train your AI system.\n" + \
               "   b) Explain how you would preprocess and represent artistic and neuroscientific data.\n" + \
               "   c) Discuss any ethical considerations in using an artist's work and personal information.\n\n" + \
               "4. Output Analysis and Validation (200-250 words):\n" + \
               "   a) Propose methods for evaluating the authenticity and quality of the AI-generated artworks.\n" + \
               "   b) Describe how you would validate the accuracy of the simulated cognitive processes.\n" + \
               "   c) Suggest experiments to compare the AI's artistic process with human artists.\n\n" + \
               "5. Implications and Applications (150-200 words):\n" + \
               "   a) Discuss potential insights this system might provide into human creativity and cognition.\n" + \
               "   b) Explore possible applications in fields such as art therapy, neuroscience research, or art education.\n" + \
               "   c) Consider the philosophical implications of simulating an artist's cognitive processes.\n\n" + \
               "Ensure your response demonstrates a deep understanding of neuroscience, art history, and AI principles. Be creative in your approach while maintaining scientific and artistic plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.\n\n" + \
               "Format your response with clear headings for each section. Number your paragraphs within each section. Your total response should be between 1000-1250 words. Include at least one equation or formula using LaTeX notation to represent a key concept in your AI system."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of neuroscience, art history, and AI principles, with specific reference to {t['name']}'s style and {t['neurological_feature']}",
            f"The proposed AI system effectively integrates {t['name']}'s neurological feature into the cognitive model and considers their typical color palette: {t['color_palette']}",
            "The approach to simulating artistic style is innovative, plausible, and balances imitation with novel creation",
            "The training and data processing methods are well-thought-out, addressing ethical considerations and potential biases",
            "The output analysis and validation techniques are rigorous, appropriate, and include specific experiments",
            "The discussion of implications and applications is insightful, considering multiple perspectives and potential impacts on various fields",
            "The response includes at least one relevant equation or formula using LaTeX notation",
            "The response adheres to the specified format and word count requirements"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
