import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_linguistic_principles = [
            "Conceptual metaphor theory",
            "Frame semantics",
            "Cognitive grammar",
            "Prototype theory",
            "Mental spaces theory"
        ]
        neurolinguistic_aspects = [
            "Broca's area function",
            "Wernicke's area processing",
            "N400 component",
            "P600 component",
            "Mirror neuron system"
        ]
        ai_communication_challenges = [
            "Contextual understanding",
            "Ambiguity resolution",
            "Emotional interpretation",
            "Pragmatic inference",
            "Cross-cultural communication"
        ]
        communication_modalities = [
            "Text-based",
            "Speech-based",
            "Multimodal (text and speech)",
            "Visual-linguistic"
        ]
        task1 = {
            "cognitive_principle": random.choice(cognitive_linguistic_principles),
            "neurolinguistic_aspect": random.choice(neurolinguistic_aspects),
            "ai_challenge": random.choice(ai_communication_challenges),
            "modality": random.choice(communication_modalities)
        }
        task2 = {
            "cognitive_principle": random.choice(cognitive_linguistic_principles),
            "neurolinguistic_aspect": random.choice(neurolinguistic_aspects),
            "ai_challenge": random.choice(ai_communication_challenges),
            "modality": random.choice(communication_modalities)
        }
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        cognitive_principle = t["cognitive_principle"]
        neurolinguistic_aspect = t["neurolinguistic_aspect"]
        ai_challenge = t["ai_challenge"]
        modality = t["modality"]
        
        return f"Design an AI system that enhances human-AI communication by leveraging principles from cognitive linguistics and neurolinguistics. Your system should incorporate the cognitive linguistic principle of {cognitive_principle}, address the neurolinguistic aspect of {neurolinguistic_aspect}, tackle the AI communication challenge of {ai_challenge}, and focus on the {modality} modality. Your response should include the following sections:\n\n" \
               f"1. Theoretical Framework (250-300 words):\n" \
               f"   a) Explain the relevance of {cognitive_principle} to human-AI communication.\n" \
               f"   b) Describe how {neurolinguistic_aspect} influences language processing and production.\n" \
               f"   c) Discuss the challenges posed by {ai_challenge} in current AI systems.\n" \
               f"   d) Propose a novel hypothesis about enhancing human-AI communication based on these concepts.\n\n" \
               f"2. System Architecture (300-350 words):\n" \
               f"   a) Describe the key components of your AI system for enhancing human-AI communication.\n" \
               f"   b) Explain how your system incorporates {cognitive_principle} in its language processing.\n" \
               f"   c) Detail how your system accounts for {neurolinguistic_aspect} in its communication model.\n" \
               f"   d) Discuss how your system addresses the challenge of {ai_challenge}.\n" \
               f"   e) Explain how your system is optimized for the {modality} modality.\n" \
               f"   f) Provide a high-level diagram or flowchart of your system architecture (describe it textually).\n\n" \
               f"3. Implementation Strategy (250-300 words):\n" \
               f"   a) Outline the key algorithms or techniques your system would use to process and generate language.\n" \
               f"   b) Explain how you would train or develop your system to incorporate the specified cognitive and neurolinguistic principles.\n" \
               f"   c) Describe any novel computational approaches in your system design.\n" \
               f"   d) Discuss potential challenges in implementing your system and how you would address them.\n\n" \
               f"4. Evaluation Methodology (200-250 words):\n" \
               f"   a) Propose methods to evaluate the effectiveness of your system in enhancing human-AI communication.\n" \
               f"   b) Describe specific metrics or experiments you would use to assess improvement in {ai_challenge}.\n" \
               f"   c) Explain how you would measure the system's alignment with {cognitive_principle} and {neurolinguistic_aspect}.\n" \
               f"   d) Discuss potential limitations of your evaluation approach and how you might address them.\n\n" \
               f"5. Practical Applications (200-250 words):\n" \
               f"   a) Describe potential real-world applications of your enhanced human-AI communication system.\n" \
               f"   b) Explain how your system could improve current AI technologies in areas such as virtual assistants, language translation, or human-robot interaction.\n" \
               f"   c) Discuss any ethical considerations or potential societal impacts of your system.\n\n" \
               f"6. Future Directions (150-200 words):\n" \
               f"   a) Propose two potential extensions or improvements to your system for future development.\n" \
               f"   b) Suggest a research question that could further the integration of cognitive linguistics, neurolinguistics, and AI in enhancing human-AI communication.\n\n" \
               f"Ensure your response demonstrates a deep understanding of cognitive linguistics, neurolinguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, neurolinguistics, and artificial intelligence, with appropriate use of technical terminology.",
            "The AI system design effectively incorporates the specified cognitive linguistic principle, neurolinguistic aspect, and addresses the given AI communication challenge.",
            "The system architecture and implementation strategy are well-explained, scientifically plausible, and optimized for the specified communication modality.",
            "The evaluation methodology and practical applications are thoroughly addressed and relevant to the proposed system.",
            "The response is innovative while maintaining scientific and practical plausibility.",
            "The response is well-structured, follows the given format with clear headings, and adheres to the word count guidelines.",
            "The response includes specific examples or use cases that illustrate how the system would work in practice.",
            "The future directions proposed are relevant and demonstrate forward-thinking in the field of human-AI communication."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
