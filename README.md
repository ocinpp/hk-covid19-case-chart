# Chart on Hong Kong COVID-19 Confirmed Cases

This tool is to generate the chart on the daily confirmed cases, showing the case classifications.

![Sample Chart](sample/daily-count-chart-sample.png)

## Prerequisite

Python 3 is requirement to run the script.

Please make sure the below packages have been installed

- Requests
- Pandas
- NumPy
- Matplotlib

## How to use

Clone the repository

```bash
git clone https://github.com/ocinpp/hk-covid19-case-chart.git
```

Create a directory `charts` where the generate charts will be stored

Execute the below command and a PNG file will be generated in the `charts` directory, with the file name containing the latest date provided in the dataset (e.g. `daily-count-chart-20200717.png`).

```bash
python daily-count.py
```

The PNG file will be overwritten if the same file name is generated.

### Virtual Environment

If you prefer to use virtual environment to run, you can refer to the below on `venv` and `pipenv`.

#### venv

For example, we wish to have a **venv** with the name `venc`

```bash
python -m venv venc
```

Activate the **venv** and you shall see `(venc)` in the terminal

```bash
source venc/bin/activate
```

Install packages

```bash
pip install requests
pip install pandas
pip install matplotlib
```

Run the script

```bash
python daily-count.py
```

Leave **venc**

```bash
deactivate
```

#### pipenv

Make sure you have `pipenv` installed. If not, please install using:

```bash
pip install pipenv
```

Create the virtual environment and launch the subshell. A Virtualenv location will be created and a `Pipfile` will be created

```bash
pipenv shell
```

Install packages

```bash
pip install requests
pip install pandas
pip install matplotlib
```

Run the script

```bash
python daily-count.py
```

Exit the shell

```bash
exit
```

Remove the virtual environment if it is no longer needed

```bash
pipenv --rm
```
