import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Spatial Relations",
                "cognitive_principle": "Image Schemas",
                "text_type": "Descriptive Paragraph"
            },
            {
                "domain": "Emotional Expression",
                "cognitive_principle": "Conceptual Metaphor",
                "text_type": "Dialogue"
            },
            {
                "domain": "Abstract Reasoning",
                "cognitive_principle": "Embodied Simulation",
                "text_type": "Argumentative Essay"
            },
            {
                "domain": "Social Interaction",
                "cognitive_principle": "Situated Cognition",
                "text_type": "Short Story"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language model that incorporates principles of cognitive linguistics and embodied cognition, then use it to generate and analyze text in the domain of {t['domain']}, focusing on the cognitive principle of {t['cognitive_principle']}. Your task is to create a {t['text_type']} using this model. Provide a detailed response addressing the following points:

1. Model Architecture (250-300 words):
   a) Describe the key components of your embodied cognitive language model.
   b) Explain how it incorporates the principle of {t['cognitive_principle']}.
   c) Discuss how your model simulates embodied experiences in language processing.
   d) Include a diagram or flowchart illustrating the model's architecture (describe it textually if unable to produce an actual diagram).

2. Cognitive-Linguistic Integration (200-250 words):
   a) Explain how your model integrates cognitive linguistics theories with natural language processing techniques.
   b) Describe how it handles the relationship between language, thought, and physical experience.
   c) Discuss any novel algorithms or approaches used in your design.

3. Text Generation (200-250 words):
   a) Generate a {t['text_type']} (exactly 100 words) in the domain of {t['domain']} using your model.
   b) Explain how the cognitive principle of {t['cognitive_principle']} influenced the generation process.
   c) Analyze the key features of the generated text and how they reflect embodied cognition.

4. Comparative Analysis (150-200 words):
   a) Compare your embodied cognitive language model to traditional language models.
   b) Discuss the potential advantages and limitations of your approach.
   c) Explain how your model might handle ambiguity or context-dependent meanings differently.

5. Cognitive Science Implications (150-200 words):
   a) Discuss the implications of your model for our understanding of human language processing and cognition.
   b) Explore how your model might support or challenge existing theories in cognitive linguistics.
   c) Propose an experiment to test a hypothesis derived from your model.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Address potential ethical concerns related to embodied AI language models.
   b) Suggest future research directions or potential applications of your model in fields such as education, therapy, or human-AI interaction.
   c) Discuss how your model might be extended to incorporate other cognitive principles or linguistic phenomena.

Ensure your response demonstrates a deep understanding of cognitive linguistics, embodied cognition, and natural language processing. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive linguistics, embodied cognition, and natural language processing.",
            "The model architecture and cognitive-linguistic integration are well-explained and scientifically plausible.",
            "The generated text is exactly 100 words and clearly incorporates the specified cognitive principle and domain.",
            "The comparative analysis and cognitive science implications are insightful and well-reasoned.",
            "The discussion of ethical considerations and future directions is thoughtful and relevant.",
            "The response shows creativity and innovation while maintaining scientific rigor.",
            "Technical terminology is used appropriately and complex concepts are explained clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
