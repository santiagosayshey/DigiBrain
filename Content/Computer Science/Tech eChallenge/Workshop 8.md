

help me with this workshop? dont add any more risks, just expand and add actual experiements to the ones ive given in the context of the ... context.

  

List 3-5 Risks

- What are we unsure abou
- What's one experiment we can run this week?

  
| Concern | Experiment |
| ------- | ---------- |
|         |            |

Risks

- cost / business model.
	- we have already discussed potentially business models (b2b and b2c not sure if these are the correct terms). Either we sell to businesses (universities, journals, research platforms, google scholar, etc) OR we sell to individual customers.
	- is what we're doing going to be viable in b2c? are researchers / post grads going to shell out the amount of money on an individual subscription for this? or are we going to have more luck with businesses?
	- more on that, our initial testing has shown us its quite expensive to generate a single video - 3-5$. Is this going to be viable in production? are we going to be able to get this price down? Most likely yes, we have done 0 optimisation to our pipeline, but we still need to figure out how fast we can do this. this directly ties back to the b2b and b2c stuff. if we cant get the price down, are we going to be able to actually sell to individuals at a fair price without losing money? 
	- potential business models - just look at how AI is priced today. Open AI lets people use its models via an api through bought credits, or they sell direct access to the models through chatGPT via a subscription. Perhaps we give access to both, banking on credit money from businesses on the API side and front the cost on the customer side so that we can work on (a new risk)
- how do we actually grow? where are we getting customers from?
	- so, going back to the existing issue, where are we getting customers from? outside of our initial friends / connections at uni, how does this grow? can we front the cost, and do some kind of freemium model (just like LLMs do) to get people IN on the business? like they generate 1 video, then need to subscribe to do more? 
- copyright
	- how are going to deal with copyright issues here? does any of what we do fall under fair use? do we need to implement DRM for generated videos if we allow anyone to generate them?
- too tech focused
	- how do we show how our product works? a live demo might be really confusing. maybe we prerecord stuff and present that instead. 

- copyright. 


context:

# synapsis

  

