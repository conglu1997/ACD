class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "brain_region": "Visual cortex",
                "art_style": "Abstract expressionism",
                "ethical_focus": "Authenticity and authorship"
            },
            "2": {
                "brain_region": "Prefrontal cortex",
                "art_style": "Surrealism",
                "ethical_focus": "Privacy and mental autonomy"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system that translates neural activity from the {t['brain_region']} into visual art in the style of {t['art_style']}. Your system should use AI to interpret brain signals and generate art. Throughout your design, carefully consider and address the ethical implications, with a particular focus on {t['ethical_focus']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your BCI system, including neural signal acquisition, processing, and art generation.
   b) Explain how AI is used to interpret brain signals and translate them into artistic elements.
   c) Detail how your system captures and incorporates the specific characteristics of {t['art_style']}.
   d) Include a high-level diagram of your system architecture (describe it in words).
   e) Discuss any ethical considerations in the system's design and implementation.

2. Neural Signal Processing (250-300 words):
   a) Explain your approach to processing neural signals from the {t['brain_region']}.
   b) Describe any novel algorithms or techniques used for signal decoding and feature extraction.
   c) Discuss how you handle noise, artifacts, and individual variability in brain signals.
   d) Address potential ethical concerns related to neural data collection and processing.

3. AI-Powered Art Generation (250-300 words):
   a) Detail the AI models or algorithms used for generating art based on processed neural signals.
   b) Explain how your system ensures the output adheres to the principles of {t['art_style']}.
   c) Describe any techniques used to maintain coherence and aesthetic quality in the generated art.
   d) Discuss ethical considerations in AI-generated art, particularly regarding {t['ethical_focus']}.

4. User Experience and Interaction (200-250 words):
   a) Describe the user interface and experience of your BCI art system.
   b) Explain how users can control or influence the art generation process.
   c) Discuss any feedback mechanisms that allow users to refine their neural-to-art translation skills.
   d) Address ethical aspects of user interaction, including informed consent and user autonomy.

5. Ethical Considerations (200-250 words):
   a) Provide an in-depth analysis of the ethical consideration of {t['ethical_focus']} in the context of your BCI art system.
   b) Discuss potential risks or misuses of the technology and propose comprehensive safeguards.
   c) Explore the broader implications of this technology for the future of art, human creativity, and cognitive liberty.

6. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the effectiveness and quality of your neural art synthesis system.
   b) Describe how you would validate the authenticity of the neural-art connection.
   c) Suggest experiments to compare AI-generated art with traditional human-created art in the {t['art_style']} style.
   d) Discuss ethical considerations in the evaluation process, including potential biases.

7. Potential Applications and Future Directions (150-200 words):
   a) Discuss potential applications of your system beyond artistic expression.
   b) Suggest how this technology could be extended to other creative domains.
   c) Propose a research agenda for further developing neural-AI creative collaboration.
   d) Address potential long-term ethical and societal impacts of advancing this technology.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and art theory, while consistently addressing ethical considerations throughout. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all seven required sections comprehensively.",
            "The system design demonstrates a deep understanding of neuroscience, AI, and art theory.",
            "The proposed BCI system is innovative, plausible, and well-explained.",
            "The response adequately addresses the specified brain region, art style, and ethical focus.",
            "Ethical considerations are thoroughly integrated throughout the entire response.",
            "The ethical analysis is comprehensive and considers multiple perspectives.",
            "The response shows creativity in addressing complex interdisciplinary challenges while maintaining ethical integrity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
