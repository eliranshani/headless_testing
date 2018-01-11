# Headless testing using chrome "headless"
Running Selenium tests under py.test convention with docker support.

![Carpe Diem - Seize the day](files/shark.png "Carpe Diem")

## Requirements

- [Python](http://selenium-python.readthedocs.io/)
- [Pytest](https://docs.pytest.org/en/latest/)
- [ChromeDriver v2.35 - latest is preferred](https://sites.google.com/a/chromium.org/chromedriver/)
- [Chrome v59+](https://developers.google.com/web/updates/2017/04/headless-chrome)
- [Docker - optional](https://www.docker.com/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

### Run tests via virtual environment
```bash
$ source PATH_TO_VIRTUAL_ENV/bin/activate
$ (VIRTUAL_ENV) pytest tests/test_website_titles.py
```

# Run with default command using docker
```bash
$ ./scripts/run-tests.bash
```

# Run with extra py.test arguments
```bash
$ ./scripts/run-tests.bash --env=$ENV tests/test_purhcase_tickets.py --verbose
```

## Motivation

This project allows other developers to understand how to:
1. Create auto tests in python under py.test convention
2. Run tests using "headless" mode

## Links

[PhantomJS single maintainer stepping down](https://groups.google.com/forum/#!topic/phantomjs/9aI5d-LDuNE)
[Chrome headless youtube announcement](https://www.youtube.com/watch?v=zNoc4zEkWPo)

## Contributors

Eliran Shani

## License

MIT

