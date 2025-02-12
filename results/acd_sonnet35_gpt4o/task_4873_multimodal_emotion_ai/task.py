import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        modalities = ['visual', 'auditory', 'textual']
        emotions = ['anger', 'fear', 'joy', 'sadness', 'disgust', 'surprise']
        brain_regions = ['amygdala', 'prefrontal cortex', 'insula', 'anterior cingulate cortex']
        
        tasks = [
            {
                'modality': random.choice(modalities),
                'emotion': random.choice(emotions),
                'brain_region': random.choice(brain_regions)
            },
            {
                'modality': random.choice(modalities),
                'emotion': random.choice(emotions),
                'brain_region': random.choice(brain_regions)
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the human brain's ability to recognize and process emotions, focusing on the {t['modality']} modality for detecting {t['emotion']}, and incorporating recent neuroscientific findings about the role of the {t['brain_region']} in emotion processing. Your response should include the following sections:

1. Neuroscientific Foundation (200-250 words):
   a) Explain the role of the {t['brain_region']} in emotion processing, particularly for {t['emotion']}.
   b) Describe how this brain region interacts with other areas during emotion recognition.
   c) Discuss recent neuroscientific findings relevant to emotion processing in the {t['modality']} modality.

2. AI System Architecture (250-300 words):
   a) Propose a novel AI architecture that mimics the identified neural processes.
   b) Explain how your system incorporates the functioning of the {t['brain_region']}.
   c) Describe how your model processes {t['modality']} input to recognize {t['emotion']}.
   d) Include a diagram or detailed description of your proposed architecture.

3. Emotion Recognition Process (200-250 words):
   a) Detail the step-by-step process of how your AI system recognizes {t['emotion']} from {t['modality']} input.
   b) Explain how your system handles ambiguous or mixed emotional signals.
   c) Discuss any novel approaches or algorithms used in your emotion recognition process.

4. Multimodal Integration (200-250 words):
   a) Describe how your system could be extended to incorporate other modalities beyond {t['modality']}.
   b) Explain the challenges and potential solutions for integrating multiple modalities in emotion recognition.
   c) Discuss how multimodal integration might improve emotion recognition accuracy.

5. Training and Adaptation (150-200 words):
   a) Propose a method for training your AI system.
   b) Explain how your model could adapt to individual differences in emotion expression and perception.
   c) Discuss any potential challenges in the training process and how they might be overcome.

6. Evaluation and Benchmarking (150-200 words):
   a) Suggest methods to evaluate the performance of your AI system in recognizing {t['emotion']}.
   b) Propose benchmarks to compare your model's performance against existing emotion recognition systems and human performance.
   c) Discuss how you would measure the model's ability to mimic human-like emotion processing.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of developing AI systems that closely mimic human emotion recognition.
   b) Address any limitations of your proposed architecture and suggest areas for future research.
   c) Propose guidelines for the responsible development and use of emotion recognition AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and emotion theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words.

Example (partial, for Neuroscientific Foundation only):
1. Neuroscientific Foundation
The {t['brain_region']} plays a crucial role in emotion processing, particularly in recognizing and regulating {t['emotion']}. Recent studies using fMRI have shown increased activation in this region during {t['emotion']} recognition tasks involving {t['modality']} stimuli. For instance, ..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all seven required sections with appropriate content related to {t['emotion']} recognition in the {t['modality']} modality.",
            f"The system design demonstrates integration of neuroscience (particularly regarding the {t['brain_region']}) and artificial intelligence principles.",
            "The proposed AI architecture is innovative while remaining scientifically plausible.",
            "The response shows a deep understanding of emotion processing in the human brain and how it can be mimicked by AI systems.",
            "The ethical considerations and limitations are thoughtfully addressed, including proposed guidelines for responsible development.",
            "The response includes specific examples, algorithms, or mathematical representations where appropriate.",
            "The multimodal integration section provides a clear explanation of how to extend the system beyond the given modality.",
            "The evaluation and benchmarking section proposes concrete methods and metrics for assessing the system's performance."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
