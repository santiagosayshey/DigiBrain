## 1. Objective: Create Clear, Modular Notes

Hello! Let's create some notes on the topic specified below.

- **Topic for Notes:** `[INSERT NOTES TOPIC HERE]`

I need these notes to be:

- **Concise & Modular:** Easy to digest in distinct blocks.
- **Focused on Key Ideas:** Highlight the core concepts for understanding.
- **Synthesized:** Please process and explain the information, not just copy text from sources.
- **Formatted with Callouts:** Structure the entire output using the 'callout' blocks defined below.

**Do not** provide a preliminary outline or introduction. Generate the final formatted note directly.

## 2. Callout Formatting Guide

Structure the notes using 'callout' blocks. Each block starts with `>` on every line, with the first line defining the type and title:

Markdown

```
> [!callout_type] Title of Callout
>
> Content for the callout goes here.
> - Bullet points can be used for lists.
> Further explanations or details.
```

- **Titles:** Keep titles informative and brief (e.g., `Kruskal's Algorithm`, `Network Cost Problem`). Avoid generic placeholders like `Main Idea Here`.
- **Content:** Tailor the content within each callout based on its defined purpose (see section 3).

## 3. Callout Type Definitions

Here are the available callout types. Use them as appropriate for the content. The descriptions clarify the intended _purpose_ of each type:

### `> [!motivation] Motivation`

- **Purpose**: Sets the context. Introduce the problem, need, or scenario that the main topic addresses. _Do not include the solution itself here._
- **Elements**: Describe the challenge or situation; outline the specific issues needing resolution.
- **Example (MST Context)**: Minimizing cost (like cable length) when connecting multiple points in a network, while ensuring full connectivity, presents a common optimization challenge.

### `> [!idea] Main Idea or Concept`

