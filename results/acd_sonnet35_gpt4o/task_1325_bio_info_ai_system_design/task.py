import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'system_type': 'DNA-based computing',
                'application': 'pattern recognition',
                'constraint': 'energy efficiency'
            },
            {
                'system_type': 'Cellular automata',
                'application': 'natural language processing',
                'constraint': 'self-replication'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biological computing system using {t['system_type']} for {t['application']}, with a focus on {t['constraint']}. Your response should include:

1. System Overview (150-200 words):
   a) Describe the key components and mechanisms of your biological computing system.
   b) Explain how it performs {t['application']} using biological processes.
   c) Discuss how your design addresses the constraint of {t['constraint']}.

2. Biological Mechanisms (200-250 words):
   a) Detail at least three specific biological processes or structures utilized in your system.
   b) Explain how these mechanisms are adapted or engineered for computation.
   c) Discuss any novel biological concepts you've incorporated into your design.
   d) Provide at least two citations to relevant scientific literature for the biological mechanisms used.

3. Information Processing (200-250 words):
   a) Describe how information is encoded, processed, and retrieved in your system.
   b) Explain the computational model underlying your biological system.
   c) Compare the information processing capabilities of your system to traditional electronic computers.
   d) Discuss potential error rates or limitations in your biological computing system.

4. Implementation and Challenges (150-200 words):
   a) Outline the steps required to implement your biological computing system.
   b) Discuss the main technical challenges and potential solutions.
   c) Address any ethical considerations related to engineering biological systems for computation.

5. Performance Analysis (150-200 words):
   a) Analyze the theoretical performance of your system for {t['application']}.
   b) Compare its efficiency, speed, and scalability to traditional computing methods.
   c) Discuss any unique advantages or limitations of your biological approach.

6. Future Implications (100-150 words):
   a) Speculate on potential future developments or applications of your biological computing system.
   b) Discuss how it might impact the fields of computing, AI, and biology.

7. Interdisciplinary Connections (100-150 words):
   a) Explain how your design integrates concepts from biology, information theory, and artificial intelligence.
   b) Discuss any novel insights or approaches that emerge from this interdisciplinary integration.

8. System Representation (150-200 words):
   a) Provide a simple diagram or pseudocode representation of your biological computing system.
   b) Explain the key elements and processes illustrated in your representation.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and computational principles. Use technical terminology appropriately and provide explanations where necessary. Be creative and speculative in your design while maintaining scientific plausibility. Format your response using clear headings for each section.

Important Notes:
- When mentioning specific biological mechanisms or computational models, provide brief citations or references to relevant scientific literature to ground your speculative design in existing knowledge.
- Clearly state any assumptions you make in your design and justify them based on current scientific understanding.
- Address potential limitations and error rates in your biological computing system.
- To evaluate the feasibility of your proposed system, consider: (1) current technological limitations, (2) theoretical constraints of biological systems, and (3) potential conflicts between biological and computational requirements.

Your entire response should be between 1200-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The biological computing system design is innovative, coherently integrating concepts from biology, information theory, and AI in a non-trivial way.",
            "At least three specific, relevant biological mechanisms are detailed and supported by at least two appropriate citations to scientific literature.",
            "The information processing approach is clearly described, including a thoughtful discussion of potential error rates and limitations.",
            "Implementation challenges and ethical considerations are thoroughly addressed, with creative yet plausible solutions proposed.",
            "The performance analysis comprehensively compares the system to traditional computing methods, providing quantitative estimates where possible.",
            "Future implications and interdisciplinary connections are thoughtfully discussed, presenting novel and insightful ideas.",
            f"The design adequately addresses the application of {t['application']} using {t['system_type']}, demonstrating a clear understanding of both the biological system and the computational task.",
            f"The system effectively incorporates the constraint of {t['constraint']}, with a detailed explanation of how this is achieved.",
            "Each section of the response contains the key elements specified in the instructions, with a high level of detail and scientific accuracy.",
            "The response demonstrates a deep understanding of molecular biology, information theory, and computational principles, going beyond basic concepts.",
            "The provided diagram or pseudocode accurately represents the proposed biological computing system and is clearly explained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
