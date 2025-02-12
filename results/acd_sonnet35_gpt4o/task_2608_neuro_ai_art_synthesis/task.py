import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "visual cortex",
            "prefrontal cortex",
            "hippocampus",
            "amygdala",
            "motor cortex"
        ]
        art_styles = [
            "abstract expressionism",
            "surrealism",
            "digital art",
            "generative art",
            "neuroaesthetic art"
        ]
        ai_techniques = [
            "generative adversarial networks",
            "reinforcement learning",
            "neural style transfer",
            "transformer models",
            "evolutionary algorithms"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "art_style": random.choice(art_styles),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "art_style": random.choice(art_styles),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical brain-computer interface that allows direct neural control of an AI-powered digital art generation system, focusing on the {t['brain_region']} for neural input, the art style of {t['art_style']}, and utilizing {t['ai_technique']} as the primary AI technique. Then, analyze its implications for creativity, authorship, and the nature of consciousness. Your response should include:

1. System Design (300-350 words):
   a) Describe the overall architecture of your brain-computer interface and AI art generation system.
   b) Explain how neural signals from the {t['brain_region']} are interpreted and translated into artistic instructions.
   c) Detail how the {t['ai_technique']} is integrated into the art generation process.
   d) Discuss any novel features or innovations in your design that enable the creation of {t['art_style']}.

2. Neuroscientific Basis (250-300 words):
   a) Explain the role of the {t['brain_region']} in cognitive and creative processes.
   b) Discuss how your system leverages specific neural patterns or activities from this region.
   c) Address potential challenges in accurately interpreting and translating neural signals into artistic intent.

3. Artistic Process and Output (250-300 words):
   a) Describe the step-by-step process of creating art using your system, from neural input to final output.
   b) Explain how the characteristics of {t['art_style']} are achieved through the combination of neural input and AI processing.
   c) Provide a detailed example of how a specific artistic idea might be realized using your system.

4. Implications for Creativity and Authorship (250-300 words):
   a) Analyze how your system challenges traditional notions of artistic creativity and authorship.
   b) Discuss the balance between human creative intent and AI-generated content in the final artwork.
   c) Explore potential legal and ethical issues related to copyright and ownership of the created art.

5. Consciousness and Artistic Expression (200-250 words):
   a) Examine how your system might provide insights into the nature of consciousness and its role in artistic expression.
   b) Discuss whether the AI component could be considered to have its own form of artistic consciousness.
   c) Explore the philosophical implications of merging human cognition with AI in the context of art creation.

6. Societal Impact and Future Directions (200-250 words):
   a) Predict how widespread adoption of such systems might impact the art world and society at large.
   b) Propose two potential applications of your system beyond the realm of fine arts.
   c) Suggest future research directions for further integrating neuroscience, AI, and artistic creation.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and art theory. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of how the {t['brain_region']} can be used for neural input in the brain-computer interface.",
            f"The system design should effectively incorporate {t['ai_technique']} as the primary AI technique for art generation.",
            f"The artistic process and output should clearly explain how {t['art_style']} is achieved through the system.",
            "The analysis of implications for creativity, authorship, and consciousness should be thoughtful and well-reasoned.",
            "The response should show interdisciplinary knowledge integration across neuroscience, AI, and art theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
