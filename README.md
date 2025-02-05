# RAGify

RAGify is a query response system designed to provide accurate answers to your questions. Using advanced algorithms, it processes your questions and delivers precise answers by leveraging state-of-the-art natural language processing (NLP) techniques.

## Features

- **Query Handling**: Enter your queries and get instant responses.
- **Data Preprocessing**: Load and preprocess enterprise data for analysis.
- **Embeddings**: Generate and use text embeddings for improved query responses.
- **Interactive Frontend**: Simple and intuitive frontend to interact with RAGify.
- **Scalable and Efficient**: Capable of handling large volumes of queries simultaneously.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- [SentenceTransformers](https://www.sbert.net/)
- [pandas](https://pandas.pydata.org/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HarshMishra-Git/Ragify.git
   cd Ragify
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Data Ingestion**: Load and preprocess the data.

   ```python
   python data_ingestion.py
   ```

2. **Build RAG Pipeline**: Run the main application.

   ```python
   python app.py
   ```

3. **Frontend**: Open the `frontend/index.html` in your web browser to interact with the application.

## File Structure

- `app.py`: Main application file to handle user queries.
- `data/contact_responses.csv`: Sample contact responses data.
- `data/sample_data.csv`: Sample enterprise data.
- `data_ingestion.py`: Script to load and preprocess data.
- `embeddings/embedding_utils.py`: Utilities for generating text embeddings.
- `frontend/index.html`: Frontend interface for interacting with RAGify.

## Usage

1. **Start the Application**:

   ```bash
   python server.py
   ```

2. **Interact with the System**: Enter your query in the console or through the web interface.

3. **Contact Form**: Fill in the contact form in the web interface to send a message.

## Contributing

We welcome contributions to improve RAGify. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries or feedback, please reach out to us through the contact form on the web interface or via email at [harsh.mishra2022@glbajajgroup.org](mailto:harsh.mishra2022@glbajajgroup.org).

---

© 2025 RAGify. All rights reserved.
```

This README.md file provides a clear and comprehensive overview of the project, including installation instructions, usage details, and contribution guidelines.
