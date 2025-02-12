import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        narrative_structures = [
            {"structure": "Hero's Journey", "ai_concept": "Reinforcement Learning"},
            {"structure": "In Medias Res", "ai_concept": "Attention Mechanisms"},
            {"structure": "Frame Narrative", "ai_concept": "Hierarchical Neural Networks"},
            {"structure": "Stream of Consciousness", "ai_concept": "Recurrent Neural Networks"},
            {"structure": "Epistolary", "ai_concept": "Transformer Architecture"},
            {"structure": "Nonlinear Narrative", "ai_concept": "Graph Neural Networks"},
            {"structure": "Parallel Narrative", "ai_concept": "Multi-Task Learning"},
            {"structure": "Flashback/Flash-forward", "ai_concept": "Memory Networks"},
            {"structure": "Unreliable Narrator", "ai_concept": "Adversarial Networks"},
            {"structure": "Bildungsroman", "ai_concept": "Curriculum Learning"}
        ]
        return {
            "1": random.choice(narrative_structures),
            "2": random.choice(narrative_structures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a neural network architecture inspired by the literary narrative structure '{t['structure']}', incorporating concepts from {t['ai_concept']}. Your response should include:\n\n1. Architecture Design (250-300 words):\n   a) Describe the key components of your neural network architecture.\n   b) Explain how your design is inspired by the structure and function of {t['structure']}.\n   c) Detail how you incorporate {t['ai_concept']} into your model and why it's suitable for this task.\n   d) Discuss how your architecture captures essential elements of the narrative structure.\n\n2. Training and Data (200-250 words):\n   a) Outline the training process for your neural network.\n   b) Describe the dataset you would use, including its composition and preprocessing.\n   c) Explain any specific training techniques or algorithms you would employ.\n   d) Discuss potential challenges in training and how you would address them.\n\n3. Output Generation (200-250 words):\n   a) Explain how your trained model would generate or analyze narratives.\n   b) Describe how you ensure the output adheres to the principles of {t['structure']}.\n   c) Discuss any post-processing techniques you would apply to refine the output.\n\n4. Evaluation Metrics (150-200 words):\n   a) Propose at least three quantitative metrics to evaluate the quality and style-adherence of the generated or analyzed narratives.\n   b) Describe a qualitative evaluation method involving human readers or literary experts.\n   c) Explain how you would use these evaluations to improve your model.\n\n5. Literary Theory Insights (200-250 words):\n   a) Discuss how your model's performance might provide insights into {t['structure']} as a narrative technique.\n   b) Propose a hypothesis about human narrative processing that could be tested using your model.\n   c) Explain how your approach might contribute to our understanding of creativity in literature.\n\n6. AI and Ethical Implications (150-200 words):\n   a) Discuss the potential impact of AI-generated or AI-analyzed narratives on human authors and the literary field.\n   b) Address copyright and authorship issues related to AI-involved literary works.\n   c) Explore the philosophical question: Can AI-generated narratives be considered truly creative or artistic?\n\nEnsure your response demonstrates a deep understanding of neural network architectures, AI concepts, and literary theory. Be creative in your approach while maintaining scientific accuracy and plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of both {t['structure']} as a narrative structure and {t['ai_concept']} as an AI concept.",
            "The proposed neural network architecture creatively and plausibly integrates the narrative structure with the AI concept.",
            "The training process and data considerations are well-thought-out and appropriate for the task.",
            "The output generation process is clearly explained and aligns with the chosen narrative structure.",
            "The evaluation metrics are appropriate and well-justified.",
            "The discussion of literary theory insights is thoughtful and demonstrates interdisciplinary thinking.",
            "The ethical implications are thoroughly considered and discussed.",
            "The response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
