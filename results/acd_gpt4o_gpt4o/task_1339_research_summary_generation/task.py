class TaskFamily:
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "abstracts": [
                    "This paper presents a novel approach to machine learning that combines deep learning with reinforcement learning techniques. The proposed method is evaluated on several benchmark datasets and demonstrates significant improvements in performance compared to existing methods.",
                    "In this study, we investigate the impact of data augmentation on the performance of convolutional neural networks (CNNs) in image classification tasks. Our experiments show that certain data augmentation techniques can significantly enhance the accuracy of CNNs.",
                    "The research explores the use of transfer learning in natural language processing (NLP) applications. We introduce a new model that leverages pre-trained language models to achieve state-of-the-art results on various NLP benchmarks."
                ]
            },
            "2": {
                "abstracts": [
                    "This study examines the effects of climate change on global agricultural productivity. The findings suggest that rising temperatures and changing precipitation patterns are likely to reduce crop yields in many regions, posing challenges for food security.",
                    "In this research, we propose a new framework for sustainable urban development that integrates environmental, social, and economic factors. The framework is applied to several case studies, demonstrating its potential to guide policy-making for sustainable cities.",
                    "The paper investigates the relationship between renewable energy adoption and economic growth. Using data from multiple countries, the analysis reveals that increased use of renewable energy sources is associated with positive economic outcomes, including job creation and GDP growth."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = """Your task is to generate a coherent and informative summary based on the following provided abstracts from different research papers:\n\n"""
        for abstract in t['abstracts']:
            instructions += f"- {abstract}\n"
        instructions += """\nEnsure that your summary captures the key points from each abstract and is presented in a clear and structured manner. Provide your summary in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should capture the key points from each abstract.",
            "The summary should be coherent and logically structured.",
            "The summary should be written in clear and concise language.",
            "The summary should accurately reflect the content of the provided abstracts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
