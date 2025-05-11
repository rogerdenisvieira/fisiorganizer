## Installing Dependencies

First of all, activate virtual environment (venv) to isolate project's packages from global ones:

```bash
python3 -m venv path/to/venv
source path/to/venv/bin/activate
```

Then restore the dependencies from `requirements.txt`:

```bash
python3 -m pip install -r requirements
```

## Running the application:

Once dependencies have been restored, just run:

```bash
python3 manage.py runserver
```