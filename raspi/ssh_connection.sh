#!/usr/bin/bash

#環境変数の設定
#export SSHPASS=vagrant

#環境変数でログイン
sshpass -e ssh vagrant@192.168.56.101

#ログアウト
exit