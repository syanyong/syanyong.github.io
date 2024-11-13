## README
This is the repo for build github pages.

## Public page
https://syanyong.github.io

## Public repo
https://github.com/syanyong/syanyong.github.io

## Start
```
# Up & Build
docker-compose up --build -d

# Interactive Session
docker exec -it ruby_jekyll_container /bin/bash

# May need to install some bundle
bundle install
```

## Useful commands
```
gem install github-pages
bundle exec jekyll serve
bundle exec jekyll serve --livereload
JEKYLL_ENV=production bundle exec jekyll build
open $(bundle info --path minima)
```

## DOC
https://jekyllrb.com/docs/


