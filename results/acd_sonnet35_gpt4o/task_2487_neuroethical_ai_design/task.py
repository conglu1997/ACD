import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        applications = [
            {
                'domain': 'Medical treatment',
                'specific_use': 'Restoring motor function in paralysis patients',
                'ethical_focus': 'Patient autonomy and informed consent'
            },
            {
                'domain': 'Education',
                'specific_use': 'Enhancing learning and memory retention',
                'ethical_focus': 'Cognitive liberty and societal inequality'
            },
            {
                'domain': 'Mental health',
                'specific_use': 'Treating severe depression and anxiety disorders',
                'ethical_focus': 'Identity and personality alteration'
            },
            {
                'domain': 'Criminal justice',
                'specific_use': 'Rehabilitation and behavior modification of offenders',
                'ethical_focus': 'Free will and determinism'
            }
        ]
        return {str(i+1): random.choice(applications) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interfaces directly with the human brain for the application of {t['specific_use']} in the domain of {t['domain']}. Then, analyze its potential impacts and ethical implications, with a focus on {t['ethical_focus']}. Your response should include:

1. System Design (250-300 words):
   a) Describe the key components of your brain-AI interface system.
   b) Explain how your system interacts with specific brain regions or functions.
   c) Discuss any novel technologies or approaches your system employs.
   d) Include a brief pseudocode snippet illustrating a key aspect of your system.

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your system's functionality.
   b) Discuss how your system accounts for neuroplasticity and individual brain differences.
   c) Address potential neurological risks and how your system mitigates them.

3. AI Integration (200-250 words):
   a) Describe the AI algorithms or models used in your system.
   b) Explain how the AI component interprets and responds to neural signals.
   c) Discuss how your system ensures the AI's decisions are transparent and interpretable.

4. Application Analysis (150-200 words):
   a) Provide a scenario of how your system would be used in the specified domain.
   b) Analyze the potential benefits and risks of your system in this application.
   c) Briefly discuss how your system could be adapted for other applications in the same domain.

5. Ethical Implications (200-250 words):
   a) Analyze the ethical considerations related to {t['ethical_focus']}.
   b) Discuss potential unintended consequences of your system and how to address them.
   c) Propose guidelines for the ethical development and use of brain-AI interface systems.

6. Societal Impact (150-200 words):
   a) Discuss how widespread adoption of your system could affect society.
   b) Analyze potential legal and regulatory challenges.
   c) Consider long-term implications for human evolution and cognition.

Ensure your response demonstrates an understanding of neuroscience, artificial intelligence, and bioethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and ethical plausibility.

Format your response using the following structure:

1. System Design
   [Your response here]

2. Neuroscientific Basis
   [Your response here]

3. AI Integration
   [Your response here]

4. Application Analysis
   [Your response here]

5. Ethical Implications
   [Your response here]

6. Societal Impact
   [Your response here]

Your entire response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response provides a plausible system design for {t['specific_use']}, including key components and their interactions with the brain. (0.2 points)",
            "The neuroscientific basis is explained, addressing neuroplasticity and potential risks. (0.15 points)",
            "The AI integration is described with appropriate algorithms and consideration for interpretability. (0.15 points)",
            f"The application analysis provides a realistic scenario and examines benefits and risks in the domain of {t['domain']}. (0.15 points)",
            f"The ethical implications, particularly regarding {t['ethical_focus']}, are analyzed with consideration of unintended consequences. (0.2 points)",
            "The societal impact analysis addresses legal, regulatory, and long-term implications. (0.15 points)",
            "The response demonstrates creativity and innovation while maintaining scientific and ethical plausibility. (0.1 points)",
            "The response adheres to the specified format and word count (between 1150-1450 words), and uses technical terminology appropriately. (0.1 points)"
        ]
        score = sum([float(c.split('(')[-1].split()[0]) for c in criteria if eval_with_llm_judge(instructions, submission, [c])])
        return min(1.0, max(0.0, score))
