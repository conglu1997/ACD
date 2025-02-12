import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_cognitive_features = [
            {
                'cognitive_feature': 'analytic vs. holistic thinking',
                'cultural_context': 'Western vs. East Asian cultures',
                'neuroscience_principle': 'default mode network activation patterns'
            },
            {
                'cognitive_feature': 'individualistic vs. collectivistic decision-making',
                'cultural_context': 'North American vs. Japanese cultures',
                'neuroscience_principle': 'medial prefrontal cortex activity'
            }
        ]
        
        return {str(i+1): random.choice(cultural_cognitive_features) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel AI architecture inspired by cultural variations in human cognition, focusing on the cognitive feature of {t['cognitive_feature']} as observed in {t['cultural_context']}, and incorporating the neuroscience principle of {t['neuroscience_principle']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen cognitive feature and its cultural variation.
   b) Describe the relevant neuroscience principle and its role in this cognitive process.
   c) Propose a hypothesis for how these elements could be integrated into an AI architecture.
   d) Discuss potential advantages of this culturally-inspired approach over traditional AI architectures.

2. AI Architecture Design (300-350 words):
   a) Describe the main components of your AI architecture and how they interact.
   b) Explain how your design incorporates the specified cognitive feature and cultural variation.
   c) Detail how the neuroscience principle is implemented in your architecture.
   d) Provide a high-level diagram or pseudocode to illustrate your architecture.
   e) Discuss any novel features or mechanisms in your design that differ from existing AI systems.

3. Learning and Adaptation (200-250 words):
   a) Explain how your AI system would learn and adapt to different cultural contexts.
   b) Describe the training process and data requirements for your system.
   c) Discuss how your architecture might simulate aspects of human cultural learning and adaptation.
   d) Address potential challenges in implementing cross-cultural adaptability in AI.

4. Potential Applications (200-250 words):
   a) Propose three potential applications of your AI architecture in fields such as cross-cultural communication, global business, or international relations.
   b) For each application, explain how the culturally-inspired features of your AI would provide unique advantages.
   c) Discuss any ethical considerations or potential misuses of your system in these applications.

5. Comparative Analysis (200-250 words):
   a) Compare your proposed architecture to existing AI systems in terms of potential performance on tasks requiring cultural understanding or adaptation.
   b) Discuss possible limitations or challenges of your approach.
   c) Propose methods to empirically evaluate the effectiveness of your culturally-inspired AI compared to traditional systems.

6. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of your AI architecture for our understanding of culture, cognition, and artificial intelligence.
   b) Explore how this approach might influence future developments in AI and cognitive science.
   c) Propose two directions for future research or development based on your architecture.
   d) Speculate on potential long-term impacts of culturally-adaptive AI on global society and human culture.

7. Summary (100-150 words):
   Provide a concise summary of your proposed AI architecture, its key features, potential applications, and broader implications.

Ensure your response demonstrates a deep understanding of cultural anthropology, neuroscience, and artificial intelligence. Be creative and innovative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specified cognitive feature, cultural variation, and neuroscience principle.",
            "The AI architecture design is innovative, coherently incorporates the cultural and neuroscientific elements, and is clearly explained.",
            "The learning and adaptation process is well-thought-out and addresses cross-cultural challenges.",
            "The potential applications are creative, well-reasoned, and demonstrate the unique advantages of the culturally-inspired AI.",
            "The comparative analysis critically evaluates the proposed architecture against existing systems and suggests valid empirical evaluation methods.",
            "The discussion of implications and future directions shows deep insight into the potential impacts of culturally-adaptive AI on science and society.",
            "The summary effectively synthesizes the key points of the proposed AI architecture, its applications, and implications.",
            "The response is well-structured, within the specified word count, and demonstrates originality and interdisciplinary integration throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
