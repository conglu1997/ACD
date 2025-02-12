import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synesthesia_types = [
            {"type": "grapheme-color", "description": "associating letters or numbers with specific colors"},
            {"type": "chromesthesia", "description": "associating sounds with colors"},
            {"type": "lexical-gustatory", "description": "associating words with tastes"},
            {"type": "spatial-sequence", "description": "perceiving numerical sequences as points in space"},
            {"type": "mirror-touch", "description": "feeling the same sensation that another person feels"}
        ]
        return {
            "1": random.choice(synesthesia_types),
            "2": random.choice(synesthesia_types)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI language model that incorporates principles of {t['type']} synesthesia ({t['description']}) to generate and interpret multi-sensory linguistic outputs. Then, analyze its potential applications and implications for human-AI interaction. Your response should include:\n\n1. Model Architecture (300-350 words):\n   a) Describe the key components of your AI model and how they simulate {t['type']} synesthesia.\n   b) Explain how your model integrates this form of synesthesia with language processing.\n   c) Detail any novel neural network structures or algorithms used in your design.\n   d) Provide a high-level diagram or flowchart illustrating your model's architecture (describe it textually).\n\n2. Training and Data (200-250 words):\n   a) Outline the types of data you would use to train your synesthetic AI model.\n   b) Describe any unique data collection or preprocessing methods required.\n   c) Explain how you would validate the model's synesthetic associations.\n\n3. Output Generation (250-300 words):\n   a) Provide an example of how your model would generate a multi-sensory output for a given input.\n   b) Explain the process of translating between linguistic and synesthetic representations.\n   c) Discuss how your model handles ambiguity or conflicts in sensory associations.\n\n4. Cognitive Implications (200-250 words):\n   a) Analyze how your model's synesthetic capabilities might influence its language understanding and generation.\n   b) Discuss potential insights this model could provide into human cognition and perception.\n   c) Explore any limitations or biases that might arise from this synesthetic approach.\n\n5. Applications and Ethics (250-300 words):\n   a) Propose three potential applications of your synesthetic AI model in different fields.\n   b) Discuss the ethical implications of using AI systems that simulate human sensory experiences.\n   c) Suggest guidelines for responsible development and use of synesthetic AI technologies.\n\n6. Experimental Design (200-250 words):\n   Propose an experiment to test the effectiveness and impact of your synesthetic AI model:\n   a) Describe the experimental setup, methodology, and expected results.\n   b) Explain how the results would validate (or invalidate) your model's design.\n   c) Discuss how this experiment could contribute to our understanding of both AI and human cognition.\n\n7. Limitations and Challenges (100-150 words):\n   Discuss potential limitations or challenges in implementing and scaling your synesthetic AI language model.\n\n8. Conclusion (50-100 words):\n   Summarize the key points of your design and its potential impact on AI and cognitive science.\n\nEnsure your response demonstrates a deep understanding of synesthesia, cognitive neuroscience, linguistics, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1550-1950 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['type']} synesthesia and its integration with AI language models.",
            "The model architecture is well-explained and scientifically plausible.",
            "The training approach and data requirements are thoughtfully considered.",
            "The output generation process is clearly described with a concrete example.",
            "The cognitive implications are insightfully analyzed.",
            "The proposed applications are innovative and span different fields.",
            "Ethical considerations are thoroughly discussed with thoughtful guidelines proposed.",
            "The experimental design is well-structured and relevant to validating the model.",
            "Limitations and challenges of the model are realistically assessed.",
            "The conclusion effectively summarizes the key points of the design.",
            "The response demonstrates creativity while maintaining scientific accuracy.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
