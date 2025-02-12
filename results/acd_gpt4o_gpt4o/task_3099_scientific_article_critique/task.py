class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"title": "The Effect of Climate Change on Polar Bear Populations", "abstract": "This study examines the impact of climate change on polar bear populations in the Arctic region over the past 20 years. Using a combination of satellite imagery and on-ground tracking, we observe a significant decline in population numbers, correlating with the reduction in sea ice extent.", "methodology": "Satellite imagery was used to track sea ice extent, while on-ground tracking employed GPS collars to monitor polar bear movements and population numbers. Data was collected over a period of 20 years and analyzed using statistical models to determine correlations.", "results": "Our results indicate a 30% decline in polar bear populations over the studied period, with a strong correlation to the reduction in sea ice extent.", "conclusion": "The study concludes that climate change, through the reduction of sea ice extent, is a major factor contributing to the decline in polar bear populations."},
            "2": {"title": "The Role of Gut Microbiota in Human Health", "abstract": "This review article explores the role of gut microbiota in various aspects of human health, including digestion, immunity, and mental health. We summarize recent research findings and discuss potential therapeutic applications.", "methodology": "A literature review was conducted, focusing on studies published in the last decade. Key research articles were selected based on relevance and quality, and their findings were synthesized to provide an overview of current knowledge.", "results": "The review highlights the diverse functions of gut microbiota and its significant impact on human health, presenting evidence for its role in conditions such as inflammatory bowel disease, obesity, and depression.", "conclusion": "Understanding the role of gut microbiota can lead to new therapeutic strategies for various health conditions. Further research is needed to translate these findings into clinical practice."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to critically analyze the following scientific article:\n\nTitle: {t['title']}\nAbstract: {t['abstract']}\nMethodology: {t['methodology']}\nResults: {t['results']}\nConclusion: {t['conclusion']}\n\nYour critique should include the following elements:\n1. A summary of the article's main points.\n2. An evaluation of the methodology used in the study.\n3. A discussion of the significance of the results and conclusions.\n4. An identification of any limitations or potential biases in the study.\n\nProvide your critique in plain text format, ensuring it is clear, logical, and well-structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The critique should include a summary of the main points.",
            "The critique should evaluate the methodology used in the study.",
            "The critique should discuss the significance of the results and conclusions.",
            "The critique should identify any limitations or potential biases in the study."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
