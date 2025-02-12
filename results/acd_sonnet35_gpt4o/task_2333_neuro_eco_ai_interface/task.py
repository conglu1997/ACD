import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "Biodiversity loss",
            "Climate change",
            "Deforestation",
            "Ocean pollution"
        ]
        neural_interfaces = [
            "EEG-based headset",
            "fMRI-guided stimulation",
            "Optogenetic neural implant",
            "Transcranial magnetic stimulation"
        ]
        return {
            "1": {
                "challenge": random.choice(environmental_challenges),
                "interface": random.choice(neural_interfaces)
            },
            "2": {
                "challenge": random.choice(environmental_challenges),
                "interface": random.choice(neural_interfaces)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface system that uses AI to enhance human connection with nature and promote sustainable behavior, focusing on the environmental challenge of {t['challenge']} and utilizing a {t['interface']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your neuro-eco AI interface system.
   b) Explain how the {t['interface']} integrates with AI components.
   c) Detail how your system enhances human-nature connection and promotes sustainable behavior related to {t['challenge']}.

2. Neuroscience Foundation (200-250 words):
   a) Explain the neurological basis for human-nature connection in your system.
   b) Describe how the {t['interface']} interacts with relevant brain regions or processes.
   c) Discuss any potential neuroplasticity effects of using your system.

3. AI and Data Processing (200-250 words):
   a) Describe the AI algorithms used in your system and their functions.
   b) Explain how environmental data related to {t['challenge']} is processed and integrated.
   c) Detail how the AI adapts its output based on individual user's brain activity and behavior.

4. User Experience and Behavior Change (200-250 words):
   a) Describe the user experience of interacting with your system.
   b) Explain how your system promotes sustainable behavior related to {t['challenge']}.
   c) Discuss potential long-term effects on users' environmental attitudes and behaviors.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in using brain-computer interfaces for behavior modification.
   b) Discuss data privacy and security concerns specific to your system.
   c) Propose guidelines for ethical development and use of neuro-eco AI interfaces.

6. Societal Impact and Scalability (150-200 words):
   a) Analyze the potential broader impacts of your system on society and the environment.
   b) Discuss how your system could be scaled or adapted to address other environmental challenges.
   c) Identify potential barriers to widespread adoption and propose solutions.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and environmental psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering real-world constraints.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of neuroscience, AI, and environmental psychology, especially in relation to {t['challenge']}.",
            f"The system design effectively integrates the {t['interface']} with AI components to enhance human-nature connection.",
            "The proposed solution is innovative yet scientifically plausible.",
            "The response thoroughly addresses ethical considerations and societal impacts.",
            "The writing is clear, well-structured, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
