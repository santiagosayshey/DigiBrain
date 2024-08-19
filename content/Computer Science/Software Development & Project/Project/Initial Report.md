
# Tech Stack and Standards

## Containerize!

With a team bringing diverse skills and experiences to the table, ensuring a consistent development environment poses a significant challenge. To address this, we're leveraging **containerization** throughout our tech stack. We've chosen **Docker** as our containerization tool, offering several key advantages:

• **Consistency**: Ensures identical environments across all team members' setups
• **Rapid Onboarding**: Enables quick setup of development environments using documented processes
• **Isolation**: Allows separate containerization of each component (frontend, backend, database)

Our development strategy focuses on **simplicity and agility** to rapidly deliver a Minimum Viable Product (MVP). By using Docker, we address the "it works on my machine" problem, ensuring consistent environments across the team. This approach allows us to concentrate on core features and iterate quickly, embracing agile principles of flexibility and continuous improvement. 

Our tech stack is designed to leverage these containerization benefits while maintaining simplicity and agility. Here's a breakdown of our key components:

## Frontend
• React, Vite, and Tailwind CSS for the main application
• Initial MVPs built with plain HTML, CSS, and JS for rapid prototyping
• Containerized using a Node.js-based Dockerfile
• Development environment set up with VS Code dev containers

**Justification**: React's component-based architecture supports modular development and code reusability, key for rapid iterations. Vite's fast build times accelerate the development; alternatives such as create-react-app are quite slow in use with virtualisation tools like Docker. Tailwind CSS allows for quick UI prototyping. Starting with plain HTML/CSS/JS enables immediate visual progress, with a clear path to React for scaling.
## Backend
• Python with Flask for a RESTful API
• InfluxDB for time-series data storage
• Grafana for data visualization
• Each component containerized separately using Python and InfluxDB Dockerfiles
• Docker Compose used to orchestrate backend services

**Justification**: Python and Flask offer simplicity and quick development cycles. InfluxDB is purpose-built for time-series data, crucial for our application. Containerizing each component separately enhances isolation and modularity.
## Tooling
• Git for version control, with a branching strategy aligned with our containerized workflow
• CI/CD pipeline using GitHub Actions, integrated with our Docker builds
• ESLint and Prettier for frontend code quality, containerized in the dev environment
• Black and pylint for backend code formatting and linting, integrated into backend containers

This structure allows us to maintain consistency across environments while enabling quick iterations towards our MVP.