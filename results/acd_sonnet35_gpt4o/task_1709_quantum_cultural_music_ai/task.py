import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_traditions = [
            {
                "tradition": "Tuvan throat singing",
                "region": "Tuva, Russia",
                "key_features": "Overtone singing, drone, spiritual significance"
            },
            {
                "tradition": "Gamelan music",
                "region": "Indonesia",
                "key_features": "Metallophones, cyclic structures, communal performance"
            }
        ]
        return {
            "1": random.choice(musical_traditions),
            "2": random.choice(musical_traditions)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network for analyzing and generating music from the endangered cultural tradition of {t['tradition']} from {t['region']}. Your system should address ethical concerns and preservation challenges while leveraging quantum computing principles for enhanced musical analysis and generation. Focus on the key features: {t['key_features']}.

Your response should include the following sections:

1. Quantum-Neural Architecture (300-350 words):
   a) Describe the overall structure of your quantum-inspired neural network.
   b) Explain how it incorporates quantum principles (e.g., superposition, entanglement) into its design.
   c) Detail how the network processes and represents musical information.
   d) Provide a visual representation of your architecture (use ASCII art or Unicode characters).
   e) Include pseudocode for a key quantum-inspired component of your network.

2. Musical Analysis and Generation (250-300 words):
   a) Explain how your system analyzes the unique features of {t['tradition']}.
   b) Describe the process of generating new music in this style.
   c) Discuss how quantum principles enhance the analysis or generation process.
   d) Provide an example of how your system would handle a specific musical element from {t['tradition']}.
   e) Describe a short (30-second) piece of music that your system might generate, explaining how it incorporates key elements of {t['tradition']}.

3. Cultural Preservation and Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of using AI to preserve and generate traditional music.
   b) Explain how your system ensures cultural authenticity and respects intellectual property.
   c) Propose guidelines for responsible use and development of your system.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum-inspired approach to classical machine learning methods for music analysis and generation.
   b) Discuss potential advantages and limitations of your approach.

5. Future Directions and Challenges (150-200 words):
   a) Propose two potential advancements or modifications to your system.
   b) Discuss technical and cultural challenges in implementing your system.
   c) Suggest a research agenda for further exploring the intersection of quantum computing, AI, and musical preservation.

6. Conclusion (50-100 words):
   Summarize the key aspects of your quantum-inspired neural network for {t['tradition']} and its potential impact on cultural preservation and AI research.

Ensure your response demonstrates a deep understanding of quantum computing principles, neural network architectures, and the cultural significance of {t['tradition']}. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section, adhering to the specified word counts. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of quantum computing principles and their application to neural networks.",
            f"The analysis and generation process for {t['tradition']} is well-explained and culturally sensitive.",
            "The ethical considerations are thoughtfully addressed, with concrete guidelines proposed.",
            "The comparative analysis shows a nuanced understanding of both quantum-inspired and classical approaches.",
            "The proposed future directions are innovative and demonstrate an understanding of current challenges in the field.",
            "The overall response shows strong interdisciplinary thinking, connecting concepts from quantum computing, AI, musicology, and ethics.",
            "The response includes a specific example of a generated musical piece that incorporates key elements of the tradition.",
            "The conclusion effectively summarizes the key aspects and potential impact of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
