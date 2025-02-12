import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        interface_types = [
            {
                "type": "Bi-directional thought transfer",
                "description": "Allows for direct exchange of thoughts and memories between human brain and AI"
            },
            {
                "type": "Cognitive enhancement",
                "description": "Augments human cognitive abilities using AI processing power"
            },
            {
                "type": "Sensory expansion",
                "description": "Enables humans to experience new sensory modalities through AI integration"
            }
        ]
        philosophical_questions = [
            "How does the integration of AI with human consciousness affect personal identity?",
            "Can a hybrid human-AI system be considered conscious, and if so, in what ways?",
            "What are the ethical implications of altering human cognition through AI integration?"
        ]
        return {
            "1": {
                "interface": random.choice(interface_types),
                "question": random.choice(philosophical_questions)
            },
            "2": {
                "interface": random.choice(interface_types),
                "question": random.choice(philosophical_questions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical neural interface system for {t['interface']['type']} that connects human brains to AI systems. Then, use this hypothetical technology to explore the philosophical question: {t['question']}

Your response should include the following sections:

1. Neural Interface System Design (300-350 words):
   a) Describe the key components and mechanisms of your neural interface system.
   b) Explain how it achieves {t['interface']['type']} between human brains and AI systems.
   c) Discuss potential challenges in implementation and how they might be overcome.
   d) Include a high-level diagram or flowchart of your system (use ASCII art or a structured text description).

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your interface design.
   b) Discuss how your system interacts with specific brain regions or neural processes.
   c) Address potential neuroplasticity considerations and long-term effects on the brain.

3. AI Integration (200-250 words):
   a) Describe the AI architecture that would interface with the human brain.
   b) Explain how the AI system processes and responds to neural signals.
   c) Discuss any novel AI algorithms or approaches necessary for this integration.

4. Philosophical Exploration (250-300 words):
   a) Use your theoretical system to explore the question: {t['question']}
   b) Discuss multiple perspectives or potential answers to this question.
   c) Analyze how your neural interface system challenges or supports existing philosophical theories.

5. Ethical Implications (200-250 words):
   a) Identify and discuss at least three ethical concerns raised by your neural interface system.
   b) Propose guidelines for the responsible development and use of such technology.
   c) Discuss potential societal impacts if this technology becomes widely available.

6. Future Research Directions (150-200 words):
   a) Propose two potential extensions or applications of your neural interface system.
   b) Discuss how these extensions might further our understanding of consciousness or cognition.
   c) Suggest experiments that could validate or explore the effects of your system.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and philosophy of mind. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and philosophy of mind, using appropriate terminology and concepts from each field.",
            "The neural interface system design is innovative, scientifically plausible, and clearly explained, including its mechanisms for achieving the specified type of brain-AI connection.",
            "The philosophical exploration effectively uses the proposed system to address the given question, presenting multiple perspectives and analyzing implications for existing theories.",
            "The ethical implications are thoroughly considered, with well-reasoned guidelines for responsible development and use of the technology.",
            "The response is creative and original while maintaining scientific and philosophical rigor throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
