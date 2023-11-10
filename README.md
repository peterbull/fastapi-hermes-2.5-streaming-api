
# Hermes 2.5 Model Q&A API

This repository hosts a Q&A API implementation of teknium's [Hermes 2.5 Model](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B), developed using a quantized version of the model by [The Bloke](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF). It leverages the [Llama.cpp library by ggerganov](https://github.com/ggerganov/llama.cpp) to run the model efficiently and provide answers to user queries. The application utilizes FastAPI for serving requests and Gradio for the frontend interface, enabling convenient interaction with the Hermes 2.5 model through a web interface.

## Project Structure

The project is organized as follows:

- `Dockerfile`: Contains the commands needed to build a Docker image.
- `LICENSE`: The license file.
- `README.md`: Instructions and project documentation.
- `client/`: Contains the Gradio interface implementation.
- `docker-compose.yml`: Defines and runs multi-container Docker applications.
- `entrypoint.sh`: The entrypoint script of the docker container.
- `flagged/`: Directory for storing logs.
- `model/`: Contains the machine learning models.
- `requirements.txt`: Lists the Python dependencies for the project.
- `server/`: Contains the FastAPI server implementation.

## Setup

### Dependencies

To run the project, ensure you have Docker installed as the project relies on containers for isolation and easy setup. The `requirements.txt` file includes all the necessary Python libraries.

### llama.cpp Dependency

Due to the complexity of adding CUDA settings to the container, `Llama.cpp` is not included but should be cloned into the root directory of this repo before running `docker-compose`

```bash
git clone https://github.com/ggerganov/llama.cpp
```

Please follow the installation instructions for `llamacpp` to ensure that the CUDA environment is configured correctly.

### Building the Container

To build the Docker container, navigate to the project directory and run:

```bash
docker-compose build
```

### Running the Application

Once the container is built, you can start the application using:

```bash
docker-compose up
```

## Usage

### Client Interface

The Gradio web interface is available at `http://localhost:7860/` and allows users to input their questions and receive responses from the Hermes 2.5 model.

### Server API Docs

The FastAPI server docs can be accessed at `http://localhost:8000/docs` with the following endpoints:

- `/llama`: An SSE endpoint that streams responses from the Hermes 2.5 model.
- `/llamastatic`: A standard REST endpoint that returns a single response from the Hermes 2.5 model.

## Contributing

Contributions to the Hermes 2.5 Model Q&A API are welcome. Please ensure you create a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).
