#! /bin/bash

result_filename=packages/kal.tar.gz

if [[ -f $result_filename ]]
then
  echo 'delete exists latest file'
  rm $result_filename
fi

poetry build
rm dist/kal-*.whl
filename=$( ls -lr dist/ | awk '{ print $9 }'  | grep  '.tar.gz' | head -1 )
cp "dist/$filename" $result_filename
