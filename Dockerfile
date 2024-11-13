# Use Ubuntu 24 as the base image
FROM ubuntu:24.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies and Ruby
RUN apt-get update && \
    apt-get install -y ruby-full build-essential zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Set up GEM_HOME and update PATH
RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc && \
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc && \
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc && \
    # Source bashrc for current session and install specific version of Jekyll and Bundler
    /bin/bash -c "source ~/.bashrc && gem install jekyll bundler"

# Default command (can be changed based on your needs)
CMD ["irb"]
