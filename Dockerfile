# We're using Ubuntu 20.10
# Thanks to geez-Userbot
FROM vckyouuu/geezproject:buster


RUN git clone -b Frds-Userbot https://github.com/Frds-ubot/frds-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Frds-ubot/frds-Userbot/Frds-Userbot/requirements.txt

CMD ["python3", "-m", "userbot"]
