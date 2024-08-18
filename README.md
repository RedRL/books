# Books Service Project

This project is a microservice that provides an API to manage a collection of books. It includes functionalities to perform CRUD operations (Create, Read, Update, Delete) on a MongoDB database through a RESTful API. The service is built using Python with Flask and is containerized using Docker. 

## Features

- **POST Books**: Add new books to the collection.
- **GET Books**: Retrieve books based on various query parameters like title and published date.
- **Unit Testing**: Includes automated tests using `pytest` to ensure the reliability of the service.
- **Continuous Integration**: Integrated with GitHub Actions to automate testing, building, and querying.

## CI/CD

The project is configured with GitHub Actions to automate the following tasks:
- Building the Docker image.
- Running tests to validate the service.
- Executing queries and generating reports.


Nir - first commit
