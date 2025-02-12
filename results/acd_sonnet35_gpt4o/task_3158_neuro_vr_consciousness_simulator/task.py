import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        altered_states = [
            "Synesthesia",
            "Out-of-body experience",
            "Temporal distortion",
            "Ego dissolution"
        ]
        philosophical_questions = [
            "What is the nature of subjective experience?",
            "How does perception shape our understanding of reality?",
            "Can artificial systems truly experience consciousness?",
            "How does altering consciousness affect our sense of self?"
        ]
        return {
            "1": {"altered_state": random.choice(altered_states), "question": random.choice(philosophical_questions)},
            "2": {"altered_state": random.choice(altered_states), "question": random.choice(philosophical_questions)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a virtual reality system that simulates the altered state of consciousness known as {t['altered_state']}, based on neuroscientific principles. Then, use this system to explore the philosophical question: {t['question']}

Your response should include:

1. Neuroscientific Basis (200-250 words):
   a) Explain the neurological mechanisms underlying {t['altered_state']}.
   b) Describe how these mechanisms alter perception and consciousness.
   c) Discuss any relevant neuroscientific research or theories related to this altered state.

2. VR System Design (250-300 words):
   a) Outline the key components of your VR system for simulating {t['altered_state']}.
   b) Explain how your system replicates the neurological effects of this altered state.
   c) Describe the user experience and interface of your VR simulation.
   d) Discuss any novel technologies or approaches you've incorporated into your design.

3. Simulation Scenario (200-250 words):
   a) Describe a specific scenario in your VR simulation that demonstrates {t['altered_state']}.
   b) Explain how this scenario might affect the user's perception and cognition.
   c) Discuss potential applications of this simulation (e.g., in research, therapy, or education).

4. Philosophical Exploration (250-300 words):
   a) Use your VR simulation to explore the question: {t['question']}
   b) Discuss how experiencing {t['altered_state']} in VR might provide insights into this question.
   c) Compare the philosophical implications of your simulation to traditional thought experiments or real-world altered states.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical concerns related to simulating altered states of consciousness.
   b) Explain limitations of your system and areas for future improvement.
   c) Compare your VR approach to other methods of studying consciousness and perception.

Ensure your response demonstrates a deep understanding of neuroscience, virtual reality technology, and philosophy of mind. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed design of a VR system that simulates the altered state of consciousness known as {t['altered_state']}.",
            f"The design must be based on neuroscientific principles and explore the philosophical question: {t['question']}",
            "The response should demonstrate a deep understanding of neuroscience, virtual reality technology, and philosophy of mind.",
            "The proposed system should be innovative and speculative while maintaining scientific plausibility.",
            "All five sections (Neuroscientific Basis, VR System Design, Simulation Scenario, Philosophical Exploration, and Ethical Considerations and Limitations) must be addressed comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
