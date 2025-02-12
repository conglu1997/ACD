import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        contexts = [
            "medical treatment for PTSD",
            "enhancing learning and skill acquisition",
            "criminal rehabilitation",
            "corporate espionage and information security",
            "personal relationship management"
        ]
        memory_types = [
            "episodic memories",
            "procedural memories",
            "semantic memories",
            "emotional memories"
        ]
        ethical_concerns = [
            "personal identity and authenticity",
            "consent and autonomy",
            "privacy and data security",
            "social inequality and access",
            "potential for abuse and manipulation"
        ]
        
        return {
            "1": {
                "context": random.choice(contexts),
                "memory_type": random.choice(memory_types),
                "ethical_concern": random.choice(ethical_concerns)
            },
            "2": {
                "context": random.choice(contexts),
                "memory_type": random.choice(memory_types),
                "ethical_concern": random.choice(ethical_concerns)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical AI-based memory manipulation system for {t['context']}, focusing on {t['memory_type']}. Analyze its potential applications and ethical implications, with particular attention to {t['ethical_concern']}. Your response should include:

1. System Design (250-300 words):
   a) Describe the key components and functionality of your AI-based memory manipulation system.
   b) Explain how it interacts with {t['memory_type']}.
   c) Discuss the role of AI in the system's operation and decision-making processes.

2. Potential Applications (200-250 words):
   a) Describe at least three potential applications of your system in the context of {t['context']}.
   b) Analyze the potential benefits and risks associated with each application.
   c) Discuss how the system's ability to manipulate {t['memory_type']} is particularly relevant to these applications.

3. Ethical Analysis (250-300 words):
   a) Conduct a thorough ethical analysis of your system, focusing on {t['ethical_concern']}.
   b) Present arguments both for and against the use of this technology.
   c) Discuss how the involvement of AI in memory manipulation raises unique ethical concerns.

4. Safeguards and Regulations (150-200 words):
   a) Propose potential safeguards or regulations to address the ethical concerns you've identified.
   b) Explain how these measures would be implemented and enforced.
   c) Discuss any potential limitations or challenges in regulating this technology.

5. Future Implications (150-200 words):
   a) Speculate on the long-term societal implications of widespread use of AI-based memory manipulation.
   b) Discuss how this technology might evolve and what new ethical challenges might emerge.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethical philosophy. Be creative in your system design while maintaining scientific plausibility and addressing real-world concerns."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['memory_type']} and how they could be manipulated by an AI system.",
            f"The system design is innovative, scientifically plausible, and relevant to {t['context']}.",
            f"The potential applications are well-thought-out and directly related to {t['context']}.",
            f"The ethical analysis thoroughly addresses {t['ethical_concern']} and presents balanced arguments.",
            "The proposed safeguards and regulations are practical and address the identified ethical concerns.",
            "The discussion of future implications shows foresight and consideration of long-term consequences.",
            "The response integrates knowledge from neuroscience, artificial intelligence, and ethics effectively.",
            "The writing is clear, well-structured, and demonstrates high-level analytical and creative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
