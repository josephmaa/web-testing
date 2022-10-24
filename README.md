
Web-testing:

Runs on the following [website](http://automationpractice.com/index.php).

![](imgs/main.png)

Runs on both chrome and firefox browsers to test browser compatibility.

To run the tests:

1. Run the command in order to create the conda environment.

`conda create -n web-testing python=3.10`

2. Run the command to install pip.

`conda install pip`

3. Run the command to install the required commands.

`pip install -r requirements.txt`

4. Run the command to install the local module to the conda environment.

`pip install -e .`

5. Run the tests with the command.

`python3 -m pytest`

Pytest can be run with the `-s` flag in order to print output and the `-k` flag to run single tests at a time.