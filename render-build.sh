#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src
else
  echo "...Using Chrome from cache"
fi

if [[ ! -f $STORAGE_DIR/chrome/chromedriver ]]; then
  echo "...Downloading ChromeDriver"
  wget -P $STORAGE_DIR/chrome https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
  unzip $STORAGE_DIR/chrome/chromedriver_linux64.zip -d $STORAGE_DIR/chrome
  rm $STORAGE_DIR/chrome/chromedriver_linux64.zip
fi

pip install -r requirements.txt
