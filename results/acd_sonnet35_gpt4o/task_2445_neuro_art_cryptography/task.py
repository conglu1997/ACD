import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_periods = [
            "Renaissance",
            "Baroque",
            "Impressionism",
            "Cubism",
            "Surrealism"
        ]
        historical_mysteries = [
            "The Lost Colony of Roanoke",
            "The Voynich Manuscript",
            "The Phaistos Disc",
            "Linear A script",
            "Rongorongo script of Easter Island"
        ]
        tasks = [
            {
                "art_period": random.choice(art_periods),
                "mystery": random.choice(historical_mysteries)
            },
            {
                "art_period": random.choice(art_periods),
                "mystery": random.choice(historical_mysteries)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the {t['art_period']} art period to encode and decode information, then use it to propose a solution to the mystery of {t['mystery']}. Your response should include:

1. Neural Network Design (300-350 words):
   a) Describe the key features of your neural network architecture and how they relate to the {t['art_period']} period.
   b) Explain how specific artistic elements or techniques from this period are translated into neural network components.
   c) Provide a diagram or detailed description of your network's structure, including layer types and connections.
   d) Discuss how your architecture enables encoding and decoding of information.

2. Encoding and Decoding Process (250-300 words):
   a) Explain how information would be encoded using your neural network.
   b) Describe the decoding process and how it relates to the artistic style of the {t['art_period']}.
   c) Discuss any unique features of your encoding/decoding process that distinguish it from traditional cryptographic methods.

3. Application to Historical Mystery (300-350 words):
   a) Briefly summarize the key aspects of {t['mystery']}.
   b) Explain how you would apply your neural network to analyze or decode information related to this mystery.
   c) Propose a hypothetical solution or new insight into the mystery based on your approach.
   d) Discuss how the artistic elements of your neural network might provide unique perspectives on the historical problem.

4. Comparative Analysis (200-250 words):
   a) Compare your neuro-art approach to traditional cryptographic or analytical methods for solving historical mysteries.
   b) Discuss potential advantages and limitations of your approach.
   c) Explain how your method might reveal patterns or connections that other approaches might miss.

5. Ethical and Cultural Implications (150-200 words):
   a) Discuss any ethical considerations in using AI and artistic-inspired methods to address historical mysteries.
   b) Explore potential cultural impacts of reinterpreting historical puzzles through the lens of art and neuroscience.
   c) Propose guidelines for responsible use of such interdisciplinary approaches in historical research.

Ensure your response demonstrates a deep understanding of neural network architectures, art history, and the chosen historical mystery. Be creative in your approach while maintaining scientific and historical plausibility. Use appropriate terminology from neuroscience, art history, and cryptography.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed neural network architecture inspired by the {t['art_period']} art period",
            "The encoding and decoding process is clearly explained and relates to the artistic style",
            f"The approach is creatively applied to the mystery of {t['mystery']}",
            "The comparative analysis demonstrates understanding of traditional and novel approaches",
            "Ethical and cultural implications are thoughtfully addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
