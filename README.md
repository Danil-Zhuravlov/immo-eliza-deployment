# Immo-Eliza-Deployment 🏠💻

Welcome to the repository of **Immo-Eliza-Deployment**, a project that showcases the deployment of a real estate price prediction model!

## Table of Contents 📑
- [About The Project 📘](#about-the-project-📘)
- [Built With 🛠️](#built-with-🛠️)
- [Getting Started 🏁](#getting-started-🏁)
- [Usage 🚀](#usage-🚀)
- [Contributing 🤝](#contributing-🤝)
- [License 📜](#license-📜)
- [Contact 📧](#contact-📧)
- [Acknowledgements 🎉](#acknowledgements-🎉)

## About The Project 📘

👋 Hi, I'm a passionate data scientist from BeCode, an intensive data science bootcamp. This project is a part of my learning journey, where I focus on doing rather than just theorizing.

### The Challenge 🚀

The goal was to deploy a **Random Forest Regression** model, crafted with `scikit-learn`, into a working API using `FastAPI` and integrate it with a `Streamlit` web application. This allows both technical and non-technical users to interact with the model and get real estate price predictions.

### The Outcome ✨

After 5 days of hard work, the result is a seamless connection between the frontend and backend, opening up API access to peers and providing a user-friendly web app for clients.

### Note 📝

The model predictions are not perfect and should not be taken as professional appraisals.

## Built With 🛠️

- FastAPI
- Streamlit
- scikit-learn

## Getting Started 🏁

To get a local copy up and running follow these simple steps.

### Prerequisites 🔍

- Python 3.8+
- pip

### Installation 💿

1. Clone the repo and go to the project directory
   ```sh
   git clone -b local-deployment --single-branch git@github.com:Danil-Zhuravlov/immo-eliza-deployment.git

   cd immo-eliza-deployment
    ```

2. Create a virtual environment
    ```sh
    python -m venv venv
    ```
3. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```

## Usage 🚀

You can check out the deployed app [here](https://price-predictor-immo-eliza.streamlit.app/). The api documentation is available [here](https://property-price-predictor-405i.onrender.com/docs).

### If you want to run the app locally, follow these steps:

1. Run the Streamlit app
    ```sh
    streamlit run streamlit/app.py
    ```

2. Run the FastAPI app
    ```sh
    cd app
    uvicorn main:app --reload
    ```

3. On the Streamlit app, input the property features and get the price prediction!

4. On the FastAPI app, you can access the API documentation [HERE](http://127.0.0.1:8000/docs)

## Contributing 🤝
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License 📜
Distributed under the MIT License. See [License](LICENSE) for more information.

## Contact 📧
Danil Zhuravlov - [LinkedIn](https://www.linkedin.com/in/danil-zhuravlov/)

## Acknowledgements 🎉

- [BeCode](https://becode.org/)
- [My Mentor](https://www.linkedin.com/in/vriveraq/)
- My Colleagues
