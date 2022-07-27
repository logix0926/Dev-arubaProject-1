#!/usr/bin/bash
# 接続先(AP1~4)とmacアドレスをJSONに書き込む

# 改行文字
LF=$'\n'

# jsonの内容記述。内容を
# 1行目の処理
jsonContents = "{${LF}"
# jsonContentsにforで内容の追記
  for((i=0; i<$データ行数-1; i++)); do
    jsonContents += "    ${マックアドレスの変数}:${AP1~4の変数},${LF}"
  done
# カンマがつかない最終行の処理
jsonContents += "    ${マックアドレスの変数}:${AP1~4の変数}${LF}}"

# jsonファイルに書き込み
printf "${jsonContents}" > connection_list.json


#以下、ウェブサイトからのメモ
# このシェルを実行する際には引数を１つとる
# $1:現在時刻(UNIXタイム通算秒)

# timeCount=6 # 1時間
# jsonHead='{"time":'
# LF=$'\n' # 改行文字

#   # printfで書込むjsonContentsに全て連結して１つの文字列にする処理
#   for((i=0; i<$timeCount; i++)); do
#     jsonTime[i]=`echo $(($1+(600*i))) | awk '{print strftime("%H:%M", $1)}'`
#     jsonContents+=${jsonHead}
#     jsonContents+="\"${jsonTime[i]}\"}" # 変換した時刻データを連結
#     if [ $i -lt $((timeCount - 1)) ]; then # 最終行を除く
#       jsonContents+=",${LF}    " # 空白４つ含む(改行文字も連結)
#     fi
#   done

# # printfでJSON形式でファイルにリダイレクトする
# printf '{
#   "now":[
#     %s
#   ]
# }' "${jsonContents}" > sample2.json