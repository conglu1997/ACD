import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "perceptual_mode": "color-to-sound",
                "musical_element": "harmony",
                "cognitive_process": "emotional regulation"
            },
            {
                "perceptual_mode": "sound-to-texture",
                "musical_element": "rhythm",
                "cognitive_process": "memory formation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and enhances musical synesthesia by integrating neuroscientific principles of cross-modal perception with AI-driven music generation and analysis. Your system should focus on the {t['perceptual_mode']} perceptual mode, the musical element of {t['musical_element']}, and its impact on the cognitive process of {t['cognitive_process']}. Your response should include:

1. Neuroscientific Framework (250-300 words):
   a) Explain the neurological basis of synesthesia, focusing on {t['perceptual_mode']} interactions.
   b) Describe how {t['musical_element']} is processed in the brain and its relation to {t['cognitive_process']}.
   c) Propose a mechanism by which AI could enhance or modify these neural processes.

2. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating and enhancing musical synesthesia.
   b) Explain how your system integrates neuroscientific principles with AI-driven music generation and analysis.
   c) Detail how the system processes and translates between {t['perceptual_mode']} modalities.
   d) Include a high-level diagram or detailed description of your system's architecture.

3. Synesthetic Music Generation (250-300 words):
   a) Explain how your AI system generates music based on {t['perceptual_mode']} inputs.
   b) Describe how the system ensures the generated music emphasizes {t['musical_element']}.
   c) Discuss how the generated music might influence {t['cognitive_process']}.
   d) Provide a specific example or case study demonstrating your system's music generation process.

4. Cognitive Enhancement Mechanism (200-250 words):
   a) Propose how your system could enhance {t['cognitive_process']} through synesthetic music experiences.
   b) Describe potential cognitive or perceptual benefits of using your system.
   c) Discuss any possible risks or side effects of enhancing cognition through artificial synesthesia.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your system in enhancing {t['cognitive_process']}.
   b) Describe the methodology, including participant selection, experimental procedure, and data collection.
   c) Explain how you would measure and analyze the impact on {t['cognitive_process']}.

6. Ethical Considerations and Future Implications (150-200 words):
   a) Discuss ethical considerations in developing and using AI-enhanced synesthetic experiences.
   b) Explore potential applications of your system in fields such as education, therapy, or artistic expression.
   c) Speculate on how this technology might influence our understanding of perception and cognition in the future.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Each section should adhere to the specified word count. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response thoroughly addresses the {t['perceptual_mode']} perceptual mode, providing a clear explanation of its neurological basis and integration into the AI system.",
            f"The musical element of {t['musical_element']} is properly incorporated into the system design and its role in music generation is well-explained.",
            f"The impact on the cognitive process of {t['cognitive_process']} is thoroughly discussed, including potential benefits and risks.",
            "The proposed AI system architecture integrates principles from neuroscience, music theory, and artificial intelligence in a coherent and innovative manner.",
            "The response includes a specific example or case study demonstrating the system's music generation process.",
            "The experimental design is well-thought-out and appropriate for testing the system's effectiveness.",
            "Ethical considerations and future implications are thoughtfully explored, covering multiple aspects of the technology's potential impact.",
            "The response adheres to the specified word counts for each section and the overall word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
