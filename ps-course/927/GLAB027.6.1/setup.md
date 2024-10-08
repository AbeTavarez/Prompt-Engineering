# Lab Setup

## Steps

### Pipenv Installation and Configuration

1.  In your terminal run `pip install pipenv` or depending on your environment, `pip3 install pipenv`.

2.  Create a file in your project directory called Pipfile.

3.  Copy paste the following code into that new Pipfile:

```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
langchain = "==0.0.352"
openai = "==0.27.8"
python-dotenv = "==1.0.0"

[dev-packages]

[requires]
python_version = "3.11"
```

4. Run the following command to create and enter a new environment:
   `pipenv shell`

   A new `Pipfile.lock` file will be created. (don't need to touch this file).

   If you make any changes to the Pipfile, not the Pipfile.lock, you'll need to run the `pipenv shell` command again from your terminal.

5. Now you can start working on the lab `file.ipynb` file.

Important - Anaconda users may find that Pipenv conflicts with their environment. Please deactivate your conda environment if you find this to be true.

Deprecation warnings about Langchain 0.1.0 and 0.2.0 should be ignored as we are not using these versions!
