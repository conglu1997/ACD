class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Summarize the following scientific article:", "article": "Recent studies have shown that climate change is accelerating at an unprecedented rate. The average global temperature has increased by 1.5 degrees Celsius over the past century. This has led to more frequent and severe weather events, such as hurricanes, droughts, and floods. Scientists are urging immediate action to mitigate the effects of climate change and reduce greenhouse gas emissions. Additionally, there are significant impacts on biodiversity, agriculture, and human health. For example, the melting of polar ice caps has resulted in rising sea levels, which threaten coastal communities. Changes in temperature and precipitation patterns are affecting crop yields, leading to food insecurity in some regions. Furthermore, the increase in extreme weather events has been linked to a rise in heat-related illnesses and the spread of infectious diseases."},
            "2": {"task": "Summarize the following scientific article:", "article": "Quantum computing is a rapidly evolving field that promises to revolutionize technology. Unlike classical computers, which use bits to process information, quantum computers use qubits. This allows them to perform complex calculations much faster than classical computers. Researchers are exploring various applications of quantum computing, from cryptography to drug discovery. For instance, in cryptography, quantum computers have the potential to break current encryption methods, leading to the development of new, more secure encryption techniques. In drug discovery, quantum computing can simulate molecular interactions at a much faster rate, potentially speeding up the development of new medications. Despite these advancements, there are significant challenges to overcome, such as error rates in qubit operations and the need for extremely low temperatures to maintain quantum states."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to read and summarize the following scientific article. Ensure that your summary is clear, accurate, and highlights the key points and findings. Provide your summary in plain text format.

Article:
{t['article']}

Provide your summary below:"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The summary should be clear and accurate.", "The summary should highlight the key points and findings of the article."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
