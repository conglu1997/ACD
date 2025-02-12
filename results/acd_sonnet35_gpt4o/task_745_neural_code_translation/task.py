import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                "name": "Broca's area",
                "function": "Speech production",
                "challenge": "Decoding intent and semantic content from motor planning signals"
            },
            {
                "name": "Wernicke's area",
                "function": "Language comprehension",
                "challenge": "Mapping complex semantic networks to linguistic structures"
            },
            {
                "name": "Hippocampus",
                "function": "Memory formation and spatial navigation",
                "challenge": "Translating episodic and spatial memories into narrative form"
            },
            {
                "name": "Prefrontal cortex",
                "function": "Executive function and decision-making",
                "challenge": "Interpreting abstract thought processes and decision rationales"
            }
        ]
        return {str(i+1): region for i, region in enumerate(random.sample(brain_regions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI system that can translate neural activity patterns from the {t['name']} into natural language, and vice versa. Your system should focus on the brain region's function of {t['function']}, addressing the specific challenge of {t['challenge']}.

Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for neural code translation.
   b) Explain how your system interfaces with the brain to record and stimulate neural activity.
   c) Outline the AI and machine learning techniques used for encoding and decoding neural signals.
   d) Cite at least one relevant scientific study or paper to support your proposed system design.

2. Neural-Linguistic Mapping (200-250 words):
   a) Explain your approach to mapping between neural activity patterns and linguistic constructs.
   b) Discuss how your system handles the specific challenge mentioned for this brain region.
   c) Provide an example of how a simple thought or sentence might be encoded in neural activity and then decoded by your system. Use the following format:
      Thought/Sentence: [Insert thought or sentence]
      Neural Encoding: [Describe the neural activity pattern]
      Decoded Output: [Show the system's translation]

3. Training and Data Requirements (150-200 words):
   a) Describe the type and amount of data needed to train your system.
   b) Explain any ethical considerations in data collection and use.
   c) Discuss potential methods for bootstrapping the system with limited invasive neural recordings.

4. Potential Applications (150-200 words):
   a) Propose three potential applications of your neural code translation system.
   b) For each application, discuss both beneficial outcomes and potential risks or ethical concerns.

5. Limitations and Future Directions (150-200 words):
   a) Identify three major limitations or challenges of your proposed system.
   b) For each limitation, suggest a potential avenue for future research to address it.
   c) Discuss how advancements in neuroscience or AI might impact the development of such systems in the next decade.

6. Philosophical Implications (150-200 words):
   a) Discuss how a successful neural code translation system might impact our understanding of consciousness, thought, and language.
   b) Explore potential implications for concepts like free will, privacy of thought, and the nature of the self.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and linguistics. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent design for an AI system that can translate neural activity patterns from the {t['name']} into natural language, and vice versa",
            f"The system architecture addresses the specific function of {t['function']} and the challenge of {t['challenge']}",
            "The neural-linguistic mapping approach is well-explained and scientifically plausible",
            "The training and data requirements are realistic and consider ethical implications",
            "The potential applications are innovative and their risks are thoughtfully analyzed",
            "The limitations and future directions show a deep understanding of current challenges in neuroscience and AI",
            "The philosophical implications are insightfully discussed, demonstrating an understanding of consciousness and language",
            "The overall response demonstrates interdisciplinary knowledge integration and creative problem-solving",
            "The response follows the specified format, uses clear headings for each section, and adheres to the 1000-1300 word count guideline",
            "The response includes at least one citation of a relevant scientific study or paper",
            "The neural-linguistic mapping example follows the specified format: Thought/Sentence, Neural Encoding, Decoded Output"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
