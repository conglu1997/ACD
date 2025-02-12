import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            "anxiety",
            "depression",
            "stress",
            "grief",
            "anger"
        ]
        musical_elements = [
            "rhythm",
            "harmony",
            "melody",
            "timbre",
            "dynamics"
        ]
        cognitive_principles = [
            "attention regulation",
            "emotional processing",
            "memory consolidation",
            "neural plasticity",
            "interoception"
        ]
        return {
            "1": {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "cognitive_principle": random.choice(cognitive_principles)
            },
            "2": {
                "emotional_state": random.choice(emotional_states),
                "musical_element": random.choice(musical_elements),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates personalized music therapy sessions based on real-time emotional states and cognitive neuroscience principles, then analyze its potential impact on mental health treatment and creative arts therapy. Your system should focus on the emotional state of {t['emotional_state']}, the musical element of {t['musical_element']}, and the cognitive principle of {t['cognitive_principle']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI music therapy system. (75-100 words)
   b) Explain how it incorporates real-time emotional state detection. (75-100 words)
   c) Detail how the system integrates the specified musical element and cognitive principle. (75-100 words)
   d) Discuss any novel algorithms or techniques used in your design. (75-100 words)

2. Emotional-Musical Mapping (250-300 words):
   a) Explain the theoretical basis for mapping {t['emotional_state']} to {t['musical_element']}. (80-100 words)
   b) Describe how your system adapts musical output based on detected emotional states. (80-100 words)
   c) Discuss how the principle of {t['cognitive_principle']} informs this mapping process. (80-100 words)

3. Music Generation Process (250-300 words):
   a) Detail the step-by-step process your system uses to generate therapeutic music. (80-100 words)
   b) Explain how it balances adherence to therapeutic principles with musical creativity. (80-100 words)
   c) Provide an example of how a specific musical piece might be generated for the given emotional state. (80-100 words)

4. Therapeutic Efficacy Analysis (200-250 words):
   a) Propose methods to evaluate the therapeutic effectiveness of your AI-generated music. (65-85 words)
   b) Discuss potential challenges in measuring emotional regulation outcomes. (65-85 words)
   c) Compare your approach to traditional music therapy techniques. (65-85 words)

5. Cognitive Neuroscience Integration (200-250 words):
   a) Explain how your system incorporates current understanding of {t['cognitive_principle']}. (65-85 words)
   b) Discuss how this integration enhances the therapeutic potential of the generated music. (65-85 words)
   c) Propose a hypothesis about how your system might contribute to our understanding of music cognition. (65-85 words)

6. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss potential ethical issues in using AI for music therapy and emotional regulation. (65-85 words)
   b) Analyze the potential impact of your system on mental health treatment and the field of creative arts therapy. (65-85 words)
   c) Propose guidelines for the responsible development and use of AI in therapeutic settings. (65-85 words)

Ensure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering ethical implications.

Format your response with clear headings for each section and numbered subsections as outlined above. Adhere to the word count guidelines for each subsection. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the emotional state of {t['emotional_state']}, the musical element of {t['musical_element']}, and the cognitive principle of {t['cognitive_principle']}",
            "The proposed system demonstrates a deep understanding of music theory, cognitive neuroscience, and artificial intelligence",
            "The response includes innovative approaches while maintaining scientific plausibility",
            "The system architecture and music generation process are well-described and logically consistent",
            "The response thoughtfully addresses ethical considerations and societal impacts",
            "The proposed evaluation methods and analysis of therapeutic efficacy are well-reasoned",
            "The response demonstrates creative problem-solving in integrating multiple disciplines",
            "The response adheres to the specified format and word count guidelines",
            "Each subsection provides sufficient detail and depth as per the instructions",
            "The response maintains a balance between technical accuracy and clarity of explanation"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
