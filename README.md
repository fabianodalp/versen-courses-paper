Online Appendix of "A Systematic Analysis of Higher Education on Software Engineering in the Netherlands"
-----------

This is the online appendix of the paper "A Systematic Analysis of Higher Education on Software Engineering in the Netherlands". The appendix includes materials that promote transparency, verifiability, and replication.

`course_descriptions.zip`: course descriptions, taken from the educational catalogs, for the analyzed courses;

`wordclouds.zip`: Python code (Jupyter notebook) that we used to generate the wordclouds, including the input course descriptions;

`agreement-round1.xlsx` and `agreement-round2.xlsx`: Excel files that document the changes that underwent in our coding in Phase 5 and Phase 6 of our research method (see Figure 1 in the paper);

`courselist-MASTER.xlsx`: the list of courses that are part of the analysis, including their coding. The Excel file consists of multiple tabs:

*   _Matrix_: the final list of the 207 included courses, including their final coding;
*   _Matrix removed_: the list of 109 courses that were provided by the participants in our study but that we excluded from our analysis;
*   _Notes_: some comments on the coding scheme;
*   _Categories_: the guidelines we employed as a tool to assist us in determining whether a course description would fit a certain KA/category;
*   _Counting_: aggregate sums/values from _Matrix_, which shows the frequency of KAs;
*   _Plots_: some charts that reflect our data;

`course_spider.py`: the script we used to retrieve the course descriptions from the syllabi on the universities' pages; this script led to the contents of `course_descriptions.zip`;

`heatmap_courses.py`: Python script that first calculates Spearman correlations between knowledge areas, starting from the `courselist-MASTER.xlsx` file, and then generates the heatmap visualization in Figure 14 of the paper;

`uni_topic_recurrence.py`: Python script that takes a CSV version of the courses and then generates the distribution of courses mapped to knowledge areas, organized by universities, shown in Figure 15 of the paper.
