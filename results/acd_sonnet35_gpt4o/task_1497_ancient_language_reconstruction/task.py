import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {
                "name": "Proto-Sinaitic",
                "period": "Bronze Age (c. 1850 BCE - 1550 BCE)",
                "region": "Sinai Peninsula",
                "known_info": "Early alphabetic writing system, precursor to many modern alphabets. Shows Egyptian influence and is believed to be based on Egyptian hieroglyphs.",
                "sample_words": ["𐤀𐤋𐤐", "𐤁𐤉𐤕", "𐤂𐤌𐤋", "𐤃𐤋𐤕", "𐤄𐤅𐤉"],
                "sample_meanings": ["ox", "house", "throw stick", "door", "jubilation"],
                "linguistic_features": "Consonantal alphabet, no vowels represented. Right-to-left writing direction."
            },
            {
                "name": "Linear A",
                "period": "Bronze Age Minoan civilization (c. 1800 BCE - 1450 BCE)",
                "region": "Crete",
                "known_info": "Syllabic script used for administrative purposes, still largely undeciphered. Shows some similarities to Linear B, which has been deciphered.",
                "sample_words": ["𐘇𐘂𐘈", "𐘚𐘦", "𐘀𐘁", "𐘃𐘅", "𐘾𐘸"],
                "sample_meanings": ["unknown", "unknown", "unknown", "unknown", "total"],
                "linguistic_features": "Mix of syllabic and logographic signs. Contains signs for numbers and various commodities."
            }
        ]
        
        texts = [
            "𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋𐤌𐤍𐤎𐤏𐤐𐤑𐤒𐤓𐤔𐤕",
            "𐘀𐘁𐘂𐘃𐘄𐘅𐘆𐘇𐘈𐘉𐘊𐘋𐘌𐘍𐘎𐘏𐘐𐘑𐘒𐘓𐘔𐘕𐙉𐙂𐙀"
        ]
        
        task = {
            "language": random.choice(languages),
            "text": random.choice(texts)
        }
        
        return {"1": task, "2": task}  # Both entries are the same to avoid confusion

    @staticmethod
    def get_instructions(t: dict) -> str:
        language = t["language"]
        text = t["text"]
        
        return f"Your task is to design an AI system to reconstruct the ancient language of {language['name']} and use it to translate a given text. Provide a comprehensive and detailed response for each section, demonstrating deep understanding and creative problem-solving. Follow these steps and ensure your response adheres to the specified format for each section:\n\n" \
               f"1. Language Reconstruction System Design (300-350 words):\n" \
               f"   a) Describe the architecture of your AI system for reconstructing {language['name']}, including specific algorithms and data structures.\n" \
               f"   b) Explain how your system would use the limited known information: {language['known_info']}\n" \
               f"   c) Detail the computational linguistics techniques and historical inference methods your system would employ.\n" \
               f"   d) Describe how your system would handle uncertainties and make educated guesses about unknown linguistic features.\n" \
               f"   e) Explain how your system would incorporate the known linguistic features: {language['linguistic_features']}\n" \
               f"   f) Discuss potential biases in your AI system and how you would mitigate them.\n\n" \
               f"2. Reconstruction Process (250-300 words):\n" \
               f"   a) Outline the step-by-step process your AI system would follow to reconstruct {language['name']}.\n" \
               f"   b) Explain how you would use the sample words and meanings provided: {language['sample_words']} - {language['sample_meanings']}.\n" \
               f"   c) Describe how your system would infer grammar rules and vocabulary.\n" \
               f"   d) Discuss how historical and cultural context from the {language['period']} in the {language['region']} would be incorporated.\n\n" \
               f"3. Translation Attempt (200-250 words):\n" \
               f"   a) Use your reconstructed language model to attempt a translation of the following text: {text}\n" \
               f"   b) Provide your best guess at the translation, explaining your reasoning for each part.\n" \
               f"   c) Highlight any words or phrases where you have low confidence in the translation, using [brackets].\n" \
               f"   d) Propose at least two alternative interpretations for ambiguous parts of the text.\n\n" \
               f"4. Evaluation and Limitations (200-250 words):\n" \
               f"   a) Propose a method to evaluate the accuracy of your language reconstruction and translation.\n" \
               f"   b) Discuss at least three specific limitations of your approach and potential sources of error.\n" \
               f"   c) Suggest how your system could be improved with additional data or advanced techniques.\n\n" \
               f"5. Implications and Ethics (150-200 words):\n" \
               f"   a) Discuss the potential impact of your AI system on the field of historical linguistics.\n" \
               f"   b) Explore at least two ethical considerations of using AI to reconstruct and interpret ancient languages.\n" \
               f"   c) Consider the implications for our understanding of human history and cultural heritage.\n\n" \
               f"Ensure your response demonstrates a deep understanding of computational linguistics, historical analysis, and AI technologies. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.\n\n" \
               f"Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1100-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of computational linguistics and historical analysis, with specific references to relevant techniques and methodologies.",
            "The AI system design is innovative, scientifically plausible, and comprehensively addresses the challenges of limited data in ancient language reconstruction, incorporating the provided linguistic features and historical context. It also considers potential biases and mitigation strategies.",
            "The reconstruction process is logical, well-explained, and makes appropriate use of the provided sample words and historical context, with clear steps for inferring grammar and vocabulary.",
            "The translation attempt is reasonable given the constraints, with clear explanations of the reasoning, highlighted uncertainties, and multiple interpretations for ambiguous parts.",
            "The evaluation method is specific and well-thought-out, and the limitations discussion shows critical thinking about at least three distinct challenges in this task.",
            "The implications and ethics section thoughtfully considers at least two ethical issues and the broader impact of this technology on historical linguistics and cultural heritage.",
            "The response is well-structured, follows the given format with clear headings and appropriate use of bullet points or numbered lists, and adheres to the word count guidelines."
        ]
        try:
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception as e:
            print(f"Error in scoring: {e}")
            return 0.0
