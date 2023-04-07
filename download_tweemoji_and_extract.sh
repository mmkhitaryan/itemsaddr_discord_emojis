wget https://github.com/twitter/twemoji/archive/refs/heads/master.zip
unzip master.zip
mkdir 72x72/
mv twemoji-master/assets/72x72/* 72x72/
rm -rf twemoji-master/
rm master.zip