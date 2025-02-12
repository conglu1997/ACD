class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"article": "In recent years, the applications of machine learning in healthcare have grown significantly. Various algorithms are being developed to predict patient outcomes, assist in diagnostics, and personalize treatment plans. One notable application is the use of deep learning models to analyze medical imaging data, which has shown promising results in identifying conditions such as cancer and cardiovascular diseases. However, challenges remain in terms of data privacy, model interpretability, and integration into clinical workflows."},
            "2": {"article": "Climate change is one of the most pressing issues of our time, with significant impacts on global ecosystems and human societies. Recent studies have highlighted the role of greenhouse gas emissions in driving temperature increases and extreme weather events. Efforts to mitigate climate change include the adoption of renewable energy sources, reforestation, and changes in agricultural practices. Despite these efforts, achieving the targets set by international agreements remains challenging, requiring coordinated action and significant policy changes at both national and global levels."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Read the following scientific research article and provide a concise summary that captures the key points. Your summary should be between 50 to 100 words. Ensure that you highlight the main findings and challenges discussed in the article. Do not copy large parts of the article verbatim. Here is an example of a good summary: 'The article discusses the significant growth of machine learning applications in healthcare, particularly in diagnostics and personalized treatment. Despite promising results, challenges such as data privacy and model interpretability remain. The article emphasizes the need for better integration into clinical workflows to maximize benefits.'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
