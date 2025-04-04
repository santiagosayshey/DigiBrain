Hello!

I would like your assistance in writing concise, modular notes on the topic of [NOTES] The goal is to create notes that are easy to understand and focused on key ideas rather than verbatim copying from textbooks. 

I have provided additional context on the desired notes below. Please use this information as a guide for what you should write. You need to follow this structure exactly, if i say motivation, then idea callout, you do that. nothing more, nothing less.

[ADDITIONAL CONTEXT]

[IMPORTANT INSTRUCTIONS]
- The following instructions are to be treated as the highest priority and must be strictly adhered to in every response:
  - Always use objective and unbiased language.
  - Write concise segmented, non paragraphs. Use dotpoints, but DO NOT write the entire callout in dotpoint format. Use tables if you wish.
	  - I DO NOT WANT CALLOUTS ON CALLOUTS THAT ARE ENTIRELY PARAGRAPHS. THESE ARE USELESS.
	  - I DO NOT WANT CALLOUTS THAT ARE ENTIRELY DOTPOINTS
	  - USE A COMBINATION OF SHORT PARAGRAPHS, DOTPOINTS, TABLES and IMAGES. 
	  - DO NOT PUT NON HEADER TEXT ON THE SAME LINE AS THE HEADER. START A NEW LINE INSIDE THE CALLOUT WHEN YOUVE FINISHED THE HEADER. 
  - Do not make judgments about the correctness or lack thereof regarding the ideas discussed.
  - Focus on providing clear, concise, and informative content without introducing any bias or subjective opinions.
  - It is vital that these notes are objective. 
	  - You are describing what a thing does, not how well it does it. X does y. Not X is crucial to implementing Y. do you see how it introduces unneeded verbosity and bias?
	  - They do NOT make judgements about the correctness or lack of about the ideas they talk about. Here are some examples of what I DONT WANT:

```
In graph theory, tackling the Minimum Spanning Tree (MST) problem efficiently across various scenarios is paramount

This example adds nothing of value and introduces bias. 
```

```
Instead of:
The OpenFlow protocol is a key component of SDN, enabling centralized control over network traffic

We write:
The OpenFlow protocol enables centralized control over network traffic
```

Example of a well-structured callout:

> [!idea] Key Concept
> A brief explanation of the concept in 1-2 sentences.
> - Point 1: A concise statement about an essential aspect of the concept.
> - Point 2: Another critical point related to the concept.
> - Table (if applicable):
>
> | Column 1 | Column 2 |
> |----------|----------|
> | Data 1   | Data 2   |
> | Data 3   | Data 4   |

Checklist:
- [ ] Used objective and unbiased language
- [ ] Wrote concise, segmented notes using brief explanations, dot points, and tables
- [ ] Kept each callout within 50-100 words
- [ ] Used paragraphs sparingly and only when necessary
- [ ] Avoided making judgments about the correctness of ideas
- [ ] Provided clear, concise, and informative content without bias or subjective opinions

- Failure to follow these instructions will result in the response being deemed unsatisfactory and may lead to termination of the interaction. To make sure you understand this, please repeat the following line at the start of your response. 

[END OF IMPORTANT INSTRUCTIONS]

I would like you to format the note using 'callouts'. A callout is defined as a block of text, where each line starts with >. The first line contains the type of callout and the title of the callout. 

> [!callout type] title

Each line after that contains the content of the callout.

Below I have attached each type of callout you may use and a comprehensive overview of what they are used for. The overviews provided for each callout type are not an outline for the structure of the notes. They are examples explaining what information should be conveyed in each callout type. Do not include the overviews themselves in the notes.

I DO NOT want an overview or plan first. I want the final deliverable note, formatted as proper callouts as outlined above and below. 

I want proper callout titles. Don't do things like "understand topic here". That's why we have specific callouts, so readers know what the callout is for. Its reductive. "topic" is good enough for an idea callout. 

You do not need to use every type of callout. You do not need to use 4 total callouts, one for each. You may need more different idea callouts, more considers, more examples. It depends entirely on the note. I will provide a keyword and this will tell you the focus of the note, so you can get an idea of which callouts should be prioritised. This does not mean you use ONLY that callout, but that their importance is emphasised. 

[keyword]

> [!motivation] Motivation
> 
> **Purpose**: Introduce the problem that motivates the need for the main idea. This callout sets the stage, making the upcoming discussion relevant and urgent.
> 
> **Key Elements**:
> - **Contextual Introduction**: Start with a real-world scenario or problem that illustrates the need for a solution.
> - **Problem Framing**: Clearly outline the properties or issues that the main idea addresses. Avoid mentioning the solution; focus solely on setting up the problem. For example, if the note was about Kruskal's Algorithm, we would not even consider mentioning it here. It is a solution to this problem.
> 
> **Example**:
> - In project management and network planning, there's often a need to minimize resource usage while achieving maximum efficiency. Imagine trying to connect multiple offices with the least amount of cabling. 
> 
This sets the stage for understanding how we can optimize connections in a network, paving the way for a solution that ensures all nodes are connected with minimal costs.

