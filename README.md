# g_inspect_api_sample_tests

<!-- TABLE OF CONTENTS -->
### TABLE OF CONTENTS 
* [Introduction](#introduction)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)


<!-- ABOUT THE PROJECT -->
## Introduction
this is a sample framework designed and developed for Introspection API testing
<br>
test case document [link](testplan.md)


<!-- GETTING STARTED -->
## Getting Started
* checkout the latest framework
* update API_KEY in config file config/prod_env.json

### Prerequisites
* python > 3.8
* pytest

### Installation

installing python libraries

```commandline 
pip install -r requirements.txt
```


<!-- USAGE EXAMPLES -->
## Usage

To execute the tests 
```commandline
pytest
```


<!-- ROADMAP -->
## Roadmap
Following features need to be implemented
* pending validations:
  * number of findings by info type
  * severity of findings
* pending test inputs
  * InspectConfig
* dockerfile update
* drone yml file update
* test generation using microsoft pict tool

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
