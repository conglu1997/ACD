class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "cognitive_ability": "working memory",
                "neural_network_type": "recurrent neural network"
            },
            "2": {
                "cognitive_ability": "pattern recognition",
                "neural_network_type": "convolutional neural network"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) system that enhances {t['cognitive_ability']} using a {t['neural_network_type']}. Then, analyze its potential impacts and ethical implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your BCI system, including both hardware and software elements.
   b) Explain how the {t['neural_network_type']} is integrated into the system to enhance {t['cognitive_ability']}.
   c) Detail the interface between the artificial neural network and biological neurons.
   d) Discuss any novel approaches you've incorporated to ensure seamless integration and minimal invasiveness.
   e) Provide a specific example of how information would flow through your system during a cognitive task related to {t['cognitive_ability']}.

2. Neuroscientific Basis (250-300 words):
   a) Explain the current understanding of how {t['cognitive_ability']} functions in the human brain.
   b) Describe how your BCI system interacts with and enhances the relevant neural circuits.
   c) Discuss potential neuroplasticity considerations and how your system accounts for them.
   d) Address any potential neurological risks and how your design mitigates them.

3. Enhancement Mechanism (200-250 words):
   a) Explain in detail how the {t['neural_network_type']} enhances {t['cognitive_ability']}.
   b) Provide a specific example of how a cognitive task would be improved using your system.
   c) Discuss the expected magnitude of enhancement and any potential limitations.
   d) Explain how your system adapts to individual differences in brain structure and function.

4. Ethical Analysis (250-300 words):
   a) Discuss the ethical implications of enhancing {t['cognitive_ability']} through a BCI system.
   b) Address concerns about equity and access to such technology.
   c) Analyze potential social impacts if this technology becomes widespread.
   d) Propose guidelines for the responsible development and use of cognitive enhancement BCIs.
   e) Discuss the implications for personal identity and authenticity of achievements.

5. Societal Impact (200-250 words):
   a) Predict how widespread adoption of this technology might reshape education, work, and daily life.
   b) Discuss potential new fields or professions that could emerge as a result of this technology.
   c) Address concerns about potential misuse or weaponization of this technology.
   d) Analyze how this technology might impact social interactions and relationships.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research to advance this type of BCI system.
   b) Explain how these research directions could address current limitations or open up new possibilities.
   c) Discuss potential interdisciplinary collaborations that could drive innovation in this field.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, ethics, and speculative technology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and brain-computer interfaces.",
            "The proposed BCI system is innovative yet scientifically plausible.",
            "The explanation of how the specified neural network enhances the given cognitive ability is clear and well-reasoned.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The discussion of societal impact is insightful and considers long-term consequences.",
            "The response effectively integrates knowledge from multiple disciplines.",
            "The suggested future research directions are relevant and well-justified.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
