import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {"domain": "Emergency Response", "time_alteration": "Dilation"},
            {"domain": "Space Exploration", "time_alteration": "Compression"},
            {"domain": "Cognitive Enhancement", "time_alteration": "Synchronization"},
            {"domain": "Trauma Therapy", "time_alteration": "Fragmentation"}
        ]
        return {
            "1": random.choice(domains),
            "2": random.choice(domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical system capable of altering human time perception, then apply it to solve complex problems in the domain of {t['domain']} using the time alteration method of {t['time_alteration']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your temporal perception modulation system.
   b) Explain how your system interfaces with the human brain to alter time perception.
   c) Detail the mechanisms used to achieve the specified time alteration method.
   d) Include a high-level diagram of your system architecture (describe it in words).

2. Neuroscientific Basis (200-250 words):
   a) Explain the current understanding of time perception in the human brain.
   b) Describe how your system leverages or modifies these neural mechanisms.
   c) Discuss any potential neuroplasticity considerations for long-term use.

3. Physics and Computation (200-250 words):
   a) Explain any relevant physical principles (e.g., relativity) that inform your system's design.
   b) Describe the computational models used to calculate and implement time perception alterations.
   c) Discuss how your system maintains coherence between altered subjective time and objective reality.

4. Application to {t['domain']} (250-300 words):
   a) Explain how your system's {t['time_alteration']} capability could be applied to solve problems in the specified domain.
   b) Provide a specific scenario and describe step-by-step how your system would be used.
   c) Discuss the potential benefits and risks of using time perception alteration in this context.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues arising from the ability to manipulate time perception.
   b) Discuss the implications for free will, personal identity, and social dynamics.
   c) Propose guidelines for the ethical use and regulation of this technology.

6. Limitations and Future Directions (150-200 words):
   a) Discuss current technological or scientific barriers to realizing such a system.
   b) Propose two potential advancements that could overcome these limitations.
   c) Suggest future research directions or applications for time perception modulation technology.

Ensure your response demonstrates a deep understanding of neuroscience, physics, and the chosen application domain. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, physics, and the specified application domain.",
            "The system design is innovative, scientifically plausible, and thoroughly explained.",
            "The application of the system to the given domain is well-reasoned and detailed.",
            "Ethical considerations are thoughtfully discussed and addressed.",
            "The response shows creative problem-solving and interdisciplinary knowledge integration.",
            "The writing is clear, well-structured, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