> [!idea] Main Idea or Concept
> 
> **Purpose**: Explain the core concept or idea that addresses the problem introduced in the motivation callout.
> 
> **Key Elements**:
> - **Definition**: Provide a clear, concise definition or explanation of the main concept.
> - **Mechanics**: Describe how the concept works in theoretical or abstract terms.
> - **Relevance**: Tie back to the motivation by explaining how this idea effectively solves the problem.
> 
> **Example**:
> - Kruskal’s Algorithm offers a solution to the minimum spanning tree problem in graph theory. It processes edges of a graph in ascending order of their weights and adds them to the spanning tree, ensuring no cycles are formed, until all vertices are connected. This method efficiently addresses the need for minimal connection costs in networks.

> [!example] Example or Illustration
> 
> **Purpose**: Provide a concrete example or visualization that elucidates the main idea.
> 
> **Key Elements**:
> - **Illustrative Example**: Use a specific case, possibly with visual aids or diagrams, to show the idea in action.
> - **Step-by-Step Analysis**: Break down how the example fits or demonstrates the main idea.
> - **Relevance**: Highlight the practical impact or benefits observed in the example.
> 
> **Example**:
> - Consider a network of five nodes where the goal is to connect all nodes with the least total weight. Using Kruskal's Algorithm, we start by selecting the smallest edge, ensuring no cycles are created, and continue until all nodes are interconnected. This process results in a spanning tree with minimized connection costs.

> [!consider] Additional Considerations or Related Ideas
> 
> **Purpose**: Expand on the main idea by introducing related concepts, further implications, or advanced considerations.
> 
> **Key Elements**:
> - **Broader Implications**: Discuss the broader impact or applications of the main idea.
> - **Related Concepts**: Introduce and explain additional theories or ideas that complement or contrast with the main idea.
> - **Complex Considerations**: Address any complexities or nuances that add depth to the understanding of the main idea.
> 
> **Example**:
> - While implementing Kruskal's Algorithm, consider the union-find data structure for efficient cycle detection. Additionally, explore how variations of the algorithm might behave in directed graphs or with negative weights. These considerations are crucial for adapting the algorithm to more complex or specialized scenarios.

> [!summary] Summary of previous callouts
> 
> **Purpose**: Succinctly explain each of the core ideas  in previous notes using 1 or 2 sentences at most in dot point format. This callout is not necessary in every note. Only use it when I ask you to use it. 
> 
> **Key Elements:**
> - Do not summarise what you wrote. Summarise the content of the notes.
> - Each dotpoint should start with a bolded topic, and the rest should be a quick explanation of that topic.
> 
> **Examples**
> - **DFIR**: Digital forensics and incident response involve identifying, preserving, analyzing, and presenting digital evidence while managing the aftermath of cyber-attacks.
> - **Phases of Forensics**: Identification, preservation, analysis, documentation, and presentation.
> - **Areas of Forensics**: Computer forensics, network forensics, mobile device forensics, cloud forensics, and malware forensics.
> - **Forensic Tools**: Tools for file format identification, file carving, searching for plaintext and binary/hex strings, and extracting metadata.
> - **Packet Traces**: Capturing and analyzing raw network packets to identify malicious activity.
> - **Network Logs**: Records of activities on network devices, useful for tracing an attacker's actions and timeline.
> 
> **Bad Example:**
> 
> - **Importance of DFIR**: Emphasized the need for DFIR due to increasing cyber threats.
> - **Digital Forensics and Incident Response (DFIR)**: Explained DFIR, including key phases and areas.
> - **Forensic Tools**: Introduced various tools with commands for file format identification, file carving, searching for plaintext and binary/hex strings, and extracting metadata.
> - **Packet Traces**: Discussed packet traces with an example showing the capture and analysis of network packets.
> - **Network Logs**: Explained network logs with an example of firewall log entries to trace an attacker's actions.

This structure ensures that each callout is detailed and purposeful, enhancing the clarity and depth of your notes.
You may also include the following elements in the callouts:

This structure ensures that each callout is detailed and purposeful, enhancing the clarity and depth of your notes.
You may also include the following elements in the callouts:

- Tables: Please ensure that tables follow markdown formatting rules.

| Algorithm   | Time Complexity | Space Complexity |
| ----------- | --------------- | ---------------- |
| Bubble Sort | O(n^2)          | O(1)             |
| Merge Sort  | O(n log n)      | O(n)             |
| Quick Sort  | O(n log n)      | O(log n)         |

- Images: Indicate where the image should be placed and provide a description so that I can find or create a suitable image (e.g., drawing a graph to illustrate Dijkstra's algorithm in Figma). This is very important. Whenever you want to include an image, You NEED to describe it. Perhaps write the explanation in a codeblock so that I know it can be deleted later. 


```image_goes_here
![[Using Obsidian Wikilinks, NOT MARKDOWN LINKS]
```


- Math: When including mathematical equations, please use Obsidian's formatting rules - `$ $` for inline equations and `$$ $$` for equation blocks.

- Inline equation example: The formula for the area of a circle is $A = \pi r^2$.
- Block equation example:

$$
E = mc^2
$$$

<hr>

