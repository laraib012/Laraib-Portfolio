# Portfolio Website

This is a personal portfolio website built using Flask and deployed on Azure. The website features a scrollable design with sections for Home, About, Projects, and Contact. Users can also download my resume.

## Features
- Scrollable single-page layout
- Sections: Home, About, Projects, Contact
- Downloadable resume
- Environment variable support using `.env`
- Deployed on Azure

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Deployment:** Azure

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
2. Navigate to the project folder:
   ```bash
   cd your-repo
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file and add:
   ```
   App_username=YourName
   ```

## Running the Application Locally
1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open the browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Deploying to Azure
1. Ensure all dependencies are listed in `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
2. Push your code to your Azure repository.
3. Configure the Azure Web App to use Python and set up the `.env` variables.
4. Restart the application from the Azure portal.

## Static Files Issue Fix (CSS & Resume Not Loading on Azure)
If CSS or the resume file is not loading:
- Ensure the `static/` folder is deployed.
- Use the correct path in your HTML:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
  ```
  ```html
  <a href="{{ url_for('static', filename='resume/resume.pdf') }}" download="My_Resume.pdf">Download Resume</a>
  ```
- Clear the cache and restart the Azure Web App.

## License
This project is open-source and free to use.

