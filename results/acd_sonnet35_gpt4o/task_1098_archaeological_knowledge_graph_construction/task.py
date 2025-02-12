import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        time_periods = [
            "Neolithic",
            "Bronze Age",
            "Iron Age",
            "Classical Antiquity",
            "Medieval Period",
            "Renaissance",
            "Industrial Revolution"
        ]
        cultures = [
            "Mesopotamian",
            "Egyptian",
            "Greek",
            "Roman",
            "Maya",
            "Chinese",
            "Indian",
            "Persian"
        ]
        artifact_types = [
            "pottery",
            "tools",
            "weapons",
            "jewelry",
            "architectural remains",
            "textiles",
            "writing systems",
            "religious artifacts"
        ]
        return {
            "1": {
                "time_period": random.choice(time_periods),
                "culture": random.choice(cultures),
                "artifact_type": random.choice(artifact_types)
            },
            "2": {
                "time_period": random.choice(time_periods),
                "culture": random.choice(cultures),
                "artifact_type": random.choice(artifact_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a system to construct a knowledge graph from archaeological texts and data, focusing primarily on the {t['time_period']} period, {t['culture']} culture, and {t['artifact_type']}, while also integrating information from other time periods and cultures. Your task involves the following components:

1. Data Ingestion and Preprocessing (200-250 words):
   a) Describe how your system would ingest and preprocess various types of archaeological data (e.g., excavation reports, artifact catalogs, academic papers).
   b) Explain how you would handle multilingual sources and normalize terminology across different archaeological traditions.
   c) Discuss strategies for dealing with incomplete or uncertain information in the archaeological record.

2. Knowledge Graph Construction (250-300 words):
   a) Detail the ontology and schema you would use for your knowledge graph, explaining how it captures relationships between artifacts, sites, cultures, and time periods.
   b) Describe the natural language processing techniques you would employ to extract entities and relationships from textual sources.
   c) Explain how your system would integrate structured data (e.g., radiocarbon dates, geospatial information) with information extracted from texts.
   d) Provide a small example of how a piece of archaeological information would be represented in your knowledge graph.
   e) Discuss how you would balance depth (detailed information about the focus period/culture/artifact) with breadth (connections to other periods/cultures/artifacts).

3. Inference and Reasoning (200-250 words):
   a) Describe how your system would perform reasoning over the knowledge graph to infer new relationships or fill in missing information.
   b) Explain how you would handle conflicting information or multiple hypotheses about archaeological interpretations.
   c) Discuss how your system could generate new research questions or hypotheses based on patterns in the knowledge graph.

4. Visualization and Query Interface (150-200 words):
   a) Propose an innovative method to visualize the complex relationships in your archaeological knowledge graph.
   b) Describe a user interface that would allow archaeologists to query the knowledge graph and explore connections across time periods and cultures.
   c) Explain how your visualization could help identify patterns or anomalies in the archaeological data.

5. Performance and Scalability (100-150 words):
   a) Discuss the computational challenges of constructing and querying a large-scale archaeological knowledge graph.
   b) Propose strategies for optimizing the performance and scalability of your system.
   c) Explain how you would handle real-time updates to the knowledge graph as new archaeological data becomes available.

6. Case Study (200-250 words):
   Present a hypothetical case study demonstrating how your system would be applied to analyze {t['artifact_type']} from the {t['culture']} culture during the {t['time_period']}. Include:
   a) A specific research question your system could help address, preferably one that involves connections to other cultures or time periods.
   b) The types of data and sources your system would integrate.
   c) An example of a novel insight or hypothesis your system might generate, emphasizing interdisciplinary connections.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical issues related to the use of AI in archaeological research and cultural heritage management.
   b) Address concerns about the impact of such systems on traditional archaeological methods and interpretations.
   c) Explain limitations of your approach and potential biases in the knowledge graph construction process.

Ensure your response demonstrates a deep understanding of both computational techniques and archaeological principles. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of archaeological principles and computational techniques, particularly in relation to {t['time_period']}, {t['culture']} culture, and {t['artifact_type']}.",
            "The knowledge graph construction approach is technically sound, innovative, and effectively balances depth and breadth of information.",
            "The system design effectively addresses challenges specific to archaeological data, such as incompleteness, uncertainty, and multilingual sources.",
            "The inference and reasoning methods are well-explained and show potential for generating novel insights.",
            "The visualization and query interface proposal is innovative and user-friendly for archaeologists.",
            "Performance and scalability considerations are addressed comprehensively.",
            "The case study provides a plausible and insightful application of the proposed system, including connections to other cultures or time periods.",
            "Ethical considerations and limitations are thoroughly discussed.",
            "The response shows creativity and interdisciplinary thinking throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
