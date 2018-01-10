FROM python:2

RUN apt-get update && apt-get install -yq openjdk-7-jre-headless chromium iceweasel
RUN apt-get update && apt-get install -yq git-core xvfb xsel unzip python-pytest libgconf2-4 libncurses5 libxml2-dev libxslt-dev libz-dev xclip

# Gecko and Chrome drivers
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz" -O /tmp/geckodriver.tgz
RUN wget -q "https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip" -O /tmp/chromedriver.zip

RUN tar zxf /tmp/geckodriver.tgz -C /usr/bin/
RUN unzip /tmp/chromedriver.zip -d /usr/bin/

COPY docker-entry.sh /docker-entry.sh
COPY requirements.txt /tmp/requirements.txt
COPY tests /tests/

# xvfb fix
COPY files/xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser

RUN chmod 777 /usr/bin/xvfb-chromium
RUN chmod 777 /usr/bin/geckodriver
RUN chmod 777 /docker-entry.sh

# pip
RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["/docker-entry.sh"]
CMD ["/bin/true"]