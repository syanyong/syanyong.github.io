# Use Ubuntu 24 as the base image
FROM ubuntu:24.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies and Ruby
RUN apt-get update && \
    apt-get install -y ruby-full build-essential zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Set up GEM_HOME and update PATH
ENV GEM_HOME="/usr/local/bundle"
ENV PATH="$GEM_HOME/bin:$PATH"

# Create a working directory
WORKDIR /app

# Copy Gemfile and Gemfile.lock before running bundle install to leverage Docker caching
COPY Gemfile Gemfile.lock /app/

# Install Bundler and Jekyll based on the Gemfile
RUN gem install bundler && bundle install

# Copy the rest of the application files
COPY . /app

# Default command to run Jekyll
# CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
