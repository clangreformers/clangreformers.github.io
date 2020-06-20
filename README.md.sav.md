# README for clangreformers.github.io

## Install tooling

Run the following commands one after another:

```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew install ruby

echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.bash_profile

gem install --user-install bundler jekyll
```

## Here’s the location of the repo for the hosted webpages

```
https://github.com/clangreformers/clangreformers.github.io
```

### Clone the repo

```git clone https://github.com/clangreformers/clangreformers.github.io.git```

cd to clangreformers directory

run the following command once:

```bundle init```

## Directory structures

Familiarize yourself with the structure of the directories. 

* “home” will display all the articles under the _posts directory
  * each post filename is prefixed with a timestamp. This is significant as the article will be generated in the achronologically
  * each locale variations having a -en, -cn or -tw suffix in the filename
* Each topics on the navigation bar is under a separate directory.

## Content of the articles

The contents are using Jekyll’s markup language. You don't need to understand Jekyll if you are editing the article.
However, if you are curious, see [Jekyll](https://jekyllrb.com/).

## Editing an article

Make modifications in place in the articles.

## To Preview Changes

1. Run this command so that it generates static html pages under the _site directory,
and launch a http server on your laptop:

```bundle exec jekyll serve --trace```

Open the pages using your favorite browser at https://localhost:4000

## Push your changes to the master branch:

Once you are satisfied with your change, do the following to commit your changes:

```
git add .

git commit -m “a comment specifying what changes you have made”

git push origin master
```
