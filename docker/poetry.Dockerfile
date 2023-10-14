ARG base_image
FROM ${base_image}

USER root
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        curl \
        git \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.6.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python

RUN python -m venv "$VIRTUAL_ENV"

ARG username=appuser
USER ${username}
