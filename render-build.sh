STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome

  # Chrome tarayıcısını indir ve çıkar
  wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -x ./google-chrome-stable_current_amd64.deb .
  rm ./google-chrome-stable_current_amd64.deb

  # ChromeDriver'ı indir
  wget -P ./ https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
  unzip ./chromedriver_linux64.zip
  chmod +x chromedriver
  rm ./chromedriver_linux64.zip
else
  echo "...Using Chrome and ChromeDriver from cache"
fi

pip install -r requirements.txt
