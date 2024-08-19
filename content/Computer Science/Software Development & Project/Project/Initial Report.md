
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

**Justification**: React's component-based architecture supports modular development and code reusability, key for rapid iterations. Vite's fast build times accelerate the development feedback loop, especially crucial when working with containerization; alternatives such as create-react-app are notably slower when used with virtualization tools like Docker. Tailwind CSS allows for quick UI prototyping. Starting with plain HTML/CSS/JS enables immediate visual progress, with a clear path to React for scaling.
## Backend
• Python with Flask for a RESTful API
• InfluxDB for time-series data storage
• Grafana for data visualization
• Each component containerized separately using Python and InfluxDB Dockerfiles
• Docker Compose used to orchestrate backend services

**Justification**: Python and Flask offer a low barrier to entry and rapid development cycles, crucial for MVP iteration. Flask's minimalist approach avoids over-engineering and eases us into integrating with InfluxDB. Separate containerization supports the single responsibility principle and enables independent scaling.
## Tooling
• Git for version control
• VS Code with dev containers for consistent development environments
• ESLint, Prettier (frontend); Black, pylint (backend) for code quality
• Discord for informal chat, Microsoft Teams for formal meetings with our Product Owner (tutor)
• Google Docs and Drive for documentation and file sharing
• GitHub for code hosting and project management:
  - Projects for sprint planning and task tracking
  - Pull requests and code reviews
  - .github repo documenting best practices, including pull request processes, Definition of Done (DoD), commit standards, and workflow

**Note**: Due to university GitHub limitations, we're unable to use multiple repositories or implement GitHub Actions for CI/CD as initially planned.

**Justification**: Git supports parallel development and rollbacks, crucial for rapid prototyping. Linting tools maintain code quality and consistency. VS Code with dev containers, along with our containerization strategy, ensures consistent environments across the team. GitHub centralizes our workflow, while Discord, Teams, and Google tools facilitate effective communication and documentation.