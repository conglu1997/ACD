import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        civilizations = [
            'Ancient Egypt',
            'Mayan',
            'Indus Valley',
            'Ancient Greece',
            'Mesopotamia'
        ]
        artifact_types = [
            'pottery shards',
            'stone tablets',
            'metal objects',
            'architectural remains',
            'textile fragments'
        ]
        ai_techniques = [
            '3D reconstruction',
            'pattern recognition',
            'natural language processing',
            'generative adversarial networks',
            'reinforcement learning'
        ]
        tasks = [
            {
                'civilization': random.choice(civilizations),
                'artifact': random.choice(artifact_types),
                'ai_technique': random.choice(ai_techniques)
            },
            {
                'civilization': random.choice(civilizations),
                'artifact': random.choice(artifact_types),
                'ai_technique': random.choice(ai_techniques)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for analyzing and reconstructing ancient artifacts and civilizations, focusing on {t['civilization']} and {t['artifact']}. Then, apply your system to solve a complex archaeological problem using {t['ai_technique']}. Your response should include:

1. AI Archaeologist System Design (300-350 words):
   a) Describe the key components and architecture of your AI system for archaeological analysis and reconstruction.
   b) Explain how your system incorporates knowledge of {t['civilization']} and handles {t['artifact']}.
   c) Detail how your system utilizes {t['ai_technique']} for archaeological problem-solving.
   d) Discuss any novel features that make your system particularly suited for archaeological applications.

2. Data Processing and Analysis (250-300 words):
   a) Explain how your system processes and analyzes archaeological data, particularly {t['artifact']}.
   b) Describe the AI algorithms or methods used for pattern recognition, feature extraction, or anomaly detection.
   c) Discuss how your system handles incomplete or damaged artifacts.

3. Reconstruction and Visualization (250-300 words):
   a) Detail how your AI system reconstructs artifacts or entire sites from fragmentary evidence.
   b) Explain the process of generating hypothetical models of ancient structures or objects.
   c) Describe how your system visualizes results for archaeologists and the public.

4. Application to a Complex Problem (300-350 words):
   a) Present a specific archaeological problem related to {t['civilization']} that your system can address.
   b) Provide a step-by-step explanation of how your AI Archaeologist system would approach this problem.
   c) Describe the expected outputs and how they would contribute to archaeological knowledge.
   d) Discuss any challenges specific to this application and how your system overcomes them.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss the ethical implications of using AI in archaeology and cultural heritage studies.
   b) Address concerns about AI potentially replacing human archaeologists or misinterpreting cultural artifacts.
   c) Explain the limitations of your AI system and situations where human expertise is still crucial.
   d) Propose guidelines for the responsible use of AI in archaeology.

6. Future Developments and Interdisciplinary Impact (150-200 words):
   a) Suggest potential future enhancements to your AI Archaeologist system.
   b) Discuss how this technology might impact related fields such as history, anthropology, or museum studies.
   c) Propose an interdisciplinary research project that could build upon your AI system.

Ensure your response demonstrates a deep understanding of archaeology, artificial intelligence, and computer vision. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and historical plausibility.

Format your response with clear headings for each section, using the exact numbering and lettering provided above. Include at least one concrete example or case study related to {t['civilization']} and {t['artifact']} in your response.

Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of archaeology, artificial intelligence, and computer vision, particularly in relation to {t['civilization']}, {t['artifact']}, and {t['ai_technique']}.",
            "The AI Archaeologist system design is innovative, scientifically plausible, and effectively incorporates the specified AI technique for archaeological applications.",
            "The data processing, analysis, reconstruction, and visualization methods are well-explained and appropriate for archaeological purposes.",
            "The application to a complex problem is well-thought-out and demonstrates how the AI system can contribute to archaeological knowledge.",
            "Ethical considerations and limitations are thoroughly discussed, showing an understanding of the broader impacts of AI in archaeology.",
            "Future developments and interdisciplinary impacts are thoughtfully considered and show potential for advancing the field.",
            f"The response includes at least one concrete example or case study related to {t['civilization']} and {t['artifact']}.",
            "The response follows the exact structure and numbering provided in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
