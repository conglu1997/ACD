import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            "relaxation",
            "motivation",
            "focus",
            "joy",
            "catharsis"
        ]
        therapeutic_goals = [
            "stress reduction",
            "depression management",
            "anxiety relief",
            "PTSD treatment",
            "addiction recovery"
        ]
        
        return {
            "1": {
                "emotional_state": random.choice(emotional_states),
                "therapeutic_goal": random.choice(therapeutic_goals)
            },
            "2": {
                "emotional_state": random.choice(emotional_states),
                "therapeutic_goal": random.choice(therapeutic_goals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that composes music to induce specific emotional states, then use it to create a musical piece for a given therapeutic goal. Focus on inducing the emotional state of {t['emotional_state']} for the therapeutic goal of {t['therapeutic_goal']}. Your response should include:\n\n" \
               f"1. AI System Architecture (300-350 words):\n" \
               f"   a) Describe the key components of your AI system for composing emotionally targeted music.\n" \
               f"   b) Explain how the system integrates knowledge from music theory, psychology of emotions, and AI.\n" \
               f"   c) Detail how the AI ensures the composed music effectively induces the target emotional state.\n" \
               f"   d) Include a brief textual description of a flowchart representing your system's architecture.\n" \
               f"   e) Specify the types of AI models or algorithms used (e.g., neural networks, rule-based systems).\n" \
               f"   f) Explain how your system handles potential conflicts between emotional targets and therapeutic goals.\n\n" \
               f"2. Emotional-Musical Mapping (250-300 words):\n" \
               f"   a) Analyze how musical elements (e.g., rhythm, melody, harmony, tempo, key) correlate with the target emotional state of {t['emotional_state']}.\n" \
               f"   b) Explain how your AI system translates psychological understanding of emotions into musical parameters.\n" \
               f"   c) Describe any novel approaches your system uses to create emotionally evocative music.\n" \
               f"   d) Provide specific examples of how musical features would be adjusted to induce {t['emotional_state']}.\n" \
               f"   e) Discuss how cultural differences in emotional perception of music are addressed in your system.\n\n" \
               f"3. Composition Process (250-300 words):\n" \
               f"   a) Outline the step-by-step process your AI system would follow to compose a piece for {t['emotional_state']}.\n" \
               f"   b) Explain how the system adapts its composition to suit the therapeutic goal of {t['therapeutic_goal']}.\n" \
               f"   c) Discuss how the AI balances creativity with the need to meet specific emotional and therapeutic targets.\n" \
               f"   d) Describe any constraints or guidelines provided to the AI to ensure therapeutic efficacy.\n" \
               f"   e) Explain how your system handles potential composer's block or creative impasses.\n\n" \
               f"4. Sample Composition Description (200-250 words):\n" \
               f"   a) Describe a musical piece your AI system would generate for the given emotional state and therapeutic goal.\n" \
               f"   b) Explain the key musical elements (e.g., tempo, key, instrumentation, dynamics) and how they contribute to inducing the target emotional state.\n" \
               f"   c) Discuss how the composition would be tailored to support the specific therapeutic goal.\n" \
               f"   d) Provide a brief 'virtual walkthrough' of the composition, describing how it might progress over time.\n" \
               f"   e) Address how the composition accounts for potential listener fatigue or habituation.\n\n" \
               f"5. Evaluation and Iteration (200-250 words):\n" \
               f"   a) Propose methods to evaluate the effectiveness of the AI-generated music in inducing the target emotional state.\n" \
               f"   b) Describe how your system would use feedback to improve future compositions.\n" \
               f"   c) Discuss potential challenges in accurately assessing emotional impact and therapeutic efficacy.\n" \
               f"   d) Suggest a specific experimental design to test the system's effectiveness.\n" \
               f"   e) Explain how your system would handle cases where the music fails to induce the intended emotion.\n\n" \
               f"6. Ethical Considerations (150-200 words):\n" \
               f"   a) Discuss ethical implications of using AI-generated music for emotional manipulation and therapy.\n" \
               f"   b) Address potential risks or misuses of this technology and propose safeguards.\n" \
               f"   c) Consider the impact on human composers and the music industry.\n" \
               f"   d) Discuss issues of consent and transparency when using AI-generated music in therapy.\n" \
               f"   e) Analyze potential long-term psychological effects of relying on AI-generated emotional music.\n\n" \
               f"7. Future Directions (150-200 words):\n" \
               f"   a) Suggest two potential improvements or extensions to your AI system for emotional music composition.\n" \
               f"   b) Propose a novel application of your system beyond therapy (e.g., education, gaming, personalized entertainment).\n" \
               f"   c) Discuss how this approach could influence future trends in AI, music, and emotional well-being.\n" \
               f"   d) Speculate on potential long-term societal impacts of widespread use of emotionally targeted AI-generated music.\n" \
               f"   e) Propose a potential integration of this technology with other emerging fields (e.g., virtual reality, brain-computer interfaces).\n\n" \
               f"Ensure your response demonstrates a deep understanding of music theory, psychology of emotions, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.\n\n" \
               f"Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1500-1850 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of music theory, psychology of emotions, and artificial intelligence.",
            f"The AI system architecture is well-defined, with clear explanations of its components and how they integrate knowledge from multiple disciplines.",
            f"The emotional-musical mapping is thoroughly explained, with specific examples related to {t['emotional_state']}.",
            f"The composition process is clearly outlined, with a logical approach to balancing creativity and therapeutic goals.",
            f"The sample composition description provides a detailed 'virtual walkthrough' of a piece designed for {t['emotional_state']} and {t['therapeutic_goal']}.",
            "The evaluation methods and iteration process are well-thought-out and scientifically sound.",
            "Ethical considerations are comprehensively addressed, including potential risks and safeguards.",
            "Future directions and potential impacts are insightfully discussed.",
            "The response is well-structured, with clear headings and numbered paragraphs as requested.",
            "The overall approach is creative, innovative, and scientifically plausible.",
            "The response addresses all sub-points (a-e) for each main section.",
            "The word count is within the specified range of 1500-1850 words."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
