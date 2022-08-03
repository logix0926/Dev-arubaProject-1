#!/usr/bin/bash

str = "\n\nClient List\n-----------\nName  IP Address     MAC Address        OS    ESSID  Access Point  Channel  Type  Role  IPv6 Address               Signal    Speed (mbps)\n----  ----------     -----------        --    -----  ------------  -------  ----  ----  ------------               ------    ------------      \n172.31.99.74   02:fa:2e:52:25:0b  NOFP  dev    AP2           1        GN    dev   fe80::182a:5f6e:15be:7f65  59(good)  65(good)      \n172.31.99.239  f2:6c:7a:17:da:34  NOFP  dev    AP2           52E      a-HE  dev   fe80::1481:800c:c9ab:7d48  58(good)  1200(good)\nNumber of Clients   :2\nInfo timestamp      :455"
regex='*:*:*:*:*:*'
arrA = ()
arrB = ()
arrC = ()

# 出力から必要箇所（接続先アクセスポイント名、MACアドレス）を抜き出し
#     a. 出力全体を行ごとに分割し、各行を要素に持つ配列Aを作成
arrA=($(echo $str | tr "." "\n"))

for line in "${arrA[@]}"
do
#     b. 必要箇所を含む行を判定
    if [[ $line =~ $regex ]] ;
    then
        arrB = ("${arrB[@]}" $line) 
    fi
#     c. 必要箇所を含む行を要素に持つ配列Bの作成

#     d. 配列Bの各要素に格納されている行を空白で区切り、配列Cを作成

# 必要箇所をJSON_βに変換
#     a. 配列Cから必要箇所を抜き出し、JSON_の作成
done