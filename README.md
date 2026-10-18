# AbhishekThakur_CI_Project

A small Python CI project for assignment 4, built with GitHub Actions and pytest.

## Structure

- `codes/` contains the 10 Python programs (21 to 30)
- `test_cases/` contains one pytest file per program
- `.github/workflows/python-ci.yml` runs the test suite automatically on GitHub

## Local usage

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```
