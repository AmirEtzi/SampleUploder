document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('upload-form');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            loadProjects();
        }
    });
    
    async function loadProjects() {
        const response = await fetch('/projects');
        const projects = await response.json();
        
        const projectsList = document.getElementById('projects-list');
        projectsList.innerHTML = '';
        
        projects.forEach(project => {
            const projectDiv = document.createElement('div');
            projectDiv.innerHTML = `
                <h3>${project.title}</h3>
                <img src="/static/uploads/${project.image}" alt="${project.title}">
                <p>${project.description}</p>
            `;
            projectsList.appendChild(projectDiv);
        });
    }
    
    loadProjects();
});
