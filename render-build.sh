#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render

# Chrome indir ve kur
if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
  rm ./google-chrome-stable_current_amd64.deb
  cd $HOME/project/src # Make sure we return to where we were
else
  echo "...Using Chrome from cache"
fi

# Chromedriver indir ve kur
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
  echo "...Downloading Chromedriver"
  wget -P $STORAGE_DIR https://chromedriver.storage.googleapis.com/$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
  unzip $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR
  rm $STORAGE_DIR/chromedriver_linux64.zip
fi

# PATH'e Chrome'u ekle
export PATH="${PATH}:$STORAGE_DIR/chrome/opt/google/chrome:$STORAGE_DIR"