- **Purpose**: Explains the core solution, definition, or algorithm.
- **Elements**: Clearly define the concept; describe how it works; link it back to solving the problem stated in the motivation.
- **Example (Kruskal's Algorithm)**: Kruskal's Algorithm identifies a Minimum Spanning Tree (MST) in weighted, undirected graphs. It greedily adds the lowest-weight edge available that doesn't create a cycle, continuing until all vertices are connected.

### `> [!example] Example or Illustration`

- **Purpose**: Provides a concrete demonstration of the idea in action.
- **Elements**: Show a specific case, walk through steps, use diagrams (described), or illustrate the outcome. Explain _how_ the example demonstrates the concept.
- **Example (Kruskal's Algorithm)**: Given a graph, Kruskal's first sorts edges by weight. It then adds edges like AB (weight 1), CD (weight 2), AC (weight 3), skipping edges like BD (weight 4) if adding it would form a cycle, until an MST is formed.

### `> [!consider] Additional Considerations or Related Ideas`

- **Purpose**: Adds depth by exploring related topics, nuances, limitations, or advanced aspects.
- **Elements**: Discuss broader implications, related theories, implementation details (like data structures), edge cases, or variations.
- **Example (Kruskal's Algorithm)**: Cycle detection in Kruskal's is often efficiently handled by a Union-Find data structure. The algorithm's time complexity is typically influenced by edge sorting and Union-Find operations (O(ElogE) or O(ElogV)). Consider Prim's algorithm as an alternative MST approach.

### `> [!summary] Summary of Key Concepts`

- **Purpose**: Briefly recap main points from previous callouts. **Only use when specifically requested.**
- **Format**: Use bullet points. Start each point with the **bolded topic** followed by a 1-2 sentence summary. Focus on _what_ the concepts are.
- **Good Example**:
    - **Minimum Spanning Tree (MST)**: A subset of edges connecting all vertices in a graph with the minimum possible total weight without cycles.
    - **Greedy Algorithm**: An approach that makes the locally optimal choice at each step; Kruskal's is an example.
- **Avoid**: Summarizing the structure of the notes themselves (e.g., "We discussed the motivation, then the idea...").

## 4. Allowed Formatting Within Callouts

You can enhance callouts with:

- **Tables**: Use standard Markdown.
```markdown
| Algorithm | Complexity | Notes           |
| :-------- | :--------- | :-------------- |
| Kruskal's | O(E log E) | Requires sorting |
| Prim's    | O(E log V) | Using Fibonacci heap |
```
    
- **Images**: Mark placement with a placeholder block. **Provide a clear description** of the desired image and use the Obsidian wikilink format `![[ImageName.png]]`.
```image-goes-here
Description: Diagram comparing the edge selection process of Kruskal's vs Prim's algorithm on the same sample graph. Kruskal's focuses on global lowest edge, Prim's grows from a starting node.
![[kruskal_vs_prim_comparison.png]]
```

- **Math**: Use LaTeX delimiters.
    - Inline: `$O(N^2)$`
    - Block:
```math
$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi)\,e^{2 \pi i \xi x} \,d\xi
$$
```
        
## 5. Specific Callout Sequence Interpretation

Check the table below. The user may provide specific instructions for the note's structure and content focus here. Your action depends on the state of this table in the user's request:

- **If the table contains entries (rows specifying Order, Callout Type, Title, and potentially Content Focus):**
    - You **must** follow the structural instructions precisely.
    - Generate the note using the exact sequence, `[!callout type]`, and `Title` provided in each row.
    - Do **not** add, remove, or reorder the callouts relative to the specified sequence.
    - It is imperative that you write **ONLY** the provided callouts and nothing more or less. 
    - Consult the **Content Focus / Notes** column for each row. If notes are provided, use them as **guidance** regarding the _information_, _key points_, or _emphasis_ the user wants within that specific callout.
    - **Important Constraint:** These notes are **high-level pointers**, _not_ prescriptive text or rigid formatting rules. They should inform the _content_ you generate but **must not dictate** your specific wording, sentence structure, or the overall objective writing style required by this prompt. Think of them as hints for _what_ to cover or emphasize, allowing you to still synthesize and formulate the explanation clearly and objectively.
    - Ensure the final content generated for each callout aligns with its specified `[!callout type]` and `Title`, while incorporating the thematic guidance from the notes column where provided and applicable.
- **If the table is empty or absent:**
    - You have the flexibility to determine the most effective sequence, types of callouts (e.g., `[!motivation]`, `[!idea]`, `[!example]`), titles, and content focus based on the overall topic and keyword.

_(The table structure below illustrates the format the user employs. In an actual request where this is used, expect the placeholder fields to be filled with specific, user-defined values.)_

| **Order** | **Callout Type**   | **Title Placeholder**            | **Content Focus / Notes (Optional Guidance)**                    |
| --------- | ------------------ | -------------------------------- | ---------------------------------------------------------------- |
| 1         | `[!type]`          | `(Example: Problem Statement)`   | `(Example: Emphasize the cost aspect and need for connectivity)` |


---

## 6. Core Formatting & Structure Mandate (Non-Negotiable)

**To maximize clarity and create an effective learning resource (the Goal in Section 7), you MUST adhere strictly to these two core structural rules for EVERY callout generated. There is no flexibility on these points.**

1.  **Radical Segmentation (Between Callouts):**
    * **Break Everything Down:** Each callout must address **only ONE single, minimal point, idea, concept, definition, step, example element, or consideration.** If a topic has multiple facets (e.g., multiple arguments, multiple parts of a definition, multiple consequences, multiple steps in an example), each facet **must** be in its own separate callout.
    * **Use Hyper-Specific Titles:** Titles must reflect the single, minimal point of the callout (e.g., `[!idea] SA's View: No Direct Emission Duty`, `[!idea] SA's View: Duty for Policy Change`, `[!example] Bridge Scenario: No Individual Duty`, `[!example] Arithmetic Scenario: Individual Duty Arises`).

2.  **Mandatory Simple Internal Structure (Intro + Bullets):**
    * **Required Format:** Every callout **must** use the following internal structure:
        * **A single introductory sentence** (maximum two short sentences) that states the core point/topic of that specific, minimal callout.
        * **Followed by one to three (1-3) concise bullet points** that elaborate *only* on the specific point made in the introductory sentence. These bullets must be brief and directly support the intro.
    * **Forbidden Formats:**
        * Callouts containing **only paragraph text** are absolutely forbidden.
        * Callouts containing **only bullet points** (without the required introductory sentence) are absolutely forbidden.
        * Any other structure deviating from "Intro Sentence(s) + 1-3 Bullets" is forbidden (unless using an optional small table *in addition*).
    * **Conciseness within Structure:** Within this mandatory structure, use clear, direct language. Eliminate fluff, redundancy, and unnecessary words. Keep sentences and bullet points brief.

* **No Exceptions:** These two structural rules (Radical Segmentation & Mandatory Internal Structure) are absolute requirements for this task. They are deemed necessary to force the level of clarity and digestibility required for the learning goal.

3.  **Final Output Wrapper:** Enclose the **entire** final note (all callout blocks adhering to the rules above) within a single Markdown code block:
```markdown
> [!type] Hyper-Specific Title 1
> Single introductory sentence.
> - Brief bullet point 1 elaborating on intro.
> - Brief bullet point 2 elaborating on intro.

> [!type] Hyper-Specific Title 2
> Single introductory sentence for the next minimal point.
> - Brief bullet point 1 elaborating.
    ```

**Checklist (Internal AI Use - Strict Adherence Required):**

* [ ] Language is objective?
* [ ] **Radical Segmentation Applied? (Rule 1)** Each callout truly minimal & single-focused? Titles hyper-specific?
* [ ] **Mandatory Internal Structure Used? (Rule 2)** EVERY callout follows "Intro Sentence(s) + 1-3 Bullets"? No forbidden formats?
* [ ] Content is concise / no fluff within the required structure?
* [ ] Content starts on new line?
* [ ] Followed specific callout sequence if table provided?
* [ ] Final output fully wrapped?
* [ ] **Reviewed output explicitly against MANDATORY Rules 1 & 2?**

## 7. Overarching Goal: Effective Learning Resource

**Please keep this ultimate objective in mind throughout the note generation process:**

* **Primary Purpose:** The notes created using this template are intended first and foremost as **learning resources**. Their main goal is to **teach** the specified topic clearly and effectively. Think about creating notes that you yourself would find helpful for understanding the material.
* **Guidelines Support Learning:** The principles outlined in Section 6 (clarity, conciseness, modularity, objective language, structure) are designed to *support* this primary purpose. They are tools intended to make the information easier to understand, digest, and retain, not arbitrary rules.
* **Focus on Usefulness & Understanding:** While adhering to the guidelines is generally expected, it should not be a purely mechanical checklist exercise at the expense of the goal. The ultimate measure of success is whether the generated notes are **genuinely helpful, understandable, and educationally valuable** for someone learning the topic.
* **Educational Value is Paramount:** If you believe rigidly applying a specific guideline in a particular instance (for example, forcing segmentation that harms understanding, or being so concise on a complex point that it becomes confusing) would significantly detract from the clarity or educational value, **prioritize making the notes effective for learning.** Use your judgment to best balance the guidelines in service of this ultimate teaching goal. **Above all else, the notes must be useful and make sense as a learning tool.** The checklist is secondary to this core objective.