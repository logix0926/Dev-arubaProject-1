#!/usr/bin/bash

# azcopyの実行ファイルをスクリプトと同じファイルに入れること
# ./azcopy copy '/home/vagrant/scriptfile/memo.txt' 'http://10.0.2.2:10000/devstoreaccount1/testcontainer01?sv=2018-03-28&st=2022-07-29T06%3A18%3A14Z&se=2022-08-31T06%3A18%3A00Z&sr=c&sp=racwl&sig=GPPvl7pqopFcKKsOldOfPuzFUrnp8oqhB1Qs4FKybK0%3D' --from-to LocalBlob
# ./azcopy copy '/full/path/to/a/file' 'http://10.0.2.2:10000/devstoreaccount1/testcontainer01?[SAS token]' 