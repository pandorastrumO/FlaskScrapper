# Flask Web App With Scrapy Framework
> A simple flask app integrated with scrapy framework to run over facebook to mine data
> Also using embeded twisted reactor along with gunicorn WSGI server for Heorku Usage

[![Python Version][python-image]][python-url]
[![Build Status][travis-image]][travis-url]
[![Build Status][appveyor-image]][appveyor-url]

This is a project for scrapping likers and commenters of a given post URL of facebook
It also collects the likers likings and commenters likings from their profile and store all the data
into mongo databases collections.

## Installation & Setup (Development Environment)

OS X & Linux & Windows:

```bash
git clone https://github.com/PandorAstrum/FlaskScrapper.git
pip install -r requirements.txt
```

Download (Extras):
- [Python 3.6](https://www.python.org/)
- [VS CODE](https://code.visualstudio.com/)

## Usage example (Development Environment)

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

To run the flask project:
```
python app.py
```



## Release History

* 1.0.0
    * Add: flask web app
    * Add: MongoDB integrations
    * Add: Scrapy framework integrations
    * Add: helpers library

## Meta

Ashiquzzaman Khan – [@dreadlordn](https://twitter.com/dreadlordn)

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/PandorAstrum/Readme_Template](https://github.com/PandorAstrum/Readme_Template)

## Contributing

1. Fork it (<https://github.com/PandorAstrum/Readme_Template/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[python-image]: https://img.shields.io/badge/Python-3.6-yellowgreen.svg?style=flat-square
[python-url]: https://www.python.org/

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://www.npmjs.com/
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square

[travis-image]: https://travis-ci.org/PandorAstrum/_vault.svg?branch=master
[travis-url]: https://travis-ci.org/PandorAstrum/_vault

[appveyor-image]: https://ci.appveyor.com/api/projects/status/8dxrtild5jew79pq?svg=true
[appveyor-url]: https://ci.appveyor.com/project/PandorAstrum/vault

[ReadTheDoc]: https://github.com/yourname/yourproject/wiki

<!-- Header Pictures and Other media-->
[header-pic]: header.png