[](https://github.com/SynapsisAI#synapsis)

  

> **Complex text to visual clarity.**

  

## About Us

  

[](https://github.com/SynapsisAI#about-us)

  

Synapsis AI is a collaborative project focused on transforming complex text into concise visual summaries through systematic decomposition and reconstruction of core meanings. Our technology decomposes text into fundamental components before synthesizing these elements into structured, visually-enhanced summaries that preserve essential information while significantly reducing complexity.

  

## Our Team

  

[](https://github.com/SynapsisAI#our-team)

  

- **Noah Mialaret**

- **Michelle Nguyen**

- **Samuel Chau**

  

## Our Approach

  

[](https://github.com/SynapsisAI#our-approach)

  

We follow a first-principles approach to text understanding:

  

1. **Decomposition**: Breaking down documents into paragraphs, sentences, and core meanings

2. **Synthesis**: Reconstructing essential elements into coherent, structured arguments

3. **Visualization**: Enhancing understanding through complementary visual representations

  

## Projects

  

[](https://github.com/SynapsisAI#projects)

  

#### core

  

[](https://github.com/SynapsisAI#core)

  

Our monorepo containing all project components, libraries, and services that power the Synapsis ecosystem. This unified codebase facilitates seamless integration between our decomposition engine, synthesis algorithms, and visualization tools.

  

[View core Repository](https://github.com/SynapsisAI/core)



| Concern (Risk)                                  | What are we unsure about? (Underlying Questions)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Experiment (One thing we can run this week)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Cost / Business Model Viability**          | - **B2C Unwillingness to Pay:** Will individual researchers (PhD students, postdocs, academics) pay a subscription fee that covers our $3-5 (current) cost per video plus margin? What price point feels acceptable to them for regular use? <br> - **B2B Potential Value:** Do universities, research platforms, or journals perceive enough value to pay for institutional access? What specific problem does it solve for *them* (e.g., increasing research accessibility, promoting publications)? <br> - **Cost Reduction:** What are the primary drivers of the $3-5 video generation cost? Can we identify low-hanging fruit for optimization *without* a major engineering overhaul yet? | **Experiment 1a (Price Gauge):** Create a simple mock-up of a subscription page (maybe on the landing page?). Offer 2-3 hypothetical pricing tiers (e.g., Basic: 3 videos/month for $X, Pro: 10 videos/month for $Y, Premium: Unlimited for $Z). Approach 10-15 target researchers. Briefly explain the service and show them an example video. Ask them which tier, if any, they would consider and why. *Goal: Gauge initial price sensitivity and preferred features.* <br><br> **Experiment 1b (B2B Problem/Solution Fit Interviews):** Identify 3-5 in target B2B areas (e.g., a university librarian, a journal editor, someone at a research funding body). Request a 20-30 minute "informational interview." Focus on *their* current challenges in disseminating complex research and making it understandable. Perhaps we can do this in an interview with Alex or something? Then, briefly introduce Synapsis AI's concept and gauge their reaction. *Goal: Understand B2B pain points and initial reaction to your solution, not to sell yet.* <br><br> **Experiment 1c (Cost Analysis):** Break down the $3-5 video generation cost.  *Goal: Identify the single most expensive component in the current pipeline to target for future optimization discussions.* |
| **2. Growth / Customer Acquisition**            | - **Initial Traction:** Beyond personal networks, which channels are most effective for reaching early adopters in the academic/research community? <br> - **Freemium Effectiveness:** Will offering a limited free trial (e.g., one free video) effectively convert users to paid subscriptions? What's an appealing freemium offer?                                                                                                                                                                                                                                                                                                                                                            | **Experiment 2a (Targeted Content Teaser):** Select one highly relevant academic community online (e.g., a specific subreddit like r/PhD, r/labrats). Create one high-quality example visual summary from a recent, relevant open-access paper. Post it with a brief explanation of how it was made (mentioning Synapsis AI) and a link to our landing page where they can express interest or request a demo/their own free sample. *Goal: Test channel effectiveness and initial interest generation.* <br><br> **Experiment 2b  (Freemium Model):** Offer to manually create one free visual summary for free users. Use this as an opportunity to gather detailed feedback on the output and their perceived value, and ask if they'd pay for more. *Goal: Test the "hook" of a free video and gather qualitative feedback on product value and willingness to pay after trying.*                                                                                                                                                                                                                                                                                                                                                                                          |
| **3. Copyright**                                | - **Fair Use:** For summarizing and visualizing published research, what aspects of our process fall under fair use, and what might require permissions? <br> - **User Responsibility vs. Platform Responsibility:** Who is responsible if a user uploads copyrighted material they don't have rights to summarize? How do other AI content generation tools handle this? <br> - **Output Ownership:** Who owns the copyright of the generated visual summary – the user, author, or Synapsis?                                                                                                                                                                                                   | <br>**Experiment 3a (Competitor Copyright Policy Review):** Identify 3-5 other AI tools that transform or summarize existing content (text-to-video, AI summarizers, presentation generators). Carefully review their Terms of Service and Copyright Policies. How do they address input material rights and output ownership? *Goal: Understand industry standards and common approaches. <br><br> **Experiment 3b (Document Your Transformation Process):** Create a detailed internal document outlining exactly how a source text is processed by Synapsis AI. What elements are extracted? How are they transformed? What new creative input does your system (or the user via prompts) add? _Goal: Prepare necessary documentation for seeking legal advice_                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **4. Too Tech Focused (Product Communication)** | - **Clarity of Value:** How can we quickly and clearly communicate the  value proposition of Synapsis AI to a non-technical academic audience without them getting lost in the "decomposition, synthesis, visualisation" jargon? <br> - **Demo Effectiveness:** Is a live demo too risky or confusing? What's the most impactful way to showcase the product's capability?                                                                                                                                                                                                                                                                                                                       | **Experiment 4a (Pre-recorded Demo & Feedback):** Create a concise (60-90 second) pre-recorded demo video. Start with a problem (e.g., "Struggling to keep up with dense research papers?"), show the input (a complex text snippet), briefly illustrate the Synapsis AI process (conceptually, not deep tech), and showcase the engaging visual summary output. Show this video to 5-7 people from your target audience (researchers, students) and 2-3 people *outside* your immediate field. Get feedback: What was clear? What was confusing? What was most exciting? Did they understand the benefit? *Goal: Test the clarity and impact of a pre-recorded demo and refine messaging.*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| Concern (Risk)                         | What are we unsure about? (Underlying Questions)                                                                                                                                                                                                                                                                                         | Experiment (One thing we can run this week)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Cost / Business Model Viability** | - **B2C Willingness to Pay:** Will individual researchers (PhD students, postdocs, academics) pay a subscription fee that adequately covers our current $3-5 cost per video and provides a margin? What price point would they find acceptable for regular use? <br> - **B2B Potential Value:** Do universities, research platforms, or journals see enough value to justify paying for institutional access? What specific problems can this solve for *them* (e.g., improving research accessibility, promoting publications)? <br> - **Cost Reduction:** What are the main factors driving the $3-5 video generation cost? Can we identify opportunities for optimization without requiring a major engineering overhaul at this stage? | **Experiment 1a (Price Gauge):** Create a simple mock-up of a subscription page. Offer 2-3 hypothetical pricing tiers (e.g., Basic: 3 videos/month for $X, Pro: 10 videos/month for $Y, Premium: Unlimited for $Z). Approach 10-15 target researchers. Briefly explain the service and show an example video. Ask them which tier, if any, they would consider and why. *Goal: Gauge initial price sensitivity and identify preferred features.* <br><br> **Experiment 1b (B2B Problem/Solution Fit Interviews):** Identify 3-5 contacts in target B2B sectors (e.g., a university librarian, a journal editor, someone at a research funding body). Request a 20-30 minute informational interview. Focus on their current challenges in disseminating complex research and making it understandable. (Perhaps arrange an interview with Alex?) Then, briefly introduce Synapsis AI's concept and get their reaction. *Goal: Understand B2B pain points and their initial reaction to our solution, not to sell at this stage.* <br><br> **Experiment 1c (Cost Analysis):** Break down the $3-5 video generation cost. *Goal: Identify the most expensive component in the current pipeline to target for future optimization discussions.* |
| **2. Growth / Customer Acquisition** | - **Initial Traction:** Beyond personal networks, which channels are most effective for reaching early adopters in the academic and research community? <br> - **Freemium Effectiveness:** Will offering a limited free trial (e.g., one free video) effectively convert users to paid subscriptions? What constitutes an appealing freemium offer? | **Experiment 2a (Targeted Content Teaser):** Select a highly relevant online academic community (e.g., a specific subreddit like r/PhD, r/labrats). Create one high-quality example visual summary from a recent, relevant open-access paper. Post it with a brief explanation of how it was made (mentioning Synapsis AI) and a link to our landing page where they can express interest or request a demo/free sample. *Goal: Test channel effectiveness and generate initial interest.* <br><br> **Experiment 2b (Freemium Model Test):** Offer to manually create one free visual summary for users. Use this to gather detailed feedback on the output and its perceived value, and ask if they would pay for more. *Goal: Test the appeal of a free video and gather qualitative feedback on product value and willingness to pay.* |
| **3. Copyright** | - **Fair Use:** When summarizing and visualizing published research, what aspects of our process fall under fair use, and what might require permissions? <br> - **User Responsibility vs. Platform Responsibility:** Who is responsible if a user uploads copyrighted material they don't have rights to summarize? How do other content generation tools handle this? <br> - **Output Ownership:** Who owns the copyright of the generated visual summary – the user, the original author, or Synapsis? | **Experiment 3a (Competitor Copyright Policy Review):** Identify 3-5 other tools that transform or summarize existing content (e.g., text-to-video, AI summarizers, presentation generators). Carefully review their Terms of Service and Copyright Policies. Note how they address input material rights and output ownership. *Goal: Understand industry standards and common approaches.* <br><br> **Experiment 3b (Document Transformation Process):** Create a detailed internal document outlining exactly how Synapsis AI processes source text. Specify what elements are extracted, how they are transformed, and what new creative input the system (or user via prompts) adds. _Goal: Prepare necessary documentation for seeking legal advice._ |
| **4. Product Communication (Avoiding "Too Techy")** | - **Clarity of Value:** How can we quickly and clearly communicate Synapsis AI's value proposition to a non-technical academic audience without them getting lost in jargon like "decomposition, synthesis, visualization"? <br> - **Demo Effectiveness:** Is a live demo too risky or confusing? What's the most impactful way to showcase the product's capabilities? | **Experiment 4a (Pre-recorded Demo & Feedback):** Create a concise (60-90 second) pre-recorded demo video. Start with a problem (e.g., "Struggling to keep up with dense research papers?"), show the input (a complex text snippet), briefly illustrate the Synapsis AI process conceptually (not overly technical), and showcase the engaging visual summary output. Show this video to 5-7 people from the target audience (researchers, students) and 2-3 people outside the immediate field. Get their feedback: What was clear? What was confusing? What was most exciting? Did they understand the benefit? *Goal: Test the clarity and impact of a pre-recorded demo and refine messaging.* |