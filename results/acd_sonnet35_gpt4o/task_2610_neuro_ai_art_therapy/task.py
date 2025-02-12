import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_forms = ['visual art', 'music', 'interactive digital art', 'poetry']
        mental_states = ['anxiety', 'depression', 'stress', 'trauma recovery']
        neuroimaging_techniques = ['fMRI', 'EEG', 'MEG']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'art_form': random.choice(art_forms),
                'mental_state': random.choice(mental_states),
                'neuroimaging_technique': random.choice(neuroimaging_techniques)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that creates personalized {t['art_form']} experiences for therapeutic purposes, focusing on individuals experiencing {t['mental_state']}. The system should use real-time {t['neuroimaging_technique']} data and psychological profiles to generate adaptive art experiences. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI art therapy system.
   b) Explain how the system integrates {t['neuroimaging_technique']} data with psychological profiles.
   c) Detail the AI algorithms or models used for art generation and adaptation.
   d) Discuss how the system ensures real-time responsiveness to the user's mental state.

2. Art Generation Process (250-300 words):
   a) Explain how your system translates neuroimaging data and psychological profiles into artistic elements.
   b) Describe the specific techniques used to generate {t['art_form']} tailored for {t['mental_state']}.
   c) Discuss how the system maintains artistic coherence while adapting to real-time inputs.

3. Therapeutic Approach (200-250 words):
   a) Outline the therapeutic principles underlying your system's approach.
   b) Explain how the generated art experiences are expected to benefit individuals with {t['mental_state']}.
   c) Discuss potential risks or limitations of using AI-generated art for therapy.

4. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to using AI and neuroimaging in art therapy.
   b) Propose guidelines to ensure responsible use of the system.
   c) Discuss data privacy and consent considerations.

5. Evaluation Methods (200-250 words):
   a) Propose a method for assessing the therapeutic effectiveness of your system.
   b) Describe how you would measure the artistic quality and personalization of the generated experiences.
   c) Suggest a framework for comparing your AI art therapy system to traditional art therapy approaches.

6. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how emerging technologies in AI or neuroscience could enhance your system's capabilities.
   c) Propose a related application of your system in a non-therapeutic context.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and art therapy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and art therapy",
            "The proposed system integrates neuroimaging data and psychological profiles effectively",
            "The art generation process is well-explained and tailored to the given art form and mental state",
            "Ethical considerations are thoroughly addressed",
            "The evaluation methods and future developments are thoughtfully proposed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
