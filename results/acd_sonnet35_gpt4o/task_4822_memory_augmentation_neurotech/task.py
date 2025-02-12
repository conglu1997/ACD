import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_types = [
            "episodic memory",
            "semantic memory",
            "procedural memory",
            "working memory"
        ]
        neurotechnologies = [
            "optogenetics",
            "brain-computer interfaces",
            "transcranial magnetic stimulation",
            "nanorobots"
        ]
        ai_techniques = [
            "deep learning",
            "reinforcement learning",
            "natural language processing",
            "computer vision"
        ]
        return {
            "1": {
                "memory_type": random.choice(memory_types),
                "neurotechnology": random.choice(neurotechnologies),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "memory_type": random.choice(memory_types),
                "neurotechnology": random.choice(neurotechnologies),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered neurotechnology system to enhance and augment human {t['memory_type']}, utilizing {t['neurotechnology']} and {t['ai_technique']}. Then, analyze its potential impacts and ethical implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your memory augmentation system, including both hardware and software elements.
   b) Explain how {t['neurotechnology']} is integrated into the system to enhance {t['memory_type']}.
   c) Detail how {t['ai_technique']} is utilized to process and augment memory-related neural signals.
   d) Discuss any novel approaches you've incorporated to ensure seamless integration with natural memory processes.
   e) Include a high-level diagram or pseudocode to illustrate your system's architecture (describe it textually).

2. Neuroscientific Basis (250-300 words):
   a) Explain the current understanding of how {t['memory_type']} functions in the human brain.
   b) Describe how your system interacts with and enhances the relevant neural circuits.
   c) Discuss potential neuroplasticity considerations and how your system accounts for them.
   d) Address any potential neurological risks and how your design mitigates them.

3. AI-Neurotechnology Integration (200-250 words):
   a) Explain in detail how {t['ai_technique']} and {t['neurotechnology']} work together in your system.
   b) Provide a specific example of how a memory task would be enhanced using your system.
   c) Discuss the expected magnitude of enhancement and any potential limitations.
   d) Explain how your system adapts to individual differences in brain structure and function.

4. Ethical Analysis (250-300 words):
   a) Discuss the ethical implications of enhancing {t['memory_type']} through AI and neurotechnology.
   b) Address concerns about privacy, autonomy, and potential misuse of the technology.
   c) Analyze potential social impacts if this technology becomes widespread.
   d) Propose guidelines for the responsible development and use of memory augmentation systems.
   e) Discuss the implications for personal identity and authenticity of memories.

5. Societal Impact (200-250 words):
   a) Predict how widespread adoption of this technology might reshape education, work, and daily life.
   b) Discuss potential new fields or professions that could emerge as a result of this technology.
   c) Address concerns about potential exacerbation of social inequalities.
   d) Analyze how this technology might impact interpersonal relationships and social dynamics.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research to advance this type of memory augmentation system.
   b) Explain how these research directions could address current limitations or open up new possibilities.
   c) Discuss potential interdisciplinary collaborations that could drive innovation in this field.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, cognitive psychology, and ethics. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively integrates {t['neurotechnology']} and {t['ai_technique']} to enhance {t['memory_type']}.",
            "The response demonstrates a deep understanding of the neuroscientific basis of the chosen memory type.",
            "The ethical analysis is comprehensive and considers multiple perspectives.",
            "The societal impact analysis is well-reasoned and considers both positive and negative potential outcomes.",
            "The proposed future research directions are innovative and relevant to advancing the field.",
            "The overall response is scientifically plausible, creative, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
