import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = ['visual', 'auditory', 'tactile', 'olfactory', 'gustatory']
        abstract_concepts = ['freedom', 'time', 'justice', 'love', 'knowledge']
        
        task1 = {
            "concept": random.choice(abstract_concepts),
            "primary_modality": random.choice(sensory_modalities)
        }
        task1["secondary_modality"] = random.choice([m for m in sensory_modalities if m != task1["primary_modality"]])
        
        task2 = {
            "concept": random.choice([c for c in abstract_concepts if c != task1["concept"]]),
            "primary_modality": random.choice(sensory_modalities)
        }
        task2["secondary_modality"] = random.choice([m for m in sensory_modalities if m != task2["primary_modality"]])
        
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract concepts using synesthesia-like associations across different sensory modalities, then apply it to the following scenario:

Abstract Concept: {t['concept']}
Primary Sensory Modality: {t['primary_modality']}
Secondary Sensory Modality: {t['secondary_modality']}

Your task has the following parts:

1. Synesthetic Mapping Framework (200-250 words):
   Explain the cognitive processes involved in synesthesia and how they can be applied to abstract concept representation. Describe how your AI system would implement these processes.

2. AI System Architecture (200-250 words):
   Provide a high-level overview of your AI system's architecture and its unique features for cross-modal concept generation and interpretation.

3. Application to the Given Scenario (250-300 words):
   Apply your AI system to generate a synesthetic representation of the given abstract concept using the primary and secondary sensory modalities. Provide a detailed explanation of the representation and the system's process.

4. Interpretation Mechanism (150-200 words):
   Describe how your AI system would interpret and explain synesthetic representations created by humans, addressing potential challenges.

5. Evaluation and Refinement (150-200 words):
   Propose a method for evaluating the generated synesthetic representations and describe how your AI system would improve its process based on feedback.

6. Cognitive and Neuroscientific Implications (100-150 words):
   Discuss potential implications of this technology for our understanding of human cognition and sensory processing.

Ensure your response demonstrates a deep understanding of cognitive science, neuroscience, synesthesia research, and AI system design. Be creative and innovative while maintaining scientific rigor. Your total response should be between 1050-1350 words.

Format your response with clear headings for each section, and include a word count for each section in parentheses at the end."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synesthesia, cognitive science, and AI system design.",
            "The proposed AI system architecture is innovative and plausible.",
            "The application to the given scenario is creative and well-explained.",
            "The interpretation mechanism addresses potential challenges in human-AI interaction.",
            "The evaluation method and refinement process are scientifically sound.",
            "The discussion of cognitive and neuroscientific implications is insightful and well-reasoned.",
            "The response maintains scientific rigor while being creative and innovative.",
            "The response follows the specified format with clear headings and word counts for each section.",
            "The total word count is within the specified range (1050-1350 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
