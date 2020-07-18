# Chart on Hong Kong COVID-19 Confirmed Cases

This tool is to generate the chart on the daily confirmed cases showing the case classifications.

![Sample Chart](sample/daily-count-chart-sample.png)

## Prerequisite

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

Execute the below command and a PNG file will be generated in the `charts` directory, with the file name containing the latest date provided in the dataset (e.g. `daily-count-chart-20200717.png`).

```bash
python daily-count.py
```

The PNG file will be overwritten if the same file name is generated.

### venv

If you prefer to use **venv** to run, please follow the below commands. For example, we wish to have a **venv** with the name `venc`

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
