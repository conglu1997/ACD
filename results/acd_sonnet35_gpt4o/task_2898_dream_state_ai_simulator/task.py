import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dream_aspects = [
            {
                "aspect": "Emotional Valence",
                "description": "The system should simulate dreams with varying emotional tones and analyze their potential psychological impacts."
            },
            {
                "aspect": "Temporal Distortion",
                "description": "The system should model the non-linear time perception often experienced in dreams and its effects on narrative structure."
            },
            {
                "aspect": "Symbolic Representation",
                "description": "The system should generate and interpret symbolic imagery commonly found in dreams, considering cultural and personal contexts."
            }
        ]
        return {str(i+1): aspect for i, aspect in enumerate(random.sample(dream_aspects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of simulating and analyzing dream-like states, with a focus on the aspect of {t['aspect']}. Your system should incorporate principles from neuroscience, psychology, and machine learning. {t['description']}

Your response should include the following sections, with each section clearly labeled and containing the specified content:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI dream simulation system.
   b) Explain how your system integrates knowledge from neuroscience, psychology, and machine learning.
   c) Detail how the system models and applies the specified dream aspect.
   d) Provide a high-level diagram or flowchart illustrating the system's architecture (describe it textually using bullet points or a numbered list).

2. Dream Generation Process (250-300 words):
   a) Outline the step-by-step process your AI system would use to generate a dream-like narrative or experience.
   b) Explain how your system ensures the generated dreams incorporate the specified aspect.
   c) Describe any techniques used for maintaining dream-like qualities (e.g., non-linearity, symbolism, emotional resonance).

3. Analysis and Interpretation (250-300 words):
   a) Describe how your AI system would analyze and interpret the generated dream-like states.
   b) Explain the metrics or features your system would use to quantify aspects of the dream.
   c) Discuss how your system might derive potential psychological or emotional significance from the dream content.

4. Neuroscientific Basis (200-250 words):
   a) Explain how your AI system models brain activity or neural processes associated with dreaming.
   b) Discuss any insights your system might provide into the neuroscience of dreaming.
   c) Describe how your system's performance compares to current understanding of human dream states.

5. Potential Applications (150-200 words):
   a) Propose three potential applications of your AI dream simulation system (e.g., in psychology, art, or personal growth).
   b) Explain how each application leverages the unique features of your system.
   c) Discuss potential benefits and challenges of these applications.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical concerns related to AI-generated and analyzed dream-like states.
   b) Propose guidelines for the responsible use and development of such systems.
   c) Consider potential psychological impacts on users interacting with AI-generated dreams.

7. Limitations and Future Directions (150-200 words):
   a) Identify key limitations in your current system design.
   b) Propose two potential improvements or extensions to your system for future development.
   c) Discuss how advances in neuroscience or AI might inform future versions of your dream simulation system.

Ensure your response demonstrates a deep understanding of neuroscience, psychology, and artificial intelligence as they relate to dream states. Be creative in your system design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, and include all required subsections (a, b, c, etc.) under each heading. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI system for simulating and analyzing dream-like states, focusing on the aspect of {t['aspect']}",
            "The system design should integrate knowledge from neuroscience, psychology, and machine learning",
            "The response should include all required sections with appropriate content and word counts",
            "Each section should be clearly labeled and contain all specified subsections (a, b, c, etc.)",
            "The System Architecture section should include a textual description of a diagram or flowchart",
            "The proposed system should be innovative yet scientifically plausible",
            "The response should demonstrate a deep understanding of dream states, neuroscience, and AI",
            "The Dream Generation Process should describe a clear step-by-step approach",
            "The Analysis and Interpretation section should include specific metrics or features for quantifying dream aspects",
            "The Neuroscientific Basis section should compare the system's performance to current understanding of human dream states",
            "The Potential Applications section should propose three distinct applications with benefits and challenges",
            "The Ethical Considerations section should propose specific guidelines for responsible use",
            "The Limitations and Future Directions section should identify current limitations and propose improvements",
            "The response should be well-organized with clear headings for each section",
            "The total response should be between 1450-1800 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
