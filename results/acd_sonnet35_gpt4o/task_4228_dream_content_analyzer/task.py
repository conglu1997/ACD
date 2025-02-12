import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "dream_type": "lucid",
                "cognitive_enhancement": "memory consolidation",
                "real_world_application": "skill acquisition"
            },
            {
                "dream_type": "recurring",
                "cognitive_enhancement": "problem-solving",
                "real_world_application": "trauma processing"
            },
            {
                "dream_type": "archetypal",
                "cognitive_enhancement": "creativity",
                "real_world_application": "innovation in art and science"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and manipulating {t['dream_type']} dream content, then apply it to enhance {t['cognitive_enhancement']} and solve real-world problems in {t['real_world_application']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI dream analysis and manipulation system.
   b) Explain how your system interfaces with human brain activity during sleep.
   c) Detail how your system processes and interprets dream content.
   d) Discuss any novel algorithms or techniques you've incorporated for dream manipulation.
   e) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Dream Content Analysis (250-300 words):
   a) Explain how your system identifies and categorizes elements of {t['dream_type']} dreams.
   b) Describe the methods used to extract meaningful patterns or symbols from dream content.
   c) Discuss how your system accounts for individual and cultural variations in dream interpretation.
   d) Provide a specific example of how your system would analyze a dream related to {t['cognitive_enhancement']}.

3. Dream Manipulation Techniques (250-300 words):
   a) Detail the methods your system uses to influence or manipulate dream content.
   b) Explain how these manipulations are tailored to enhance {t['cognitive_enhancement']}.
   c) Discuss any potential risks or side effects of dream manipulation and how your system mitigates them.
   d) Give an example of how your system would manipulate a dream to improve {t['cognitive_enhancement']}.

4. Application to {t['real_world_application']} (200-250 words):
   a) Describe how your system could be applied to {t['real_world_application']}.
   b) Provide a specific example of how dream analysis and manipulation could lead to improvements in this area.
   c) Discuss any challenges in translating dream-based insights to real-world applications.

5. Ethical Considerations (200-250 words):
   a) Analyze potential ethical implications of using AI for dream analysis and manipulation.
   b) Discuss privacy concerns and propose guidelines for responsible use of this technology.
   c) Consider the potential impact on personal autonomy and decision-making.

6. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness of your system in enhancing {t['cognitive_enhancement']}.
   b) Describe how you would validate the real-world benefits in {t['real_world_application']}.
   c) Discuss the challenges in measuring the impact of dream manipulation on cognitive abilities.

7. Comparative Analysis and Future Directions (200-250 words):
   a) Compare your proposed system with existing dream analysis techniques or technologies.
   b) Discuss the advantages and potential limitations of your approach.
   c) Propose two potential future developments or extensions of your system.
   d) Explain how these developments could further advance the field of dream analysis and manipulation.

Ensure your response demonstrates a deep understanding of neuroscience, psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words. Include a word count at the end of your submission.

IMPORTANT: Do not include any actual code or implementation details in your response. Focus on high-level design and conceptual explanations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, psychology, and artificial intelligence, using appropriate technical terminology.",
            "The proposed system is innovative, scientifically plausible, and specifically addresses {t['dream_type']} dreams, {t['cognitive_enhancement']}, and {t['real_world_application']}.",
            "The response addresses all required sections with appropriate depth and clarity, adhering to the specified word count ranges.",
            "Specific examples are provided for dream content analysis and manipulation related to {t['cognitive_enhancement']}.",
            "The application to {t['real_world_application']} is well-reasoned and potentially impactful, with clear examples.",
            "Ethical considerations are thoroughly analyzed and addressed, including privacy concerns and guidelines for responsible use.",
            "The evaluation and validation methods proposed are appropriate, comprehensive, and specific to {t['cognitive_enhancement']} and {t['real_world_application']}.",
            "The comparative analysis effectively contextualizes the proposed system within existing scientific literature and technologies.",
            "Future directions are insightful and demonstrate an understanding of potential advancements in the field.",
            "The response does not include any actual code or low-level implementation details."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
