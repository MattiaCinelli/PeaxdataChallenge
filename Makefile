##############################
ENVIRONMENT_PREFIX=$(shell pwd)
ENVIRONMENT_NAME=.venv_peax
ALTERNATIVE_ENV_NAME=${ENVIRONMENT_NAME}
VENV_NAME=${ENVIRONMENT_PREFIX}/${ENVIRONMENT_NAME}
VENV_BIN=${VENV_NAME}/bin
VENV_PYTHON=${VENV_BIN}/python3

# Virtualenv for project
dev: requirements.txt
	echo "Creating virtual environment..."
	python3 -m piptools sync requirements.txt requirements.txt

requirements.txt: venv
	python3 -m piptools compile requirements.in --output-file requirements.txt

# Conflicts btw pip and pip-tools follows this issue: https://github.com/jazzband/pip-tools/issues/1617
venv: requirements.in	
	echo "Compiling requirements..."
	python3 -m venv ${ENVIRONMENT_NAME}
	pip3 install --upgrade 'pip'
	. ${ENVIRONMENT_NAME}/bin/activate
	pip install 'pip==22.0.4'
	pip install --upgrade pip-tools
	pip install setuptools>=41.0.0
	python3 -m ipykernel install --user --name=${ENVIRONMENT_NAME} --display-name "${ALTERNATIVE_ENV_NAME}"

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete