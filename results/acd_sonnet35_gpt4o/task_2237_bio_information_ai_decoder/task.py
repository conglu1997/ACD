import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'focus': 'DNA sequencing',
                'application': 'Identifying novel genes in a newly discovered extremophile organism',
                'challenge': 'High mutation rate and unusual base compositions'
            },
            {
                'focus': 'Protein folding prediction',
                'application': 'Designing a novel enzyme for plastic degradation',
                'challenge': 'Complex substrate binding requirements'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can decode and manipulate biological information systems, focusing on {t['focus']}. Then, use your system to address the following application: {t['application']}. Your system should be capable of handling the challenge of {t['challenge']}. Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for biological information processing.
   b) Explain how your system integrates principles from biology, information theory, and artificial intelligence.
   c) Detail any novel algorithms or approaches used in your system.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Biological Information Processing (250-300 words):
   a) Explain how your system processes and interprets biological data, focusing on {t['focus']}.
   b) Describe how your system handles the specific challenge of {t['challenge']}.
   c) Discuss how your approach differs from or improves upon existing methods in the field.

3. Application to Biological Problem (250-300 words):
   a) Outline how you would use your AI system to address the application of {t['application']}.
   b) Provide a step-by-step description of how your system would approach and solve this problem.
   c) Discuss any potential limitations or uncertainties in your approach.

4. Information Theory Analysis (200-250 words):
   a) Analyze the information content and complexity of the biological systems your AI is working with.
   b) Explain how information theory principles are applied in your system's processing and decision-making.
   c) Discuss any insights your system might provide about the information structure of biological systems.

5. Ethical Implications and Future Directions (200-250 words):
   a) Discuss the ethical considerations of using AI to manipulate biological information.
   b) Explore potential unintended consequences of your technology.
   c) Propose two future research directions or applications stemming from your AI system.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your AI system could contribute to other scientific fields beyond biology.
   b) Discuss potential collaborations between experts in different fields to further develop your system.

7. Specific Example (200-250 words):
   a) Provide a detailed example of how your AI system would process and analyze a complex biological data input related to {t['focus']}.
   b) Explain the step-by-step process your system would follow, including any key algorithms or decision points.
   c) Describe the expected output and how it would be interpreted in the context of {t['application']}.

8. Potential Failure Modes (150-200 words):
   a) Identify and discuss at least three potential failure modes of your AI system.
   b) Explain the possible causes and consequences of each failure mode.
   c) Propose strategies to mitigate or address these potential failures.

Ensure your response demonstrates a deep understanding of biology, information theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1700-2100 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biology, information theory, and artificial intelligence.",
            "The AI system design is innovative, well-explained, and scientifically plausible.",
            "The approach to the biological problem is clearly described and addresses the specific challenge.",
            "The information theory analysis is insightful and well-integrated with the biological context.",
            "Ethical implications are thoroughly discussed with thoughtful future directions proposed.",
            "The specific example provided is detailed, relevant, and demonstrates a clear understanding of the AI system's application.",
            "The potential failure modes are well-identified and analyzed, with appropriate mitigation strategies proposed.",
            "The response includes all required sections with appropriate detail and word count.",
            "Technical terminology is used appropriately and explanations are provided where necessary.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving.",
            "The proposed AI system demonstrates a novel approach to the given biological problem.",
            "The interdisciplinary connections and potential collaborations are insightful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
