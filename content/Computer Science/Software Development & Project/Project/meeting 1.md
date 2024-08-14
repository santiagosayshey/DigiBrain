## Kickoff Meeting - Customer Q&A

| Context | Question | Answer |
|---------|----------|--------|
| Users can easily pick a time range [US1] | How atomic does this need to be? Minutes? Hourly? Daily? | |
| Users can select a measurement from a list [US1] | Does it need to work for a specific use case? Or just any generic time series data: eg, can our mvp just be weather data for now | |
| The system should prepare to generate the query [US1] | What does prepare mean? Would a template influx query with parameterized inputs suffice? | |
| | Does the user need to see this? Or can it be in the background? | |
| The system shows the generated query code based on user selections | Can this just be a simple text file output? | |
| Users can review the code before execution | Does this mean they can leave comments? Ask for edits / explanation? Or just look at it? | |
| Visualization of data results | Are there any specific graph customization options we should prioritize (e.g., colors, legends, axis labels)? | |

## User Roles

| Role | Responsibilities | Potential Actions |
|------|------------------|-------------------|
| Data Analyst | - Querying and analyzing time-series data<br>- Creating visualizations<br>- Generating reports | - Selecting time ranges and measurements<br>- Reviewing generated queries<br>- Customizing visualizations<br>- Saving queries for future use |
| Dashboard Creator | - Building and maintaining dashboards for data visualization and monitoring | - Creating new dashboards<br>- Adding and configuring various chart types<br>- Setting up data refresh intervals<br>- Sharing dashboards with other users |
| Business User | - Interpreting data trends<br>- Making data-driven decisions without deep technical knowledge | - Viewing pre-built dashboards<br>- Adjusting time ranges for data exploration<br>- Exporting visualizations for presentations or reports |
| System Administrator | - Managing user access<br>- Configuring integrations<br>- Ensuring system performance | - Setting up authentication<br>- Managing user roles and permissions<br>- Configuring InfluxDB and Grafana connections<br>- Monitoring system usage |

**Question for the client:** Anything we should remove? Anything we are missing?