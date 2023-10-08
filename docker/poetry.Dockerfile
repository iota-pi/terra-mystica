ARG base_image
FROM ${base_image}

ENV POETRY_VERSION=1.6.1
ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

USER root
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        curl \
        git \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python \
    && chmod +x $POETRY_HOME/bin/poetry \
    && poetry config virtualenvs.create false

RUN python -m venv $VENV_PATH

ARG username=appuser
USER ${username}
