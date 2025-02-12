import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'planetary_type': 'Super-Earth',
                'biochemistry': 'Silicon-based',
                'environment': 'Methane atmosphere'
            },
            {
                'planetary_type': 'Ocean world',
                'biochemistry': 'Ammonia-based',
                'environment': 'Subsurface ocean'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical communication protocol for potential extraterrestrial life on a {t['planetary_type']} with {t['biochemistry']} biochemistry in a {t['environment']}. Your protocol should be based on astrobiological principles and information theory. Provide your response in the following format:

1. Astrobiological Context (200-250 words):
   a) Describe the potential characteristics of life forms on this planet, considering the given biochemistry and environment.
   b) Discuss how these characteristics might influence their sensory and cognitive capabilities.
   c) Explain potential evolutionary pressures that could shape their communication needs and abilities.

2. Communication Medium (150-200 words):
   a) Propose a suitable medium for communication (e.g., electromagnetic waves, chemical signals, gravitational waves).
   b) Justify your choice based on the planetary characteristics and potential life forms.
   c) Discuss any unique challenges or advantages of this medium in the given environment.

3. Information Encoding (250-300 words):
   a) Design an information encoding system suitable for the chosen medium and potential life forms.
   b) Explain how your encoding system incorporates principles from information theory.
   c) Describe how this system could convey complex concepts or abstract ideas.
   d) Provide a simple example of how a basic message would be encoded.

4. Protocol Structure (200-250 words):
   a) Outline the key components of your communication protocol (e.g., initiation sequence, error correction, message structure).
   b) Explain how your protocol addresses potential differences in perception and cognition between humans and the extraterrestrial life forms.
   c) Discuss how your protocol could evolve or adapt over time as communication progresses.

5. Universal Concepts (150-200 words):
   a) Propose 3-5 concepts or principles that you believe could serve as a foundation for mutual understanding.
   b) Explain why you think these concepts might be universal across different forms of life and intelligence.
   c) Describe how these concepts are incorporated into your communication protocol.

6. Limitations and Challenges (150-200 words):
   a) Discuss potential limitations or challenges in implementing your communication protocol.
   b) Propose methods to overcome or mitigate these challenges.
   c) Explain how your protocol could be verified or tested within the constraints of current human technology.

7. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of establishing communication with extraterrestrial life.
   b) Address any risks or concerns associated with your specific communication protocol.
   c) Propose guidelines for responsible use of your protocol in potential first contact scenarios.

Ensure your response demonstrates a deep understanding of astrobiology, information theory, and linguistics. Use appropriate technical terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of astrobiology, information theory, and linguistics.",
            "The proposed communication protocol is innovative, scientifically plausible, and well-justified.",
            "The information encoding system effectively incorporates principles from information theory.",
            "The protocol structure adequately addresses potential differences in perception and cognition between humans and extraterrestrial life forms.",
            "The proposed universal concepts are well-reasoned and integrated into the communication protocol.",
            "The discussion of limitations, challenges, and ethical considerations is thorough and insightful.",
            "The response shows strong integration of knowledge from multiple scientific disciplines.",
            "The response includes creative solutions while maintaining scientific rigor.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
