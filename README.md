# pnwapi

Pnwapi is a Python library for accessing the Politics and War API. It uses a simple, object-oriented approach to accessing the API, caching data, and handling errors. Pnwapi is designed around the concept of keeping a local copy of important data in a database, allowing for faster access, less reliance on the API and more advanced queries.

## Installation

Python 3.10 or higher is required. Pnwapi is available on PyPI and can be installed with pip:

```bash
pip install pnwapi
```

## Usage

```python
import pnwapi

pnw = pnwapi.init("YOUR_API_KEY", "YOUR_BOT_KEY", "DB_CONNECTION_STRING")
```

## Documentation

Documentation can be found at [pnwapi.readthedocs.io](https://pnwapi.readthedocs.io/en/latest/).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
