# GitHub Pages with Jekyll

This repository builds a Dockerized environment for [GitHub Pages](https://pages.github.com/) using Jekyll.

## Public Page
[https://syanyong.github.io](https://syanyong.github.io)

## Public Repository
[https://github.com/syanyong/syanyong.github.io](https://github.com/syanyong/syanyong.github.io)

---

## Getting Started

To get started with building and running the environment, follow these steps:

```bash

git submodule update --init --recursive

# Build and start the container in detached mode
docker compose up --build -d

# Start an interactive session in the running container
docker exec -it jekyll-site-container /bin/bash

# Install bundle dependencies if needed
bundle install

# Start Jekyll server
bundle exec jekyll serve --host 0.0.0.0

# Start Jekyll with live reload
bundle exec jekyll serve --host 0.0.0.0 --livereload

# Build for production
JEKYLL_ENV=production bundle exec jekyll build

# Open the path to the installed theme (e.g., 'minima')
open $(bundle info --path minima)
