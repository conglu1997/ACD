import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'social_phenomenon': 'spread of misinformation',
                'network_type': 'online social media platform'
            },
            '2': {
                'social_phenomenon': 'adoption of new ideas',
                'network_type': 'corporate organizational structure'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical neural network architecture inspired by social dynamics and information propagation in human social networks, then apply it to analyze and predict the {t['social_phenomenon']} in a {t['network_type']}. Your response should include:

1. Theoretical Foundation (200-250 words):
   a) Explain key concepts from neuroscience, information theory, and social psychology that inform your design.
   b) Discuss how these concepts relate to information propagation in social networks.

2. Neural Network Architecture (300-350 words):
   a) Describe the components and structure of your neural network architecture.
   b) Explain how your architecture incorporates principles of social dynamics and information propagation.
   c) Provide a diagram or mathematical representation of your architecture (describe it textually).
   d) Discuss how your architecture differs from traditional neural networks.

3. Information Propagation Model (250-300 words):
   a) Explain how your model simulates the spread of information in a social network.
   b) Describe the key parameters or variables in your model and their significance.
   c) Discuss how your model accounts for individual and group-level behaviors in information sharing.

4. Application to {t['social_phenomenon']} (250-300 words):
   a) Apply your model to analyze and predict the {t['social_phenomenon']} in a {t['network_type']}.
   b) Describe how you would set up and run a simulation using your model.
   c) Discuss potential insights or predictions your model might generate.
   d) Explain how these insights could be used to address real-world challenges related to {t['social_phenomenon']}.

5. Evaluation and Limitations (200-250 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your model.
   b) Discuss potential limitations or challenges in implementing your model.
   c) Suggest areas for future research or improvement.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using your model to analyze and predict social behavior.
   b) Address concerns related to privacy, manipulation, and social influence.
   c) Propose guidelines for the responsible use of your model in research or practical applications.

Ensure your response demonstrates a deep understanding of neuroscience, information theory, and social psychology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of neuroscience, information theory, and social psychology concepts.",
            "The proposed neural network architecture is innovative and effectively incorporates principles of social dynamics and information propagation.",
            "The information propagation model is well-explained and accounts for both individual and group-level behaviors.",
            "The application of the model to the given social phenomenon is thoughtful and generates potentially valuable insights.",
            "The evaluation methods and limitations discussion show critical thinking and awareness of the model's constraints.",
            "The ethical considerations are comprehensive and demonstrate an understanding of the potential impacts of the model.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
